/**
 * Package directory location without relying on package `exports` maps:
 * several design/font packages restrict subpath imports, so we resolve the
 * physical directory under node_modules directly (with a require.resolve
 * fallback where the exports map allows it).
 */
import { existsSync } from "node:fs";
import { createRequire } from "node:module";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const require = createRequire(import.meta.url);
const here = dirname(fileURLToPath(import.meta.url));

export function locatePackage(name: string): string {
  const candidates: string[] = [];
  try {
    const resolved = require.resolve(name);
    candidates.push(join(dirname(resolved), ".."), dirname(resolved));
  } catch {
    // exports map may block bare resolution; node_modules walk below handles it
  }
  try {
    const pkgJson = require.resolve(`${name}/package.json`);
    candidates.push(dirname(pkgJson));
  } catch {
    // same
  }
  candidates.push(join(here, "..", "..", "node_modules", ...name.split("/")));

  for (const dir of candidates) {
    if (existsSync(join(dir, "package.json"))) return dir;
  }
  throw new Error(`Cannot locate package directory for ${name}`);
}
