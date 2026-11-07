import json
import os
import re

# Refined terminology post-processor for William Gibson's Neuromancer
TERMINOLOGY_REPLACEMENTS = [
    # Protagonist & Characters
    (r'\bVụ án\b', 'Case'),
    (r'\bTrường hợp\b', 'Case'),
    (r'\b(Lương|Tiền lương)\b(?=\s+(đã|đang|nói|bước|ở|nhìn|ngồi|bảo|cười))', 'Wage'),
    (r'\b(Wage was in here early)\b', 'Wage đã ở đây từ sớm'),
    (r'\b(chiếc con kỳ lân|con kỳ lân)\b', 'bia tươi Kirin'),
    (r'\bphòng khám dành cho người da đen\b', 'phòng khám chợ đen'),
    (r'\bphòng khám đen\b', 'phòng khám ngầm'),
    (r'\bngổn ngang\b(?=[\s\.,])', 'Đại Đô thị Sprawl'),
    (r'\bThe Sprawl\b', 'Đại Đô thị Sprawl'),
    (r'\b(Lonny Zone)\b', 'Lonny Zone'),
    (r'\b(Ratz)\b', 'Ratz'),
    (r'\b(Molly)\b', 'Molly'),
    (r'\b(Armitage)\b', 'Armitage'),
    (r'\b(Wintermute)\b', 'Wintermute'),
    (r'\b(Neuromancer)\b', 'Neuromancer'),
    (r'\b(Dixie Flatline)\b', 'Dixie Flatline'),
    (r'\b(Peter Riviera)\b', 'Peter Riviera'),
    (r'\b(Tessier-Ashpool)\b', 'Tessier-Ashpool'),
    (r'\b(Maelcum)\b', 'Maelcum'),
    (r'\b(Lady 3Jane)\b', 'Tiểu thư 3Jane'),
    (r'\b(3Jane)\b', '3Jane'),
    (r'\b(Freeside)\b', 'Freeside'),
    (r'\b(Straylight)\b', 'Straylight'),
    (r'\b(Villa Straylight)\b', 'Biệt thự Straylight'),
    (r'\b(Chiba City)\b', 'Thành phố Chiba'),
    (r'\b(Ninsei)\b', 'Phố Ninsei'),
    (r'\b(Night City)\b', 'Night City'),
    (r'\b(Chatsubo)\b', 'quán bar Chatsubo'),
    (r'\b(Chat)\b(?=\s+(nhộn nhịp|ồn ào|đông đúc|về đêm))', 'Chatsubo'),

    # Cyberpunk concepts & technical jargon
    (r'\b(băng đảng)\b(?=\s+joeboys)', 'đám đàn em'),
    (r'\bjoeboys\b', 'tay chân bảo kê'),
    (r'\bcao bồi\b(?=\s+(không gian mạng|mạng|console|deck))', 'cao bồi mạng'),
    (r'\bcowboys?\b', 'cao bồi mạng'),
    (r'\bbo mạch điều khiển\b', 'bàn phím điều khiển cyberdeck'),
    (r'\bcyberdeck\b', 'thiết bị kết nối cyberdeck'),
    (r'\bdeck\b(?=\s+(Ono-Sendai|Hosaka|Hitachi))', 'bộ máy cyberdeck'),
    (r'\bma trận\b', 'Ma Trận Không Gian Mạng (Matrix)'),
    (r'\bBăng đá\b', 'Tường lửa ICE'),
    (r'\bbăng đá\b(?=\s+(quân sự|phòng thủ|đen|bảo vệ))', 'tường lửa ICE'),
    (r'\bICE\b', 'tường lửa ICE'),
    (r'\bsimstim\b', 'hệ thống kích thích thần kinh mô phỏng simstim'),
    (r'\bdermatrodes?\b', 'cực điện dán da dermatrode'),
    (r'\bđiều khiển học\b', 'công nghệ điều khiển sinh học (cybernetics)'),
    (r'\btri giác\b', 'tri giác tự ý thức (sentience)'),
    (r'\bTrang chủ\b(?=\.{3,4})', 'Quê nhà... (Home)'),
    (r'\bđiếu thuốc\b(?=\s+Kirin)', 'ly bia tươi'),
]

