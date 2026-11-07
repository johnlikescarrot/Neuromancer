import json
import os
import sys
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

# Register Unicode fonts for Vietnamese & English
FONT_DIR = "/usr/share/fonts/truetype"
pdfmetrics.registerFont(TTFont('Serif', f'{FONT_DIR}/dejavu/DejaVuSerif.ttf'))
pdfmetrics.registerFont(TTFont('Serif-Bold', f'{FONT_DIR}/dejavu/DejaVuSerif-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Sans', f'{FONT_DIR}/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('Sans-Bold', f'{FONT_DIR}/dejavu/DejaVuSans-Bold.ttf'))

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
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            # Skip cover page
            return

        self.saveState()
        self.setFont("Sans", 8)
        self.setFillColor(colors.HexColor("#718096"))

        # Header (pages 3+)
        if self._pageNumber > 2:
            self.drawString(54, 755, "NEUROMANCER — AN ANNOTATED BILINGUAL CRITICAL EDITION (EN-VI)")
            self.drawRightString(612 - 54, 755, "William Gibson")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, 747, 612 - 54, 747)

        # Footer
        footer_text = f"Trang / Page {self._pageNumber} of {page_count}"
        self.drawRightString(612 - 54, 38, footer_text)
        self.drawString(54, 38, "Advanced ESL / Academic Proficiency Edition (C1/C2 • IELTS 7.0+ • TOEFL 90+)")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 48, 612 - 54, 48)

        self.restoreState()

