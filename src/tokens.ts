import { readFileSync, existsSync } from 'node:fs';
import { rgb, type RGB } from 'pdf-lib';
// Design tokens parsed from Astryx neutral theme (facebook/astryx, @astryxdesign/theme-neutral).
// Astryx principle used here: theme = token overrides, guidance over enforcement.
// We consume its generated CSS custom properties and map the light values to print.
export interface Tokens { ink: RGB; secondary: RGB; accent: RGB; accentSoft: RGB; surface: RGB; muted: RGB; border: RGB; en: RGB; vi: RGB; warn: RGB; raw: Record<string,string>; }
function hex(h:string):RGB{ const s=h.replace('#',''); const v=parseInt(s.length===3?s.split('').map(c=>c+c).join(''):s,16); return rgb(((v>>16)&255)/255,((v>>8)&255)/255,(v&255)/255); }
export function loadTokens(cssPath='node_modules/@astryxdesign/theme-neutral/dist/theme.css'):Tokens{
  const raw:Record<string,string>={};
  if(existsSync(cssPath)){ const css=readFileSync(cssPath,'utf8'); for(const m of css.matchAll(/(--[\w-]+)\s*:\s*([^;]+);/g)) raw[m[1]]=m[2].trim(); }
  const pick=(k:string,fb:string)=>{ const v=raw[k]??''; const m=v.match(/#[0-9a-fA-F]{3,8}/); return hex(m?m[0]:fb); };
  return { raw, ink:pick('--color-text-primary','#111111'), secondary:pick('--color-text-secondary','#474747'), accent:hex('#6741d9'), accentSoft:hex('#ece7fb'), surface:pick('--color-background-surface','#ffffff'), muted:pick('--color-background-muted','#f1f1f1'), border:hex('#d9d4e8'), en:hex('#12355b'), vi:hex('#5b2333'), warn:hex('#8a5a00') };
}
