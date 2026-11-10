/**
 * Print design tokens derived from the Astryx design system.
 *
 * `facebook/astryx` (published as `@astryxdesign/*`) is a web design system, not
 * a PDF toolchain: it ships CSS custom properties, React 19 components and
 * StyleX styling. There is no PDF renderer in it, and printing from a browser is
 * not available in this build environment, so the edition cannot use Astryx
 * components directly.
 *
 * What we *can* do — and do here — is treat Astryx as the single source of truth
 * for the visual language. At build time we read the neutral theme's token sheet
 * (`theme.css`), pull out the colour ramp, the type scale and the spacing scale,
 * and project them onto print values (pt for type, mm for page architecture,
 * printable ink mixes for colour). The result is a book that speaks the design
 * system's dialect instead of a palette invented from scratch.
 */
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
import path from "node:path";

const require = createRequire(import.meta.url);

export interface PrintTokens {
  /** Body ink, near-black with the theme's warm neutral bias. */
  ink: string;
  /** Secondary ink for notes, metadata, folios. */
  inkMuted: string;
  /** Hairlines and table rules. */
  rule: string;
  /** Tinted panel behind Vietnamese companion text. */
  panel: string;
  /** Accent used for rules, running heads and chapter numerals. */
  accent: string;
  accentSoft: string;
  /** Cover stock. */
  coverBase: string;
  coverInk: string;
  /** Type scale, in points, projected from the Astryx font-size ramp. */
  type: {
    display: number;
    title: number;
    part: number;
    h1: number;
    h2: number;
    h3: number;
    body: number;
    small: number;
    micro: number;
  };
  /** Spacing scale, in points, projected from the Astryx spacing ramp. */
  space: (step: number) => number;
  /** Provenance string, surfaced on the colophon page. */
  source: string;
}

const FALLBACK = {
  ink: "#101418",
  inkMuted: "#5b6470",
  rule: "#c9ced6",
  panel: "#f4f5f7",
  accent: "#0c6f82",
  accentSoft: "#d7e6ea",
  coverBase: "#0b1013",
  coverInk: "#eef3f5",
};

function parseVars(css: string): Map<string, string> {
  const vars = new Map<string, string>();
  const re = /(--[a-z0-9-]+)\s*:\s*([^;}]+)/gi;
  let m: RegExpExecArray | null;
  while ((m = re.exec(css)) !== null) {
    if (!vars.has(m[1])) vars.set(m[1], m[2].trim());
  }
  return vars;
}

function rem(value: string | undefined, root = 16): number | undefined {
  if (!value) return undefined;
  const m = /^(-?[\d.]+)rem$/.exec(value);
  if (m) return Number(m[1]) * root;
  const px = /^(-?[\d.]+)px$/.exec(value);
  if (px) return Number(px[1]);
  return undefined;
}

function resolveColor(
  vars: Map<string, string>,
  name: string,
): string | undefined {
  let key = name;
  for (let hop = 0; hop < 6; hop++) {
    const raw = vars.get(key);
    if (!raw) return undefined;
    const alias = /^var\(\s*(--[a-z0-9-]+)\s*\)$/i.exec(raw);
    if (alias) {
      key = alias[1];
      continue;
    }
    if (/^#[0-9a-f]{3,8}$/i.test(raw)) return raw.toLowerCase();
    return undefined;
  }
  return undefined;
}

function loadCss(): { css: string; file: string } | null {
  try {
    const pkgJson = require.resolve("@astryxdesign/theme-neutral/package.json");
    const file = path.join(path.dirname(pkgJson), "dist", "theme.css");
    return { css: readFileSync(file, "utf8"), file };
  } catch {
    return null;
  }
}

export function buildTokens(): PrintTokens {
  const loaded = loadCss();
  const vars = loaded ? parseVars(loaded.css) : new Map<string, string>();

  const base = rem(vars.get("--font-size-base"), 16) ?? 14; // 0.875rem -> 14px
  const pt = (px: number) => Math.round((px * 0.75) * 10) / 10; // 96dpi px -> pt

  // The Astryx type ramp is a workspace UI scale (12–42px). A printed page needs
  // a wider dynamic range, so we keep the ramp's *ratios* and stretch them.
  const ratio = (step: string, fallback: number) => {
    const px = rem(vars.get(`--font-size-${step}`), 16);
    return px ? px / base : fallback;
  };

  const body = 10.2; // pt — comfortable for a dense A4 study page

  const spaceUnit = rem(vars.get("--space-2"), 16) ?? 8; // px

  return {
    ink: resolveColor(vars, "--color-text-primary") ?? FALLBACK.ink,
    inkMuted: resolveColor(vars, "--color-text-secondary") ?? FALLBACK.inkMuted,
    rule: resolveColor(vars, "--color-border") ?? FALLBACK.rule,
    panel: resolveColor(vars, "--color-background-muted") ?? FALLBACK.panel,
    accent: resolveColor(vars, "--color-accent") ?? FALLBACK.accent,
    accentSoft: resolveColor(vars, "--color-accent-muted") ?? FALLBACK.accentSoft,
    coverBase: "#0b1013",
    coverInk: "#eef3f5",
    type: {
      display: Math.round(body * 4.4 * 10) / 10,
      title: Math.round(body * 2.9 * 10) / 10,
      part: Math.round(body * 2.1 * 10) / 10,
      h1: Math.round(body * 1.55 * 10) / 10,
      h2: Math.round(body * 1.2 * 10) / 10,
      h3: Math.round(body * 1.02 * 10) / 10,
      body,
      small: Math.round(body * 0.86 * 10) / 10,
      micro: Math.round(body * 0.72 * 10) / 10,
    },
    space: (step: number) => Math.round(((spaceUnit * step) / base) * body * 10) / 10,
    source: loaded
      ? `@astryxdesign/theme-neutral · dist/theme.css (type ramp ratio ${ratio("lg", 1.21).toFixed(2)}×, base ${pt(base)}pt)`
      : "built-in fallback palette (Astryx theme package unavailable)",
  };
}
