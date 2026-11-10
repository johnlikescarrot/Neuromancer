import type {
  Book,
  ChapterUnit,
  GlossaryEntry,
  GrammarUnit,
  GuideEntry,
  Mcq,
  ProseSection,
} from "../model.js";
import { printCss } from "../design/print-css.js";

const esc = (s: string): string =>
  s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

function chips(items: string[], cls = "theme"): string {
  return `<div class="chips">${items.map((t) => `<span class="chip ${cls}">${esc(t)}</span>`).join("")}</div>`;
}

function mcq(q: Mcq, tag: string): string {
  const letters = ["A", "B", "C", "D"];
  return `
  <div class="panel practice avoid">
    <h4><span class="tag">${esc(tag)}</span> Practice · Luyện tập</h4>
    <div class="stem">${esc(q.stem.en)}<span class="vi">${esc(q.stem.vi)}</span></div>
    <ol type="A">
      ${q.options.map((o, i) => `<li><strong>${letters[i]}.</strong> ${esc(o)}</li>`).join("")}
    </ol>
    <div class="answer-note">Answer key at the back · Đáp án ở cuối sách (${esc(q.id)})</div>
  </div>`;
}

function proseSection(s: ProseSection): string {
  return `
  <section class="page-break" id="${esc(s.id)}">
    <div class="kicker">Section · <span class="accent">${esc(s.id)}</span></div>
    <h2 style="margin:1.5mm 0 3mm 0">${esc(s.title.en)}</h2>
    <p class="small" style="margin-bottom:3mm"><em>${esc(s.title.vi)}</em></p>
    ${s.paragraphs.map((p) => `<div class="synopsis-en"><p>${esc(p.en)}</p></div><div class="synopsis-vi"><div class="lbl">Tóm tắt tiếng Việt</div><p>${esc(p.vi)}</p></div>`).join("")}
    ${s.bullets ? `<ul class="mech">${s.bullets.map((b) => `<li>${esc(b.en)}<span class="vi">${esc(b.vi)}</span></li>`).join("")}</ul>` : ""}
  </section>`;
}

function guideEntry(e: GuideEntry): string {
  return `
  <div class="panel avoid" style="border-left-color:var(--blue)">
    <h4>${esc(e.name)} <span class="chip mono" style="margin-left:2mm">${esc(e.kind)}</span></h4>
    <p>${esc(e.summary.en)}</p>
    <p class="small" style="font-family:var(--vi)">${esc(e.summary.vi)}</p>
    <p class="small"><strong>Study value · Giá trị học tập:</strong> ${esc(e.studyValue.en)} <span style="font-family:var(--vi)">${esc(e.studyValue.vi)}</span></p>
  </div>`;
}

