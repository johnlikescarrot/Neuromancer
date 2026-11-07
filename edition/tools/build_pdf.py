# -*- coding: utf-8 -*-
"""
Professional PDF Compiler for Neuromancer Bilingual Academic Learning Companion.
Uses ReportLab with custom Be Vietnam Pro fonts, professional running headers/footers,
two-tier Table of Contents, full 24-chapter bilingual pedagogy, and comprehensive glossaries.
"""
import os
import sys

# Ensure repo root is on sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch, cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from edition.content.curriculum import CURRICULUM

class NumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas that accumulates total page count and renders
    running headers and footers with accurate 'Page X of Y' numbering.
    """
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
            # Suppress headers and footers on cover page
            return

        self.saveState()
        self.setFont("BeVietnamPro", 8)
        self.setFillColor(colors.HexColor("#4A5568"))

        width, height = A4
        margin = 40

        # Running Header
        header_text = "WILLIAM GIBSON'S NEUROMANCER — BILINGUAL ACADEMIC COMPANION"
        self.drawString(margin, height - 30, header_text)
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(margin, height - 34, width - margin, height - 34)

        # Running Footer
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(width - margin, 25, page_str)
        footer_vi = "Ấn bản Học thuật Song ngữ Anh - Việt | Mục tiêu C1/C2 (IELTS 7.0+ • TOEFL 90+)"
        self.drawString(margin, 25, footer_vi)
        self.line(margin, 35, width - margin, 35)

        self.restoreState()


def register_fonts():
    fonts_dir = os.path.join(repo_root, "edition", "fonts")
    pdfmetrics.registerFont(TTFont("BeVietnamPro", os.path.join(fonts_dir, "BeVietnamPro-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("BeVietnamPro-Bold", os.path.join(fonts_dir, "BeVietnamPro-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("BeVietnamPro-Italic", os.path.join(fonts_dir, "BeVietnamPro-Italic.ttf")))
    pdfmetrics.registerFontFamily(
        "BeVietnamPro",
        normal="BeVietnamPro",
        bold="BeVietnamPro-Bold",
        italic="BeVietnamPro-Italic"
    )


def create_styles():
    styles = getSampleStyleSheet()

    # Base Cyberpunk Palette
    # Dark slate: #0F172A, Neon Cyan: #0EA5E9, Deep Indigo: #312E81, Charcoal: #1E293B

    styles.add(ParagraphStyle(
        name="BookCoverTitle",
        fontName="BeVietnamPro-Bold",
        fontSize=30,
        leading=38,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#0F172A")
    ))

    styles.add(ParagraphStyle(
        name="BookCoverSubtitle",
        fontName="BeVietnamPro",
        fontSize=13,
        leading=18,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#0284C7")
    ))

    styles.add(ParagraphStyle(
        name="BookCoverMeta",
        fontName="BeVietnamPro",
        fontSize=10,
        leading=15,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#475569")
    ))

    styles.add(ParagraphStyle(
        name="PartHeading",
        fontName="BeVietnamPro-Bold",
        fontSize=16,
        leading=22,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#1E3A8A"),
        spaceBefore=15,
        spaceAfter=10
    ))

    styles.add(ParagraphStyle(
        name="ChapterHeading",
        fontName="BeVietnamPro-Bold",
        fontSize=14,
        leading=18,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#0F172A"),
        spaceBefore=14,
        spaceAfter=6
    ))

    styles.add(ParagraphStyle(
        name="SubSectionHeading",
        fontName="BeVietnamPro-Bold",
        fontSize=11,
        leading=15,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#0369A1"),
        spaceBefore=10,
        spaceAfter=4
    ))

    styles.add(ParagraphStyle(
        name="BodyEN",
        fontName="BeVietnamPro",
        fontSize=9.5,
        leading=13.5,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor("#1E293B"),
        spaceBefore=3,
        spaceAfter=5
    ))

    styles.add(ParagraphStyle(
        name="BodyVI",
        fontName="BeVietnamPro",
        fontSize=9.5,
        leading=13.5,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor("#047857"),
        spaceBefore=3,
        spaceAfter=6
    ))

    styles.add(ParagraphStyle(
        name="MetaLabel",
        fontName="BeVietnamPro-Bold",
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#64748B")
    ))

    styles.add(ParagraphStyle(
        name="VocabTerm",
        fontName="BeVietnamPro-Bold",
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#0F172A")
    ))

    styles.add(ParagraphStyle(
        name="VocabDef",
        fontName="BeVietnamPro",
        fontSize=9,
        leading=12.5,
        textColor=colors.HexColor("#334155")
    ))

    styles.add(ParagraphStyle(
        name="QuestionPrompt",
        fontName="BeVietnamPro-Bold",
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#1E293B"),
        spaceBefore=4,
        spaceAfter=3
    ))

    styles.add(ParagraphStyle(
        name="QuestionOption",
        fontName="BeVietnamPro",
        fontSize=9,
        leading=12.5,
        textColor=colors.HexColor("#334155"),
        leftIndent=12,
        spaceBefore=1,
        spaceAfter=2
    ))

    styles.add(ParagraphStyle(
        name="Explanation",
        fontName="BeVietnamPro-Italic",
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#0284C7"),
        leftIndent=12,
        spaceBefore=2,
        spaceAfter=6
    ))

    return styles


def build_pdf():
    output_path = os.path.join(repo_root, "edition", "Neuromancer-Bilingual-Learning-Companion.pdf")
    print(f"Building PDF: {output_path}")

    register_fonts()
    styles = create_styles()

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=45,
        bottomMargin=45
    )

    story = []
    content_width = A4[0] - 72

    # ==========================================
    # 1. FRONT COVER
    # ==========================================
    story.append(Spacer(1, 40))
    story.append(Paragraph("WILLIAM GIBSON", styles["BookCoverSubtitle"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph("NEUROMANCER", styles["BookCoverTitle"]))
    story.append(Spacer(1, 5))
    story.append(Paragraph("ẤN BẢN SONG NGỮ ANH - VIỆT & TÀI LIỆU HỌC THUẬT C1/C2", styles["BookCoverSubtitle"]))
    story.append(Spacer(1, 15))

    # Decorative Rule
    story.append(HRFlowable(width="60%", thickness=2, color=colors.HexColor("#0284C7"), spaceAfter=20, spaceBefore=10))

    cover_desc = (
        "<b>Bilingual Critical & Academic Study Companion for Advanced English Proficiency</b><br/><br/>"
        "Bao quát toàn bộ 24 chương và Coda của kiệt tác văn học Cyberpunk.<br/>"
        "Được biên soạn chuẩn mực hỗ trợ học viên đạt các chứng chỉ quốc tế:<br/>"
        "• <b>IELTS Academic:</b> 7.0+ (Band 8.0+ Lexical Resource & Grammatical Range)<br/>"
        "• <b>TOEFL iBT:</b> 90+ (trước 21/01/2026) hoặc 5+ (từ 21/01/2026 trở đi)<br/>"
        "• <b>PTE Academic:</b> 65+ (Proficient English C1)<br/>"
        "• <b>Cambridge English:</b> 185+ (C1 Advanced / C2 Proficiency)<br/>"
        "• <b>Duolingo English Test (DET):</b> 120+ (Advanced / Comprehensive)"
    )
    story.append(Paragraph(cover_desc, styles["BookCoverMeta"]))
    story.append(Spacer(1, 50))

    # Cover Footer Box
    meta_box_data = [
        [
            Paragraph("<b>Biên soạn & Thiết kế:</b> Nhóm Nghiên cứu Song ngữ Văn học & Khảo thí", styles["MetaLabel"]),
            Paragraph("<b>Phông chữ:</b> Be Vietnam Pro (SIL OFL)", styles["MetaLabel"])
        ],
        [
            Paragraph("<b>Độ phủ tác phẩm:</b> 24 Chương + Coda | 120 Mục từ C1/C2", styles["MetaLabel"]),
            Paragraph("<b>Tiêu chuẩn xuất bản:</b> PDF/A ReportLab Engine", styles["MetaLabel"])
        ]
    ]
    meta_table = Table(meta_box_data, colWidths=[content_width*0.55, content_width*0.45])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#E2E8F0")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(meta_table)

    story.append(PageBreak())

    # ==========================================
    # 2. FOREWORD & EXAM BENCHMARK GUIDE
    # ==========================================
    story.append(Paragraph("LỜI NÓI ĐẦU & HƯỚNG DẪN LUYỆN THI CHUẨN HÓA", styles["PartHeading"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#0284C7"), spaceAfter=15))

    foreword_en = (
        "<b>Academic Rationale:</b> William Gibson's <i>Neuromancer</i> (1984) is not merely the founding monument of cyberpunk fiction; "
        "it is a stylistic masterclass in linguistic economy, dense metaphoric layering, and high-register speculative discourse. "
        "Studying the text's sophisticated vocabulary, Latinate syntactic nominalizations, and complex sentence structures provides "
        "advanced English learners with an unparalleled bridge from upper-intermediate competency (CEFR B2) to effective operational "
        "proficiency and mastery (CEFR C1/C2)."
    )
    story.append(Paragraph(foreword_en, styles["BodyEN"]))

    foreword_vi = (
        "<b>Mục đích sư phạm:</b> Kiệt tác <i>Neuromancer</i> (1984) của William Gibson không chỉ là viên đá tảng khai sinh văn hóa cyberpunk, "
        "mà còn là một đỉnh cao nghệ thuật về ngôn ngữ học: mật độ thông tin dày đặc, ẩn dụ đa tầng và cấu trúc câu học thuật phức hợp. "
        "Ấn bản này được biên soạn độc lập và toàn diện nhằm giúp người học tiếng Anh nâng tầm năng lực từ mức B2 lên trình độ C1/C2, "
        "đáp ứng xuất sắc các tiêu chuẩn chấm điểm khắt khe nhất trong các kỳ thi học thuật quốc tế."
    )
    story.append(Paragraph(foreword_vi, styles["BodyVI"]))
    story.append(Spacer(1, 10))

    # Benchmark Table
    story.append(Paragraph("BẢNG ĐỐI CHIẾU MỤC TIÊU NĂNG LỰC QUỐC TẾ (TARGET BENCHMARKS)", styles["SubSectionHeading"]))
    benchmark_data = [
        [Paragraph("<b>Hệ thống Khảo thí / Kỳ thi</b>", styles["MetaLabel"]), Paragraph("<b>Mục tiêu Điểm số</b>", styles["MetaLabel"]), Paragraph("<b>Yêu cầu Năng lực Ngôn ngữ Tương ứng</b>", styles["MetaLabel"])],
        [
            Paragraph("<b>IELTS Academic</b>", styles["VocabTerm"]),
            Paragraph("<b>7.0+ Overall</b><br/>(Writing/Reading ≥ 7.0)", styles["VocabDef"]),
            Paragraph("Khả năng vận dụng linh hoạt từ vựng hiếm (uncommon lexical items), ngữ pháp đa dạng phức hợp, kiểm soát lạc quan lỗi nhỏ.", styles["VocabDef"])
        ],
        [
            Paragraph("<b>TOEFL iBT</b>", styles["VocabTerm"]),
            Paragraph("<b>90+</b> (trước 21/01/2026)<br/><b>5+</b> (sau 21/01/2026)", styles["VocabDef"]),
            Paragraph("Đọc hiểu và phân tích văn bản học thuật chuyên sâu, tổng hợp và lập luận sắc bén trong phần thi Tích hợp (Integrated Tasks).", styles["VocabDef"])
        ],
        [
            Paragraph("<b>PTE Academic</b>", styles["VocabTerm"]),
            Paragraph("<b>65+</b> (Proficient C1)", styles["VocabDef"]),
            Paragraph("Đọc hiểu tốc độ cao, nhận biết ngữ cảnh từ vựng học thuật, phát âm và xử lý trôi chảy cấu trúc câu dài phức tạp.", styles["VocabDef"])
        ],
        [
            Paragraph("<b>Cambridge English (CAE/CPE)</b>", styles["VocabTerm"]),
            Paragraph("<b>185+</b><br/>(C1 Advanced / C2)", styles["VocabDef"]),
            Paragraph("Sử dụng chuẩn xác các cấu trúc đảo ngữ (Inversion), câu chẻ (Cleft sentences), thể giả định, và sắc thái biểu cảm cao cấp.", styles["VocabDef"])
        ],
        [
            Paragraph("<b>Duolingo English Test (DET)</b>", styles["VocabTerm"]),
            Paragraph("<b>120+</b><br/>(Literacy & Comprehension)", styles["VocabDef"]),
            Paragraph("Vốn từ vựng học thuật C1 rộng, khả năng hoàn thành bài đọc điền từ (C-test) chính xác và viết luận diễn đạt tự nhiên.", styles["VocabDef"])
        ]
    ]
    b_table = Table(benchmark_data, colWidths=[content_width*0.28, content_width*0.25, content_width*0.47])
    b_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F1F5F9")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('PADDING', (0, 0), (-1, -1), 6),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(b_table)

    story.append(PageBreak())

    # ==========================================
    # 3. TABLE OF CONTENTS
    # ==========================================
    story.append(Paragraph("MỤC LỤC CHI TIẾT (TABLE OF CONTENTS)", styles["PartHeading"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#0284C7"), spaceAfter=15))

    toc_data = [
        [Paragraph("<b>Chương / Phần</b>", styles["MetaLabel"]), Paragraph("<b>Nội dung Tác phẩm & Trọng tâm Học thuật</b>", styles["MetaLabel"]), Paragraph("<b>Số từ gốc</b>", styles["MetaLabel"])]
    ]
    for ch in CURRICULUM.chapters:
        toc_data.append([
            Paragraph(f"<b>Chương {ch.number}</b>", styles["VocabTerm"]),
            Paragraph(f"{ch.chapter_title_en}<br/><i>{ch.chapter_title_vi}</i>", styles["VocabDef"]),
            Paragraph(f"{ch.word_count:,}", styles["VocabDef"])
        ])
    toc_table = Table(toc_data, colWidths=[content_width*0.18, content_width*0.67, content_width*0.15])
    toc_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F8FAFC")),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#F1F5F9")),
        ('PADDING', (0, 0), (-1, -1), 4),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(toc_table)

    story.append(PageBreak())

    # ==========================================
    # 4. PEDAGOGICAL CHAPTER CHAPTER MODULES
    # ==========================================
    current_part = ""
    for ch in CURRICULUM.chapters:
        if ch.part_title_en != current_part:
            current_part = ch.part_title_en
            story.append(Spacer(1, 10))
            story.append(Paragraph(ch.part_title_en, styles["PartHeading"]))
            story.append(Paragraph(ch.part_title_vi, styles["BookCoverSubtitle"]))
            story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1E3A8A"), spaceAfter=12, spaceBefore=4))

        # Chapter Title Block
        ch_title_block = (
            f"<b>CHAPTER {ch.number}: {ch.chapter_title_en.split(': ', 1)[-1]}</b><br/>"
            f"<font color='#0369A1'><i>Chương {ch.number}: {ch.chapter_title_vi.split(': ', 1)[-1]}</i></font> "
            f"<font color='#64748B' size=8>({ch.word_count:,} words in source)</font>"
        )
        story.append(Paragraph(ch_title_block, styles["ChapterHeading"]))
        story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#94A3B8"), spaceAfter=8, spaceBefore=2))

        # Section 1: Plot & Academic Summary
        story.append(Paragraph("1. TÓM TẮT CỐT TRUYỆN SONG NGỮ (BILINGUAL SUMMARY & ANALYSIS)", styles["SubSectionHeading"]))
        story.append(Paragraph(f"<b>[English Analysis]</b> {ch.summary_en}", styles["BodyEN"]))
        story.append(Paragraph(f"<b>[Bản dịch & Bình giải]</b> {ch.summary_vi}", styles["BodyVI"]))

        # Section 2: Literary & Sociological Critical Analysis
        story.append(Paragraph("2. PHÂN TÍCH PHÊ BÌNH VĂN HỌC & XÃ HỘI HỌC (CRITICAL LITERARY DISCOURSE)", styles["SubSectionHeading"]))
        story.append(Paragraph(f"<b>[Literary Context]</b> {ch.literary_analysis_en}", styles["BodyEN"]))
        story.append(Paragraph(f"<b>[Phân tích chuyên sâu]</b> {ch.literary_analysis_vi}", styles["BodyVI"]))

        # Section 3: Cyberpunk Terminology & Technological Lore
        story.append(Paragraph("3. THUẬT NGỮ CÔNG NGHỆ & VĂN HÓA CYBERPUNK (CYBERPUNK TERMINOLOGY & LORE)", styles["SubSectionHeading"]))
        lore_rows = [
            [Paragraph("<b>Khái niệm / Thuật ngữ</b>", styles["MetaLabel"]), Paragraph("<b>Định nghĩa & Ý nghĩa Văn hóa Xã hội</b>", styles["MetaLabel"])]
        ]
        for item in ch.cyberpunk_lore:
            desc = (
                f"<b>{item.category}:</b> {item.explanation_en}<br/>"
                f"<font color='#047857'>{item.explanation_vi}</font><br/>"
                f"<i>Impact: {item.cultural_impact}</i>"
            )
            lore_rows.append([
                Paragraph(f"<b>{item.term}</b>", styles["VocabTerm"]),
                Paragraph(desc, styles["VocabDef"])
            ])
        lore_table = Table(lore_rows, colWidths=[content_width*0.28, content_width*0.72])
        lore_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F8FAFC")),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
            ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
            ('PADDING', (0, 0), (-1, -1), 4),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        story.append(lore_table)
        story.append(Spacer(1, 6))

        # Section 4: Academic Lexicon (C1/C2 IELTS/TOEFL/Cambridge)
        story.append(Paragraph("4. TỪ VỰNG HỌC THUẬT NÂNG CAO C1/C2 (ACADEMIC & LITERARY LEXICON)", styles["SubSectionHeading"]))
        vocab_rows = [
            [
                Paragraph("<b>Từ vựng & IPA</b>", styles["MetaLabel"]),
                Paragraph("<b>Định nghĩa Anh - Việt & Cụm từ (Collocations)</b>", styles["MetaLabel"]),
                Paragraph("<b>Câu ví dụ ngữ cảnh (Contextual Exemplar)</b>", styles["MetaLabel"])
            ]
        ]
        for v in ch.vocabulary:
            colloc_str = " • ".join(v.collocations)
            v_desc = (
                f"<b>[{v.part_of_speech.upper()}] ({v.cefr_level}):</b> {v.definition_en}<br/>"
                f"<font color='#047857'>{v.definition_vi}</font><br/>"
                f"<b>Collocations:</b> <i>{colloc_str}</i>"
            )
            vocab_rows.append([
                Paragraph(f"<b>{v.term}</b><br/><font color='#64748B'>{v.ipa}</font>", styles["VocabTerm"]),
                Paragraph(v_desc, styles["VocabDef"]),
                Paragraph(f"\"{v.context_sentence}\"", styles["VocabDef"])
            ])
        vocab_table = Table(vocab_rows, colWidths=[content_width*0.22, content_width*0.48, content_width*0.30])
        vocab_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F1F5F9")),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
            ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
            ('PADDING', (0, 0), (-1, -1), 4),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        story.append(vocab_table)
        story.append(Spacer(1, 6))

        # Section 5: Grammar Masterclass
        story.append(Paragraph("5. CẤU TRÚC NGỮ PHÁP CHUYÊN SÂU (ADVANCED GRAMMATICAL DISCOURSE)", styles["SubSectionHeading"]))
        g = ch.grammar_focus
        g_box_data = [
            [Paragraph(f"<b>Trọng tâm:</b> {g.point}", styles["VocabTerm"])],
            [Paragraph(f"<b>Cấu trúc chuẩn:</b> <code>{g.structure}</code>", styles["VocabDef"])],
            [Paragraph(f"<b>Giải thích:</b> {g.explanation_en}<br/><font color='#047857'>{g.explanation_vi}</font>", styles["VocabDef"])],
            [Paragraph(f"<b>Câu mẫu văn học:</b> <i>\"{g.exemplar_sentence}\"</i>", styles["VocabDef"])],
            [Paragraph(f"<b>Ứng dụng thi cử (IELTS/TOEFL/Cambridge):</b> {g.exam_utility}", styles["MetaLabel"])]
        ]
        g_table = Table(g_box_data, colWidths=[content_width])
        g_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#EFF6FF")),
            ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#93C5FD")),
            ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#DBEAFE")),
            ('PADDING', (0, 0), (-1, -1), 5),
        ]))
        story.append(g_table)
        story.append(Spacer(1, 6))

        # Section 6: Exam Practice Questions & Detailed Keys
        story.append(Paragraph("6. BÀI TẬP RÀ SOÁT CHUẨN HÓA QUỐC TẾ (STANDARDIZED EXAM PRACTICE)", styles["SubSectionHeading"]))
        for idx, q in enumerate(ch.practice_questions, 1):
            story.append(Paragraph(f"<b>Question {idx} [{q.question_type}]:</b> {q.prompt_en}", styles["QuestionPrompt"]))
            letters = ["A", "B", "C", "D"]
            for opt_idx, opt_text in enumerate(q.options):
                story.append(Paragraph(f"<b>({letters[opt_idx]})</b> {opt_text}", styles["QuestionOption"]))
            correct_letter = letters[q.correct_option]
            ans_str = (
                f"<b>Đáp án đúng: ({correct_letter})</b> — <i>{q.explanation_en}</i> "
                f"<font color='#047857'>{q.explanation_vi}</font>"
            )
            story.append(Paragraph(ans_str, styles["Explanation"]))

        story.append(Spacer(1, 15))
        story.append(PageBreak())

    # ==========================================
    # 5. APPENDIX: COMPREHENSIVE ANSWER KEY & INDEX
    # ==========================================
    story.append(Paragraph("PHỤ LỤC: BẢNG TRA CỨU ĐÁP ÁN TOÀN BỘ BÀI TẬP", styles["PartHeading"]))
    story.append(Paragraph("COMPREHENSIVE EXAM PRACTICE ANSWER KEY (CHAPTERS 1 - 24)", styles["BookCoverSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#0284C7"), spaceAfter=15))

    key_rows = [
        [
            Paragraph("<b>Chương</b>", styles["MetaLabel"]),
            Paragraph("<b>Câu hỏi 1 (Loại bài & Đáp án)</b>", styles["MetaLabel"]),
            Paragraph("<b>Câu hỏi 2 (Loại bài & Đáp án)</b>", styles["MetaLabel"])
        ]
    ]
    letters = ["A", "B", "C", "D"]
    for ch in CURRICULUM.chapters:
        q1 = ch.practice_questions[0]
        q2 = ch.practice_questions[1]
        key_rows.append([
            Paragraph(f"<b>Chương {ch.number}</b>", styles["VocabTerm"]),
            Paragraph(f"<b>({letters[q1.correct_option]})</b> {q1.question_type}", styles["VocabDef"]),
            Paragraph(f"<b>({letters[q2.correct_option]})</b> {q2.question_type}", styles["VocabDef"])
        ])

    key_table = Table(key_rows, colWidths=[content_width*0.2, content_width*0.4, content_width*0.4])
    key_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F8FAFC")),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('PADDING', (0, 0), (-1, -1), 4),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(key_table)

    print("Compiling PDF document with NumberedCanvas...")
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF build successful! Output file: {output_path}")

if __name__ == "__main__":
    build_pdf()
