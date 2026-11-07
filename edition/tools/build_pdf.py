#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the comprehensive bilingual learning companion PDF for Neuromancer."""

import sys
from pathlib import Path

# Add project root to path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import edition.data.companion_data as data


class NumberedCanvas(canvas.Canvas):
    """Canvas that performs a two-pass calculation to display 'Page X of Y' and running headers."""

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

    def draw_page_decorations(self, page_count):
        # Do not print header/footer on cover page (page 1)
        if self._pageNumber == 1:
            return

        self.saveState()
        self.setFont("BeVietnamPro", 8)
        self.setFillColor(colors.HexColor("#4A5568"))

        # Header
        self.drawString(54, 11 * inch - 36, "William Gibson's Neuromancer — Bilingual Critical & Educational Edition")
        self.drawRightString(8.5 * inch - 54, 11 * inch - 36, "English – Tiếng Việt")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 11 * inch - 40, 8.5 * inch - 54, 11 * inch - 40)

        # Footer
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawString(54, 32, "Target: TOEFL 90/5 | IELTS 7.0 | PTE 65 | Cambridge C1/C2 185 | DET 120")
        self.drawRightString(8.5 * inch - 54, 32, page_str)
        self.line(54, 42, 8.5 * inch - 54, 42)

        self.restoreState()


