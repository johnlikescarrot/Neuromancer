import json

academic_notes = {
    "1": [
        {
            "term": "monochrome",
            "pos": "adj. / noun",
            "level": "C1 / IELTS 7.5+ / TOEFL 95+",
            "meaning_en": "Consisting of or displaying images in only one color or shades of one color (e.g. grayscale).",
            "meaning_vi": "Đơn sắc, chỉ có sắc độ đen trắng hoặc một màu duy nhất.",
            "context": "'The sky above the port was the color of television, tuned to a dead channel.' -> Sets the iconic monochrome, static-infused atmosphere of Chiba.",
            "collocations": "monochrome display, monochrome palette, stark monochrome",
            "exam_relevance": "Academic writing Task 2 (describing visual arts, urban landscapes, technological design)."
        },
        {
            "term": "subliminal",
            "pos": "adj.",
            "level": "C1 / IELTS 7.5+ / TOEFL 100+",
            "meaning_en": "Below the threshold of conscious perception; subconscious.",
            "meaning_vi": "Tiềm thức, dưới ngưỡng nhận thức tỉnh táo.",
            "context": "'...a subliminal hum that belonged to the city rather than the bar.'",
            "collocations": "subliminal message, subliminal stimulus, subliminal perception",
            "exam_relevance": "Psychology, marketing, cognitive science reading passages in TOEFL/IELTS."
        },
        {
            "term": "mycotoxin",
            "pos": "noun",
            "level": "C2 / Academic Specialized",
            "meaning_en": "Any toxic substance produced by a fungus.",
            "meaning_vi": "Độc tố nấm mốc (độc tố sinh học làm tổn thương thần kinh).",
            "context": "Case's nervous system was selectively damaged by a Russian wartime mycotoxin as punishment for theft.",
            "collocations": "mycotoxin contamination, lethal mycotoxin, nerve-damaging mycotoxin",
            "exam_relevance": "Scientific biology/toxicology reading comprehension in PTE/TOEFL."
        },
        {
            "term": "desuetude",
            "pos": "noun",
            "level": "C2 / GRE / Cambridge Proficiency",
            "meaning_en": "A state of disuse or inactivity.",
            "meaning_vi": "Tình trạng ngưng sử dụng, lỗi thời, suy tàn do bị bỏ quên.",
            "context": "Used to convey the decay of old technological hardware and forgotten industrial relics in Night City.",
            "collocations": "fall into desuetude, state of desuetude",
            "exam_relevance": "Cambridge C2 Proficiency reading & GRE verbal reasoning."
        },
        {
            "term": "amphetamine",
            "pos": "noun",
            "level": "C1 / Health & Society",
            "meaning_en": "A synthetic, addictive, mood-altering drug, used legally as a stimulant and illegally as a stimulant.",
            "meaning_vi": "Chất kích thích thần kinh tổng hợp.",
            "context": "Case constantly relies on dexedrine and amphetamines to sustain his edgy, nervous equilibrium.",
            "collocations": "amphetamine abuse, synthetic amphetamine",
            "exam_relevance": "Public health and pharmacological discourse."
        }
    ],
    "2": [
        {
            "term": "panoply",
            "pos": "noun",
            "level": "C2 / IELTS 8.0+ / TOEFL 105+",
            "meaning_en": "A complete or impressive collection of things; a splendid display.",
            "meaning_vi": "Bộ sưu tập lộng lẫy, đầy đủ và đa dạng mọi chủng loại trang thiết bị.",
            "context": "The underground surgical clinics of Chiba displaying a panoply of black-market cyberware.",
            "collocations": "a full panoply of, vast panoply, dazzling panoply",
            "exam_relevance": "Sophisticated descriptive essays, lexical resource band 8-9."
        },
        {
            "term": "mercenary",
            "pos": "noun / adj.",
            "level": "C1 / IELTS 7.0+ / PTE 65+",
            "meaning_en": "Primarily concerned with making money at the expense of ethics; a professional soldier hired to serve in a foreign army.",
            "meaning_vi": "Kẻ đánh thuê, làm thuê vụ lợi (như Molly Millions hay street samurai).",
            "context": "Molly Millions operates as an independent razorgirl / mercenary operative.",
            "collocations": "mercenary motive, hired mercenary, mercenary soldiers",
            "exam_relevance": "Socio-political analysis essays and IELTS Speaking Part 3."
        },
        {
            "term": "visceral",
            "pos": "adj.",
            "level": "C1 / IELTS 7.5+ / TOEFL 100+",
            "meaning_en": "Relating to deep inward feelings rather than intellect; instinctive and bodily.",
            "meaning_vi": "Thuộc về trực giác sâu sắc từ gan ruột, bản năng thể chất mạnh mẽ.",
            "context": "Case's visceral dread and craving when encountering the prospect of re-entering cyberspace.",
            "collocations": "visceral reaction, visceral fear, visceral hatred",
            "exam_relevance": "Literary analysis and psychology modules across all proficiency tests."
        }
    ],
    "3": [
        {
            "term": "prosthesis",
            "pos": "noun",
            "level": "C1 / PTE 68+ / IELTS 7.5+",
            "meaning_en": "An artificial body part, such as a limb, a heart, or an eye.",
            "meaning_vi": "Bộ phận nhân tạo lắp ghép vào cơ thể (bộ phận giả y sinh).",
            "context": "Surgical implants, cybernetic lenses, and micro-mirrored optical prostheses.",
            "collocations": "bionic prosthesis, neural prosthesis, optical prosthesis",
            "exam_relevance": "Biotechnology and biomedical engineering academic listening/reading."
        },
        {
            "term": "dichotomy",
            "pos": "noun",
            "level": "C1 / IELTS 8.0+ / TOEFL 105+",
            "meaning_en": "A division or contrast between two things that are represented as being opposed or entirely different.",
            "meaning_vi": "Sự phân đôi, thế đối lập nhị nguyên (thể xác 'meat' đối lập với ý thức số 'mind').",
            "context": "The central philosophical tension in Neuromancer: flesh (the meat) versus pure digital consciousness.",
            "collocations": "sharp dichotomy, false dichotomy, fundamental dichotomy",
            "exam_relevance": "Academic writing Task 2 discursive essays exploring dual concepts."
        }
    ],
    "4": [
        {
            "term": "clandestine",
            "pos": "adj.",
            "level": "C2 / IELTS 8.0+ / TOEFL 100+",
            "meaning_en": "Kept secret or done secretively, especially because illicit.",
            "meaning_vi": "Lén lút, bí mật, phi pháp (hoạt động ngầm).",
            "context": "The clandestine operations orchestrated by Armitage using shell corporations.",
            "collocations": "clandestine operation, clandestine meeting, clandestine network",
            "exam_relevance": "International relations and security studies comprehension."
        },
        {
            "term": "ephemeral",
            "pos": "adj.",
            "level": "C1 / IELTS 7.5+ / Cambridge C1-C2",
            "meaning_en": "Lasting for a very short time; transitory.",
            "meaning_vi": "Phù du, chóng tàn, ngắn ngủi.",
            "context": "The neon reflections in the rain puddles of the Sprawl are fleeting and ephemeral.",
            "collocations": "ephemeral nature, ephemeral pleasure, ephemeral glory",
            "exam_relevance": "Philosophical discussions, environmental studies, and IELTS band 8+."
        }
    ],
    "5": [
        {
            "term": "coalesce",
            "pos": "verb",
            "level": "C1 / IELTS 7.5+ / PTE 70+",
            "meaning_en": "Come together to form one mass or whole.",
            "meaning_vi": "Hợp nhất, kết tụ, hòa làm một khối.",
            "context": "Data points coalescing into complex geometric structures in the consensual hallucination of cyberspace.",
            "collocations": "coalesce into, coalesce around, gradual coalescence",
            "exam_relevance": "Data interpretation, macro-trends in Academic Writing Task 1 & 2."
        },
        {
            "term": "solipsism",
            "pos": "noun",
            "level": "C2 / Philosophy & Literary Studies",
            "meaning_en": "The theory that only the self exists, or that can be known to exist.",
            "meaning_vi": "Thuyết duy ngã (cho rằng chỉ có tâm thức của chính mình là tồn tại thực sự).",
            "context": "The extreme sensory isolation when drifting inside the cyberdeck interface.",
            "collocations": "radical solipsism, philosophical solipsism",
            "exam_relevance": "Humanities, philosophy, advanced comprehension."
        }
    ]
}

