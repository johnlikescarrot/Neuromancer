import json
import sys
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT

# Register Fonts
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FONT_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

pdfmetrics.registerFont(TTFont("DejaVuSerif", FONT_REG))
pdfmetrics.registerFont(TTFont("DejaVuSerif-Bold", FONT_BOLD))
pdfmetrics.registerFont(TTFont("DejaVuSans", FONT_SANS))
pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", FONT_SANS_BOLD))

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

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            return # Cover page
        self.saveState()
        self.setFont("DejaVuSans", 8)
        self.setFillColor(colors.HexColor("#555555"))
        # Running header
        self.drawString(54, 11 * inch - 36, "Neuromancer (William Gibson) — Ấn Bản Song Ngữ Anh - Việt & Cẩm Nang Học Thuật C1/C2")
        self.setStrokeColor(colors.HexColor("#CCCCCC"))
        self.setLineWidth(0.5)
        self.line(54, 11 * inch - 40, 8.5 * inch - 54, 11 * inch - 40)
        # Running footer
        page_str = f"Trang {self._pageNumber} / {page_count}"
        self.drawRightString(8.5 * inch - 54, 30, page_str)
        self.drawString(54, 30, "TOEFL 90+ / IELTS 7.0+ / PTE 65+ / Cambridge C1-C2 / DET 120+")
        self.line(54, 42, 8.5 * inch - 54, 42)
        self.restoreState()

