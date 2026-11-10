# Archived: the v1 Python pipeline

These six files are the previous build system for this repository, kept for reference and
recoverable history. They are **not** part of the current build and are not run by any script,
test or CI job.

| File | What it did |
| :--- | :--- |
| `extract_text.py` | Pulled chapter text out of an EPUB into `data/extracted_novel.json` |
| `translate_novel.py` | Machine-translated the novel paragraph by paragraph via a public web endpoint |
| `build_bilingual_edition.py` | Assembled bilingual JSON plus an academic glossary |
| `render_html.py` | Wrote a single A4 HTML document with inline CSS |
| `generate_pdf.py` | Printed that HTML to PDF with Playwright/Chromium |
| `test_bilingual_edition.py` | Integrity tests for the v1 output |

**Why it was retired.** Two reasons, one technical and one editorial.

*Technical:* the v1 pipeline depended on a browser (Playwright plus a Chromium download) and on a
live translation endpoint, and it produced a 2.5 MB, ~358-page HTML-to-PDF print of a novel
rather than a designed book. The current TypeScript pipeline has no browser and no network
dependency, breaks its own lines, paginates deliberately, aligns the bilingual columns and
resolves its own table of contents.

*Editorial:* v1 generated a complete unauthorised translation of a novel still in copyright. The
current edition is an original companion — synopses, analysis, a levelled lexicon, exercises —
and reproduces none of the novel's text beyond a few words for critical analysis.
`tests/content.test.ts` now enforces that boundary mechanically.

`data/` still contains the v1 inputs (`extracted_novel.json`, `translated_cache.json`,
`bilingual_novel.json`, `novel_bilingual.html`). They are legacy artefacts, unused by the build.
