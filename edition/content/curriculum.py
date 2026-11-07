# -*- coding: utf-8 -*-
"""
Main Curriculum Registry for Neuromancer Bilingual Academic Learning Companion.
Covers all 24 chapters and Coda.
Benchmarks:
- TOEFL iBT: 90+ (Pre-Jan 2026) / 5+ (Post-Jan 21, 2026 Scale)
- IELTS Academic: 7.0+
- PTE Academic: 65+
- Cambridge English Qualifications: 185+ (C1 Advanced / C2 Proficiency)
- Duolingo English Test (DET): 120+
"""
import sys
import os

# Ensure repo root is in python path
current_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

from edition.content.models import CurricularOverview, ChapterContent
from edition.content.part1_data import PART1_CHAPTERS
from edition.content.part2_data import PART2_CHAPTERS
from edition.content.part3_data import PART3_CHAPTERS
from edition.content.part4_complete import ALL_PART4_AND_CODA

ALL_CHAPTERS = PART1_CHAPTERS + PART2_CHAPTERS + PART3_CHAPTERS + ALL_PART4_AND_CODA

CURRICULUM = CurricularOverview(
    title="Neuromancer: Bilingual Academic Learning Companion",
    subtitle="An English–Vietnamese Critical & Pedagogical Edition for Advanced Fluency (CEFR C1/C2)",
    cefr_framework={
        "Level": "CEFR C1 (Effective Operational Proficiency) to C2 (Mastery)",
        "Description": "Designed for advanced learners developing sophisticated literary analysis, complex grammatical precision, nuance in rhetorical discourse, and academic English argumentation."
    },
    exam_benchmarks={
        "TOEFL iBT": "90+ (Pre-Jan 21, 2026) / 5+ (Post-Jan 21, 2026 1-6 Scale)",
        "IELTS Academic": "7.0+ (with specific Band 8.0+ Lexical & Grammatical targets)",
        "PTE Academic": "65+ (Proficient English benchmark)",
        "Cambridge English": "185+ (C1 Advanced / C2 Proficiency Scale)",
        "Duolingo English Test (DET)": "120+ (Advanced / Comprehensive)"
    },
    chapters=ALL_CHAPTERS
)

if __name__ == "__main__":
    print(f"Curriculum loaded successfully!")
    print(f"Total chapters: {len(CURRICULUM.chapters)}")
    for ch in CURRICULUM.chapters:
        print(f"Chapter {ch.number:02d}: {ch.chapter_title_en} ({len(ch.vocabulary)} vocab, {len(ch.practice_questions)} practice questions)")