def register_fonts():
    font_dir = ROOT / "edition" / "fonts"
    pdfmetrics.registerFont(TTFont("BeVietnamPro", str(font_dir / "BeVietnamPro-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("BeVietnamPro-Bold", str(font_dir / "BeVietnamPro-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("BeVietnamPro-Italic", str(font_dir / "BeVietnamPro-Italic.ttf")))


def build_pdf(output_path: Path):
    register_fonts()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom typography styles
    style_cover_title = ParagraphStyle(
        "CoverTitle",
        fontName="BeVietnamPro-Bold",
        fontSize=24,
        leading=30,
        textColor=colors.HexColor("#0F172A"),
        alignment=1,
        spaceAfter=12
    )
    style_cover_sub = ParagraphStyle(
        "CoverSub",
        fontName="BeVietnamPro-Bold",
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#0284C7"),
        alignment=1,
        spaceAfter=16
    )
    style_cover_meta = ParagraphStyle(
        "CoverMeta",
        fontName="BeVietnamPro",
        fontSize=10,
        leading=15,
        textColor=colors.HexColor("#334155"),
        alignment=1,
        spaceAfter=10
    )
    style_h1 = ParagraphStyle(
        "Heading1_Custom",
        fontName="BeVietnamPro-Bold",
        fontSize=16,
        leading=20,
        textColor=colors.HexColor("#0F172A"),
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )
    style_h2 = ParagraphStyle(
        "Heading2_Custom",
        fontName="BeVietnamPro-Bold",
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#0369A1"),
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True
    )
    style_body = ParagraphStyle(
        "Body_Custom",
        fontName="BeVietnamPro",
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor("#1E293B"),
        spaceAfter=6
    )
    style_body_vi = ParagraphStyle(
        "Body_VI_Custom",
        fontName="BeVietnamPro-Italic",
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=6
    )
    style_table_text = ParagraphStyle(
        "TableText",
        fontName="BeVietnamPro",
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#1E293B")
    )
    style_table_bold = ParagraphStyle(
        "TableBold",
        fontName="BeVietnamPro-Bold",
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#0F172A")
    )

    story = []

    # 1. FRONT COVER / TITLE PAGE
    story.append(Spacer(1, 40))
    story.append(Paragraph("NEUROMANCER", style_cover_title))
    story.append(Paragraph("A Bilingual English–Vietnamese Critical Learning Edition & Companion", style_cover_sub))
    story.append(Paragraph("Ấn Bản Nghiên Cứu Song Ngữ Anh – Việt & Cẩm Nang Học Thuật Toàn Diện", ParagraphStyle(
        "CoverViSub", fontName="BeVietnamPro-Bold", fontSize=13, leading=17, textColor=colors.HexColor("#0369A1"), alignment=1, spaceAfter=24
    )))
    story.append(HRFlowable(width="80%", thickness=1.5, color=colors.HexColor("#0284C7"), spaceAfter=24))

    intro_box = [
        [Paragraph("<b>Author / Tác giả</b>", style_table_bold), Paragraph("William Gibson (1984 Cyberpunk Masterpiece)", style_table_text)],
        [Paragraph("<b>Curated Scope / Phạm vi</b>", style_table_bold), Paragraph("All 24 Chapters across 4 Parts and Coda — Complete Critical Companion", style_table_text)],
        [Paragraph("<b>Target Proficiencies</b>", style_table_bold), Paragraph(
            "• TOEFL iBT: 90+ (Pre-Jan 2026) / Band 5.0+ (Post-Jan 2026)<br/>"
            "• IELTS Academic: Band 7.0 – 8.0+<br/>"
            "• Pearson Test of English (PTE) Academic: 65 – 75+<br/>"
            "• Cambridge English: 185+ (C1 Advanced / C2 Proficiency)<br/>"
            "• Duolingo English Test (DET): 120 – 135+",
            style_table_text
        )],
        [Paragraph("<b>Editorial Framework</b>", style_table_bold), Paragraph(
            "Designed for ambitious English learners and scholars: parallel bilingual synopses, thematic deconstructions, "
            "rigorous C1/C2 academic & cyberpunk lexicons with IPA, grammatical stylistics, and standardized test questions with keys.",
            style_table_text
        )]
    ]
    t_intro = Table(intro_box, colWidths=[150, 350])
    t_intro.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(t_intro)
    story.append(Spacer(1, 30))
    story.append(Paragraph(
        "<i>“Bầu trời trên bến cảng có màu của một chiếc tivi dò trúng kênh mất sóng.”</i><br/>"
        "“The sky above the port was the color of television, tuned to a dead channel.”",
        ParagraphStyle("QuoteIntro", fontName="BeVietnamPro-Italic", fontSize=10, leading=15, alignment=1, textColor=colors.HexColor("#475569"))
    ))
    story.append(PageBreak())

    # 2. METHODOLOGY & EXAM ALIGNMENT GUIDE
    story.append(Paragraph("Methodology & Standardized Exam Alignment", style_h1))
    story.append(Paragraph("Phương Pháp Biên Soạn & Khung Tiêu Chuẩn Năng Lực Quốc Tế", style_h2))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#0284C7"), spaceAfter=12))

    story.append(Paragraph(
        "To achieve advanced English proficiency (TOEFL 90+, IELTS 7.0+, PTE 65+, Cambridge C1/C2 185, DET 120+), learners "
        "must develop high-level competence in four essential cognitive dimensions: (1) Syntactic deciphering of complex compound-complex "
        "sentence structures; (2) Semantic agility with nuanced low-frequency academic and idiomatic vocabulary; (3) Discourse synthesis "
        "and inferential reasoning; and (4) Stylistic sensitivity to register, tone, and rhetorical defamiliarization.",
        style_body
    ))
    story.append(Paragraph(
        "Để chinh phục các mốc điểm cao nhất trong các kỳ thi chuẩn hóa quốc tế, người học cần làm chủ cả 4 trụ cột ngôn ngữ: "
        "giải mã cú pháp câu phức đa tầng, thẩm thấu vốn từ vựng học thuật cao cấp C1/C2 kèm phiên âm IPA chuẩn xác, tư duy suy luận logic sâu sắc "
        "và cảm thụ văn phong nghệ thuật đa thanh sắc của nguyên tác kinh điển.",
        style_body_vi
    ))
    story.append(Spacer(1, 10))

    # Test mapping table
    exam_rows = [
        [Paragraph("<b>Standardized Exam / Kỳ thi</b>", style_table_bold), Paragraph("<b>Target Score / Mục tiêu</b>", style_table_bold), Paragraph("<b>Targeted Competencies / Kỹ năng trọng tâm</b>", style_table_bold)],
        [Paragraph("<b>TOEFL iBT</b>", style_table_bold), Paragraph("90+ (Pre-Jan 2026)<br/>Band 5.0+ (Post-Jan 2026)", style_table_text), Paragraph("Inference, rhetorical purpose, negative factual info, vocabulary in context.", style_table_text)],
        [Paragraph("<b>IELTS Academic</b>", style_table_bold), Paragraph("Band 7.0 – 8.0+", style_table_text), Paragraph("Identifying writer's views, summary completion, matching features, advanced discourse cohesion.", style_table_text)],
        [Paragraph("<b>PTE Academic</b>", style_table_bold), Paragraph("65 – 75+", style_table_text), Paragraph("Reading & writing fill in the blanks, re-order paragraphs, academic collocation precision.", style_table_text)],
        [Paragraph("<b>Cambridge C1/C2</b>", style_table_bold), Paragraph("185+ (CAE / CPE)", style_table_text), Paragraph("Key word transformation, gapped text, multiple matching, register and nuance.", style_table_text)],
        [Paragraph("<b>Duolingo (DET)</b>", style_table_bold), Paragraph("120 – 135+", style_table_text), Paragraph("Interactive reading, complete the passage, C1 lexical selection.", style_table_text)]
    ]
    t_exam = Table(exam_rows, colWidths=[110, 130, 260])
    t_exam.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#E2E8F0")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t_exam)
    story.append(PageBreak())

    # 3. CHAPTERS MODULES (ALL 24 CHAPTERS)
    current_part = None
    for ch_data in data.CHAPTERS_DATA:
        # Check if new part header is needed
        if ch_data["part_num"] != current_part:
            current_part = ch_data["part_num"]
            part_meta = next((p for p in data.PARTS_METADATA if p["part_num"] == current_part), None)
            if part_meta:
                story.append(Spacer(1, 15))
                story.append(Paragraph(f"<b>{part_meta['part_num']}</b> — {part_meta['title_en']}", style_h1))
                story.append(Paragraph(f"<b>{part_meta['title_vi']}</b>", style_h2))
                story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0284C7"), spaceAfter=10))

                part_summary_table = [
                    [Paragraph("<b>Part Overview (English)</b>", style_table_bold), Paragraph(part_meta["part_overview_en"], style_table_text)],
                    [Paragraph("<b>Tổng quan Phần (Tiếng Việt)</b>", style_table_bold), Paragraph(part_meta["part_overview_vi"], style_table_text)]
                ]
                t_part = Table(part_summary_table, colWidths=[140, 360])
                t_part.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F1F5F9")),
                    ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#CBD5E1")),
                    ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ('TOPPADDING', (0, 0), (-1, -1), 6),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                ]))
                story.append(t_part)
                story.append(Spacer(1, 15))

        # Chapter Header
        story.append(Paragraph(f"Chapter {ch_data['chapter']}: {ch_data['title_en']}", style_h1))
        story.append(Paragraph(f"Chương {ch_data['chapter']}: {ch_data['title_vi']}", style_h2))
        story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#94A3B8"), spaceAfter=8))

        # Parallel Synopses Table (Two Column Comparison)
        synopsis_table = [
            [
                Paragraph("<b>Narrative Synopsis (English)</b>", style_table_bold),
                Paragraph("<b>Tóm Tắt & Đối Chiếu Diễn Biến (Tiếng Việt)</b>", style_table_bold)
            ],
            [
                Paragraph(ch_data["synopsis_en"], style_table_text),
                Paragraph(ch_data["synopsis_vi"], style_table_text)
            ]
        ]
        t_synopsis = Table(synopsis_table, colWidths=[250, 250])
        t_synopsis.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F8FAFC")),
            ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#CBD5E1")),
            ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ]))
        story.append(t_synopsis)
        story.append(Spacer(1, 10))

        # Thematic Analysis
        themes_table = [
            [
                Paragraph("<b>Thematic & Critical Dissection (EN & VI)</b>", style_table_bold)
            ],
            [
                Paragraph(f"<b>Key Themes:</b> {ch_data['literary_themes_en']}<br/><br/><b>Phân tích chuyên sâu:</b> {ch_data['literary_themes_vi']}", style_table_text)
            ]
        ]
        t_themes = Table(themes_table, colWidths=[500])
        t_themes.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F0FDF4")),
            ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#BBF7D0")),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ]))
        story.append(t_themes)
        story.append(Spacer(1, 10))

        # Academic Vocabulary Lexicon (CEFR C1/C2)
        vocab_rows = [
            [
                Paragraph("<b>Word & IPA</b>", style_table_bold),
                Paragraph("<b>POS</b>", style_table_bold),
                Paragraph("<b>Tiếng Việt</b>", style_table_bold),
                Paragraph("<b>Definition & Advanced Collocation / Context</b>", style_table_bold)
            ]
        ]
        for v in ch_data["vocabulary"]:
            vocab_rows.append([
                Paragraph(f"<b>{v['word']}</b><br/>{v['ipa']}", style_table_text),
                Paragraph(f"<i>{v['pos']}</i>", style_table_text),
                Paragraph(v["vi"], style_table_text),
                Paragraph(f"<b>Def:</b> {v['def']}<br/><b>Ex:</b> <i>{v['ex']}</i>", style_table_text)
            ])
        t_vocab = Table(vocab_rows, colWidths=[110, 45, 115, 230])
        t_vocab.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#EFF6FF")),
            ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#BFDBFE")),
            ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#DBEAFE")),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ]))
        story.append(t_vocab)
        story.append(Spacer(1, 10))

        # Stylistic Spotlight & Standardized Exam Task
        exam = ch_data["exam_practice"]
        opts_formatted = "<br/>".join(exam["options"])
        assessment_table = [
            [
                Paragraph("<b>Stylistics & Standardized Exam Competency Task</b>", style_table_bold)
            ],
            [
                Paragraph(
                    f"<b>Rhetorical Analysis:</b> {ch_data['style_notes_en']}<br/>"
                    f"<i>{ch_data['style_notes_vi']}</i><br/><br/>"
                    f"<b>Exam Task ({exam['test_type']}):</b><br/>"
                    f"{exam['question']}<br/><br/>"
                    f"{opts_formatted}<br/><br/>"
                    f"<b>Correct Answer:</b> <b>{exam['answer']}</b><br/>"
                    f"<b>Explanatory Rationale:</b> {exam['rationale']}",
                    style_table_text
                )
            ]
        ]
        t_assess = Table(assessment_table, colWidths=[500])
        t_assess.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#FFFBEB")),
            ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#FDE68A")),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ]))
        story.append(t_assess)
        story.append(Spacer(1, 20))
        story.append(PageBreak())

    # Build document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated PDF at: {output_path}")


def main():
    target = ROOT / "edition" / "Neuromancer-Bilingual-Learning-Companion.pdf"
    print("Building Neuromancer Bilingual Edition PDF...")
    build_pdf(target)


if __name__ == "__main__":
    main()
