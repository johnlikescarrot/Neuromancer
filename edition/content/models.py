"""
Data models for the Neuromancer Bilingual Academic Learning Companion.
Designed to target C1/C2 proficiency (IELTS 7.0+, TOEFL 90+ / 5+, PTE 65+, Cambridge 185+, DET 120+).
"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class VocabularyItem:
    term: str
    ipa: str
    part_of_speech: str
    definition_en: str
    definition_vi: str
    context_sentence: str
    collocations: List[str]
    cefr_level: str = "C1"  # C1 or C2

@dataclass
class CyberpunkTerm:
    term: str
    category: str  # Tech, Subculture, AI, Corporate, Philosophy
    explanation_en: str
    explanation_vi: str
    cultural_impact: str

@dataclass
class GrammarFocus:
    point: str
    structure: str
    explanation_en: str
    explanation_vi: str
    exemplar_sentence: str
    exam_utility: str  # How it boosts IELTS/TOEFL/Cambridge writing/speaking

@dataclass
class PracticeQuestion:
    question_type: str  # "Reading Comprehension", "Lexical Precision", "Sentence Transformation", "Error Identification"
    prompt_en: str
    options: List[str]  # 4 choices
    correct_option: int  # 0-indexed
    explanation_en: str
    explanation_vi: str

@dataclass
class ChapterContent:
    number: int
    part_title_en: str
    part_title_vi: str
    chapter_title_en: str
    chapter_title_vi: str
    word_count: int
    summary_en: str
    summary_vi: str
    literary_analysis_en: str
    literary_analysis_vi: str
    cyberpunk_lore: List[CyberpunkTerm]
    vocabulary: List[VocabularyItem]
    grammar_focus: GrammarFocus
    practice_questions: List[PracticeQuestion]

@dataclass
class CurricularOverview:
    title: str
    subtitle: str
    cefr_framework: Dict[str, str]
    exam_benchmarks: Dict[str, str]
    chapters: List[ChapterContent] = field(default_factory=list)