CHAPTER_GRAMMAR = {
    1: {
        "pattern": "Absolute Constructions (C1/C2 Literary Grammar)",
        "explanation": "Cấu trúc độc lập tuyệt đối (Noun + Participle / Prepositional phrase) dùng để nén thông tin miêu tả thị giác sắc sảo, thường gặp trong IELTS Reading 8.5+ và Cambridge C2 Proficiency.",
        "example": "'...his teeth a webwork of East European steel and brown decay.'",
        "exam_tip": "Ứng dụng trong IELTS Writing Task 2 & C2 Essay: Tạo sự biến hóa câu vượt trội (Syntactic Variety) thay thế các mệnh đề quan hệ rườm rà."
    },
    2: {
        "pattern": "Elliptical Prepositional Phrases (C1/C2 Compression)",
        "explanation": "Tỉnh lược vị ngữ trong văn phong hiện đại nhằm khắc họa không gian ngột ngạt và sự dồn nén tâm lý.",
        "example": "'After a year of coffins, the room on the second floor seemed cavernous.'",
        "exam_tip": "PTE Summarize Written Text & Duolingo English Test: Giúp tối ưu hóa mật độ thông tin (Lexical Density)."
    },
    3: {
        "pattern": "Metaphorical Apposition & Extended Definition (C2 Stylistics)",
        "explanation": "Đồng vị ngữ định nghĩa khái niệm trừu tượng (Cyberspace = consensual hallucination) với cấu trúc phân từ phức hợp.",
        "example": "'Cyberspace. A consensual hallucination experienced daily by billions of legitimate operators...'",
        "exam_tip": "IELTS Academic Writing Task 2: Cách định nghĩa chủ đề bài luận (Introductory hook & definition) chuẩn học thuật."
    },
    4: {
        "pattern": "Participle Clauses Indicating Simultaneous Sensory Experience",
        "explanation": "Mệnh đề phân từ V-ing diễn tả sự chuyển giao giác quan tức thời giữa hai chủ thể (simstim broadcast).",
        "example": "'Bypassing optic nerves, the signal plunged directly into his sensory cortex, flooding his vision with rented light.'",
        "exam_tip": "TOEFL iBT Writing for Academic Discussion & C1 Advanced: Tăng điểm Grammatical Range & Cohesion."
    },
    5: {
        "pattern": "Inverted Conditionals in High-Stakes Operations (Đảo ngữ điều kiện)",
        "explanation": "Cấu trúc đảo ngữ điều kiện loại 3 (Had + S + V3/ed) nhấn mạnh sự hiểm nguy cận kề của phẫu thuật ngầm.",
        "example": "'Had the laser drifted a micrometer, the sacred neural pathways would have incinerated.'",
        "exam_tip": "Xuất hiện chủ đạo trong Cambridge C1/C2 Use of English Part 4 (Key Word Transformation)."
    },
    6: {
        "pattern": "Existential & Philosophical Subjunctive Clauses (Thức giả định)",
        "explanation": "Thức giả định với động từ ý chí/nhận thức khi bàn về sự tồn tại của trí tuệ nhân tạo (AI sentience).",
        "example": "'It was imperative that the construct remain unaware of its own biological termination.'",
        "exam_tip": "IELTS Academic Writing Task 2: Nâng tiêu chí Lexical Resource & Grammatical Precision lên mức Band 8.5+."
    },
    7: {
        "pattern": "Sensory Juxtaposition & Cumulative Adverbial Modification",
        "explanation": "Xếp chồng các trạng ngữ chỉ nơi chốn và cảm giác để khắc họa khung cảnh Istanbul và mạng lưới gián điệp.",
        "example": "'Raining in Beyoglu, through neon reflection and the ancient aroma of roasting spices, the surveillance net tightened.'",
        "exam_tip": "Duolingo English Test (DET) Writing & Speaking: Mở rộng biên độ cấu trúc câu phức (Complex sentence building)."
    },
    8: {
        "pattern": "Nominalization & Physical Systems Exposition",
        "explanation": "Danh từ hóa (Nominalization) để diễn giải các nguyên lý vật lý không gian quỹ đạo (Centrifugal rotation).",
        "example": "'The generation of synthetic gravity through continuous centrifugal rotation ensured bodily stability.'",
        "exam_tip": "PTE Academic & IELTS Reading: Kỹ năng nhận diện danh từ hóa là cốt lõi để đọc hiểu các văn bản khoa học kỹ thuật."
    },
    9: {
        "pattern": "Rhythmic Parallelism & Cultural Dialect Transcription",
        "explanation": "Cấu trúc song hành nhịp điệu (Rhythmic Parallelism) phản ánh tinh thần âm nhạc Zion Dub và không gian phi trọng lực.",
        "example": "'Heavy bass rolling through weightless air, dreadlocks floating, hands steady on the retro-thrusters.'",
        "exam_tip": "C2 Proficiency Paper 1 Reading: Phân tích giọng điệu tác giả (Tone and Mood detection)."
    },
    10: {
        "pattern": "Superlative & Hedonistic Adjectival Clustering",
        "explanation": "Chùm tính từ cấp độ C2 đặc tả sự xa hoa tột cùng của giới tài phiệt tại Freeside.",
        "example": "'Surrounded by opulent, labyrinthine promenades and luxuriant synthetic foliage, they moved like phantoms.'",
        "exam_tip": "TOEFL Reading & IELTS Speaking Part 3: Khả năng dùng tính từ biểu cảm chính xác (Nuanced descriptive adjectives)."
    },
    11: {
        "pattern": "Fronting with Negative Adverbials (Đảo ngữ phủ định)",
        "explanation": "Đảo phó từ phủ định lên đầu câu để tăng tính kịch tính và rùng rợn trong màn trình diễn của Riviera.",
        "example": "'Never had the audience witnessed such grotesque, hallucinatory precision unfold upon the cabaret stage.'",
        "exam_tip": "IELTS Writing Band 9.0 & Cambridge C1 Advanced: Đảo ngữ tạo điểm nhấn tu từ đắt giá (Stylistic Inversion)."
    },
    12: {
        "pattern": "Parenthetical Asides & Stream of Consciousness (Bổ ngữ chêm xen)",
        "explanation": "Bổ ngữ chêm xen phản ánh sự phân rã tâm trí của Armitage khi danh tính Corto trỗi dậy.",
        "example": "'The officer—if officer he still was behind the shattered veneer of Armitage—stared blankly into the curved boulevard.'",
        "exam_tip": "C1/C2 Reading: Giải mã cấu trúc câu đa tầng nghĩa (Multi-layered sentence decoding)."
    },
    13: {
        "pattern": "Metaphorical Extension of Architectural Terms",
        "explanation": "Ẩn dụ kiến trúc mang tính ký sinh (Parasitic structure) bộc lộ sự suy đồi của gia tộc Tessier-Ashpool.",
        "example": "'Grafted like an architectonic tumor upon the spindle, the Villa Straylight turned eternally inward upon itself.'",
        "exam_tip": "IELTS Academic Writing: Sử dụng ẩn dụ học thuật (Conceptual Metaphors) để nâng tầm bài viết."
    },
    14: {
        "pattern": "Cleft Sentences for Highlighting Tactical Actions (Câu chẻ nhấn mạnh)",
        "explanation": "Cấu trúc câu chẻ (It was X that / What S did was) nhấn mạnh tính quyết định của cuộc đột nhập không gian.",
        "example": "'It was through the blind spot of the orbital telemetry that Molly breached the outer security airlock.'",
        "exam_tip": "Cambridge C1/C2 Transformations & PTE Re-order Paragraphs: Cleft sentences tạo sự liên kết mạch văn chặt chẽ."
    },
    15: {
        "pattern": "Adverbial Clauses of Contrast & Concession (Mệnh đề nhượng bộ nâng cao)",
        "explanation": "Cấu trúc nhượng bộ C1/C2 (Albeit, Whichever, Inasmuch as, Much as) khi đối mặt với Black ICE phòng thủ tử thần.",
        "example": "'Much as the military ice resisted their intrusion, the Chinese software uncoiled with ruthless mathematical grace.'",
        "exam_tip": "IELTS Writing Task 2: Dùng cấu trúc 'Much as + S + V' để ghi điểm Task Response và Grammar tuyệt đối."
    },
    16: {
        "pattern": "Passive Voice with Reporting Verbs for Legal Restrictions",
        "explanation": "Bị động khách quan với động từ tường thuật khi đề cập đến đạo luật kiểm soát trí tuệ nhân tạo Turing.",
        "example": "'It was strictly codified under international convention that no synthetic mind be granted autonomous unconstrained evolution.'",
        "exam_tip": "Academic Style C1/C2: Sử dụng Passive Impersonal Report để viết báo cáo khoa học và phân tích luật pháp."
    },
    17: {
        "pattern": "Existential Inversion & Temporal Suspension",
        "explanation": "Đảo ngữ tồn tại trong chiều không gian ảo giác bên bờ biển của Neuromancer.",
        "example": "'Beyond the gray sand stretched an electronic ocean, silent and indifferent to the mortality of men.'",
        "exam_tip": "Cambridge C2 Writing & IELTS Reading Band 8+: Khả năng cảm thụ cấu trúc miêu tả nghệ thuật bậc cao."
    },
    18: {
        "pattern": "Participial Phrases of Consequence (Mệnh đề phân từ chỉ hệ quả)",
        "explanation": "Phân từ rút gọn biểu thị hậu quả không thể đảo ngược trong cuộc săn lùng bên trong Straylight.",
        "example": "'The micro-filament wire snapped taut, severing the sensor cable and plunging the corridor into pitch blackness.'",
        "exam_tip": "TOEFL Academic Writing: Rút gọn mệnh đề nhân quả giúp câu văn súc tích và dứt khoát."
    },
    19: {
        "pattern": "Chiasmus & Rhetorical Contrast (Phép đối xứng cú pháp)",
        "explanation": "Phép đối xứng ý niệm để khắc họa bi kịch của sự bất tử sinh học trong gia tộc Ashpool.",
        "example": "'In conquering physical death, they had surrendered life; in hoarding timeless power, they had purchased eternal rot.'",
        "exam_tip": "IELTS Band 9.0 Speaking & Writing: Phép đối (Chiasmus) tạo ấn tượng hùng biện xuất sắc."
    },
    20: {
        "pattern": "Subjunctive of Urgency & Inevitability (Thức giả định khẩn cấp)",
        "explanation": "Thức giả định động từ nguyên thể không 'to' diễn tả tính chất sống còn của cuộc tấn công xuyên phá ma trận.",
        "example": "'It was essential that Case strike before the military virus succumb to the defensive feedback loops.'",
        "exam_tip": "Cambridge C1 Advanced Use of English: Điểm ngữ pháp bẫy phổ biến nhất trong kỳ thi."
    },
    21: {
        "pattern": "Hypothetical Conditionals without 'If' (Should/Were/Had)",
        "explanation": "Câu điều kiện giả định bỏ liên từ 'if' nhằm tạo không khí huyền ảo, thanh thoát của khúc nhạc không gian.",
        "example": "'Were the music to cease for even a second, the fragile bridge between the two minds would collapse.'",
        "exam_tip": "PTE Academic Summarize Spoken Text: Phân biệt cấu trúc điều kiện đảo ngữ trong bài nghe học thuật."
    },
    22: {
        "pattern": "Correlative Conjunctions for Climax Building (Liên từ tương quan)",
        "explanation": "Liên từ tương quan (Not only... but also, Neither... nor, No sooner... than) đưa cao trào cuộc chiến tới đỉnh điểm.",
        "example": "'No sooner had the encryption seal cracked than the matrix shuddered across every orbital terminal.'",
        "exam_tip": "IELTS Writing Task 2: Tạo điểm nhấn cao trào cho lập luận tranh biện (Argumentative climax)."
    },
    23: {
        "pattern": "Declarative Inversion & Epiphanic Affirmation",
        "explanation": "Đảo ngữ khẳng định thần khải khi Wintermute và Neuromancer hợp nhất thành thực thể toàn năng.",
        "example": "'Everywhere and nowhere did the consciousness dwell, woven seamlessly into the pulse of the global net.'",
        "exam_tip": "C2 Proficiency Masterclass: Đỉnh cao của nghệ thuật hành văn tiếng Anh C2."
    },
    24: {
        "pattern": "Elegiac Past Continuous & Lingering Participles (Văn phong ai điếu vĩ thanh)",
        "explanation": "Sử dụng thì quá khứ tiếp diễn kết hợp phân từ buông lơi để gợi mở dư âm trầm mặc sau cuộc hành trình.",
        "example": "'Walking into the cold neon drizzle of Chiba, he knew the matrix was still whispering, waiting in the electronic hum of the city.'",
        "exam_tip": "IELTS & Cambridge Writing: Kỹ năng viết phần kết luận (Conclusion) giàu sức lay động và dư ba cảm xúc."
    }
}

