#!/usr/bin/env python3
"""Build the Neuromancer Bilingual Learning Companion PDF using ReportLab."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "edition"))

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from content.chapters_01_07 import CHAPTERS as c1
from content.chapters_08_12 import CHAPTERS as c2
from content.chapters_13_18 import CHAPTERS as c3
from content.chapters_19_24 import CHAPTERS as c4

FONTS_DIR = ROOT / "edition" / "fonts"
pdfmetrics.registerFont(TTFont("BeVietnamPro", str(FONTS_DIR / "BeVietnamPro-Regular.ttf")))
pdfmetrics.registerFont(TTFont("BeVietnamPro-Bold", str(FONTS_DIR / "BeVietnamPro-Bold.ttf")))
pdfmetrics.registerFont(TTFont("BeVietnamPro-Italic", str(FONTS_DIR / "BeVietnamPro-Italic.ttf")))

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        if self._pageNumber == 1:
            return  # Suppress headers/footers on cover page
        self.saveState()
        self.setFont("BeVietnamPro", 8)
        self.setFillColor(colors.HexColor("#64748B"))

        # Header
        self.drawString(45, 805, "Neuromancer — English-Vietnamese Bilingual Learning Companion (CEFR C1/C2)")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(45, 798, 550, 798)

        # Footer
        page_str = f"Trang {self._pageNumber} / {total_pages}"
        self.drawRightString(550, 35, page_str)
        self.drawString(45, 35, "IELTS 7.0 • TOEFL 90 / 5.0 • PTE 65 • Cambridge C1/C2 185 • DET 120")
        self.line(45, 45, 550, 45)
        self.restoreState()

def build_pdf(out_path: Path):
    doc = SimpleDocTemplate(
        str(out_path),
        pagesize=A4,
        leftMargin=45,
        rightMargin=45,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "CoverTitle",
        fontName="BeVietnamPro-Bold",
        fontSize=24,
        leading=30,
        textColor=colors.HexColor("#0F172A"),
        alignment=1,
        spaceAfter=12
    )
    subtitle_style = ParagraphStyle(
        "CoverSubtitle",
        fontName="BeVietnamPro",
        fontSize=12,
        leading=18,
        textColor=colors.HexColor("#334155"),
        alignment=1,
        spaceAfter=20
    )
    h1_style = ParagraphStyle(
        "ChapterHeading",
        fontName="BeVietnamPro-Bold",
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#1E293B"),
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )
    h2_style = ParagraphStyle(
        "SectionHeading",
        fontName="BeVietnamPro-Bold",
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#0284C7"),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )
    body_style = ParagraphStyle(
        "Body",
        fontName="BeVietnamPro",
        fontSize=8.5,
        leading=12.5,
        textColor=colors.HexColor("#1E293B"),
        spaceAfter=5
    )
    body_vi_style = ParagraphStyle(
        "BodyVI",
        fontName="BeVietnamPro-Italic",
        fontSize=8.5,
        leading=12.5,
        textColor=colors.HexColor("#334155"),
        spaceAfter=6
    )
    box_style = ParagraphStyle(
        "BoxText",
        fontName="BeVietnamPro",
        fontSize=8,
        leading=11.5,
        textColor=colors.HexColor("#0F172A")
    )
    table_cell = ParagraphStyle(
        "TableCell",
        fontName="BeVietnamPro",
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor("#1E293B")
    )
    table_cell_bold = ParagraphStyle(
        "TableCellBold",
        fontName="BeVietnamPro-Bold",
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor("#0F172A")
    )

    story = []

    # --- COVER PAGE ---
    story.append(Spacer(1, 40))
    story.append(Paragraph("NEUROMANCER", title_style))
    story.append(Paragraph("ẤN BẢN SONG NGỮ ANH – VIỆT & TÀI LIỆU HỌC THUẬT CHUYÊN SÂU<br/><i>Bilingual Academic Learning Companion & Critical Guide</i>", subtitle_style))
    story.append(HRFlowable(width="60%", thickness=1.5, color=colors.HexColor("#0284C7"), spaceAfter=20))

    target_box = [
        [Paragraph("<b>Mục tiêu Năng lực & Khảo thí Quốc tế Định hướng (C1 / C2 Framework):</b>", box_style)],
        [Paragraph("• <b>TOEFL iBT:</b> 90 điểm (trước 21/01/2026) hoặc <b>5.0 điểm</b> (từ 21/01/2026 trở đi)<br/>"
                   "• <b>IELTS:</b> 7.0 Overall (Academic & General Training)<br/>"
                   "• <b>PTE Academic:</b> 65+ điểm<br/>"
                   "• <b>Cambridge English Qualifications:</b> 185+ điểm (C1 Advanced / C2 Proficiency)<br/>"
                   "• <b>Duolingo English Test (DET):</b> 120+ điểm", box_style)]
    ]
    t_target = Table(target_box, colWidths=[500])
    t_target.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
        ('PADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(t_target)
    story.append(Spacer(1, 20))

    intro_p1 = Paragraph(
        "<b>Lời giới thiệu & Phương pháp luận:</b><br/>"
        "Ấn bản này được biên soạn độc lập như một công trình học thuật và cẩm nang đồng hành song ngữ (Bilingual Study Companion) "
        "dành riêng cho kiệt tác <i>Neuromancer</i> (William Gibson, 1984). Công trình bao quát toàn diện toàn bộ 24 chương tác phẩm qua 5 phần: "
        "tóm tắt cốt truyện song ngữ đối chiếu, phân tích góc nhìn văn học & xã hội học (critical lens), câu hỏi tư duy kèm đáp án phản biện, "
        "bảng từ vựng học thuật C1/C2 kèm nghĩa và ngữ cảnh, phân tích cú pháp nâng cao và bài tập thực hành đa kỹ năng.",
        body_style
    )
    story.append(intro_p1)
    story.append(PageBreak())

    # --- CHAPTER CONTENT ---
    all_chapters = c1 + c2 + c3 + c4

    for ch in all_chapters:
        n = ch["n"]
        ch_title = f"Chương {n}: {ch['title']}"
        ch_title_vi = f"{ch['vi_title']}"
        story.append(Paragraph(ch_title, h1_style))
        story.append(Paragraph(ch_title_vi, subtitle_style))
        story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#E2E8F0"), spaceAfter=8))

        # Summary EN & VI
        story.append(Paragraph("1. Tóm tắt Cốt truyện Song ngữ (Bilingual Plot Summary)", h2_style))
        story.append(Paragraph(f"<b>[EN]</b> {ch['summary_en']}", body_style))
        story.append(Paragraph(f"<b>[VI]</b> {ch['summary_vi']}", body_vi_style))

        # Critical Lens & Discourse Analysis
        story.append(Paragraph("2. Lăng kính Phân tích & Tư duy Phản biện (Critical Lens & Discussion)", h2_style))
        story.append(Paragraph(f"<b>Góc nhìn [EN]:</b> {ch['lens_en']}", body_style))
        story.append(Paragraph(f"<b>Góc nhìn [VI]:</b> {ch['lens_vi']}", body_vi_style))
        story.append(Paragraph(f"<b>Câu hỏi / Question:</b> {ch['q_en']} <i>({ch['q_vi']})</i>", body_style))
        story.append(Paragraph(f"<b>Phân tích / Analysis:</b> {ch['a_en']} <i>({ch['a_vi']})</i>", body_vi_style))

        # Vocabulary C1/C2 Table
        story.append(Paragraph("3. Hệ thống Từ vựng Học thuật Trọng tâm (C1/C2 Academic Vocabulary)", h2_style))
        table_data = [
            [Paragraph("<b>Từ vựng (POS)</b>", table_cell_bold),
             Paragraph("<b>Định nghĩa Tiếng Anh</b>", table_cell_bold),
             Paragraph("<b>Nghĩa Tiếng Việt</b>", table_cell_bold),
             Paragraph("<b>Cụm từ / Collocation</b>", table_cell_bold)]
        ]
        for term, pos, definition, vi_meaning, collocation in ch["vocab"]:
            table_data.append([
                Paragraph(f"<b>{term}</b> <i>({pos})</i>", table_cell),
                Paragraph(definition, table_cell),
                Paragraph(vi_meaning, table_cell),
                Paragraph(f"<i>{collocation}</i>", table_cell)
            ])

        t_vocab = Table(table_data, colWidths=[90, 160, 120, 130])
        t_vocab.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#F1F5F9")),
            ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor("#CBD5E1")),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('PADDING', (0,0), (-1,-1), 4),
        ]))
        story.append(t_vocab)
        story.append(Spacer(1, 6))

        # Grammar & Exam Skills Application
        story.append(Paragraph("4. Cấu trúc Cú pháp Nâng cao & Nhiệm vụ Khảo thí (Advanced Syntax & Exam Tasks)", h2_style))
        story.append(Paragraph(f"<b>Ngữ pháp [EN]:</b> {ch['grammar_en']}", body_style))
        story.append(Paragraph(f"<b>Ngữ pháp [VI]:</b> {ch['grammar_vi']}", body_vi_style))
        story.append(Paragraph(f"<b>Ví dụ:</b> <i>{ch.get('example_en', '')}</i> — {ch.get('example_vi', '')}", body_style))
        story.append(Paragraph(f"<b>Thực hành Khảo thí:</b> {ch['task_en']} <i>({ch['task_vi']})</i>", body_vi_style))

        story.append(PageBreak())

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated PDF at {out_path}")

if __name__ == "__main__":
    out = ROOT / "edition" / "Neuromancer-Bilingual-Learning-Companion.pdf"
    build_pdf(out)