def create_bilingual_edition_pdf(
    translated_json="translated_chapters.json",
    glossary_json="data/glossary.json",
    output_pdf="Neuromancer_Bilingual_Edition.pdf"
):
    print("Loading data...")
    with open(translated_json, "r", encoding="utf-8") as f:
        book_data = json.load(f)

    with open(glossary_json, "r", encoding="utf-8") as f:
        glossary_data = json.load(f)

    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Serif-Bold',
        fontSize=32,
        leading=38,
        textColor=colors.HexColor('#0F172A'),
        alignment=1, # Center
        spaceAfter=15
    )

    sub_title_style = ParagraphStyle(
        'CoverSubTitle',
        parent=styles['Normal'],
        fontName='Sans',
        fontSize=15,
        leading=22,
        textColor=colors.HexColor('#0284C7'),
        alignment=1,
        spaceAfter=25
    )

    author_style = ParagraphStyle(
        'CoverAuthor',
        parent=styles['Normal'],
        fontName='Serif',
        fontSize=18,
        leading=24,
        textColor=colors.HexColor('#334155'),
        alignment=1,
        spaceAfter=40
    )

    h1_style = ParagraphStyle(
        'PartHeading',
        parent=styles['Normal'],
        fontName='Sans-Bold',
        fontSize=18,
        leading=24,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=18,
        spaceAfter=12,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'ChapterHeading',
        parent=styles['Normal'],
        fontName='Sans-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#0369A1'),
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )

    body_en = ParagraphStyle(
        'BodyEN',
        parent=styles['Normal'],
        fontName='Serif',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#1E293B'),
        spaceAfter=0
    )

    body_vi = ParagraphStyle(
        'BodyVI',
        parent=styles['Normal'],
        fontName='Serif',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=0
    )

    col_header_en = ParagraphStyle(
        'ColHeaderEN',
        parent=styles['Normal'],
        fontName='Sans-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#1E3A8A'),
        alignment=0
    )

    col_header_vi = ParagraphStyle(
        'ColHeaderVI',
        parent=styles['Normal'],
        fontName='Sans-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#0F766E'),
        alignment=0
    )

    glossary_term_style = ParagraphStyle(
        'GlossaryTerm',
        parent=styles['Normal'],
        fontName='Sans-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#0369A1')
    )

    glossary_desc_style = ParagraphStyle(
        'GlossaryDesc',
        parent=styles['Normal'],
        fontName='Serif',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#334155')
    )

    story = []

    # ================= COVER PAGE =================
    story.append(Spacer(1, 40))
    story.append(Paragraph("NEUROMANCER", title_style))
    story.append(Paragraph("ẤN BẢN SONG NGỮ ANH - VIỆT TOÀN DIỆN & ĐỐI CHIẾU CHUẨN XÁC<br/><i>The Comprehensive Parallel Bilingual & Critical Study Edition</i>", sub_title_style))
    story.append(HRFlowable(width="60%", thickness=2, color=colors.HexColor('#0284C7'), spaceBefore=10, spaceAfter=20))
    story.append(Paragraph("Tác giả / Author: <b>WILLIAM GIBSON</b>", author_style))
    story.append(Spacer(1, 20))

    # Pedagogical Framework Card on Cover
    framework_info = [
        [Paragraph("<b>HỆ THỐNG TIÊU CHUẨN NĂNG LỰC NGÔN NGỮ QUỐC TẾ HỖ TRỢ</b>", ParagraphStyle('FwHead', fontName='Sans-Bold', fontSize=10, leading=14, textColor=colors.HexColor('#0F172A'), alignment=1))],
        [Paragraph(
            "Ấn bản này được biên soạn đặc biệt để phục vụ người học nâng cao kiến thức học thuật, văn phong hiện đại và đạt các chuẩn điểm ngôn ngữ quốc tế:<br/>"
            "• <b>TOEFL iBT:</b> 90+ điểm (trước 21/01/2026) hoặc <b>Band 5.0+</b> (từ 21/01/2026 trở đi)<br/>"
            "• <b>IELTS Academic:</b> <b>Band 7.0+</b> (Good to Very Good User)<br/>"
            "• <b>PTE Academic:</b> <b>65+ điểm</b> (Proficient Communicator)<br/>"
            "• <b>Cambridge English Qualifications:</b> <b>185+ điểm</b> (C1 Advanced / C2 Proficiency)<br/>"
            "• <b>Duolingo English Test (DET):</b> <b>120+ điểm</b> (Advanced Integrated Literacy)<br/>"
            "<i>Bao gồm toàn văn nguyên tác tiếng Anh, bản dịch Việt ngữ chuẩn xác trung thực với phong cách Cyberpunk, phân tích thuật ngữ chuyên ngành và từ vựng học thuật CEFR C1/C2.</i>",
            ParagraphStyle('FwBody', fontName='Sans', fontSize=8.5, leading=12.5, textColor=colors.HexColor('#334155'))
        )]
    ]
    fw_table = Table(framework_info, colWidths=[530])
    fw_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('PADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
    ]))
    story.append(fw_table)
    story.append(Spacer(1, 40))
    story.append(Paragraph("<b>XUẤT BẢN TOÀN TẬP TOÀN BỘ 24 CHƯƠNG & TOÀN BỘ 2.597 ĐOẠN VĂN</b>", ParagraphStyle('PubNote', fontName='Sans-Bold', fontSize=9, leading=13, alignment=1, textColor=colors.HexColor('#64748B'))))
    story.append(PageBreak())

    # ================= INTRODUCTION & GLOSSARY SECTION =================
    story.append(Paragraph("LỜI GIỚI THIỆU & CẨM NANG HỌC LIỆU C1/C2", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0284C7'), spaceBefore=4, spaceAfter=12))

    intro_p1 = (
        "<i>Neuromancer</i> (1984) của William Gibson là kiệt tác khai sinh thể loại Cyberpunk và là tác phẩm duy nhất giành trọn cả ba giải thưởng khoa học viễn tưởng danh giá nhất (Hugo, Nebula, Philip K. Dick). Tác phẩm mở ra thế giới vị lai u tối nơi ranh giới giữa thực tại và không gian số bị xóa nhòa, với những khái niệm tiên tri vĩ đại như <i>cyberspace</i>, <i>matrix</i>, và trí tuệ nhân tạo thức tỉnh."
    )
    intro_p2 = (
        "Ấn bản song ngữ đối chiếu này cung cấp văn bản Anh - Việt song song toàn bộ tác phẩm (toàn bộ 24 chương), được chuẩn hóa cấu trúc đoạn đối đoạn nhằm tối ưu hóa trải nghiệm đọc văn học lẫn nghiên cứu ngôn ngữ học thuật ở cấp độ C1/C2."
    )
    story.append(Paragraph(intro_p1, glossary_desc_style))
    story.append(Spacer(1, 6))
    story.append(Paragraph(intro_p2, glossary_desc_style))
    story.append(Spacer(1, 14))

    # Cyberpunk Terminology Table
    story.append(Paragraph("I. BẢNG THUẬT NGỮ CYBERPUNK TRỌNG TÂM", h2_style))
    cp_table_data = [[
        Paragraph("<b>Thuật ngữ (English)</b>", col_header_en),
        Paragraph("<b>Nghĩa Việt & Định nghĩa Ngữ cảnh</b>", col_header_vi)
    ]]
    for item in glossary_data.get("cyberpunk_terms", []):
        cp_table_data.append([
            Paragraph(f"<b>{item['term']}</b>", glossary_term_style),
            Paragraph(f"<b>{item['vi']}</b>: {item['definition']}", glossary_desc_style)
        ])
    cp_table = Table(cp_table_data, colWidths=[150, 380])
    cp_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#E2E8F0')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('PADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(cp_table)
    story.append(Spacer(1, 14))

    # Academic Vocabulary Table
    story.append(Paragraph("II. BỘ TỪ VỰNG HỌC THUẬT C1/C2 & ĐỐI CHIẾU CHUẨN THI QUỐC TẾ", h2_style))
    acad_table_data = [[
        Paragraph("<b>Từ vựng & CEFR</b>", col_header_en),
        Paragraph("<b>Chuẩn Điểm Bài Thi</b>", col_header_en),
        Paragraph("<b>Định nghĩa & Ví dụ Ngữ cảnh trong Tác phẩm</b>", col_header_vi)
    ]]
    for item in glossary_data.get("academic_vocabulary_cefr_c1_c2", []):
        benchmarks = "<br/>".join([f"• {k}: {v}" for k, v in item['proficiency_benchmarks'].items()])
        acad_table_data.append([
            Paragraph(f"<b>{item['word']}</b><br/><i>{item['pos']} - {item['cefr']}</i>", glossary_term_style),
            Paragraph(benchmarks, ParagraphStyle('BenchStyle', fontName='Sans', fontSize=7.5, leading=10, textColor=colors.HexColor('#475569'))),
            Paragraph(
                f"<b>{item['vi_definition']}</b> ({item['definition']})<br/>"
                f"<i>Ngữ cảnh:</i> \"{item['context_in_text']}\"<br/>"
                f"<i>Cụm từ liên kết (Collocations):</i> {', '.join(item['collocations'])}",
                glossary_desc_style
            )
        ])
    acad_table = Table(acad_table_data, colWidths=[110, 140, 280])
    acad_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#E2E8F0')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('PADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(acad_table)
    story.append(PageBreak())

    # ================= MỤC LỤC / TABLE OF CONTENTS =================
    story.append(Paragraph("MỤC LỤC TÁC PHẨM / TABLE OF CONTENTS", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0284C7'), spaceBefore=4, spaceAfter=14))

    toc_data = [[
        Paragraph("<b>Phần / Chương</b>", col_header_en),
        Paragraph("<b>Tên Phần & Nội Dung Song Ngữ</b>", col_header_vi),
        Paragraph("<b>Số đoạn</b>", col_header_en)
    ]]
    for ch in book_data['chapters']:
        toc_data.append([
            Paragraph(f"Chương / Chapter {ch['chapter']}", glossary_term_style),
            Paragraph(f"{ch['part']}", glossary_desc_style),
            Paragraph(f"{len(ch['paragraphs'])} đoạn", glossary_desc_style)
        ])
    toc_table = Table(toc_data, colWidths=[120, 330, 80])
    toc_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('PADDING', (0,0), (-1,-1), 4.5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(toc_table)
    story.append(PageBreak())

    # ================= BILINGUAL BODY =================
    current_part = ""
    col_width = 260

    print("Building bilingual chapters...")
    total_ch = len(book_data['chapters'])
    for ch_idx, ch in enumerate(book_data['chapters']):
        if ch['part'] != current_part:
            current_part = ch['part']
            story.append(Spacer(1, 10))
            story.append(Paragraph(f"{current_part}", h1_style))
            story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0284C7'), spaceBefore=2, spaceAfter=10))

        story.append(Paragraph(f"CHƯƠNG / CHAPTER {ch['chapter']}", h2_style))

        table_rows = [
            [
                Paragraph("<b>ORIGINAL ENGLISH TEXT</b>", col_header_en),
                Paragraph("<b>BẢN DỊCH TIẾNG VIỆT ĐỐI CHIẾU</b>", col_header_vi)
            ]
        ]

        for p_pair in ch['paragraphs']:
            p_en = Paragraph(p_pair['en'], body_en)
            p_vi = Paragraph(p_pair['vi'], body_vi)
            table_rows.append([p_en, p_vi])

        chapter_table = Table(table_rows, colWidths=[col_width, col_width], repeatRows=1)
        chapter_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
            ('LINEBELOW', (0,0), (-1,0), 1, colors.HexColor('#0284C7')),
            ('INNERGRID', (0,0), (-1,-1), 0.3, colors.HexColor('#E2E8F0')),
            ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('PADDING', (0,0), (-1,-1), 4),
            ('TOPPADDING', (0,1), (-1,-1), 4),
            ('BOTTOMPADDING', (0,1), (-1,-1), 4),
        ]))

        story.append(chapter_table)
        story.append(Spacer(1, 15))
        if ch_idx < total_ch - 1:
            story.append(PageBreak())

    print(f"Compiling PDF to {output_pdf} with NumberedCanvas...")
    doc.build(story, canvasmaker=NumberedCanvas)
    print("PDF build successful!")

if __name__ == "__main__":
    create_bilingual_edition_pdf()
