import fs from 'fs';
import path from 'path';

function runValidationTests() {
  console.log('Running TypeScript Validation Test Suite for Astryx Neuromancer Edition...');

  const dataPath = path.resolve('data/bilingual_novel.json');
  const htmlPath = path.resolve('data/novel_bilingual.html');
  const pdfPath = path.resolve('output/neuromancer_bilingual_edition.pdf');

  if (!fs.existsSync(dataPath)) {
    throw new Error('data/bilingual_novel.json does not exist!');
  }
  if (!fs.existsSync(htmlPath)) {
    throw new Error('data/novel_bilingual.html does not exist!');
  }
  if (!fs.existsSync(pdfPath)) {
    throw new Error('output/neuromancer_bilingual_edition.pdf does not exist!');
  }

  const rawJson = fs.readFileSync(dataPath, 'utf-8');
  const novel = JSON.parse(rawJson);

  // Assert target benchmarks
  const benchmarks = novel.target_benchmarks;
  if (!benchmarks.IELTS.includes('7.0')) {
    throw new Error('Benchmark IELTS 7.0 not found');
  }
  if (!benchmarks.TOEFL_iBT.includes('90+') && !benchmarks.TOEFL_iBT.includes('5.0')) {
    throw new Error('Benchmark TOEFL iBT 90+ / 5.0 not found');
  }
  if (!benchmarks.Cambridge.includes('185') || !benchmarks.Cambridge.includes('C1')) {
    throw new Error('Benchmark Cambridge 185 (C1/C2) not found');
  }
  if (!benchmarks.PTE_Academic.includes('65')) {
    throw new Error('Benchmark PTE Academic 65 not found');
  }
  if (!benchmarks.DET.includes('120')) {
    throw new Error('Benchmark DET 120 not found');
  }

  // Assert parts & chapters
  if (novel.parts.length !== 5) {
    throw new Error(`Expected 5 parts, got ${novel.parts.length}`);
  }

  let totalChapters = 0;
  let totalParagraphs = 0;
  for (const part of novel.parts) {
    totalChapters += part.chapters.length;
    for (const chap of part.chapters) {
      if (!chap.study_guide || !chap.study_guide.summary_vi) {
        throw new Error(`Chapter ${chap.chapter_index} is missing study guide!`);
      }
      totalParagraphs += chap.paragraphs.length;
      for (const p of chap.paragraphs) {
        if (!p.en || p.en.trim().length === 0) {
          throw new Error(`Empty English paragraph in chap ${chap.chapter_index}`);
        }
        if (!p.vi || p.vi.trim().length === 0) {
          throw new Error(`Empty Vietnamese paragraph in chap ${chap.chapter_index}`);
        }
      }
    }
  }

  if (totalChapters !== 24) {
    throw new Error(`Expected 24 chapters, got ${totalChapters}`);
  }
  if (totalParagraphs !== 2598) {
    throw new Error(`Expected 2598 paragraphs, got ${totalParagraphs}`);
  }

  // Check PDF magic header and size
  const pdfBuffer = Buffer.alloc(4);
  const fd = fs.openSync(pdfPath, 'r');
  fs.readSync(fd, pdfBuffer, 0, 4, 0);
  fs.closeSync(fd);
  if (pdfBuffer.toString() !== '%PDF') {
    throw new Error('Output is not a valid PDF file');
  }

  const pdfStats = fs.statSync(pdfPath);
  if (pdfStats.size < 1_000_000) {
    throw new Error(`PDF file size too small: ${pdfStats.size} bytes`);
  }

  console.log(`✅ All tests passed!`);
  console.log(`- Chapters: ${totalChapters}`);
  console.log(`- Paragraphs: ${totalParagraphs}`);
  console.log(`- Benchmarks verified: IELTS 7.0, TOEFL 90/5.0, Cambridge 185 (C1/C2), PTE 65, DET 120`);
  console.log(`- PDF Size: ${(pdfStats.size / (1024 * 1024)).toFixed(2)} MB`);
}

runValidationTests();
