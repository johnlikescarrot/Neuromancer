"""
pedagogy.py - Core pedagogical framework and vocabulary database for
Neuromancer Bilingual Edition.

Target Benchmarks:
- IELTS: 7.0+ (Band 7-8 lexical resource, collocations, idiomatic phrasing)
- TOEFL iBT: 90+ (Academic & advanced prose comprehension, nuanced semantics)
- PTE Academic: 65+ (Advanced vocabulary in context, discourse markers)
- Cambridge English: 185+ (C1 Advanced / C2 Proficiency lexical mastery)
- Duolingo English Test (DET): 120+ (Advanced literary vocabulary and morphology)
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class VocabularyItem:
    word: str
    part_of_speech: str
    phonetic: str
    vietnamese_def: str
    english_def: str
    context_sentence: str
    cefr_level: str  # B2, C1, C2
    target_tests: List[str]  # ['IELTS 7.5', 'TOEFL 100', 'C1 Advanced', 'DET 125']
    synonyms: List[str]
    collocations: List[str]
    cyberpunk_note: Optional[str] = None

@dataclass
class ParagraphPair:
    id: int
    english: str
    vietnamese: str
    vocab_keys: List[str] = field(default_factory=list)
    stylistic_note: Optional[str] = None

# Comprehensive curated vocabulary bank for Chapter 1
CHAPTER_1_VOCAB: Dict[str, VocabularyItem] = {
    "prosthetic": VocabularyItem(
        word="prosthetic",
        part_of_speech="adj.",
        phonetic="/prɒsˈθet.ɪk/",
        vietnamese_def="thuộc bộ phận giả, lắp ghép cơ học",
        english_def="denoting an artificial body part, prosthesis",
        context_sentence="Ratz was tending bar, his prosthetic arm jerking monotonously...",
        cefr_level="C1",
        target_tests=["IELTS 7.0+", "TOEFL 90+", "C1 Advanced"],
        synonyms=["artificial", "bionic", "replacement"],
        collocations=["prosthetic limb", "prosthetic device"],
        cyberpunk_note="Cyberware motif: human bodily modification and dehumanization."
    ),
    "monotonously": VocabularyItem(
        word="monotonously",
        part_of_speech="adv.",
        phonetic="/məˈnɒt.ən.əs.li/",
        vietnamese_def="một cách đều đều tẻ nhạt, đơn điệu",
        english_def="in a dull, repetitive, and unvarying manner",
        context_sentence="...his prosthetic arm jerking monotonously as he filled a tray of glasses...",
        cefr_level="C1",
        target_tests=["IELTS 7.5", "TOEFL 95", "C1 Advanced"],
        synonyms=["repetitively", "tediously", "invariably", "unvaryingly"],
        collocations=["droning monotonously", "repeated monotonously"]
    ),
    "obsolete": VocabularyItem(
        word="obsolete",
        part_of_speech="adj.",
        phonetic="/ˌɒb.səˈliːt/",
        vietnamese_def="lỗi thời, cổ lỗ sĩ, không còn được sử dụng",
        english_def="no longer produced or used; out of date",
        context_sentence="It was a Russian military prosthetic, a seven-function force-feedback manipulator, cased in grubby pink plastic... obsolete, crude.",
        cefr_level="C1",
        target_tests=["IELTS 7.0+", "TOEFL 90+", "PTE 65+", "C1 Advanced"],
        synonyms=["outdated", "archaic", "antiquated", "superseded"],
        collocations=["rapidly obsolete", "render obsolete", "obsolete technology"]
    ),
    "disdain": VocabularyItem(
        word="disdain",
        part_of_speech="n., v.",
        phonetic="/dɪsˈdeɪn/",
        vietnamese_def="sự khinh thị, coi thường; khinh bỉ",
        english_def="the feeling that someone or something is unworthy of one's consideration or respect",
        context_sentence="...looked on his profession with a mild amusement tinged with disdain.",
        cefr_level="C2",
        target_tests=["IELTS 8.0", "TOEFL 105", "C2 Proficiency"],
        synonyms=["contempt", "scorn", "derision", "disrespect"],
        collocations=["treat with disdain", "tinged with disdain", "look of disdain"]
    ),
    "myopic": VocabularyItem(
        word="myopic",
        part_of_speech="adj.",
        phonetic="/maɪˈɒp.ɪk/",
        vietnamese_def="cận thị; (nghĩa bóng) thiển cận, tầm nhìn hạn hẹp",
        english_def="nearsighted; lacking imagination, foresight, or intellectual insight",
        context_sentence="He squinted through myopic eyes behind thick lenses.",
        cefr_level="C2",
        target_tests=["IELTS 8.0", "TOEFL 100+", "GRE/GMAT", "C2 Proficiency"],
        synonyms=["short-sighted", "narrow-minded", "purblind", "insular"],
        collocations=["myopic vision", "myopic view of the future"]
    ),
    "translucent": VocabularyItem(
        word="translucent",
        part_of_speech="adj.",
        phonetic="/trænzˈluː.sənt/",
        vietnamese_def="bán trong suốt, để ánh sáng xuyên mờ mờ qua",
        english_def="allowing light, but not detailed shapes, to pass through; semitransparent",
        context_sentence="...the neon glow bleeding through translucent plastic domes.",
        cefr_level="C1",
        target_tests=["IELTS 7.5", "TOEFL 95", "C1 Advanced"],
        synonyms=["semitransparent", "pellucid", "frosted"],
        collocations=["translucent skin", "translucent surface", "translucent jade"]
    ),
    "symbiosis": VocabularyItem(
        word="symbiosis",
        part_of_speech="n.",
        phonetic="/ˌsɪm.baɪˈoʊ.sɪs/",
        vietnamese_def="sự cộng sinh, mối quan hệ tương hỗ đôi bên cùng phụ thuộc",
        english_def="interaction between two different organisms or entities living in close physical association",
        context_sentence="A bizarre symbiosis existed between the black clinics and the street flesh-peddlers.",
        cefr_level="C1",
        target_tests=["IELTS 7.5+", "TOEFL 100+", "PTE 70+", "C1 Advanced"],
        synonyms=["mutualism", "interdependence", "coexistence"],
        collocations=["close symbiosis", "living in symbiosis", "parasitic symbiosis"]
    ),
    "labyrinthine": VocabularyItem(
        word="labyrinthine",
        part_of_speech="adj.",
        phonetic="/ˌlæb.əˈrɪn.θaɪn/",
        vietnamese_def="chằng chịt như mê cung, phức tạp rối rắm",
        english_def="irregular and twisting; intricate and confusing",
        context_sentence="The labyrinthine alleys of Night City smelled of fried grease and stale ozone.",
        cefr_level="C2",
        target_tests=["IELTS 8.0", "TOEFL 105", "C2 Proficiency", "DET 130"],
        synonyms=["convoluted", "tortuous", "intricate", "maze-like", "meandering"],
        collocations=["labyrinthine corridors", "labyrinthine system", "labyrinthine alleys"]
    ),
    "arcane": VocabularyItem(
        word="arcane",
        part_of_speech="adj.",
        phonetic="/ɑːˈkeɪn/",
        vietnamese_def="bí truyền, huyền bí, đòi hỏi kiến thức chuyên sâu đặc thù",
        english_def="understood by few; mysterious or secret",
        context_sentence="The arcane codes of the military ICE programs danced across his memories.",
        cefr_level="C2",
        target_tests=["IELTS 8.5", "TOEFL 110", "C2 Proficiency"],
        synonyms=["esoteric", "cryptic", "enigmatic", "recondite"],
        collocations=["arcane knowledge", "arcane procedures", "arcane jargon"]
    ),
    "permeate": VocabularyItem(
        word="permeate",
        part_of_speech="v.",
        phonetic="/ˈpɜː.mi.eɪt/",
        vietnamese_def="thấm qua, lan tỏa khắp, bao trùm",
        english_def="spread throughout something; pervade",
        context_sentence="The smell of burnt circuits and frying food permeated the narrow stairwell.",
        cefr_level="C1",
        target_tests=["IELTS 7.5", "TOEFL 95", "C1 Advanced"],
        synonyms=["pervade", "saturate", "suffuse", "infiltrate"],
        collocations=["permeate through", "permeate the atmosphere", "completely permeate"]
    ),
    "neurotoxin": VocabularyItem(
        word="neurotoxin",
        part_of_speech="n.",
        phonetic="/ˈnjʊə.rəʊˌtɒk.sɪn/",
        vietnamese_def="độc tố thần kinh",
        english_def="a poison that acts on the nervous system",
        context_sentence="They had damaged his nervous system with a wartime fungus, a Russian mycotoxin.",
        cefr_level="C1",
        target_tests=["TOEFL 95+", "IELTS 7.5+", "SAT/ACT"],
        synonyms=["nerve agent", "neural poison"],
        collocations=["potent neurotoxin", "exposed to neurotoxins"]
    ),
    "clandestine": VocabularyItem(
        word="clandestine",
        part_of_speech="adj.",
        phonetic="/klænˈdes.tɪn/",
        vietnamese_def="lén lút, bí mật, phi pháp",
        english_def="kept secret or done secretively, especially because illicit",
        context_sentence="The clandestine clinics in Chiba were known for illicit neural augmentation.",
        cefr_level="C2",
        target_tests=["IELTS 8.0", "TOEFL 105", "C2 Proficiency", "PTE 75"],
        synonyms=["covert", "surreptitious", "undercover", "illicit", "furtive"],
        collocations=["clandestine operation", "clandestine meeting", "clandestine deal"]
    )
}

EXAM_TIPS = {
    "IELTS_READING": (
        "Tip for IELTS Academic Reading: William Gibson's dense descriptive prose frequently employs compound adjectives "
        "and non-standard register metaphors (e.g. 'the sky was the color of television, tuned to a dead channel'). "
        "In IELTS Reading, identify the nominal core of sentences and ignore parenthetical post-modifiers during your first skimming pass."
    ),
    "TOEFL_SYNTAX": (
        "TOEFL iBT Sentence Simplification & Inferences: Look out for participial phrases and absolute constructions "
        "('his prosthetic arm jerking monotonously as he filled...'). Practice rephrasing these into explicit causal or temporal clauses "
        "to rapidly eliminate distractors in multiple-choice questions."
    ),
    "C1_C2_COLLOCATIONS": (
        "Cambridge C1/C2 Lexical Focus: Pay special attention to sensory and evaluative collocations such as 'tinged with disdain', "
        "'cheap perfume and scorched circuitry', and 'labyrinthine alleys'. C1 Advanced (CAE) and C2 Proficiency (CPE) reward natural prepositional collocations."
    )
}
