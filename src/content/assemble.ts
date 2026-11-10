/** Assembly helpers: chapters into blocks, and the table of contents. */
import type { Block, ChapterGuide } from "../types.js";
import type { TocItem } from "../engine/render.js";

export const chapterBlock = (guide: ChapterGuide): Block => ({ t: "chapter", guide });

/** Every division and every chapter, in reading order. */
export function collectToc(blocks: Block[]): TocItem[] {
  const items: TocItem[] = [];
  for (const block of blocks) {
    if (block.t === "divider") {
      items.push({ level: 1, text: block.title, id: block.id });
    } else if (block.t === "h1" && block.id) {
      items.push({ level: block.kicker && block.kicker.startsWith("Front matter") ? 2 : 1, text: block.text, id: block.id });
    } else if (block.t === "chapter") {
      items.push({
        level: 2,
        text: `Chapter ${block.guide.num} · ${block.guide.title}`,
        id: `chapter-${block.guide.num}`,
      });
    }
  }
  return items;
}