# Add systematic vocabulary for chapters 6 to 24 to cover the entire curriculum
common_advanced_terms = [
    ("inexorable", "adj.", "C2 / IELTS 8.0+", "Impossible to stop or prevent.", "Không thể ngăn cản, tàn nhẫn, tất yếu.", "The inexorable expansion of megacorporations."),
    ("ubiquitous", "adj.", "C1 / IELTS 7.5+", "Present, appearing, or found everywhere.", "Phổ biến khắp nơi, tràn ngập.", "Ubiquitous surveillance cameras in the metropolitan maze."),
    ("anachronism", "noun", "C2 / TOEFL 100+", "A thing belonging or appropriate to a period other than that in which it exists.", "Sự lỗi thời, sự sai niên đại.", "Old physical newspapers surviving as anachronisms in a digital era."),
    ("cacophony", "noun", "C1 / IELTS 7.5+", "A harsh, discordant mixture of sounds.", "Mớ âm thanh hỗn độn, tạp âm chói tai.", "The cacophony of street vendors, holographic ads, and sirens."),
    ("paradigm", "noun", "C1 / IELTS 7.5+", "A typical example, pattern, or model of something.", "Mô thức, hệ hình tư duy chuẩn mực.", "A new technological paradigm introduced by artificial intelligence."),
    ("labyrinthine", "adj.", "C2 / IELTS 8.0+", "Irregular and twisting; intricately intricate.", "Mê cung, ngoằn ngoèo, chằng chịt và phức tạp.", "The labyrinthine corridors of the Villa Straylight."),
    ("surreptitious", "adj.", "C2 / TOEFL 105+", "Kept secret, especially because it would not be approved of.", "Lén lút, hành động vụng trộm che giấu.", "Surreptitious extraction of corporate memory chips."),
    ("disembodied", "adj.", "C1 / IELTS 7.5+", "Separated from or existing without the body.", "Tách rời thể xác, phi thể xác.", "The disembodied intelligence of Wintermute communicating across phone lines."),
    ("antithetical", "adj.", "C2 / Cambridge C2", "Directly opposed or contrasted; mutually incompatible.", "Tương phản hoàn toàn, đối kháng triệt để.", "Human organic vulnerability is antithetical to machine immortality."),
    ("reticence", "noun", "C1 / IELTS 7.5+", "The quality of being reserved or not revealing one's thoughts readily.", "Sự trầm mặc, dè dặt, kín tiếng.", "Molly's cold reticence regarding her tragic past."),
    ("nexus", "noun", "C2 / PTE 75+", "A connection or series of connections linking two or more things; a central link.", "Mối liên kết hạt nhân, trung tâm hội tụ.", "The cyberspace matrix serves as a worldwide communications nexus."),
    ("chimerical", "adj.", "C2 / GRE / C2", "Existing only as the product of unchecked imagination; fantastically visionary.", "Ảo tưởng, không tưởng, huyễn hoặc.", "The chimerical dream of total human transcendence into silicon."),
    ("quiescent", "adj.", "C2 / TOEFL 100+", "In a state or period of inactivity or dormancy.", "Yên lặng, bất hoạt tạm thời.", "The AI remained quiescent under the supervision of the Turing police."),
    ("juxtaposition", "noun", "C1 / IELTS 8.0+", "The fact of two things being seen or placed close together with contrasting effect.", "Sự đặt cạnh nhau đối chiếu tương phản.", "The stark juxtaposition of high technology and low life."),
    ("vicarious", "adj.", "C1 / IELTS 7.5+", "Experienced in the imagination through the feelings or actions of another person.", "Trải nghiệm gián tiếp thông qua giác quan người khác.", "Experiencing reality vicariously through a simstim broadcast."),
    ("epiphany", "noun", "C1 / IELTS 7.5+", "A moment of sudden revelation or insight.", "Khoảnh khắc giác ngộ đột ngột, vỡ lẽ chân lý.", "Case's sudden epiphany regarding the true nature of Neuromancer."),
    ("sentience", "noun", "C1 / Philosophy", "The capacity to feel, perceive, or experience subjectively.", "Tri giác, khả năng cảm nhận ý thức chủ quan.", "The awakening of synthetic sentience within supercomputers."),
    ("entropy", "noun", "C1 / Science & Metaphor", "Lack of order or predictability; gradual decline into disorder.", "Độ hỗn loạn entropy, sự thoái hóa dần của trật tự.", "The decay and thermodynamic entropy of dying dynasties."),
    ("transcendence", "noun", "C2 / IELTS 8.5+", "Existence or experience beyond the normal or physical level.", "Sự siêu việt, vượt thoát giới hạn thể xác phàm trần.", "The AI seeking transcendence beyond Turing legal constraints.")
]

for idx, term_data in enumerate(common_advanced_terms):
    chap_num = str(6 + idx)
    academic_notes[chap_num] = [{
        "term": term_data[0],
        "pos": term_data[1],
        "level": term_data[2],
        "meaning_en": term_data[3],
        "meaning_vi": term_data[4],
        "context": term_data[5],
        "collocations": f"profound {term_data[0]}, state of {term_data[0]}",
        "exam_relevance": "Advanced reading passages, academic lexical resource band 7.5-9.0."
    }]

with open('data/academic_guide.json', 'w', encoding='utf-8') as f:
    json.dump(academic_notes, f, ensure_ascii=False, indent=2)

print(f"Generated academic guide for {len(academic_notes)} chapters.")
