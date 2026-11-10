# Fonts

| File | Family | Licence |
| :--- | :--- | :--- |
| `DejaVuSerif*.ttf` | DejaVu Serif (regular, bold, italic, bold-italic) | Bitstream Vera / DejaVu licence (permissive, attribution) |
| `DejaVuSans*.ttf` | DejaVu Sans (regular, bold, oblique, bold-oblique) | Bitstream Vera / DejaVu licence (permissive, attribution) |
| `DejaVuSansMono*.ttf` | DejaVu Sans Mono | Bitstream Vera / DejaVu licence (permissive, attribution) |

Chosen for complete Vietnamese diacritic coverage: every glyph in the edition's Vietnamese text
exists in these faces, which is not true of many web-oriented typefaces. See
<https://dejavu-fonts.github.io/> for the full licence text.

`src/engine/page.ts` registers all ten faces; `tests/pdf.test.ts` asserts that the resulting PDF
embeds font programmes rather than referencing standard (non-embedded) fonts.
