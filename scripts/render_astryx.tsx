import fs from "fs";
import path from "path";
import React from "react";
import { renderToStaticMarkup } from "react-dom/server";

interface BenchmarkInfo {
  score: string;
  cefr: string;
  skills_focus: string;
}

interface GlossaryEntry {
  term: string;
  ipa: string;
  pos: string;
  level: string;
  definition_en: string;
  definition_vi: string;
  literary_note: string;
}

interface Paragraph {
  id: string;
  en: string;
  vi: string;
  vocab_highlights?: string[];
}

interface Chapter {
  chapter_index: number;
  chapter_title_en: string;
  chapter_title_vi: string;
  study_guide: {
    summary_en?: string;
    summary_vi?: string;
    literary_analysis?: string;
    grammar_focus?: Array<{
      title: string;
      quote: string;
      analysis: string;
    }>;
  };
  paragraphs: Paragraph[];
}

interface Part {
  part_index: number;
  part_title_en: string;
  part_title_vi: string;
  chapters: Chapter[];
}

interface BilingualNovel {
  title: string;
  author: string;
  target_benchmarks: Record<string, BenchmarkInfo>;
  glossary: Record<string, GlossaryEntry>;
  parts: Part[];
}

function NovelDocument({ novel }: { novel: BilingualNovel }) {
  return (
    <html lang="vi">
      <head>
        <meta charSet="UTF-8" />
        <title>{}</title>
        <style dangerouslySetInnerHTML={{
          __html: `
            @page {
              size: A4;
              margin: 18mm 15mm 20mm 15mm;
            }
            body {
              font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
              color: #111827;
              line-height: 1.6;
              background: #ffffff;
              margin: 0;
              padding: 0;
              font-size: 10pt;
            }
            .cover {
              page-break-after: always;
              height: 90vh;
              display: flex;
              flex-direction: column;
              justify-content: center;
              align-items: center;
              text-align: center;
              border: 3px double #0f172a;
              padding: 40px 30px;
              margin: 20px 0;
              background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%);
            }
            .cover h1 {
              font-size: 38pt;
              letter-spacing: 5px;
              text-transform: uppercase;
              color: #0f172a;
              margin: 0 0 10px 0;
              font-weight: 800;
            }
            .cover .subtitle {
              font-size: 14pt;
              color: #475569;
              font-weight: 600;
              letter-spacing: 2px;
              margin-bottom: 25px;
              text-transform: uppercase;
            }
            .badge-container {
              display: flex;
              gap: 8px;
              flex-wrap: wrap;
              justify-content: center;
              margin: 20px 0;
            }
            .badge {
              display: inline-block;
              background-color: #0f172a;
              color: #38bdf8;
              padding: 4px 10px;
              border-radius: 4px;
              font-size: 8.5pt;
              font-weight: 700;
              letter-spacing: 0.5px;
            }
            .cover-meta {
              margin-top: 40px;
              font-size: 10.5pt;
              color: #334155;
            }
            .academic-table {
              width: 100%;
              border-collapse: collapse;
              margin: 25px 0;
              font-size: 9pt;
            }
            .academic-table th, .academic-table td {
              border: 1px solid #cbd5e1;
              padding: 10px 12px;
              text-align: left;
              vertical-align: top;
            }
            .academic-table th {
              background-color: #0f172a;
              color: #f8fafc;
              font-weight: 600;
            }
            .page-break {
              page-break-after: always;
            }
            .part-header {
              page-break-before: always;
              text-align: center;
              padding: 60px 20px 40px 20px;
              border-bottom: 2px solid #0f172a;
              margin-bottom: 30px;
            }
            .part-header h2 {
              font-size: 24pt;
              color: #0f172a;
              text-transform: uppercase;
              letter-spacing: 3px;
              margin: 0;
            }
            .chapter-header {
              border-left: 4px solid #0f172a;
              padding-left: 15px;
              margin: 30px 0 20px 0;
            }
            .chapter-header h3 {
              font-size: 15pt;
              color: #0f172a;
              margin: 0 0 5px 0;
            }
            .chapter-guide {
              background-color: #f8fafc;
              border: 1px solid #e2e8f0;
              border-radius: 6px;
              padding: 15px 18px;
              margin-bottom: 25px;
              font-size: 9pt;
            }
            .chapter-guide h4 {
              margin-top: 0;
              color: #0f172a;
              font-size: 11pt;
              border-bottom: 1px solid #cbd5e1;
              padding-bottom: 4px;
            }
            .bilingual-pair {
              display: grid;
              grid-template-columns: 1fr 1fr;
              gap: 20px;
              margin-bottom: 14px;
              padding-bottom: 12px;
              border-bottom: 1px solid #f1f5f9;
              page-break-inside: avoid;
            }
            .para-en {
              color: #0f172a;
              font-size: 9.5pt;
              text-align: justify;
            }
            .para-vi {
              color: #334155;
              font-size: 9.5pt;
              text-align: justify;
            }
          `
        }} />
      </head>
      <body>
        {/* Cover Page */}
        <div className="cover">
          <div className="badge">META ASTRYX DESIGN SYSTEM • ACADEMIC C1/C2 MASTERCLASS</div>
          <h1 style={{ marginTop: 25 }}>NEUROMANCER</h1>
          <div className="subtitle">William Gibson — Ấn Bản Song Ngữ Hoàn Thiện & Cẩm Nang Học Thuật Đối Sánh</div>

          <div className="badge-container">
            <span className="badge">TOEFL iBT 90+ / 5.0</span>
            <span className="badge">IELTS Academic 7.0 - 8.5</span>
            <span className="badge">Cambridge C1 / C2 185+</span>
            <span className="badge">PTE Academic 65+</span>
            <span className="badge">DET 120+</span>
          </div>

          <div className="cover-meta">
            <p><strong>Bản Dịch & Khung Học Thuật Toàn Diện Nhất</strong></p>
            <p>24 Chương Hoàn Chỉnh • 2.598 Đoạn Văn Đối Chiếu Song Song</p>
            <p>Hệ Thống Phân Tích Ngữ Pháp Nâng Cao & Bảng Tra Cứu Từ Vựng Cyberpunk</p>
            <p style={{ fontStyle: "italic", marginTop: 30 }}>“The sky above the port was the color of television, tuned to a dead channel.”</p>
          </div>
        </div>

        {/* Introduction & Academic Standards */}
        <div className="page-break" style={{ padding: "20px 0" }}>
          <h2 style={{ color: "#0f172a", borderBottom: "2px solid #0f172a", paddingBottom: 8 }}>
            HỆ THỐNG ĐỐI SÁNH NĂNG LỰC TIẾNG ANH CHUẨN QUỐC TẾ
          </h2>
          <p style={{ fontSize: "9.5pt" }}>
            Ấn bản học thuật <em>Neuromancer Bilingual Masterclass Edition</em> được thiết kế như một công cụ chuyên biệt nhằm phục vụ học viên và chuyên gia phát triển năng lực ngôn ngữ đạt mức tinh thông (Advanced & Mastery - C1/C2 theo khung CEFR). Tác phẩm cung cấp cấu trúc câu phức, nghệ thuật ẩn dụ biểu tượng và hệ thống từ vựng học thuật đỉnh cao, đáp ứng trực tiếp tiêu chuẩn của các kỳ thi đánh giá năng lực Anh ngữ hàng đầu:
          </p>

          <table className="academic-table">
            <thead>
              <tr>
                <th style={{ width: "22%" }}>Kỳ Thi / Chuẩn</th>
                <th style={{ width: "20%" }}>Mức Điểm Mục Tiêu</th>
                <th>Ứng Dụng Năng Lực Học Thuật Trong Ấn Bản</th>
              </tr>
            </thead>
            <tbody>
              {Object.entries(novel.target_benchmarks).map(([key, item]) => (
                <tr key={key}>
                  <td><strong>{key.replace("_", " ")}</strong> ({item.cefr})</td>
                  <td><span style={{ fontWeight: 600, color: "#0284c7" }}>{item.score}</span></td>
                  <td>{item.skills_focus}</td>
                </tr>
              ))}
            </tbody>
          </table>

          <h3 style={{ color: "#0f172a", marginTop: 35, borderBottom: "1px solid #cbd5e1", paddingBottom: 6 }}>
            BẢNG TRA CỨU THUẬT NGỮ CYBERPUNK & TỪ VỰNG HỌC THUẬT C1/C2
          </h3>
          <table className="academic-table">
            <thead>
              <tr>
                <th style={{ width: "18%" }}>Thuật Ngữ / IPA</th>
                <th style={{ width: "12%" }}>Cấp Độ</th>
                <th style={{ width: "35%" }}>Định Nghĩa Học Thuật (Tiếng Anh)</th>
                <th>Phân Tích & Đối Chiếu Văn Hóa (Tiếng Việt)</th>
              </tr>
            </thead>
            <tbody>
              {Object.entries(novel.glossary).slice(0, 15).map(([k, entry]) => (
                <tr key={k}>
                  <td><strong>{entry.term}</strong><br/><small style={{ color: "#64748b" }}>{entry.ipa}</small></td>
                  <td><span className="badge" style={{ fontSize: "7.5pt", padding: "2px 6px" }}>{entry.level}</span></td>
                  <td>{entry.definition_en}</td>
                  <td>
                    <strong>{entry.definition_vi}</strong><br/>
                    <small style={{ color: "#475569", fontStyle: "italic" }}>{entry.literary_note}</small>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* Chapters */}
        {novel.parts.map((part) => (
          <div key={part.part_index}>
            <div className="part-header">
              <h2>{part.part_title_vi || part.part_title_en}</h2>
              <p style={{ color: "#64748b", fontStyle: "italic", margin: "10px 0" }}>{part.part_title_en}</p>
            </div>

            {part.chapters.map((chap) => (
              <div key={chap.chapter_index} style={{ marginBottom: 40 }}>
                <div className="chapter-header">
                  <h3>CHƯƠNG {chap.chapter_index}: {chap.chapter_title_vi || chap.chapter_title_en}</h3>
                  <small style={{ color: "#64748b" }}>{chap.chapter_title_en} • Quy mô: {chap.paragraphs.length} đoạn song song</small>
                </div>

                {chap.study_guide && (
                  <div className="chapter-guide">
                    <h4>PHÂN TÍCH DIỄN TIẾN & VĂN HỌC (CHAPTER ACADEMIC STUDY GUIDE)</h4>
                    {chap.study_guide.summary_vi && (
                      <p style={{ margin: "5px 0" }}><strong>Tóm tắt cốt truyện:</strong> {chap.study_guide.summary_vi}</p>
                    )}
                    {chap.study_guide.literary_analysis && (
                      <p style={{ margin: "5px 0" }}><strong>Phân tích văn học:</strong> {chap.study_guide.literary_analysis}</p>
                    )}
                    {chap.study_guide.grammar_focus && chap.study_guide.grammar_focus.length > 0 && (
                      <div style={{ marginTop: 10, paddingTop: 8, borderTop: "1px dashed #cbd5e1" }}>
                        <strong>Điểm sáng ngữ pháp C1/C2:</strong>
                        {chap.study_guide.grammar_focus.map((gf, idx) => (
                          <div key={idx} style={{ marginTop: 4 }}>
                            <em>{gf.title}:</em> “{gf.quote}” — <span style={{ color: "#475569" }}>{gf.analysis}</span>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                )}

                {chap.paragraphs.map((p) => (
                  <div className="bilingual-pair" key={p.id}>
                    <div className="para-en">{p.en}</div>
                    <div className="para-vi">{p.vi}</div>
                  </div>
                ))}
              </div>
            ))}
          </div>
        ))}
      </body>
    </html>
  );
}

export function renderEditionHtml(): string {
  const jsonPath = path.resolve(process.cwd(), "data/bilingual_novel.json");
  const data = JSON.parse(fs.readFileSync(jsonPath, "utf-8")) as BilingualNovel;
  const markup = renderToStaticMarkup(<NovelDocument novel={data} />);
  return `<!DOCTYPE html>\n${markup}`;
}

if (process.argv[1]?.endsWith("render_astryx.tsx") || process.argv[1]?.endsWith("render_astryx.ts")) {
  const html = renderEditionHtml();
  const outputPath = path.resolve(process.cwd(), "data/novel_bilingual.html");
  fs.writeFileSync(outputPath, html, "utf-8");
  console.log(`Rendered Astryx TypeScript edition to ${outputPath} (${(html.length / 1024 / 1024).toFixed(2)} MB)`);
}