function chapterUnit(u: ChapterUnit, gloss: Map<string, GlossaryEntry>, gmap: Map<string, GrammarUnit>): string {
  const vocabRows = u.vocab
    .map((id) => gloss.get(id))
    .filter((x): x is GlossaryEntry => Boolean(x))
    .map(
      (v) => `<tr>
        <td class="term">${esc(v.term)}<span class="ipa">${esc(v.ipa)} · ${esc(v.pos)}</span></td>
        <td class="vi">${esc(v.glossVi)}</td>
        <td class="def">${esc(v.defEn)}</td>
      </tr>`,
    )
    .join("");
  const gx = u.grammarRefs
    .map((id) => gmap.get(id))
    .filter((x): x is GrammarUnit => Boolean(x))
    .map(
      (gq) => `<div class="gx"><div class="lbl">Grammar · Ngữ pháp</div>
        <div class="t">${esc(gq.title.en)}</div>
        <div class="s">${esc(gq.whatItIs.en.slice(0, 110))}…</div></div>`,
    )
    .join("");
  return `
  <section class="unit" id="${esc(u.id)}" data-mark="UNIT ${u.number.padStart(2, "0")}">
    <div class="unit-head">
      <div class="row"><span class="chipnum">UNIT ${esc(u.number.padStart(2, "0"))}</span>
        <span class="kicker">${esc(u.partId.toUpperCase())} · ${u.examLens.map(esc).join(" · ")}</span></div>
      <h2>${esc(u.title.en)}</h2>
      <div class="vi-title">${esc(u.title.vi)}</div>
      ${chips(u.themes)}
    </div>
    <div class="synopsis-en"><p>${esc(u.synopsis.en)}</p></div>
    <div class="synopsis-vi"><div class="lbl">Tóm tắt chương · Chapter synopsis</div><p>${esc(u.synopsis.vi)}</p></div>
    <div class="craft-note avoid"><div class="lbl">Craft note · Ghi chú kỹ thuật</div>
      <p>${esc(u.craftNote.en)}</p><p class="vi">${esc(u.craftNote.vi)}</p></div>
    <h3 style="margin:3mm 0 1mm 0">Vocabulary · Từ vựng</h3>
    <table class="vocab">
      <thead><tr><th>Term · Từ</th><th>Nghĩa tiếng Việt</th><th>Definition (EN)</th></tr></thead>
      <tbody>${vocabRows}</tbody>
    </table>
    <div class="grammar-xref">${gx}</div>
    ${mcq(u.practice, `UNIT ${u.number.padStart(2, "0")}`)}
    <div class="panel prompt avoid"><h4>Writing prompt · Đề viết</h4>
      <p>${esc(u.writingPrompt.en)}</p>
      <p class="small" style="font-family:var(--vi)">${esc(u.writingPrompt.vi)}</p></div>
  </section>`;
}

function grammarUnit(gq: GrammarUnit, idx: number): string {
  const code = `GRAMMAR G${String(idx + 1).padStart(2, "0")}`;
  return `
  <section class="g-unit" id="${esc(gq.id)}" data-mark="${esc(code)}">
    <div class="kicker">${esc(code)} · Grammar &amp; Rhetoric · Chuyên đề Ngữ pháp</div>
    <h2 style="margin:1.5mm 0 3mm 0">${esc(gq.title.en)}</h2>
    <p class="small" style="margin-bottom:3mm"><em>${esc(gq.title.vi)}</em></p>
    <div class="what avoid"><p>${esc(gq.whatItIs.en)}</p><p class="vi">${esc(gq.whatItIs.vi)}</p></div>
    <h3>Mechanics · Cơ chế</h3>
    <ul class="mech">${gq.mechanics.map((m) => `<li>${esc(m.en)}<span class="vi">${esc(m.vi)}</span></li>`).join("")}</ul>
    <h3>Examples · Ví dụ</h3>
    ${gq.examples
      .map(
        (ex) => `<div class="example-row"><div class="good">${esc(ex.good)}</div>
        <div class="note">${esc(ex.note.en)}<span class="vi">${esc(ex.note.vi)}</span></div></div>`,
      )
      .join("")}
    ${mcq(gq.practice, "GRAMMAR")}
    <div class="panel warn avoid"><h4>Exam value · Giá trị thi cử</h4>
      <p>${esc(gq.examValue.en)}</p><p class="small" style="font-family:var(--vi)">${esc(gq.examValue.vi)}</p></div>
  </section>`;
}

function glossaryEntry(v: GlossaryEntry): string {
  return `
  <div class="gloss-entry">
    <div class="head">
      <span class="term">${esc(v.term)}</span>
      <span class="ipa">${esc(v.ipa)}</span>
      <span class="pos">${esc(v.pos)}</span>
      <span class="chip cefr-${esc(v.cefr)}">${esc(v.cefr)}</span>
      <span class="chip">${esc(v.domain)}</span>
    </div>
    <div class="def">${esc(v.defEn)}</div>
    <div class="vi">${esc(v.glossVi)}</div>
    <div class="coll">${v.collocations.map(esc).join(" · ")}</div>
    <div class="ex">${esc(v.example)}</div>
  </div>`;
}

