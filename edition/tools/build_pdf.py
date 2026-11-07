#!/usr/bin/env python3
"""Build the bilingual learning companion PDF. Original pedagogy only."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[2]
ED = ROOT / "edition"
sys.path.insert(0, str(ED / "content"))

import chapters_01_07, chapters_08_12, chapters_13_18, chapters_19_24
import frontmatter as fm
import practice as pr

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                PageBreak, Table, TableStyle, KeepTogether, NextPageTemplate)
from reportlab.platypus.tableofcontents import TableOfContents

CHAPTERS = chapters_01_07.CHAPTERS + chapters_08_12.CHAPTERS + chapters_13_18.CHAPTERS + chapters_19_24.CHAPTERS
OUT = ED / "Neuromancer-Bilingual-Learning-Companion.pdf"

# Fonts
for name, file in [("BVP", "BeVietnamPro-Regular.ttf"), ("BVP-Bold", "BeVietnamPro-Bold.ttf"), ("BVP-Italic", "BeVietnamPro-Italic.ttf")]:
    pdfmetrics.registerFont(TTFont(name, str(ED / "fonts" / file)))
pdfmetrics.registerFontFamily("BVP", normal="BVP", bold="BVP-Bold", italic="BVP-Italic", boldItalic="BVP-Bold")

PAGE_W, PAGE_H = A4
MARGIN = 46
CONTENT_W = PAGE_W - 2 * MARGIN

INK = colors.HexColor("#101423")
MUTED = colors.HexColor("#4A5168")
ACCENT = colors.HexColor("#007C83")
ACCENT2 = colors.HexColor("#B4235A")
LIGHT = colors.HexColor("#F2F5F7")
LINE = colors.HexColor("#D7DEE6")
VI = colors.HexColor("#25304A")

styles = getSampleStyleSheet()
def st(name, **kw):
    base = dict(fontName="BVP", fontSize=9.6, leading=14, textColor=INK, alignment=TA_LEFT, spaceAfter=6)
    base.update(kw)
    s = ParagraphStyle(name, **base)
    styles.add(s)
    return s

S = {}
S["title"] = st("CoverTitle", fontName="BVP-Bold", fontSize=30, leading=36, textColor=colors.white, spaceAfter=10)
S["subtitle"] = st("CoverSub", fontSize=13, leading=19, textColor=colors.HexColor("#CFE7EA"), spaceAfter=8)
S["h1"] = st("SectionH1", fontName="BVP-Bold", fontSize=18, leading=23, textColor=ACCENT, spaceBefore=4, spaceAfter=10)
S["h2"] = st("ChapterH1", fontName="BVP-Bold", fontSize=14, leading=19, textColor=INK, spaceBefore=2, spaceAfter=8)
S["h3"] = st("SubH", fontName="BVP-Bold", fontSize=10.5, leading=15, textColor=ACCENT2, spaceBefore=6, spaceAfter=4)
S["body"] = st("Body", fontSize=9.6, leading=14.2)
S["vi"] = st("BodyVI", fontSize=9.6, leading=14.2, textColor=VI)
S["small"] = st("Small", fontSize=8.2, leading=11.5, textColor=MUTED)
S["tiny"] = st("Tiny", fontSize=7.4, leading=10, textColor=MUTED)
S["table"] = st("Table", fontSize=8.2, leading=11.4)
S["tableh"] = st("TableH", fontName="BVP-Bold", fontSize=8.2, leading=11.4, textColor=colors.white)
S["toc0"] = st("TOC0", fontName="BVP-Bold", fontSize=10, leading=16, textColor=INK)
S["toc1"] = st("TOC1", fontSize=9, leading=14, textColor=MUTED, leftIndent=14)
S["box"] = st("Box", fontSize=9.2, leading=13.6)
S["q"] = st("Question", fontSize=9.2, leading=13.6, spaceAfter=3)
S["opt"] = st("Option", fontSize=9, leading=13, leftIndent=12, spaceAfter=2)

def P(text, style="body"):
    return Paragraph(escape(str(text)), S[style])

def bi(en, vi, style_en="body", style_vi="vi"):
    return [P(en, style_en), P(vi, style_vi), Spacer(1, 4)]

def box(flowables, bg=LIGHT, border=LINE, pad=8):
    t = Table([[flowables]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("BOX", (0,0), (-1,-1), 0.6, border),
        ("LEFTPADDING", (0,0), (-1,-1), pad),
        ("RIGHTPADDING", (0,0), (-1,-1), pad),
        ("TOPPADDING", (0,0), (-1,-1), pad),
        ("BOTTOMPADDING", (0,0), (-1,-1), pad),
    ]))
    return t

def heading(text, level=1):
    p = P(text, "h1" if level == 1 else "h2")
    p._bookmark = text
    p._level = 0 if level == 1 else 1
    return p

class Doc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        super().__init__(filename, pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
                         topMargin=50, bottomMargin=46, title="Neuromancer — Bilingual Learning Companion",
                         author="Original bilingual study companion", subject="English–Vietnamese study companion, not a translation",
                         **kw)
        frame = Frame(MARGIN, 46, CONTENT_W, PAGE_H - 96, id="main", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id="cover", frames=[frame], onPage=self.draw_cover),
                               PageTemplate(id="normal", frames=[frame], onPage=self.header_footer)])
        self._outline_keys = set()

    def draw_cover(self, canv, doc):
        canv.saveState()
        canv.setFillColor(colors.HexColor("#0B1020"))
        canv.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
        # subtle grid
        canv.setStrokeColor(colors.HexColor("#1B2440"))
        canv.setLineWidth(0.5)
        for x in range(0, int(PAGE_W), 28):
            canv.line(x, 0, x, PAGE_H)
        for y in range(0, int(PAGE_H), 28):
            canv.line(0, y, PAGE_W, y)
        canv.setFillColor(ACCENT)
        canv.rect(MARGIN, PAGE_H - 120, 64, 6, fill=1, stroke=0)
        canv.setFillColor(colors.white)
        canv.setFont("BVP-Bold", 34)
        canv.drawString(MARGIN, PAGE_H - 180, "NEUROMANCER")
        canv.setFont("BVP", 15)
        canv.setFillColor(colors.HexColor("#CFE7EA"))
        canv.drawString(MARGIN, PAGE_H - 210, "Bilingual Learning Companion")
        canv.drawString(MARGIN, PAGE_H - 232, "Bản đồng hành học thuật Anh–Việt")
        canv.setFont("BVP", 10.5)
        canv.setFillColor(colors.HexColor("#9FB3C8"))
        lines = [
            "Original summaries, analysis, vocabulary and practice",
            "Tóm tắt, phân tích, từ vựng và luyện tập nguyên bản",
            "Covers all 24 numbered chapters and the coda",
            "Bao quát 24 chương đánh số và phần kết",
        ]
        y = PAGE_H - 290
        for ln in lines:
            canv.drawString(MARGIN, y, ln); y -= 18
        canv.setFillColor(ACCENT2)
        canv.rect(MARGIN, 120, CONTENT_W, 0.8, fill=1, stroke=0)
        canv.setFillColor(colors.HexColor("#E7B7C8"))
        canv.setFont("BVP-Bold", 10)
        canv.drawString(MARGIN, 98, "NOT A TRANSLATION • KHÔNG PHẢI BẢN DỊCH TOÀN VĂN")
        canv.setFont("BVP", 8.5)
        canv.setFillColor(colors.HexColor("#9FB3C8"))
        canv.drawString(MARGIN, 82, "Read beside a lawful copy of William Gibson’s novel.")
        canv.drawString(MARGIN, 68, "Đọc cạnh một bản tiểu thuyết hợp pháp của William Gibson.")
        canv.restoreState()

    def header_footer(self, canv, doc):
        canv.saveState()
        canv.setStrokeColor(LINE); canv.setLineWidth(0.5)
        canv.line(MARGIN, PAGE_H - 34, PAGE_W - MARGIN, PAGE_H - 34)
        canv.setFont("BVP", 7.6); canv.setFillColor(MUTED)
        canv.drawString(MARGIN, PAGE_H - 28, "Neuromancer — Bilingual Learning Companion")
        canv.drawRightString(PAGE_W - MARGIN, PAGE_H - 28, "Original study material • Không phải bản dịch")
        canv.line(MARGIN, 36, PAGE_W - MARGIN, 36)
        canv.drawRightString(PAGE_W - MARGIN, 24, f"{doc.page}")
        canv.drawString(MARGIN, 24, "English–Vietnamese • Anh–Việt")
        canv.restoreState()

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph) and hasattr(flowable, "_bookmark"):
            text = flowable._bookmark
            import hashlib
            key = "b" + hashlib.md5(text.encode()).hexdigest()[:12]
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(text, key, level=flowable._level, closed=False)
            self.notify("TOCEntry", (flowable._level, text, self.page, key))


def build_story():
    story = []
    # Cover is drawn by page template; move to normal pages.
    story += [NextPageTemplate("normal"), PageBreak()]
    # Title / scope page
    story += [heading("Scope and source / Phạm vi và nguồn", 1)]
    audit = json.loads((ED / "reports" / "source-audit.json").read_text())
    c = audit["counts"]; s = audit["structure"]
    story += bi(
        f"This PDF is an original English–Vietnamese learning companion. It is not a translation, abridgement or replacement of Neuromancer. The supplied EPUB identifies William Gibson as author and contains {s['chapter_count']} numbered chapters in {len(s['parts']) - 1} parts plus a coda. The audit counts {c['body_words']:,} body words under its stated rule. No print page numbers are claimed.",
        f"PDF này là bản đồng hành học thuật Anh–Việt nguyên bản. Nó không phải bản dịch, bản rút gọn hay thay thế Neuromancer. EPUB được cung cấp xác định tác giả William Gibson và có {s['chapter_count']} chương đánh số trong {len(s['parts']) - 1} phần chính cộng một vĩ thanh. Kiểm tra đếm {c['body_words']:,} từ thân văn bản theo quy tắc đã nêu. Không khẳng định số trang bản in.")
    story += bi(
        "Public availability does not establish a translation licence. The companion therefore uses independent summaries, short chapter labels, original examples and exercises. It avoids long quotations and does not export the source prose.",
        "Khả năng truy cập công khai không xác lập giấy phép dịch. Vì vậy bản đồng hành dùng tóm tắt độc lập, nhãn chương ngắn, ví dụ và bài tập gốc, tránh trích dài và không xuất văn xuôi nguồn.")
    story += [P("EPUB SHA-256: " + audit["source"]["sha256"], "small"), Spacer(1, 8)]
    story += [heading("How to use / Cách sử dụng", 1)]
    for en, vi in fm.INTRO:
        story += bi(en, vi)
    story += [heading("Exam targets / Mục tiêu điểm thi", 2)]
    rows = [[P("Exam / Kỳ thi", "tableh"), P("Target", "tableh"), P("Status", "tableh"), P("Ghi chú", "tableh")]]
    for a,b,c_,d in fm.EXAM_TARGETS:
        rows.append([P(a,"table"),P(b,"table"),P(c_,"table"),P(d,"table")])
    t = Table(rows, colWidths=[135,45,150,CONTENT_W-330], repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),ACCENT),("VALIGN",(0,0),(-1,-1),"TOP"),
                           ("GRID",(0,0),(-1,-1),0.4,LINE),("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
                           ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
                           ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, LIGHT])]))
    story += [t, Spacer(1,8)]
    story += bi("These are planning labels, not certified score conversions. Verify current official score descriptions before registering for a test.",
                "Đây là nhãn lập kế hoạch, không phải quy đổi điểm được chứng nhận. Hãy kiểm tra mô tả điểm chính thức hiện hành trước khi đăng ký thi.")
    # TOC
    story += [PageBreak(), heading("Contents / Mục lục", 1)]
    toc = TableOfContents()
    toc.levelStyles = [S["toc0"], S["toc1"]]
    toc.dotsMinLevel = 0
    story += [toc]
    # Study route
    story += [PageBreak(), heading("12-week route / Lộ trình 12 tuần", 1)]
    rows = [[P("Week","tableh"),P("Focus","tableh"),P("Chapters","tableh"),P("Output","tableh"),P("Đầu ra","tableh")]]
    for w,f,ch_,out,vi in fm.STUDY_ROUTE:
        rows.append([P(w,"table"),P(f,"table"),P(ch_,"table"),P(out,"table"),P(vi,"table")])
    t = Table(rows, colWidths=[34,110,48,160,CONTENT_W-352], repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),ACCENT),("VALIGN",(0,0),(-1,-1),"TOP"),
                           ("GRID",(0,0),(-1,-1),0.4,LINE),("LEFTPADDING",(0,0),(-1,-1),4),("RIGHTPADDING",(0,0),(-1,-1),4),
                           ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
                           ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, LIGHT])]))
    story += [t]
    # Methods
    story += [heading("Study methods / Phương pháp học", 2)]
    for en, vi in fm.METHODS:
        story += bi(en, vi)
    # Characters and themes
    story += [PageBreak(), heading("Character map / Bản đồ nhân vật", 1)]
    for name, role_en, role_vi, note_en, note_vi in fm.CHARACTERS:
        story += [P(name, "h3")] + bi(role_en + " " + note_en, role_vi + " " + note_vi)
    story += [heading("Themes / Chủ đề", 1)]
    for ten, tvi, en, vi in fm.THEMES:
        story += [P(ten + " / " + tvi, "h3")] + bi(en, vi)
    # Chapters
    story += [PageBreak(), heading("Chapter companions / Đồng hành theo chương", 1)]
    story += bi("Each unit is independent. Read the chapter first, then use the overview to check structure, the lens to focus analysis, and the task to produce language.",
                "Mỗi đơn vị độc lập. Đọc chương trước, rồi dùng tổng quan để kiểm tra cấu trúc, góc nhìn để tập trung phân tích và nhiệm vụ để tạo sản phẩm ngôn ngữ.")
    for ch in CHAPTERS:
        story += [PageBreak()]
        title = f"Chapter {ch['n']:02d} — {ch['title']}"
        story += [heading(title, 2), P(f"Chương {ch['n']:02d} — {ch['vi_title']}", "vi"), Spacer(1,6)]
        story += [P("Overview / Tổng quan", "h3")] + bi(ch["summary_en"], ch["summary_vi"])
        story += [box([P("Reading lens / Góc nhìn đọc", "h3")] + bi(ch["lens_en"], ch["lens_vi"], "box", "box")), Spacer(1,6)]
        story += [box([P("Check question / Câu hỏi kiểm tra", "h3")] + bi(ch["q_en"], ch["q_vi"], "q", "q"), bg=colors.HexColor("#FDF2F6"), border=colors.HexColor("#E7C2D2")), Spacer(1,8)]
        # Vocab
        story += [P("Lexical set / Bộ từ vựng", "h3")]
        rows = [[P("Word","tableh"),P("POS","tableh"),P("Meaning","tableh"),P("Nghĩa","tableh"),P("Collocation","tableh")]]
        for w,pos,en,vi,col in ch["vocab"]:
            rows.append([P(w,"table"),P(pos,"table"),P(en,"table"),P(vi,"table"),P(col,"table")])
        t = Table(rows, colWidths=[78,32,150,125,CONTENT_W-385], repeatRows=1)
        t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),ACCENT),("VALIGN",(0,0),(-1,-1),"TOP"),
                               ("GRID",(0,0),(-1,-1),0.4,LINE),("LEFTPADDING",(0,0),(-1,-1),4),("RIGHTPADDING",(0,0),(-1,-1),4),
                               ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
                               ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, LIGHT])]))
        story += [t, Spacer(1,8)]
        story += [box([P("Grammar focus / Trọng tâm ngữ pháp", "h3")] + bi(ch["grammar_en"], ch["grammar_vi"], "box", "box") + bi(ch["example_en"], ch["example_vi"], "box", "box")), Spacer(1,6)]
        task = [P("Production task / Nhiệm vụ tạo sản phẩm", "h3")] + bi(ch["task_en"], ch["task_vi"], "box", "box")
        if ch.get("task_note"):
            task += [P(ch["task_note"], "small")]
        story += [box(task, bg=colors.HexColor("#EEF7F7"), border=colors.HexColor("#BFE0E0"))]
    # Glossary
    story += [PageBreak(), heading("Cyberpunk glossary / Thuật ngữ cyberpunk", 1)]
    rows = [[P("Term","tableh"),P("English explanation","tableh"),P("Giải thích tiếng Việt","tableh")]]
    for term,en,vi in fm.GLOSSARY:
        rows.append([P(term,"table"),P(en,"table"),P(vi,"table")])
    t = Table(rows, colWidths=[110,195,CONTENT_W-305], repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),ACCENT),("VALIGN",(0,0),(-1,-1),"TOP"),
                           ("GRID",(0,0),(-1,-1),0.4,LINE),("LEFTPADDING",(0,0),(-1,-1),4),("RIGHTPADDING",(0,0),(-1,-1),4),
                           ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
                           ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, LIGHT])]))
    story += [t]
    # Practice reading
    story += [PageBreak(), heading("Reading practice / Luyện đọc", 1)]
    story += bi("Original academic passages inspired by the novel’s themes. Answer before checking the key.",
                "Đoạn học thuật gốc lấy cảm hứng từ chủ đề tiểu thuyết. Trả lời trước khi xem đáp án.")
    for r in pr.READING:
        story += [PageBreak(), heading(f"{r['id']} — {r['title']}", 2), P(r["vi_title"], "vi"), Spacer(1,4), P(r["text"], "body")]
        for i,(qen,qvi,opts,ans,een,evi) in enumerate(r["questions"],1):
            story += [P(f"{i}. {qen} / {qvi}", "q")]
            for j,opt in enumerate(opts):
                story += [P(f"{chr(65+j)}. {opt}", "opt")]
        story += [Spacer(1,6)]
    # Listening
    story += [PageBreak(), heading("Listening practice / Luyện nghe", 1)]
    story += bi("These are original scripts. Ask a partner or text-to-speech tool to read them aloud once; do not read the script before answering. Audio is not included in this PDF.",
                "Đây là kịch bản gốc. Nhờ bạn đọc hoặc công cụ chuyển văn bản thành giọng nói đọc một lần; không đọc kịch bản trước khi trả lời. PDF không kèm âm thanh.")
    for l in pr.LISTENING:
        story += [heading(f"{l['id']} — {l['title']}", 2), P(l["vi_title"], "vi")]
        story += [box([P("Script / Kịch bản", "h3"), P(l["script"], "box")]), Spacer(1,6)]
        for i,(qen,qvi,opts,ans) in enumerate(l["questions"],1):
            story += [P(f"{i}. {qen} / {qvi}", "q")]
            for j,opt in enumerate(opts):
                story += [P(f"{chr(65+j)}. {opt}", "opt")]
    # Speaking
    story += [PageBreak(), heading("Speaking cards / Thẻ luyện nói", 1)]
    for i,(en,vi,fe,fvi) in enumerate(pr.SPEAKING,1):
        story += [box([P(f"Card {i}", "h3")] + bi(en,vi,"box","box") + bi("Frame: "+fe,"Khung: "+fvi,"box","box")), Spacer(1,6)]
    # Writing
    story += [PageBreak(), heading("Writing tasks / Nhiệm vụ viết", 1)]
    for w in pr.WRITING:
        story += [heading(w["id"],2)] + bi(w["prompt"], w["vi"])
        story += [P(f"Words: {w['words']} • Time: {w['time']}", "small"), P("Plan: "+w["plan"], "small"), P("Dàn ý: "+w["vi_plan"], "small"), Spacer(1,6)]
    # Integrated
    story += [PageBreak(), heading("Integrated tasks / Nhiệm vụ tích hợp", 1)]
    for it in pr.INTEGRATED:
        story += [heading(it["id"],2)] + bi(it["task"], it["vi"])
        story += [P(f"{it['read']} {it['listen']} • {it['time']}", "small"), Spacer(1,6)]
    # Rubrics
    story += [heading("Self-assessment rubric / Khung tự đánh giá", 2)]
    rows = [[P("Criterion","tableh"),P("Tiêu chí","tableh"),P("Descriptor","tableh"),P("Mô tả","tableh")]]
    for a,b,c_,d in pr.RUBRICS:
        rows.append([P(a,"table"),P(b,"table"),P(c_,"table"),P(d,"table")])
    t = Table(rows, colWidths=[95,85,165,CONTENT_W-345], repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),ACCENT),("VALIGN",(0,0),(-1,-1),"TOP"),
                           ("GRID",(0,0),(-1,-1),0.4,LINE),("LEFTPADDING",(0,0),(-1,-1),4),("RIGHTPADDING",(0,0),(-1,-1),4),
                           ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
                           ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, LIGHT])]))
    story += [t]
    # Appendices
    story += [PageBreak(), heading("Models and review tools / Bài mẫu và công cụ ôn tập", 1)]
    for m in pr.MODEL_ANSWERS:
        story += [heading(m["id"] + " — " + m["label"], 2)] + bi(m["en"], m["vi"])
        story += [P(m["note"] + " / " + m["vi_note"], "small"), Spacer(1,6)]
    story += [heading("Spaced review / Ôn ngắt quãng", 2)]
    rows = [[P("When","tableh"),P("Task","tableh"),P("Nhiệm vụ","tableh")]]
    for a,b,c_ in pr.REVIEW_SCHEDULE:
        rows.append([P(a,"table"),P(b,"table"),P(c_,"table")])
    t = Table(rows, colWidths=[60,220,CONTENT_W-280], repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),ACCENT),("VALIGN",(0,0),(-1,-1),"TOP"),
                           ("GRID",(0,0),(-1,-1),0.4,LINE),("LEFTPADDING",(0,0),(-1,-1),4),("RIGHTPADDING",(0,0),(-1,-1),4),
                           ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
                           ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, LIGHT])]))
    story += [t, Spacer(1,8)]
    story += [heading("Error log template / Mẫu sổ lỗi", 2)]
    rows = [[P(x,"tableh") for x in pr.ERROR_LOG[0]]]
    for row in pr.ERROR_LOG[1:]:
        rows.append([P(x,"table") for x in row])
    t = Table(rows, colWidths=[55,55,80,60,110,CONTENT_W-360], repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),ACCENT),("VALIGN",(0,0),(-1,-1),"TOP"),
                           ("GRID",(0,0),(-1,-1),0.4,LINE),("LEFTPADDING",(0,0),(-1,-1),4),("RIGHTPADDING",(0,0),(-1,-1),4),
                           ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
                           ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, LIGHT])]))
    story += [t]
    # Keys
    story += [PageBreak(), heading("Answer keys / Đáp án", 1)]
    story += [P("Chapter check questions / Câu hỏi kiểm tra chương", "h3")]
    for ch in CHAPTERS:
        story += [P(f"Chapter {ch['n']:02d}", "small")] + bi(ch["a_en"], ch["a_vi"], "small", "small")
    story += [P("Reading and listening / Đọc và nghe", "h3")]
    for r in pr.READING:
        story += [P(r["id"]+" — "+r["title"], "small")]
        for i,(qen,qvi,opts,ans,een,evi) in enumerate(r["questions"],1):
            story += [P(f"{i}. {chr(65+ans)}. {opts[ans]}", "small"), P(een+" / "+evi, "tiny")]
        story += [P("Tóm tắt tiếng Việt: "+r["vi_summary"], "small"), Spacer(1,4)]
    for l in pr.LISTENING:
        story += [P(l["id"]+" — "+l["title"], "small")]
        for i,(qen,qvi,opts,ans) in enumerate(l["questions"],1):
            story += [P(f"{i}. {chr(65+ans)}. {opts[ans]}", "small")]
        story += [P("Tóm tắt tiếng Việt: "+l["vi_summary"], "small"), Spacer(1,4)]
    # Source and rights
    story += [PageBreak(), heading("Source, rights and rebuild / Nguồn, quyền và tái lập", 1)]
    story += bi(
        "The companion was compiled from the repository’s supplied EPUB and original pedagogical writing. The EPUB is an Internet Archive-derived custom file; it does not grant translation rights. Existing archive files were not modified. Fonts are Be Vietnam Pro under the SIL Open Font License.",
        "Bản đồng hành được biên soạn từ EPUB được cung cấp trong kho và phần viết sư phạm gốc. EPUB là tệp tùy chỉnh dẫn xuất từ Internet Archive; nó không cấp quyền dịch. Các tệp lưu trữ hiện có không bị sửa. Phông chữ là Be Vietnam Pro theo Giấy phép Phông chữ Mở SIL.")
    story += [P("Rebuild commands / Lệnh tái lập", "h3"),
              P("python -m venv .venv", "small"),
              P(".venv/bin/pip install -r edition/requirements.txt", "small"),
              P(".venv/bin/python edition/tools/audit_source.py", "small"),
              P(".venv/bin/python edition/tools/build_pdf.py", "small"),
              P(".venv/bin/python edition/tools/validate.py", "small")]
    story += [Spacer(1,8), P("End of companion / Hết bản đồng hành", "small")]
    return story


def main():
    doc = Doc(str(OUT))
    story = build_story()
    doc.multiBuild(story)
    print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
