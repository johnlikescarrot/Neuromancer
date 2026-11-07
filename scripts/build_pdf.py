#!/usr/bin/env python3
"""Build the complete interleaved English–Vietnamese learning PDF."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import portrait
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

PAGE_SIZE = portrait((7 * inch, 10 * inch))
PAGE_WIDTH, PAGE_HEIGHT = PAGE_SIZE
INK = colors.HexColor("#172A32")
TEAL = colors.HexColor("#0B626A")
CYAN = colors.HexColor("#43C6D4")
MUTED = colors.HexColor("#697C84")
PALE = colors.HexColor("#EDF4F4")
DARK = colors.HexColor("#071A26")
PAPER = colors.HexColor("#FCFDFC")


def register_fonts() -> None:
    font_dir = Path("/usr/share/fonts/truetype/dejavu")
    required = {
        "BookSerif": "DejaVuSerif.ttf",
        "BookSerif-Bold": "DejaVuSerif-Bold.ttf",
        "BookSans": "DejaVuSans.ttf",
        "BookSans-Bold": "DejaVuSans-Bold.ttf",
        "BookMono": "DejaVuSansMono.ttf",
    }
    for name, filename in required.items():
        path = font_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"Required Unicode font is missing: {path}")
        pdfmetrics.registerFont(TTFont(name, str(path)))
    pdfmetrics.registerFontFamily(
        "BookSerif", normal="BookSerif", bold="BookSerif-Bold"
    )
    pdfmetrics.registerFontFamily("BookSans", normal="BookSans", bold="BookSans-Bold")


def styles() -> dict[str, ParagraphStyle]:
    return {
        "cover_author": ParagraphStyle(
            "cover_author",
            fontName="BookSans-Bold",
            fontSize=11,
            leading=15,
            textColor=CYAN,
            alignment=TA_LEFT,
            spaceAfter=16,
            tracking=2,
        ),
        "cover_title": ParagraphStyle(
            "cover_title",
            fontName="BookSans-Bold",
            fontSize=34,
            leading=38,
            textColor=colors.white,
            alignment=TA_LEFT,
            spaceAfter=18,
        ),
        "cover_subtitle": ParagraphStyle(
            "cover_subtitle",
            fontName="BookSerif",
            fontSize=15,
            leading=22,
            textColor=colors.HexColor("#D6E9EC"),
            alignment=TA_LEFT,
            spaceAfter=18,
        ),
        "cover_meta": ParagraphStyle(
            "cover_meta",
            fontName="BookSans",
            fontSize=8,
            leading=14,
            textColor=colors.HexColor("#9FC3CA"),
            alignment=TA_LEFT,
        ),
        "h1": ParagraphStyle(
            "h1",
            fontName="BookSans-Bold",
            fontSize=20,
            leading=26,
            textColor=DARK,
            spaceBefore=4,
            spaceAfter=14,
            keepWithNext=True,
        ),
        "h2": ParagraphStyle(
            "h2",
            fontName="BookSans-Bold",
            fontSize=14,
            leading=20,
            textColor=TEAL,
            spaceBefore=14,
            spaceAfter=8,
            keepWithNext=True,
        ),
        "part": ParagraphStyle(
            "part",
            fontName="BookSans-Bold",
            fontSize=22,
            leading=30,
            textColor=DARK,
            spaceAfter=16,
        ),
        "part_vi": ParagraphStyle(
            "part_vi",
            fontName="BookSerif",
            fontSize=15,
            leading=23,
            textColor=TEAL,
            spaceAfter=14,
        ),
        "chapter": ParagraphStyle(
            "chapter",
            fontName="BookSans-Bold",
            fontSize=25,
            leading=30,
            textColor=DARK,
            spaceAfter=8,
        ),
        "chapter_part": ParagraphStyle(
            "chapter_part",
            fontName="BookSans",
            fontSize=7.5,
            leading=12,
            textColor=MUTED,
            spaceAfter=18,
        ),
        "dedication_en": ParagraphStyle(
            "dedication_en",
            fontName="BookSerif",
            fontSize=14,
            leading=23,
            textColor=INK,
            spaceAfter=24,
        ),
        "dedication_vi": ParagraphStyle(
            "dedication_vi",
            fontName="BookSerif",
            fontSize=13,
            leading=22,
            textColor=TEAL,
        ),
        "body": ParagraphStyle(
            "body",
            fontName="BookSerif",
            fontSize=9.3,
            leading=14,
            textColor=INK,
            alignment=TA_JUSTIFY,
            spaceAfter=8,
            allowWidows=0,
            allowOrphans=0,
        ),
        "english": ParagraphStyle(
            "english",
            fontName="BookSerif",
            fontSize=9.2,
            leading=13.5,
            textColor=INK,
            alignment=TA_JUSTIFY,
            spaceAfter=4,
            allowWidows=0,
            allowOrphans=0,
        ),
        "vietnamese": ParagraphStyle(
            "vietnamese",
            fontName="BookSerif",
            fontSize=9.35,
            leading=13.8,
            textColor=TEAL,
            alignment=TA_JUSTIFY,
            leftIndent=11,
            spaceAfter=9,
            allowWidows=0,
            allowOrphans=0,
        ),
        "pid": ParagraphStyle(
            "pid",
            fontName="BookMono",
            fontSize=5.8,
            leading=8,
            textColor=MUTED,
            spaceBefore=5,
            spaceAfter=2,
            keepWithNext=True,
        ),
        "small": ParagraphStyle(
            "small",
            fontName="BookSans",
            fontSize=7.5,
            leading=11.5,
            textColor=MUTED,
            spaceAfter=6,
        ),
        "note": ParagraphStyle(
            "note",
            fontName="BookSerif",
            fontSize=8.5,
            leading=13,
            textColor=INK,
            backColor=PALE,
            borderPadding=10,
            spaceBefore=8,
            spaceAfter=10,
        ),
        "table_header": ParagraphStyle(
            "table_header",
            fontName="BookSans-Bold",
            fontSize=7.2,
            leading=10,
            textColor=colors.white,
        ),
        "table_cell": ParagraphStyle(
            "table_cell",
            fontName="BookSans",
            fontSize=7.1,
            leading=10.5,
            textColor=INK,
        ),
        "table_term": ParagraphStyle(
            "table_term",
            fontName="BookSans-Bold",
            fontSize=7.4,
            leading=10.5,
            textColor=DARK,
        ),
        "toc_title": ParagraphStyle(
            "toc_title",
            fontName="BookSans-Bold",
            fontSize=20,
            leading=26,
            textColor=DARK,
            spaceAfter=18,
        ),
    }


class AccentRule(Flowable):
    def __init__(self, width: float = 90, height: float = 8):
        super().__init__()
        self.width = width
        self.height = height

    def draw(self) -> None:
        self.canv.setStrokeColor(CYAN)
        self.canv.setLineWidth(2)
        self.canv.line(0, self.height / 2, self.width, self.height / 2)


class BookDocTemplate(BaseDocTemplate):
    def beforeDocument(self) -> None:
        self.running_title = "NEUROMANCER · ANH–VIỆT"

    def afterFlowable(self, flowable: Flowable) -> None:
        if not isinstance(flowable, Paragraph):
            return
        running_title = getattr(flowable, "_running_title", None)
        if running_title:
            self.running_title = running_title
        level = getattr(flowable, "_toc_level", None)
        if level is None:
            return
        title = flowable.getPlainText()
        key = flowable._bookmark_name
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(title, key, level=level, closed=level == 0)
        self.notify("TOCEntry", (level, title, self.page, key))


def on_page(canvas, document) -> None:
    canvas.saveState()
    canvas.setTitle("Neuromancer — Ấn bản song ngữ Anh–Việt")
    canvas.setAuthor("William Gibson; bản dịch máy hỗ trợ")
    canvas.setSubject("Bilingual English–Vietnamese learning edition, 24 chapters")
    canvas.setKeywords("Neuromancer, William Gibson, English, Vietnamese, bilingual, CEFR")
    canvas.setCreator("Neuromancer bilingual reproducible edition pipeline")
    if document.page == 1:
        canvas.setFillColor(DARK)
        canvas.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
        canvas.setFillColor(CYAN)
        canvas.rect(0, PAGE_HEIGHT - 16, PAGE_WIDTH, 16, fill=1, stroke=0)
        canvas.setStrokeColor(colors.HexColor("#174151"))
        for offset in range(0, 7):
            canvas.line(
                PAGE_WIDTH - 160 + offset * 18,
                60,
                PAGE_WIDTH - 60 + offset * 18,
                PAGE_HEIGHT - 70,
            )
    else:
        canvas.setFillColor(PAPER)
        canvas.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
        canvas.setStrokeColor(colors.HexColor("#CFDCDD"))
        canvas.setLineWidth(0.5)
        canvas.line(46, PAGE_HEIGHT - 39, PAGE_WIDTH - 46, PAGE_HEIGHT - 39)
        canvas.setFont("BookSans", 6.3)
        canvas.setFillColor(MUTED)
        header = getattr(document, "running_title", "NEUROMANCER")
        canvas.drawString(46, PAGE_HEIGHT - 31, header[:95])
        canvas.setStrokeColor(colors.HexColor("#CFDCDD"))
        canvas.line(46, 38, PAGE_WIDTH - 46, 38)
        canvas.setFont("BookSans", 6.2)
        canvas.drawString(46, 25, "ANH–VIỆT · BẢN DỊCH MÁY HỖ TRỢ")
        canvas.setFont("BookMono", 7)
        canvas.setFillColor(INK)
        canvas.drawRightString(PAGE_WIDTH - 46, 25, str(document.page))
    canvas.restoreState()


def heading(
    text: str,
    style: ParagraphStyle,
    *,
    toc_level: int | None = None,
    bookmark: str | None = None,
    running_title: str | None = None,
) -> Paragraph:
    paragraph = Paragraph(escape(text), style)
    if toc_level is not None:
        paragraph._toc_level = toc_level
        paragraph._bookmark_name = bookmark or re.sub(r"\W+", "-", text.lower())
    if running_title:
        paragraph._running_title = running_title
    return paragraph


def p(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(escape(text), style)


def rich(text: str, style: ParagraphStyle) -> Paragraph:
    """Render trusted, editor-authored ReportLab inline markup."""
    return Paragraph(text, style)


def link(label: str, url: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(
        f'<link href="{escape(url)}" color="#0B626A">{escape(label)}</link>', style
    )


def front_matter(source: dict, translation: dict, editorial: dict, st: dict) -> list:
    story: list = [
        Spacer(1, 118),
        p("WILLIAM GIBSON", st["cover_author"]),
        p("NEUROMANCER", st["cover_title"]),
        AccentRule(128),
        Spacer(1, 12),
        p("ẤN BẢN SONG NGỮ ANH–VIỆT", st["cover_subtitle"]),
        Spacer(1, 112),
        rich(
            f"{source['chapter_count']} CHƯƠNG · {source['paragraph_count']:,} ĐOẠN ĐỐI CHIẾU<br/>"
            "ĐỌC B2 → C2 · TỪ VỰNG CYBERPUNK THEO NGỮ CẢNH<br/><br/>"
            "BẢN DỊCH MÁY HỖ TRỢ · CÓ ĐÁNH DẤU RÀ SOÁT THỦ CÔNG",
            st["cover_meta"],
        ),
        PageBreak(),
        heading("THÔNG TIN ẤN BẢN", st["h1"], toc_level=0, bookmark="imprint"),
        p(
            "Nguyên tác: Neuromancer (1984), William Gibson. Quyền đối với nguyên tác thuộc "
            "tác giả và các chủ sở hữu liên quan. Ấn bản học tập này được tạo từ tệp EPUB do "
            "người dùng cung cấp; tệp nguồn không kèm giấy phép cho phép phát hành lại hoặc "
            "tạo bản dịch thương mại. Không có tuyên bố nào ở đây thay thế cho việc xin phép "
            "khi pháp luật hiện hành yêu cầu.",
            st["body"],
        ),
        p(
            "Trạng thái bản dịch: bản nháp máy hỗ trợ. Mỗi đoạn đều giữ nguyên tiếng Anh và có "
            "một đoạn Việt tương ứng; chỉ các đoạn được đánh dấu ‘human-reviewed’ trong dữ liệu "
            "nguồn là đã rà soát thủ công. Chưa có một quy trình biên tập văn học độc lập toàn "
            "sách. Không dùng bản nháp này làm căn cứ trích dẫn học thuật hoặc gọi là bản dịch "
            "tốt nhất/chuẩn xác tuyệt đối.",
            st["body"],
        ),
        rich(
            f"Nguồn: {source['source_file']} · SHA-256 {source['source_sha256']}<br/>"
            f"Cấu trúc: {source['chapter_count']} chương, {source['paragraph_count']:,} đoạn, "
            f"{source['body_word_count']:,} từ thân bài tiếng Anh.<br/>"
            f"Mô hình dịch: {translation['model']} · chuyển đổi {translation['model_revision']} "
            f"· giấy phép mô hình {translation['model_license']}.",
            st["small"],
        ),
        p(
            "Ghi công mô hình: QuickMT English→Vietnamese (CC BY 4.0); bản CTranslate2 int8 do "
            "thiennq chuyển đổi. Mã dựng sách và dữ liệu QA nằm trong kho đi kèm. Ngày tra cứu "
            f"các nguồn thang điểm: {editorial['accessed']}.",
            st["small"],
        ),
        PageBreak(),
        Spacer(1, 142),
        heading(
            "DEDICATION · LỜI ĐỀ TẶNG",
            st["h1"],
            toc_level=0,
            bookmark="dedication",
        ),
        AccentRule(88),
        Spacer(1, 20),
        rich(
            "<br/>".join(escape(line) for line in source["frontmatter"]["dedication_en"]),
            st["dedication_en"],
        ),
        rich(
            "<br/>".join(escape(line) for line in editorial["dedication_vi"]),
            st["dedication_vi"],
        ),
        PageBreak(),
        heading(
            "ĐỌC NEUROMANCER NHƯ MỘT VĂN BẢN C1–C2",
            st["h1"],
            toc_level=0,
            bookmark="reader-guide",
        ),
        p(
            "Neuromancer là văn bản giàu tiếng lóng, danh từ tự tạo, cú pháp cắt gọt và hình ảnh "
            "gián tiếp. Mục tiêu của ấn bản là giúp người đọc giữ mạch suy luận mà không biến "
            "tiếng Việt thành đáp án thay thế tiếng Anh. Bản đối chiếu đầy đủ 24 chương, không "
            "rút gọn; phần thuật ngữ và hoạt động đọc là lớp hỗ trợ thêm, không phải nội dung "
            "của tiểu thuyết.",
            st["body"],
        ),
        heading("Bốn lượt đọc cho mỗi đoạn", st["h2"]),
        rich(
            "<b>1 · Ngữ cảnh:</b> đọc tiếng Anh trước, đánh dấu điều chưa hiểu nhưng chưa tra "
            "ngay. <b>2 · Đối chiếu:</b> đọc tiếng Việt để kiểm tra quan hệ nhân quả, chủ thể "
            "và nghĩa bóng. <b>3 · Ngôn ngữ:</b> quay lại tiếng Anh, ghi cụm động từ, cách nối "
            "ý và một lựa chọn dịch khác. <b>4 · Thu hồi:</b> che tiếng Việt, tóm tắt bằng "
            "tiếng Anh 2–4 câu rồi tự kiểm tra với bạn học hoặc giáo viên.",
            st["body"],
        ),
        rich(
            "Mã như <font name='BookMono'>ch01-p0001</font> là khóa ổn định để tra cứu và báo "
            "lỗi. Màu xanh than là tiếng Anh; màu xanh ngọc là tiếng Việt. Phụ lục thuật ngữ "
            "dẫn tới lần xuất hiện đầu tiên khi tìm được bằng khớp văn bản.",
            st["note"],
        ),
        heading("Mục tiêu điểm: định hướng, không phải cam kết", st["h2"]),
        p(
            "Đọc tiểu thuyết chủ yếu rèn đọc hiểu, từ vựng và cảm nhận phong cách. Nó không tự "
            "động rèn đủ nghe, nói, viết theo thời gian hay chiến thuật từng bài thi. Các mục "
            "tiêu dưới đây do người học chọn; chúng không tương đương nhau trên mọi thang CEFR.",
            st["body"],
        ),
    ]

    goal_rows = [
        [
            p("BÀI THI", st["table_header"]),
            p("MỤC TIÊU", st["table_header"]),
            p("ĐỐI CHIẾU CẦN LƯU Ý", st["table_header"]),
        ]
    ]
    for goal in editorial["reading_goals"]:
        goal_rows.append(
            [
                p(goal["exam"], st["table_term"]),
                p(goal["target"], st["table_cell"]),
                p(goal["alignment"], st["table_cell"]),
            ]
        )
    goal_table = Table(goal_rows, colWidths=[133, 58, 205], repeatRows=1, hAlign="LEFT")
    goal_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), DARK),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#C5D4D6")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PALE]),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.extend(
        [
            goal_table,
            Spacer(1, 10),
            p(
                "Đặc biệt: bảng ETS hiện hành khuyến nghị yêu cầu TOEFL 90 cũ tương ứng 4,5; "
                "band 5 mới có tổng điểm tham chiếu từ 95. DET 120 thuộc B2 theo công bố CEFR "
                "2026 của Duolingo (C1: 130–150). Luôn kiểm tra yêu cầu của tổ chức nhận điểm "
                "tại thời điểm nộp hồ sơ.",
                st["note"],
            ),
            heading("Nguồn đối chiếu thang điểm", st["h2"]),
        ]
    )
    for index, source_link in enumerate(editorial["score_sources"], start=1):
        story.append(
            link(
                f"[{index}] {source_link['label']} — {source_link['url']}",
                source_link["url"],
                st["small"],
            )
        )
    story.extend(
        [
            PageBreak(),
            heading("MỤC LỤC", st["toc_title"], toc_level=0, bookmark="contents"),
        ]
    )
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(
            "TOC0",
            fontName="BookSans-Bold",
            fontSize=8.5,
            leading=15,
            leftIndent=0,
            firstLineIndent=0,
            textColor=DARK,
            spaceBefore=5,
        ),
        ParagraphStyle(
            "TOC1",
            fontName="BookSerif",
            fontSize=8.2,
            leading=13,
            leftIndent=16,
            firstLineIndent=0,
            textColor=TEAL,
        ),
    ]
    toc.dotsMinLevel = 0
    story.append(toc)
    return story


def first_occurrence(term: str, source: dict) -> str | None:
    # Acronyms and mixed-case names need exact matching; common words are
    # matched case-insensitively to find their first contextual use.
    flags = 0 if any(character.isupper() for character in term[1:]) else re.IGNORECASE
    pattern = re.compile(re.escape(term), flags)
    for chapter in source["chapters"]:
        for paragraph in chapter["paragraphs"]:
            if pattern.search(paragraph["en"]):
                return paragraph["id"]
    return None


def glossary(source: dict, editorial: dict, st: dict) -> list:
    story = [
        PageBreak(),
        heading(
            "PHỤ LỤC A · THUẬT NGỮ & ĐỊA DANH",
            st["h1"],
            toc_level=0,
            bookmark="glossary",
            running_title="PHỤ LỤC A · THUẬT NGỮ",
        ),
        p(
            "Các nghĩa dưới đây là gợi ý theo ngữ cảnh Neuromancer, không phải quy tắc thay thế "
            "mọi lần xuất hiện. Mã đoạn là liên kết tới lần xuất hiện đầu tiên tìm được tự động; "
            "dấu — nghĩa là cụm chính xác không có trong nguyên bản dưới dạng đã liệt kê.",
            st["body"],
        ),
    ]
    rows = [
        [
            p("THUẬT NGỮ · THAM CHIẾU", st["table_header"]),
            p("GỢI Ý VIỆT", st["table_header"]),
            p("GHI CHÚ NGỮ CẢNH", st["table_header"]),
        ]
    ]
    for entry in editorial["glossary"]:
        reference = first_occurrence(entry["term"], source)
        if reference:
            term_markup = (
                f"{escape(entry['term'])}<br/>"
                f'<link href="#{reference}" color="#697C84">'
                f"<font name='BookMono' size='5.8'>{reference}</font></link>"
            )
        else:
            term_markup = f"{escape(entry['term'])}<br/><font color='#697C84'>—</font>"
        rows.append(
            [
                Paragraph(term_markup, st["table_term"]),
                p(entry["vi"], st["table_cell"]),
                p(entry["note"], st["table_cell"]),
            ]
        )
    table = Table(rows, colWidths=[112, 105, 179], repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), DARK),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#CAD8DA")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PALE]),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(table)
    return story


def methodology(source: dict, translation: dict, st: dict) -> list:
    reviewed = sum(
        1 for record in translation["paragraphs"].values() if record.get("status") == "human-reviewed"
    )
    machine = translation["completed_paragraphs"] - reviewed
    return [
        PageBreak(),
        heading(
            "PHỤ LỤC B · PHƯƠNG PHÁP & KIỂM CHỨNG",
            st["h1"],
            toc_level=0,
            bookmark="methodology",
            running_title="PHỤ LỤC B · PHƯƠNG PHÁP & QA",
        ),
        heading("Chuỗi sản xuất có thể tái lập", st["h2"]),
        p(
            "EPUB gốc được đọc theo spine; tiêu đề h1/h2 xác định phần, h3 xác định chương. "
            "Mỗi đoạn nhận một ID ổn định và SHA-256 của câu chữ tiếng Anh. Bộ chia câu pysbd "
            "gom các câu thành đơn vị tối đa 320 token SentencePiece để giữ ngữ cảnh gần; câu "
            "quá dài được chia ở ranh giới từ với kiểm tra ghép lại toàn văn. Mô hình CTranslate2 "
            "dịch theo lô, lưu checkpoint sau mỗi lô và toàn cục sau mỗi chương.",
            st["body"],
        ),
        heading("Các kiểm tra bắt buộc", st["h2"]),
        p(
            "Đủ 24 chương và 2.597 ID đoạn; không thiếu, thừa hoặc trùng ID; SHA-256 nguồn "
            "khớp; không đoạn Việt rỗng; không token lỗi hay ký tự điều khiển; kiểm tra tỷ lệ "
            "độ dài, lặp cụm bất thường, dấu hiệu giữ nguyên tiếng Anh và độ phủ tên riêng. "
            "Sau khi kết xuất, PyMuPDF mở lại PDF để kiểm tra số trang, metadata, font nhúng, "
            "text layer, điểm đầu/cuối và toàn bộ mã đoạn. Báo cáo JSON đi kèm tệp PDF.",
            st["body"],
        ),
        heading("Số liệu của tệp này", st["h2"]),
        p(
            f"Nguồn: {source['chapter_count']} chương · {source['paragraph_count']:,} đoạn · "
            f"{source['body_word_count']:,} từ thân bài. Bản dịch: "
            f"{translation['completed_paragraphs']:,}/{translation['total_paragraphs']:,} đoạn; "
            f"{machine:,} đoạn máy nháp; {reviewed:,} đoạn có ghi nhận rà soát thủ công. "
            f"Beam size: {translation['decoding']['beam_size']}.",
            st["body"],
        ),
        p(
            "Kiểm tra tự động chứng minh độ phủ và tính toàn vẹn kỹ thuật, không chứng minh "
            "chất lượng văn học. Cần người biên tập song ngữ rà toàn sách để đánh giá giọng "
            "noir, nhịp câu, ẩn dụ, đại từ, sắc thái tiếng lóng và tính nhất quán của từng cảnh.",
            st["note"],
        ),
        heading("Phản hồi có thể truy vết", st["h2"]),
        p(
            "Khi báo lỗi, ghi mã đoạn, câu tiếng Anh, bản Việt hiện tại, phương án đề xuất và "
            "lý do theo ngữ cảnh. Chỉnh tại translation/overrides.json cho rà soát thủ công; "
            "không sửa trực tiếp kết quả máy mà bỏ qua trạng thái nguồn.",
            st["body"],
        ),
        Spacer(1, 20),
        AccentRule(128),
        Spacer(1, 10),
        p("HẾT ẤN BẢN · END OF EDITION", st["small"]),
    ]


def build(source: dict, translation: dict, editorial: dict, output: Path) -> None:
    register_fonts()
    st = styles()
    output.parent.mkdir(parents=True, exist_ok=True)
    frame = Frame(
        46,
        48,
        PAGE_WIDTH - 92,
        PAGE_HEIGHT - 100,
        id="book-frame",
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
    )
    document = BookDocTemplate(
        str(output),
        pagesize=PAGE_SIZE,
        leftMargin=46,
        rightMargin=46,
        topMargin=50,
        bottomMargin=50,
        title="Neuromancer — Ấn bản song ngữ Anh–Việt",
        author="William Gibson; bản dịch máy hỗ trợ",
        pageCompression=1,
    )
    document.addPageTemplates([PageTemplate(id="book", frames=[frame], onPage=on_page)])
    story = front_matter(source, translation, editorial, st)
    current_part = None
    part_index = 0
    for chapter in source["chapters"]:
        if chapter["part"] != current_part:
            current_part = chapter["part"]
            part_index += 1
            part_vi = editorial["parts"][current_part]
            story.extend(
                [
                    PageBreak(),
                    Spacer(1, 168),
                    heading(
                        current_part,
                        st["part"],
                        toc_level=0,
                        bookmark=f"part-{part_index}",
                        running_title=part_vi,
                    ),
                    AccentRule(112),
                    Spacer(1, 12),
                    p(part_vi, st["part_vi"]),
                    p(
                        f"Chương {chapter['number']}–"
                        f"{max(c['number'] for c in source['chapters'] if c['part'] == current_part)}",
                        st["small"],
                    ),
                    PageBreak(),
                ]
            )
        chapter_label = f"CHƯƠNG {chapter['number']:02d} · CHAPTER {chapter['number']:02d}"
        story.append(
            heading(
                chapter_label,
                st["chapter"],
                toc_level=1,
                bookmark=chapter["id"],
                running_title=f"{chapter_label} · {editorial['parts'][current_part]}",
            )
        )
        story.append(
            rich(
                f"{current_part}<br/>{editorial['parts'][current_part]} · "
                f"{len(chapter['paragraphs'])} đoạn",
                st["chapter_part"],
            )
        )
        story.append(AccentRule(70))
        story.append(Spacer(1, 8))
        for source_paragraph in chapter["paragraphs"]:
            pid = source_paragraph["id"]
            record = translation["paragraphs"][pid]
            identifier = Paragraph(
                f'<a name="{pid}"/>{pid} · {record["status"].upper()}', st["pid"]
            )
            english = p(source_paragraph["en"], st["english"])
            vietnamese = Paragraph(
                f"<font name='BookSans' size='5.8'>VI</font>  {escape(record['vi'])}",
                st["vietnamese"],
            )
            if len(source_paragraph["en"].split()) + len(record["vi"].split()) <= 115:
                story.append(KeepTogether([identifier, english, vietnamese]))
            else:
                story.extend([identifier, english, vietnamese])
    story.extend(glossary(source, editorial, st))
    story.extend(methodology(source, translation, st))
    document.multiBuild(story)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("build/source.json"))
    parser.add_argument("--translation", type=Path, default=Path("translation/vi.json"))
    parser.add_argument("--editorial", type=Path, default=Path("edition/editorial.json"))
    parser.add_argument(
        "--output", type=Path, default=Path("dist/Neuromancer-EN-VI-Bilingual.pdf")
    )
    parser.add_argument("--allow-partial", action="store_true")
    args = parser.parse_args()
    source = json.loads(args.source.read_text(encoding="utf-8"))
    translation = json.loads(args.translation.read_text(encoding="utf-8"))
    editorial = json.loads(args.editorial.read_text(encoding="utf-8"))
    source_ids = {
        paragraph["id"]
        for chapter in source["chapters"]
        for paragraph in chapter["paragraphs"]
    }
    translated_ids = set(translation["paragraphs"])
    if not args.allow_partial:
        if source_ids != translated_ids:
            missing = sorted(source_ids - translated_ids)
            extra = sorted(translated_ids - source_ids)
            raise ValueError(f"Coverage mismatch; missing={missing[:8]}, extra={extra[:8]}")
        if translation.get("source_sha256") != source.get("source_sha256"):
            raise ValueError("Translation and source EPUB hashes differ")
        if translation.get("completed_paragraphs") != source.get("paragraph_count"):
            raise ValueError("Translation completion count is not the full source")
    else:
        source["chapters"] = [
            {
                **chapter,
                "paragraphs": [
                    paragraph
                    for paragraph in chapter["paragraphs"]
                    if paragraph["id"] in translated_ids
                ],
            }
            for chapter in source["chapters"]
        ]
        source["chapters"] = [
            chapter for chapter in source["chapters"] if chapter["paragraphs"]
        ]
        if not source["chapters"]:
            raise ValueError("No translated paragraphs available for partial smoke build")
        source["chapter_count"] = len(source["chapters"])
        source["paragraph_count"] = sum(len(c["paragraphs"]) for c in source["chapters"])
    build(source, translation, editorial, args.output)
    print(f"Wrote {args.output} ({args.output.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