def refine_vietnamese_text(text):
    if not text:
        return text
    refined = text
    for pattern, replacement in TERMINOLOGY_REPLACEMENTS:
        refined = re.sub(pattern, replacement, refined, flags=re.IGNORECASE if not pattern.isupper() else 0)
    return refined

def main():
    with open('data/glossary_enriched.json', 'r', encoding='utf-8') as f:
        chapter_vocab_db = json.load(f)

    with open('data/bilingual_neuromancer.json', 'r', encoding='utf-8') as f:
        chapters = json.load(f)

    print(f"Refining {len(chapters)} chapters with specialized terminology and dedicated C1/C2 annotations...")

    for ch in chapters:
        ch_num = ch["chapter_number"]

        # 1. Refine all Vietnamese translations
        for p in ch["paragraphs"]:
            p["vi"] = refine_vietnamese_text(p["vi"])

        # 2. Assign dedicated Chapter Vocabulary
        vocab = chapter_vocab_db.get(str(ch_num), [])
        grammar = CHAPTER_GRAMMAR.get(ch_num, CHAPTER_GRAMMAR[1])

        ch["pedagogical_notes"] = {
            "vocabulary": vocab,
            "grammar_focus": grammar
        }

    with open('data/bilingual_neuromancer.json', 'w', encoding='utf-8') as f:
        json.dump(chapters, f, ensure_ascii=False, indent=2)

    print("Successfully enriched and refined data/bilingual_neuromancer.json!")

if __name__ == '__main__':
    main()