function answerKey(book: Book): string {
  const groups: { label: string; items: Mcq[] }[] = [
    {
      label: "Chapter units · Đơn vị chương",
      items: book.parts.flatMap((p) => p.chapters.map((c) => c.practice)),
    },
    { label: "Grammar masterclass · Chuyên đề ngữ pháp", items: book.grammar.map((gq) => gq.practice) },
    { label: "Exam playbooks · Cẩm nang đề thi", items: book.exams.flatMap((e) => e.practice) },
  ];
  const letters = ["A", "B", "C", "D"];
  return `
  <section class="page-break" id="answers" data-mark="Answer Key">
    <div class="kicker">Appendix · Phụ lục</div>
    <h2 style="margin:1.5mm 0 4mm 0">Answer Key · Đáp án</h2>
    <div class="answer-key">
    ${groups
      .map(
        (gq) => `<div class="grp"><h4>${esc(gq.label)}</h4>
        ${gq.items
          .map(
            (q) => `<div class="row"><span class="id">${esc(q.id)}</span>
              <span class="ex"><strong>${letters[q.answer]}</strong> — ${esc(q.explain.en)}
              <br><em style="font-family:var(--vi)">${esc(q.explain.vi)}</em></span></div>`,
          )
          .join("")}
        </div>`,
      )
      .join("")}
    </div>
  </section>`;
}

interface TocRow {
  mark: string;
  num: string;
  title: string;
  vi: string;
}

function collectToc(book: Book): TocRow[] {
  const rows: TocRow[] = [
    { mark: "How this companion works", num: "§1", title: "How this companion works", vi: "Cẩm nang này hoạt động ra sao" },
    { mark: "Target Credentials", num: "§2", title: "Target credentials & concordance", vi: "Chứng chỉ mục tiêu & quy đổi" },
    { mark: "The book and its coronation", num: "§3", title: "The novel in context", vi: "Tiểu thuyết trong bối cảnh" },
    { mark: "Character guide", num: "§4", title: "Character · Location · Concept guides", vi: "Hướng dẫn nhân vật · địa điểm · khái niệm" },
    { mark: "Close reading: one sentence, four moves", num: "§5", title: "Close reading & translation notebook", vi: "Đọc kỹ & sổ tay dịch thuật" },
  ];
  for (const p of book.parts) {
    rows.push({ mark: p.label.toUpperCase(), num: p.label, title: p.title.en, vi: p.title.vi });
    for (const c of p.chapters) {
      rows.push({ mark: `UNIT ${c.number.padStart(2, "0")}`, num: `U${c.number.padStart(2, "0")}`, title: c.title.en, vi: c.title.vi });
    }
  }
  rows.push({ mark: "GRAMMAR", num: "§6", title: "Grammar & Rhetoric Masterclass (16 units)", vi: "Chuyên đề Ngữ pháp & Tu từ" });
  rows.push({ mark: "GLOSSARY", num: "§7", title: "Academic Glossary", vi: "Từ điển Học thuật" });
  rows.push({ mark: "Exam Playbooks", num: "§8", title: "Exam playbooks: TOEFL · IELTS · PTE · Cambridge · DET", vi: "Cẩm nang đề thi" });
  rows.push({ mark: "Study Plans", num: "§9", title: "Study plans & C1 rubric", vi: "Kế hoạch học & thang C1" });
  rows.push({ mark: "Answer Key", num: "§10", title: "Answer key", vi: "Đáp án" });
  rows.push({ mark: "Gibson, William. Neuromancer", num: "§11", title: "Bibliography & sources", vi: "Thư mục & nguồn" });
  return rows;
}

