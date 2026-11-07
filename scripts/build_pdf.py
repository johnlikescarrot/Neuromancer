import os
import sys
import json
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from pedagogy import CHAPTER_1_VOCAB, EXAM_TIPS

# 1. Register Vietnamese-compatible TrueType Fonts
FONT_DIR = "/usr/share/fonts/truetype/liberation"
pdfmetrics.registerFont(TTFont("LiberationSerif", os.path.join(FONT_DIR, "LiberationSerif-Regular.ttf")))
pdfmetrics.registerFont(TTFont("LiberationSerif-Bold", os.path.join(FONT_DIR, "LiberationSerif-Bold.ttf")))
pdfmetrics.registerFont(TTFont("LiberationSerif-Italic", os.path.join(FONT_DIR, "LiberationSerif-Italic.ttf")))
pdfmetrics.registerFont(TTFont("LiberationSerif-BoldItalic", os.path.join(FONT_DIR, "LiberationSerif-BoldItalic.ttf")))

pdfmetrics.registerFont(TTFont("LiberationSans", os.path.join(FONT_DIR, "LiberationSans-Regular.ttf")))
pdfmetrics.registerFont(TTFont("LiberationSans-Bold", os.path.join(FONT_DIR, "LiberationSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("LiberationSans-Italic", os.path.join(FONT_DIR, "LiberationSans-Italic.ttf")))

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            return  # Suppress headers/footers on cover page

        self.saveState()
        self.setFont("LiberationSans", 8)
        self.setFillColor(colors.HexColor("#555555"))

        # Header
        header_text = "WILLIAM GIBSON — NEUROMANCER (BILINGUAL EN-VI CRITICAL EDITION)"
        self.drawString(54, 11 * inch - 36, header_text)
        self.setStrokeColor(colors.HexColor("#CCCCCC"))
        self.setLineWidth(0.5)
        self.line(54, 11 * inch - 42, 8.5 * inch - 54, 11 * inch - 42)

        # Footer
        footer_left = "IELTS 7.0+ | TOEFL 90+ | PTE 65 | Cambridge C1/C2 | DET 120+"
        footer_right = f"Page {self._pageNumber} of {page_count}"
        self.drawString(54, 36, footer_left)
        self.drawRightString(8.5 * inch - 54, 36, footer_right)
        self.line(54, 46, 8.5 * inch - 54, 46)

        self.restoreState()

def create_bilingual_pdf(output_pdf_path="Neuromancer_Bilingual_EN_VI.pdf"):
    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom Typography Styles
    title_style = ParagraphStyle(
        "CoverTitle",
        parent=styles["Normal"],
        fontName="LiberationSans-Bold",
        fontSize=28,
        leading=34,
        textColor=colors.HexColor("#0f172a"),
        alignment=1, # Center
        spaceAfter=12
    )

    subtitle_style = ParagraphStyle(
        "CoverSubtitle",
        parent=styles["Normal"],
        fontName="LiberationSans",
        fontSize=15,
        leading=22,
        textColor=colors.HexColor("#0284c7"),
        alignment=1,
        spaceAfter=24
    )

    meta_style = ParagraphStyle(
        "CoverMeta",
        parent=styles["Normal"],
        fontName="LiberationSerif",
        fontSize=10,
        leading=16,
        textColor=colors.HexColor("#334155"),
        alignment=1
    )

    heading1_style = ParagraphStyle(
        "SectionHeading1",
        parent=styles["Heading1"],
        fontName="LiberationSans-Bold",
        fontSize=18,
        leading=24,
        textColor=colors.HexColor("#0f172a"),
        spaceBefore=18,
        spaceAfter=10
    )

    heading2_style = ParagraphStyle(
        "SectionHeading2",
        parent=styles["Heading2"],
        fontName="LiberationSans-Bold",
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#0369a1"),
        spaceBefore=14,
        spaceAfter=8
    )

    en_para_style = ParagraphStyle(
        "EN_Paragraph",
        parent=styles["Normal"],
        fontName="LiberationSerif",
        fontSize=10,
        leading=14.5,
        textColor=colors.HexColor("#0f172a")
    )

    vi_para_style = ParagraphStyle(
        "VI_Paragraph",
        parent=styles["Normal"],
        fontName="LiberationSerif-Italic",
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor("#1e293b")
    )

    vocab_title_style = ParagraphStyle(
        "VocabTitle",
        parent=styles["Normal"],
        fontName="LiberationSans-Bold",
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#0f172a")
    )

    vocab_body_style = ParagraphStyle(
        "VocabBody",
        parent=styles["Normal"],
        fontName="LiberationSerif",
        fontSize=9,
        leading=13.5,
        textColor=colors.HexColor("#334155")
    )

    story = []

    # ================= COVER PAGE =================
    story.append(Spacer(1, 40))
    story.append(Paragraph("NEUROMANCER", title_style))
    story.append(Paragraph("Ấn Bản Song Ngữ Anh – Việt Chuẩn Mực Tuyệt Đối", subtitle_style))
    story.append(Spacer(1, 15))

    banner_text = (
        "<b>Tác Giả:</b> William Gibson | <b>Biên Dịch & Chú Giải Sư Phạm:</b> Master Bilingual Editorial Group<br/>"
        "<b>Mục Tiêu Năng Lực Chuẩn Hóa Quốc Tế:</b><br/>"
        "• IELTS 7.0+ (Band 7–8 Lexical Resources & Discourse Analysis)<br/>"
        "• TOEFL iBT 90+ / 5.0 (New Format 2026+)<br/>"
        "• Pearson PTE Academic 65+<br/>"
        "• Cambridge English Qualifications: 185+ (C1 Advanced / C2 Proficiency)<br/>"
        "• Duolingo English Test (DET): 120+"
    )
    story.append(Paragraph(banner_text, meta_style))
    story.append(Spacer(1, 30))

    # Pedagogical Framework Overview Table
    pedagogy_intro = [
        [
            Paragraph("<b>HỆ THỐNG PHƯƠNG PHÁP HỌC THÔNG QUA TÁC PHẨM</b>", vocab_title_style)
        ],
        [
            Paragraph(
                "Ấn bản này cung cấp phương thức tiếp cận song ngữ đối chiếu song song: "
                "bên cạnh bản dịch văn học tiếng Việt trung thực, chuẩn xác và giữ trọn vẹn văn phong cyberpunk nguyên tác, "
                "mỗi đoạn văn và chương đều tích hợp hệ thống chú thích từ vựng học thuật C1/C2, cụm từ cố định (collocations), "
                "ngữ pháp phức hợp và chiến thuật đọc hiểu áp dụng trực tiếp cho các kỳ thi chuẩn hóa quốc tế.",
                vocab_body_style
            )
        ]
    ]
    t_intro = Table(pedagogy_intro, colWidths=[500])
    t_intro.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('PADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_intro)
    story.append(PageBreak())

    # ================= EXAM PREPARATION GUIDE =================
    story.append(Paragraph("HƯỚNG DẪN ÔN LUYỆN NĂNG LỰC NGÔN NGỮ NÂNG CAO", heading1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0284c7"), spaceAfter=12))

    for tip_key, tip_val in EXAM_TIPS.items():
        tip_box = [
            [Paragraph(f"<b>CHIẾN THUẬT: {tip_key}</b>", vocab_title_style)],
            [Paragraph(tip_val, vocab_body_style)]
        ]
        t_tip = Table(tip_box, colWidths=[500])
        t_tip.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f0fdf4")),
            ('BOX', (0,0), (-1,-1), 0.75, colors.HexColor("#86efac")),
            ('PADDING', (0,0), (-1,-1), 8),
            ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(t_tip)
        story.append(Spacer(1, 10))

    story.append(Spacer(1, 15))
    story.append(PageBreak())

    # ================= VOCABULARY GLOSSARY C1/C2 =================
    story.append(Paragraph("BẢNG TỪ VỰNG HỌC THUẬT TRỌNG TÂM (C1/C2 - IELTS 7.0+ / TOEFL 90+)", heading1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0284c7"), spaceAfter=14))

    vocab_table_data = [
        [
            Paragraph("<b>Từ Vựng & Ngữ Âm</b>", vocab_title_style),
            Paragraph("<b>Định Nghĩa Anh - Việt</b>", vocab_title_style),
            Paragraph("<b>Chuẩn Thi & Collocations</b>", vocab_title_style)
        ]
    ]

    for word, item in CHAPTER_1_VOCAB.items():
        cell1 = Paragraph(f"<b>{item.word}</b> <i>{item.part_of_speech}</i><br/>{item.phonetic}<br/><font color='#dc2626'><b>{item.cefr_level}</b></font>", vocab_body_style)
        cell2 = Paragraph(f"<b>VI:</b> {item.vietnamese_def}<br/><b>EN:</b> {item.english_def}<br/><i>Ví dụ:</i> \"{item.context_sentence}\"", vocab_body_style)
        tests_str = ", ".join(item.target_tests)
        colloc_str = ", ".join(item.collocations)
        cell3 = Paragraph(f"<b>Mục tiêu:</b> {tests_str}<br/><b>Collocations:</b> {colloc_str}", vocab_body_style)
        vocab_table_data.append([cell1, cell2, cell3])

    t_vocab = Table(vocab_table_data, colWidths=[120, 230, 150])
    t_vocab.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#e2e8f0")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_vocab)
    story.append(PageBreak())

    # ================= CHAPTER 1 BILINGUAL TEXT =================
    with open('data/translated_ch01.json', 'r', encoding='utf-8') as f:
        ch1_data = json.load(f)

    story.append(Paragraph(ch1_data['title_vi'].upper(), heading1_style))
    story.append(Paragraph(ch1_data['title_en'], heading2_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0284c7"), spaceAfter=14))

    # Parallel 2-Column Table for Each Paragraph Pair
    table_rows = []
    # Table header
    table_rows.append([
        Paragraph("<b>ENGLISH ORIGINAL</b>", vocab_title_style),
        Paragraph("<b>BẢN DỊCH TIẾNG VIỆT ĐỐI CHIẾU</b>", vocab_title_style)
    ])

    for pair in ch1_data['pairs']:
        p_num = pair['id']
        en_text = f"<b>[{p_num}]</b> {pair['english']}"
        vi_text = f"<b>[{p_num}]</b> {pair['vietnamese']}"
        table_rows.append([
            Paragraph(en_text, en_para_style),
            Paragraph(vi_text, vi_para_style)
        ])

    bilingual_table = Table(table_rows, colWidths=[245, 255])
    bilingual_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-1), 0.4, colors.HexColor("#e2e8f0")),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))

    story.append(bilingual_table)

    # Build document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Bilingual PDF successfully built: {output_pdf_path}")

if __name__ == '__main__':
    create_bilingual_pdf()