def build_pdf(novel_json_path, notes_json_path, output_pdf_path):
    print("Loading novel and academic notes...")
    with open(novel_json_path, "r", encoding="utf-8") as f:
        novel_data = json.load(f)
    with open(notes_json_path, "r", encoding="utf-8") as f:
        notes_data = json.load(f)

    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    story = []
    styles = getSampleStyleSheet()

    # Custom styles
    cover_title_style = ParagraphStyle(
        "CoverTitle",
        parent=styles["Normal"],
        fontName="DejaVuSans-Bold",
        fontSize=32,
        leading=38,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#0A192F")
    )
    cover_sub_style = ParagraphStyle(
        "CoverSub",
        parent=styles["Normal"],
        fontName="DejaVuSerif-Bold",
        fontSize=15,
        leading=22,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#1E3A8A")
    )
    cover_meta_style = ParagraphStyle(
        "CoverMeta",
        parent=styles["Normal"],
        fontName="DejaVuSans",
        fontSize=10,
        leading=16,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#333333")
    )
    h1_style = ParagraphStyle(
        "PartHeading",
        parent=styles["Normal"],
        fontName="DejaVuSans-Bold",
        fontSize=18,
        leading=24,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#0B3C5D"),
        spaceBefore=20,
        spaceAfter=15
    )
    h2_style = ParagraphStyle(
        "ChapHeading",
        parent=styles["Normal"],
        fontName="DejaVuSans-Bold",
        fontSize=14,
        leading=18,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#1D2731"),
        spaceBefore=15,
        spaceAfter=10
    )
    en_para_style = ParagraphStyle(
        "EnPara",
        parent=styles["Normal"],
        fontName="DejaVuSerif",
        fontSize=9.5,
        leading=14,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor("#111827")
    )
    vi_para_style = ParagraphStyle(
        "ViPara",
        parent=styles["Normal"],
        fontName="DejaVuSerif",
        fontSize=9.5,
        leading=14,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor("#1E3A8A")
    )
    note_box_style = ParagraphStyle(
        "NoteBox",
        parent=styles["Normal"],
        fontName="DejaVuSans",
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#1E293B")
    )
    intro_p_style = ParagraphStyle(
        "IntroP",
        parent=styles["Normal"],
        fontName="DejaVuSerif",
        fontSize=10,
        leading=15,
        alignment=TA_JUSTIFY,
        spaceAfter=8
    )

    # ================= 1. COVER PAGE =================
    story.append(Spacer(1, 40))
    story.append(Paragraph("NEUROMANCER", cover_title_style))
    story.append(Spacer(1, 8))
    story.append(Paragraph("CƠ HƯƠNG MA TRẬN — THỰC THỂ TÂM LINH SỐ", cover_sub_style))
    story.append(Spacer(1, 15))
    story.append(Paragraph("Tác giả: William Gibson (1984)", cover_meta_style))
    story.append(Paragraph("ẤN BẢN SONG NGỮ ĐỐI CHIẾU HOÀN CHỈNH ANH - VIỆT TOÀN BỘ 24 CHƯƠNG", cover_meta_style))
    story.append(Spacer(1, 25))
    target_desc = (
        "<b>CẨM NANG VĂN HỌC & TỪ VỰNG HỌC THUẬT NÂNG CAO THIẾT KẾ ĐẠT CHUẨN:</b><br/>"
        "• <b>IELTS:</b> 7.0+ Overall (Đặc biệt phát triển Lexical Resource & Reading band 8.0+)<br/>"
        "• <b>TOEFL iBT:</b> 90+ (thi trước 21/01/2026) hoặc 5.0+ (khung định dạng mới từ 21/01/2026)<br/>"
        "• <b>PTE Academic:</b> 65+ (Pearson Test of English Academic)<br/>"
        "• <b>Cambridge English:</b> 185+ (C1 Advanced CAE & C2 Proficiency CPE)<br/>"
        "• <b>Duolingo English Test (DET):</b> 120+"
    )
    story.append(Paragraph(target_desc, cover_meta_style))
    story.append(Spacer(1, 30))
    intro_note = (
        "<i>Neuromancer</i> là kiệt tác đoạt cú ăn ba giải thưởng danh giá nhất của dòng văn học viễn tưởng thế giới: "
        "Giải Hugo, Giải Nebula và Giải Philip K. Dick. Cuốn tiểu thuyết đặt nền móng cho thuật ngữ Cyberpunk, Cyberspace, "
        "và Matrix mà cả thế giới sử dụng ngày nay. Ấn bản song ngữ này được biên soạn tỉ mỉ với mục tiêu học thuật song hành thưởng thức văn chương đỉnh cao."
    )
    story.append(Paragraph(intro_note, intro_p_style))
    story.append(PageBreak())

    # ================= 2. STUDY GUIDE & PREFACE =================
    story.append(Paragraph("LỜI TỰA & HƯỚNG DẪN HỌC TIẾNG ANH HỌC THUẬT TỪ NEUROMANCER", h1_style))
    story.append(Spacer(1, 10))
    p_intro_1 = (
        "Neuromancer của William Gibson không chỉ là một đỉnh cao văn học Cyberpunk mà còn là kho tàng vô giá về từ vựng học thuật trình độ cao (C1-C2 CEFR). "
        "Ngôn ngữ của tác phẩm chứa đựng mật độ dày đặc các cấu trúc tu từ biểu cảm, ẩn dụ công nghệ, tính từ miêu tả cảm giác, danh từ trừu tượng và cụm từ kết hợp (collocations) "
        "thường xuyên xuất hiện trong các bài thi quốc tế như IELTS Academic, TOEFL iBT, PTE Academic, Cambridge C1 Advanced và Duolingo English Test."
    )
    story.append(Paragraph(p_intro_1, intro_p_style))
    p_intro_2 = (
        "<b>Phương pháp học tập đề xuất:</b><br/>"
        "1. <b>Đọc song song đối chiếu (Parallel Reading):</b> Theo dõi văn bản tiếng Anh ở cột trái và bản dịch tiếng Việt tương ứng ở cột phải. Nhận diện cách chuyển ngữ các cấu trúc câu phức tạp và sắc thái biểu cảm.<br/>"
        "2. <b>Nghiên cứu hộp học thuật (Academic Study Notes):</b> Cuối mỗi chương, độc giả sẽ tìm thấy phần phân tích chuyên sâu các từ vựng C1-C2 then chốt, ngữ cảnh tác phẩm, collocations chuẩn xác và ứng dụng trong phòng thi.<br/>"
        "3. <b>Nắm vững thuật ngữ Cyberpunk:</b> Tra cứu bảng đối chiếu thuật ngữ ở phụ lục để hiểu sâu hệ thống khái niệm Matrix, ICE, Simstim, Deck và AI."
    )
    story.append(Paragraph(p_intro_2, intro_p_style))
    story.append(PageBreak())

    # ================= 3. CHAPTERS & BODY MATTER =================
    content_width = 8.5 * inch - 108 # 504 pt
    col_w = content_width / 2 - 6 # 246 pt each, with 12 pt gap

    current_part_name = ""
    for chapter in novel_data["chapters"]:
        chap_part = chapter.get("part_title", "")
        chap_part_vi = chapter.get("part_title_vi", chap_part)
        chap_num = chapter.get("chapter_num", "")

        if chap_part != current_part_name:
            current_part_name = chap_part
            story.append(PageBreak())
            story.append(Spacer(1, 20))
            story.append(Paragraph(chap_part_vi, h1_style))
            story.append(Spacer(1, 10))

        story.append(Paragraph(f"CHƯƠNG {chap_num} / CHAPTER {chap_num}", h2_style))
        story.append(Spacer(1, 6))

        # Render each paragraph as an individual 1-row Table to allow natural page splits
        for p in chapter["paragraphs"]:
            en_txt = p["english"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            vi_txt = p.get("vietnamese", "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            p_en = Paragraph(en_txt, en_para_style)
            p_vi = Paragraph(vi_txt, vi_para_style)
            t = Table([[p_en, p_vi]], colWidths=[col_w, col_w])
            t.setStyle(TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (0, -1), 8),
                ("LEFTPADDING", (1, 0), (1, -1), 8),
                ("RIGHTPADDING", (1, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 1),
                ("LINEAFTER", (0, 0), (0, -1), 0.5, colors.HexColor("#E2E8F0")),
            ]))
            story.append(t)

        # Chapter Academic Notes Box
        chap_notes = notes_data.get(str(chap_num), [])
        if chap_notes:
            story.append(Spacer(1, 10))
            notes_flowables = [
                Paragraph(f"<b>[TỪ VỰNG HỌC THUẬT NÂNG CAO & GHI CHÚ CHƯƠNG {chap_num}]</b>", ParagraphStyle("NoteHead", parent=note_box_style, fontName="DejaVuSans-Bold", fontSize=9, textColor=colors.HexColor("#1E3A8A"))),
                Spacer(1, 4)
            ]
            for n in chap_notes:
                term_val = n.get('term', '')
                pos_val = n.get('pos', '')
                lvl_val = n.get('level', '')
                men_val = n.get('meaning_en', '')
                mvi_val = n.get('meaning_vi', '')
                col_val = n.get('collocations', '')
                ex_val = n.get('exam_relevance', '')
                note_line = (
                    f"• <b>{term_val}</b> ({pos_val}) — <i>{lvl_val}</i><br/>"
                    f"  - <b>Định nghĩa:</b> {men_val} ({mvi_val})<br/>"
                    f"  - <b>Cụm từ trọng tâm:</b> <i>{col_val}</i><br/>"
                    f"  - <b>Ứng dụng thi cử:</b> {ex_val}"
                )
                notes_flowables.append(Paragraph(note_line, note_box_style))
                notes_flowables.append(Spacer(1, 4))

            box_table = Table([[notes_flowables]], colWidths=[content_width])
            box_table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F1F5F9")),
                ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#CBD5E1")),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
            ]))
            story.append(KeepTogether([box_table]))
            story.append(Spacer(1, 15))

    print("Building PDF with NumberedCanvas...")
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully built PDF deliverable at: {output_pdf_path}")

if __name__ == "__main__":
    build_pdf("data/neuromancer_bilingual.json", "data/academic_guide.json", "Neuromancer_Bilingual_EN_VI.pdf")