export function renderHtml(book: Book, fontCss: string, pageMap: Map<string, number> = new Map()): string {
  const gloss = new Map(book.glossary.map((v) => [v.id, v]));
  const gmap = new Map(book.grammar.map((v) => [v.id, v]));
  const tocRows = collectToc(book);

  const tocHtml = tocRows
    .map((r) => {
      const pg = pageMap.get(r.mark);
      return `<div class="toc-row"><span class="num">${esc(r.num)}</span>
        <span class="t">${esc(r.title)} <span class="vi">${esc(r.vi)}</span></span>
        <span class="dots">····</span><span class="pg">${pg ? String(pg) : ""}</span></div>`;
    })
    .join("");

  const glossaryHtml = [...book.glossary]
    .sort((a, b) => a.term.localeCompare(b.term))
    .map(glossaryEntry)
    .join("");

  const alphaHeads = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W", "Z"];

  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>${esc(book.meta.title.en)} — ${esc(book.meta.subtitle.en)}</title>
<style>${printCss(fontCss)}</style>
</head>
<body>

<!-- ============ COVER ============ -->
<div class="cover">
  <div class="corner">EDITION ${esc(book.meta.edition)}<br>${esc(book.meta.date)}<br>A4 · BILINGUAL EN/VI</div>
  <div class="monogram">N</div>
  <div class="rule-gold"></div>
  <div class="display">NEUROMANCER<br><span class="ghost">ACADEMIC</span><br>COMPANION</div>
  <div class="vi-title">${esc(book.meta.title.vi)}<br>${esc(book.meta.subtitle.vi)}</div>
  <div class="subtitle">${esc(book.meta.subtitle.en)}. An independent bilingual study layer for readers preparing C1-C2 English credentials: chapter units, grammar masterclass, a 220-entry academic glossary, and exam playbooks. Original study apparatus; the novel is not reproduced.</div>
  <div class="spacer"></div>
  <div class="benchmark-strip">
    <div class="badge">TOEFL <b>90 / B5.0</b></div>
    <div class="badge">IELTS <b>7.0</b></div>
    <div class="badge">PTE <b>65</b></div>
    <div class="badge">CAMBRIDGE <b>185</b></div>
    <div class="badge">DET <b>120</b></div>
  </div>
  <div class="edition-line">TypeScript · Astryx theme-gothic · Fontsource · Built ${esc(book.meta.date)}</div>
</div>

<!-- ============ LEGAL ============ -->
<section class="page-break" id="legal" data-mark="Copyright">
  <div class="kicker">Colophon &amp; Legal · Thông tin bản quyền</div>
  ${book.legal
    .map(
      (s) => `<h3 style="margin:4mm 0 2mm 0">${esc(s.title.en)} <span class="small">· ${esc(s.title.vi)}</span></h3>
      ${s.paragraphs.map((p) => `<div class="legal-text"><p>${esc(p.en)}</p><p style="font-family:var(--vi)">${esc(p.vi)}</p></div>`).join("")}`,
    )
    .join("")}
  <hr class="thin">
  <p class="small">Toolkit: ${esc(book.meta.toolkit)}. Typography: Manufacturing Consent &amp; UnifrakturMaguntia (Astryx gothic display roles), Playfair Display, Fustat, Source Serif 4, Inter, JetBrains Mono (OFL via Fontsource).</p>
</section>

<!-- ============ TOC ============ -->
<section class="page-break" id="toc">
  <div class="kicker">Contents · Mục lục</div>
  <h2 style="margin:1.5mm 0 4mm 0">Book Map · Sơ đồ sách</h2>
  <div class="toc-part">${tocHtml}</div>
</section>

<!-- ============ HOW TO USE ============ -->
${book.howToUse.map(proseSection).join("")}

<!-- ============ BENCHMARKS ============ -->
<section class="page-break" id="benchmarks" data-mark="Benchmarks">
  <div class="kicker">Standards · Chuẩn năng lực</div>
  <h2 style="margin:1.5mm 0 1mm 0">Target Credentials · Chứng chỉ mục tiêu</h2>
  <p class="small" style="margin-bottom:4mm"><em>Mục tiêu năng lực của ấn bản, đúng theo yêu cầu biên soạn.</em></p>
  <table class="data">
    <thead><tr><th>Test</th><th>Target</th><th>CEFR</th><th>What it proves</th><th>How this edition trains it</th></tr></thead>
    <tbody>
      ${book.benchmarks
        .map(
          (b) => `<tr>
          <td><strong>${esc(b.test)}</strong></td>
          <td><b class="mono">${esc(b.target)}</b></td>
          <td><span class="chip cefr-C1">${esc(b.cefr)}</span></td>
          <td>${esc(b.whatItProves.en)}<span class="vi">${esc(b.whatItProves.vi)}</span></td>
          <td>${esc(b.editionUse.en)}<span class="vi">${esc(b.editionUse.vi)}</span></td>
        </tr>`,
        )
        .join("")}
    </tbody>
  </table>
  <h3 style="margin:4mm 0 2mm 0">Indicative concordance · Bảng quy đổi tham khảo</h3>
  <table class="data">
    <thead><tr><th>CEFR</th><th>IELTS</th><th>TOEFL 0-120</th><th>TOEFL 1-6</th><th>PTE</th><th>DET</th><th>Cambridge</th></tr></thead>
    <tbody>
      ${book.concordance
        .map(
          (c) => `<tr><td>${esc(c.cefr)}</td><td class="mono">${esc(c.ielts)}</td><td class="mono">${esc(c.toeflLegacy)}</td>
          <td class="mono">${esc(c.toeflBand)}</td><td class="mono">${esc(c.pte)}</td><td class="mono">${esc(c.det)}</td><td class="mono">${esc(c.cambridge)}</td></tr>`,
        )
        .join("")}
    </tbody>
  </table>
  <p class="small">Mappings are indicative, drawn from each test owner's published concordance (see Bibliography). Always verify the exact requirement of your institution. · Các quy đổi mang tính tham khảo, dựa trên bảng công bố của từng đơn vị tổ chức thi (xem Thư mục). Luôn kiểm tra yêu cầu cụ thể của cơ sở bạn nộp hồ sơ.</p>
</section>

<!-- ============ CONTEXT ============ -->
<section class="page-break" id="context" data-mark="The book and its coronation">
  <div class="kicker">Part I · Background · Bối cảnh</div>
  <h1 style="margin:2mm 0 2mm 0">The Novel in Context</h1>
  <p class="small" style="margin-bottom:5mm"><em>Tiểu thuyết trong bối cảnh: lịch sử, phong cách và các chủ đề lớn.</em></p>
  ${book.context
    .map(
      (s) => `<div class="avoid" style="margin-bottom:6mm">
      <h3>${esc(s.title.en)} <span class="small">· ${esc(s.title.vi)}</span></h3>
      ${s.paragraphs.map((p) => `<p>${esc(p.en)}</p><p class="small" style="font-family:var(--vi)">${esc(p.vi)}</p>`).join("")}
    </div>`,
    )
    .join("")}
</section>

<!-- ============ GUIDES ============ -->
<section class="page-break" id="guides" data-mark="Character Guide">
  <div class="kicker">Part II · Guides · Hướng dẫn</div>
  <h1 style="margin:2mm 0 4mm 0">Character · Location · Concept</h1>
  <h3>Character guide · Chân dung nhân vật</h3>
  ${book.characters.map(guideEntry).join("")}
  <h3 style="margin-top:5mm">Location guide · Địa bàn</h3>
  ${book.locations.map(guideEntry).join("")}
  <h3 style="margin-top:5mm">Concept guide · Khái niệm</h3>
  ${book.concepts.map(guideEntry).join("")}
</section>

<!-- ============ CLOSE READING ============ -->
<section class="page-break" id="close-reading" data-mark="Close reading">
  <div class="kicker">Part III · Craft · Kỹ thuật</div>
  <h1 style="margin:2mm 0 1mm 0">${esc(book.closeReading.title.en)}</h1>
  <p class="small" style="margin-bottom:4mm"><em>${esc(book.closeReading.title.vi)}</em></p>
  <div class="pull-quote">
    <div class="en">“${esc(book.closeReading.quote.text)}”</div>
    <div class="vi">“Bầu trời phía trên bến cảng mang màu của chiếc tivi, dò phải một kênh chết.”</div>
    <div class="attr">${esc(book.closeReading.quote.attribution)}</div>
    <div class="small" style="margin-top:2mm">${esc(book.closeReading.quote.note.en)}<br><em>${esc(book.closeReading.quote.note.vi)}</em></div>
  </div>
  <div class="steps">
    ${book.closeReading.steps
      .map((s) => `<div class="step"><div class="n"></div><div class="b">${esc(s.en)}<span class="vi">${esc(s.vi)}</span></div></div>`)
      .join("")}
  </div>
  ${book.translationNotebook.map(proseSection).join("").replace('class="page-break"', 'class=""')}
</section>

<!-- ============ PARTS & UNITS ============ -->
${book.parts
  .map(
    (p) => `
  <section class="opener" data-mark="PART ${p.label.replace("Part ", "").toUpperCase()}">
    <div class="roman">${esc(p.label.toUpperCase())}</div>
    <h1>${esc(p.title.en)}</h1>
    <div class="vi-sub">${esc(p.title.vi)}</div>
    <div class="argument">${esc(p.argument.en)}<div class="vi">${esc(p.argument.vi)}</div></div>
  </section>
  ${p.chapters.map((c) => chapterUnit(c, gloss, gmap)).join("")}`,
  )
  .join("")}

<!-- ============ GRAMMAR ============ -->
<section class="opener" data-mark="Grammar & Rhetoric Masterclass">
  <div class="roman">GRAMMAR</div>
  <h1>Grammar &amp; Rhetoric Masterclass</h1>
  <div class="vi-sub">Chuyên đề Ngữ pháp &amp; Tu từ</div>
  <div class="argument">Sixteen structures that literary prose uses at full voltage, each with bilingual mechanics, original examples, and one exam item. The Cambridge Use of English engine room.<div class="vi">Mười sáu cấu trúc mà văn xuôi văn chương dùng ở điện thế đầy, mỗi cấu trúc có cơ chế song ngữ, ví dụ nguyên bản và một câu hỏi thi. Động cơ của Use of English Cambridge.</div></div>
</section>
${book.grammar.map((gq, i) => grammarUnit(gq, i)).join("")}

<!-- ============ GLOSSARY ============ -->
<section class="opener" data-mark="Academic Glossary">
  <div class="roman">GLOSSARY</div>
  <h1>Academic Glossary · Từ điển Học thuật</h1>
  <div class="vi-sub">220 entries · CEFR-tagged · IPA · collocations</div>
  <div class="argument">One engine for the whole book: chapter vocabulary points here, exam playbooks drill here, study plans schedule here. Learn an entry aloud: definition, then Vietnamese gloss, then one collocation in your own sentence.<div class="vi">Một động cơ cho cả cuốn sách: từ vựng chương trỏ tới đây, cẩm nang đề thi luyện tại đây, kế hoạch học lên lịch cho đây. Hãy học một mục thành tiếng: định nghĩa, rồi chú nghĩa Việt, rồi một cụm từ đi kèm trong câu của bạn.</div></div>
</section>
<section class="glossary-cols">
  ${glossaryHtml}
</section>

<!-- ============ EXAMS ============ -->
<section class="opener" data-mark="Exam Playbooks">
  <div class="roman">EXAMS</div>
  <h1>Exam Playbooks · Cẩm nang Đề thi</h1>
  <div class="vi-sub">TOEFL · IELTS · PTE · Cambridge · Duolingo</div>
  <div class="argument">Five playbooks, one method: know the scale, know the item types, train with this book's units, and manage the day.<div class="vi">Năm cẩm nang, một phương pháp: hiểu thang điểm, hiểu dạng câu hỏi, luyện với các đơn vị của sách, và làm chủ ngày thi.</div></div>
</section>
${book.exams
  .map(
    (e) => `
  <section class="page-break" id="${esc(e.id)}">
    <div class="exam-hero">
      <div class="kicker">Playbook · Cẩm nang</div>
      <h2>${esc(e.test)}</h2>
      <div class="target">TARGET · ${esc(e.target)}</div>
      <div class="scale-note">${esc(e.scaleNote.en)}<br><em>${esc(e.scaleNote.vi)}</em></div>
    </div>
    <h3>Format snapshot · Tóm tắt cấu trúc</h3>
    <ul class="mech">${e.formatBullets.map((f) => `<li>${esc(f.en)}<span class="vi">${esc(f.vi)}</span></li>`).join("")}</ul>
    <h3>What C1 looks like here · C1 trông ra sao</h3>
    <ul class="mech">${e.c1Profile.map((f) => `<li>${esc(f.en)}<span class="vi">${esc(f.vi)}</span></li>`).join("")}</ul>
    <h3>Training map · Lộ trình luyện</h3>
    <table class="map">
      <thead><tr><th>Skill</th><th>How to train with this book</th></tr></thead>
      <tbody>${e.trainingMap
        .map((t) => `<tr><td class="skill">${esc(t.skill)}</td><td>${esc(t.use.en)}<span class="vi">${esc(t.use.vi)}</span></td></tr>`)
        .join("")}</tbody>
    </table>
    <div class="strategy-grid">
      ${e.strategies
        .map(
          (s) => `<div class="card"><div class="t">${esc(s.title.en)}</div>
        <div class="b">${esc(s.body.en)}<span class="vi">${esc(s.body.vi)}</span></div></div>`,
        )
        .join("")}
    </div>
    ${e.practice.map((q) => mcq(q, e.test.toUpperCase())).join("")}
  </section>`,
  )
  .join("")}

<!-- ============ PLANS ============ -->
<section class="page-break" id="plans" data-mark="Study Plans">
  <div class="kicker">Part IV · Practice · Luyện tập</div>
  <h1 style="margin:2mm 0 1mm 0">Study Plans · Kế hoạch Học tập</h1>
  ${book.plans
    .map(
      (p) => `<h3 style="margin:4mm 0 1mm 0">${esc(p.title.en)} <span class="small">· ${esc(p.title.vi)}</span></h3>
    <p class="small">${esc(p.intro.en)}<br><em style="font-family:var(--vi)">${esc(p.intro.vi)}</em></p>
    ${p.weeks
      .map(
        (w) => `<div class="plan-week"><div class="wk">${esc(w.week)}</div>
      <div class="focus">${esc(w.focus.en)}<span class="vi">${esc(w.focus.vi)}</span></div>
      <ul>${w.tasks.map((t) => `<li>${esc(t.en)}<span class="vi">${esc(t.vi)}</span></li>`).join("")}</ul>
      <div class="out"><strong>Output · Sản phẩm:</strong> ${esc(w.output.en)}<span class="vi">${esc(w.output.vi)}</span></div></div>`,
      )
      .join("")}`,
    )
    .join("")}
  <h3 style="margin:5mm 0 2mm 0">C1 self-assessment rubric · Thang tự đánh giá C1</h3>
  <table class="data">
    <thead><tr><th>Skill</th><th>C1 evidence</th><th>Self-test</th></tr></thead>
    <tbody>${book.rubric
      .map(
        (r) => `<tr><td><strong>${esc(r.skill)}</strong></td>
      <td>${esc(r.c1Evidence.en)}<span class="vi">${esc(r.c1Evidence.vi)}</span></td>
      <td>${esc(r.selfTest.en)}<span class="vi">${esc(r.selfTest.vi)}</span></td></tr>`,
      )
      .join("")}</tbody>
  </table>
</section>

<!-- ============ ANSWERS ============ -->
${answerKey(book)}

<!-- ============ BIBLIOGRAPHY ============ -->
<section class="page-break" id="bibliography" data-mark="Bibliography">
  <div class="kicker">Sources · Nguồn</div>
  <h2 style="margin:1.5mm 0 4mm 0">Bibliography · Thư mục</h2>
  <div class="bib">
    ${book.bibliography
      .map((b) => `<div class="entry"><span class="id">[${esc(b.id)}]</span> ${esc(b.citation)}<span class="note">${esc(b.note)}</span></div>`)
      .join("")}
  </div>
  <hr class="thin">
  <p class="small">This companion was compiled as an original study work. It summarises and comments on Neuromancer (1984) in its own words; it reproduces one sentence of the novel for close reading and no other substantial text. · Cẩm nang này được biên soạn như một công trình học thuật nguyên bản. Nó tóm tắt và bình luận Neuromancer (1984) bằng lời của mình; chỉ trích dẫn đúng một câu của tiểu thuyết để đọc kỹ, không tái bản văn bản đáng kể nào khác.</p>
</section>

</body>
</html>`;
}
