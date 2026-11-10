#!/usr/bin/env node
/**
 * Build entry point.
 *
 *   node dist/cli/build.js  [--out output/neuromancer_bilingual_edition.pdf]
 *
 * Two passes: the first paginates the book to learn where every division and
 * chapter lands, the second writes the final PDF with a filled-in table of
 * contents. Page geometry is identical between passes because the TOC reads its
 * page numbers from a fixed-width gutter, so one measurement pass is enough.
 */
import fs from "node:fs";
import path from "node:path";
import { Writable } from "node:stream";
import { Book } from "../engine/page.js";
import { renderBlocks, type TocItem } from "../engine/render.js";
import { buildTokens } from "../design/tokens.js";
import { buildDocument, collectToc } from "../content/index.js";

interface BuildResult {
  pages: number;
  bytes: number;
  tocFilled: number;
}

async function pass(
  blocks: ReturnType<typeof buildDocument>,
  toc: TocItem[],
  sink: NodeJS.WritableStream,
  measure: boolean,
  tocPages: Map<string, string>,
): Promise<{ pages: number; filled: number }> {
  const record = measure
    ? (id: string, folio: string) => {
        if (folio) tocPages.set(id, folio);
      }
    : undefined;
  const book = new Book(
    {
      tokens: buildTokens(),
      measure,
      tocPages,
      onTocPage: record,
    },
    sink,
  );
  book.registerFonts(path.join(process.cwd(), "assets", "fonts"));
  renderBlocks(book, blocks, toc, { tocPages, onTocPage: record });
  const pages = book.doc.bufferedPageRange().count;
  await book.end();
  return { pages, filled: tocPages.size };
}

export async function build(outFile: string): Promise<BuildResult> {
  const blocks = buildDocument();
  const toc = collectToc(blocks);
  const tocPages = new Map<string, string>();

  // Pass 1 — measure only; the buffer is discarded.
  const blackhole = new Writable({
    write(_chunk, _enc, cb) {
      cb();
    },
  });
  await pass(blocks, toc, blackhole, true, tocPages);

  for (const item of toc) item.page = tocPages.get(item.id) ?? "—";

  // Pass 2 — the real book.
  fs.mkdirSync(path.dirname(outFile), { recursive: true });
  const stream = fs.createWriteStream(outFile);
  const { pages } = await pass(blocks, toc, stream, false, new Map(tocPages));
  await new Promise<void>((resolve, reject) => {
    stream.on("finish", () => resolve());
    stream.on("error", reject);
  });

  return { pages, bytes: fs.statSync(outFile).size, tocFilled: toc.filter((t) => t.page && t.page !== "—").length };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const argOut = process.argv.indexOf("--out");
  const out =
    argOut > -1 && process.argv[argOut + 1]
      ? path.resolve(process.argv[argOut + 1])
      : path.join(process.cwd(), "output", "neuromancer_bilingual_edition.pdf");
  const started = Date.now();
  build(out)
    .then((r) => {
      const secs = ((Date.now() - started) / 1000).toFixed(1);
      console.log(
        `✓ ${path.relative(process.cwd(), out)} — ${r.pages} pages, ${(r.bytes / 1024 / 1024).toFixed(2)} MB, ${r.tocFilled} TOC entries resolved, ${secs}s`,
      );
    })
    .catch((err) => {
      console.error("✗ build failed:", err);
      process.exitCode = 1;
    });
}
