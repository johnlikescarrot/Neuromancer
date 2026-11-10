/**
 * Font inlining: reads the @fontsource CSS for each family/weight and rewrites
 * the ./files/*.woff2 URLs to base64 data URIs, so the printed PDF embeds every
 * glyph (including the Vietnamese subsets) with no network access at render.
 *
 * The Astryx gothic theme ships fonts.css pointing at Google Fonts (Fustat,
 * JetBrains Mono, Manufacturing Consent, UnifrakturMaguntia). We keep those
 * roles and add Vietnamese-capable companions, since the edition is bilingual.
 */
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { locatePackage } from "./locate.js";

type Face = { pkg: string; weights: number[]; italics?: number[] };

const FACES: Face[] = [
  { pkg: "@fontsource/manufacturing-consent", weights: [400] }, // Astryx gothic display
  { pkg: "@fontsource/unifrakturmaguntia", weights: [400] }, // Astryx gothic flourish
  { pkg: "@fontsource/playfair-display", weights: [400, 500, 600, 700, 800, 900], italics: [400, 500, 600, 700] },
  { pkg: "@fontsource/fustat", weights: [400, 500, 600, 700, 800] }, // Astryx gothic body
  { pkg: "@fontsource/source-serif-4", weights: [400, 600, 700], italics: [400, 600] },
  { pkg: "@fontsource/inter", weights: [400, 500, 600, 700], italics: [400, 600] },
  { pkg: "@fontsource/jetbrains-mono", weights: [400, 500, 700], italics: [400] },
];

/** Keep only the subsets the edition needs; drop cyrillic/greek to stay lean. */
const KEEP_SUBSETS = new Set(["latin", "latin-ext", "vietnamese"]);

function pkgDir(pkg: string): string {
  return locatePackage(pkg);
}

function loadFaceCss(cssPath: string, dir: string): string {
  let css = readFileSync(cssPath, "utf8");
  // Split into @font-face blocks and keep only wanted subsets.
  const blocks = css.split(/(?=@font-face)/).filter((b) => b.includes("@font-face"));
  const kept = blocks.filter((b) => {
    const m = b.match(/\/\*\s*([a-z-]+)\s*\*\//i) ?? b.match(/unicode-range/i);
    const subsetComment = b.match(/\/\*\s*([a-z-]+)\s*\*\//i);
    if (subsetComment) return KEEP_SUBSETS.has(subsetComment[1].toLowerCase());
    return Boolean(m);
  });
  css = kept.join("\n");
  // Rewrite url(./files/x.woff2) -> data URI
  css = css.replace(/url\(\.\/(files\/[^)]+\.woff2)\)/g, (_all, rel: string) => {
    const buf = readFileSync(join(dir, rel));
    return `url(data:font/woff2;base64,${buf.toString("base64")})`;
  });
  return css;
}

let cached: string | null = null;

export function embeddedFontsCss(): string {
  if (cached) return cached;
  const parts: string[] = [];
  for (const face of FACES) {
    const dir = pkgDir(face.pkg);
    const loads: { file: string }[] = [];
    for (const w of face.weights) loads.push({ file: `${w}.css` });
    for (const w of face.italics ?? []) loads.push({ file: `${w}-italic.css` });
    for (const l of loads) {
      try {
        parts.push(loadFaceCss(join(dir, l.file), dir));
      } catch {
        // A missing weight is not fatal; the family still renders with what exists.
      }
    }
  }
  cached = parts.join("\n");
  return cached;
}
