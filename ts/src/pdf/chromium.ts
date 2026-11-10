/**
 * Headless Chromium bootstrap for the PDF pipeline.
 *
 * `@sparticuz/chromium` ships the browser binary inside its npm tarball (no
 * external downloads). Outside AWS Lambda it does not inflate the bundled
 * Amazon Linux system libraries, so we inflate them ourselves and point
 * LD_LIBRARY_PATH at them before launching.
 */
import { join } from "node:path";
import { createRequire } from "node:module";
import { locatePackage } from "../design/locate.js";

const require = createRequire(import.meta.url);

export async function launchChromium(): Promise<import("puppeteer-core").Browser> {
  const chromiumPkg = require("@sparticuz/chromium");
  const chromium = chromiumPkg.default ?? chromiumPkg;
  const pkgDir = locatePackage("@sparticuz/chromium");

  // Inflate the bundled system libs (libnss3, libnspr4, ...) if not already present.
  const lambdafs = require(join(pkgDir, "build", "lambdafs.js"));
  const libDir: string = await lambdafs.inflate(join(pkgDir, "bin", "al2023.tar.br"));
  const al2Dir: string = await lambdafs.inflate(join(pkgDir, "bin", "al2.tar.br"));
  const libPath = [join(libDir, "lib"), join(al2Dir, "lib"), process.env.LD_LIBRARY_PATH ?? ""]
    .filter(Boolean)
    .join(":");
  process.env.LD_LIBRARY_PATH = libPath;

  const executablePath: string = await chromium.executablePath();
  const puppeteer = require("puppeteer-core");
  return puppeteer.launch({
    args: chromium.args,
    executablePath,
    headless: true,
  });
}

export const FOOTER_TEMPLATE = `
<div style="width:100%;font-size:7px;font-family:Arial, sans-serif;color:#5d646b;
            padding:0 15mm;display:flex;justify-content:space-between;align-items:center;">
  <span>NEUROMANCER · BILINGUAL ACADEMIC COMPANION · C1-C2</span>
  <span><span class="pageNumber"></span> / <span class="totalPages"></span></span>
</div>`;

export const HEADER_TEMPLATE = `<div></div>`;
