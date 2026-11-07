# -*- coding: utf-8 -*-
"""Data for Part One: Chiba City Blues (Chapters 1 & 2)"""
from edition.content.models import ChapterContent, VocabularyItem, CyberpunkTerm, GrammarFocus, PracticeQuestion

PART1_CHAPTERS = [
    ChapterContent(
        number=1,
        part_title_en="PART ONE - CHIBA CITY BLUES",
        part_title_vi="PHẦN MỘT - ĐIỆU BLUES THÀNH PHỐ CHIBA",
        chapter_title_en="Chapter 1: The Sky Above the Port",
        chapter_title_vi="Chương 1: Bầu trời phía trên thương cảng",
        word_count=8129,
        summary_en=(
            "In the neon-lit, rain-soaked underworld of Chiba City, Japan, Henry Dorsett Case is a burned-out former console cowboy. "
            "Once a brilliant hacker who breached corporate databases in the virtual reality realm known as cyberspace (the matrix), "
            "Case committed the ultimate transgression: he stole from his employers. In retribution, his nervous system was injected with "
            "a Soviet wartime mycotoxin that selectively burned out his neural connectivity, banishing him permanently from the matrix. "
            "Reduced to a desperate low-level hustler in the alleys of Night City, surviving on amphetamines and black-market deals, "
            "Case discovers that his volatile drug-dealer partner Linda Lee suspects someone wants him killed. Seeking shelter at the "
            "Chatsubo bar, frequented by expatriate mercenaries and sailors, he meets Molly Millions, a cybernetically enhanced "
            "'street samurai' sporting mirrored lenses surgically sealed over her eye sockets and ten razor-sharp retractable 4-centimeter "
            "carbon-fiber blades under her burgundy fingernails. Molly informs Case that her shadowy employer wants to hire him."
        ),
        summary_vi=(
            "Tại thế giới ngầm ngập tràn ánh đèn neon và mưa phùn nhớp nháp của thành phố Chiba (Nhật Bản), Henry Dorsett Case là một cựu "
            "'cao bồi điều khiển' (hacker ma trận) đã hoàn toàn tàn tạ và kiệt quệ. Từng là một siêu trộm dữ liệu xuất chúng tung hoành trong "
            "không gian ảo ba chiều mang tên ma trận (cyberspace), Case đã phạm phải sai lầm chí mạng: ăn trộm của chính ông chủ tập đoàn tuyển mộ mình. "
            "Để trừng phạt, họ đã tiêm vào hệ thần kinh của anh một loại độc tố nấm mycotoxin thời chiến của Liên Xô, thiêu rụi có chọn lọc các nơ-ron "
            "tiếp nhận xung thần kinh, vĩnh viễn tước đoạt khả năng kết nối tâm trí vào không gian mạng. Bị lưu đày khỏi thế giới số, Case sống lay lắt "
            "như một kẻ buôn lậu lặt vặt tại Phố Đêm (Night City), ngập ngụa trong ma túy kích thích và những vụ làm ăn bẩn thỉu. Tại quán bar Chatsubo, "
            "nơi tụ tập của lính đánh thuê ngoại quốc, anh chạm trán Molly Millions — một nữ 'samurai đường phố' được nâng cấp cơ thể sinh học cơ giới: "
            "mắt được bịt kín vĩnh viễn bằng cặp kính tráng gương phẫu thuật và mười móng vuốt sợi carbon dài 4 cm sắc bén ẩn dưới ngón tay sơn đỏ. "
            "Molly thông báo rằng ông chủ bí ẩn của cô muốn chiêu mộ anh cho một phi vụ chưa từng có."
        ),
        literary_analysis_en=(
            "Gibson's iconic opening sentence—'The sky above the port was the color of television, tuned to a dead channel'—revolutionized "
            "speculative fiction by instantly projecting a technological, entropic metaphor onto nature itself. The passage establishes the foundational "
            "tropes of cyberpunk: high tech fused with low life, bodily alienation, pervasive global commodification, and Japanese-dominated "
            "techno-capitalism. Notice Gibson's economic, hard-boiled prose, heavily indebted to Dashiell Hammett and Raymond Chandler, transposed "
            "into a decaying twenty-first-century sprawl."
        ),
        literary_analysis_vi=(
            "Câu mở đầu kinh điển của Gibson — 'Bầu trời phía trên cảng mang màu sắc của màn hình vô tuyến, dò trúng một kênh chết' — đã cách mạng hóa "
            "văn học suy tưởng bằng cách áp đặt một ẩn dụ cơ giới hóa, tiêu hao entropy lên chính hiện tượng tự nhiên. Chương sách thiết lập những trụ cột "
            "cốt lõi của văn hóa cyberpunk: sự kết hợp giữa công nghệ tối tân và thân phận mạt rệp dưới đáy xã hội (high tech, low life), sự tha hóa của thân xác, "
            "sự bành trướng tuyệt đối của chủ nghĩa tư bản công nghệ Nhật Bản, và văn phong trinh thám gai góc (hard-boiled noir) chịu ảnh hưởng sâu sắc từ "
            "Raymond Chandler và Dashiell Hammett."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="Cyberspace / The Matrix",
                category="Tech & Worldbuilding",
                explanation_en="A consensual hallucination experienced daily by billions of legitimate operators, mathematical representations of data abstracted from the banks of every computer in the human system.",
                explanation_vi="Một ảo giác đồng thuận được hàng tỷ người dùng trải nghiệm mỗi ngày; biểu diễn toán học không gian ba chiều của toàn bộ dữ liệu máy tính trong hệ thống nhân loại.",
                cultural_impact="Coinage that defined the digital revolution, virtual reality, and modern Internet conceptualization."
            ),
            CyberpunkTerm(
                term="Street Samurai",
                category="Subculture & Augmentation",
                explanation_en="A cybernetically enhanced urban mercenary bound by a ruthless personal contract code, combining martial arts with advanced prosthetics.",
                explanation_vi="Lính đánh thuê đường phố được cấy ghép cơ thể máy móc tinh vi, hành động theo bộ quy tắc danh dự tàn bạo cá nhân, kết hợp võ thuật cận chiến và vũ khí cơ giới sinh học.",
                cultural_impact="Archetype that influenced countless manga, anime (Ghost in the Shell), and games (Cyberpunk 2077)."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Consensual",
                ipa="/kənˈsen.sju.əl/",
                part_of_speech="adjective",
                definition_en="Agreed to by all parties involved; mutually accepted.",
                definition_vi="Được sự đồng thuận, nhất trí giữa các bên tham gia.",
                context_sentence="Cyberspace is famously defined as a consensual hallucination experienced daily by billions.",
                collocations=["consensual agreement", "consensual hallucination", "consensual decision"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Entropy",
                ipa="/ˈen.trə.pi/",
                part_of_speech="noun",
                definition_en="A gradual decline into disorder, decay, or unpredictable chaos.",
                definition_vi="Sự suy thoái dần thành hỗn loạn, trạng thái suy tàn mất trật tự.",
                context_sentence="The decaying alleys of Chiba City exhibit a profound socio-economic entropy.",
                collocations=["social entropy", "cultural entropy", "irreversible entropy"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Expatriate",
                ipa="/ekˈspæt.ri.ət/",
                part_of_speech="noun / adjective",
                definition_en="A person residing in a country other than their native country.",
                definition_vi="Người tha hương, người cư trú hoặc làm việc ở nước ngoài.",
                context_sentence="The Chatsubo was a bar patronized almost exclusively by expatriate professional mercenaries.",
                collocations=["expatriate community", "expatriate worker", "expatriate lifestyle"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Prosthesis",
                ipa="/prɒsˈθiː.sɪs/",
                part_of_speech="noun",
                definition_en="An artificial body part, such as a limb, implant, or surgically attached device.",
                definition_vi="Bộ phận giả, thiết bị cơ học hoặc sinh học cấy ghép thay thế bộ phận cơ thể.",
                context_sentence="Molly's mirrored lenses were not removable sunglasses, but surgical prostheses inset into her skull.",
                collocations=["neural prosthesis", "bionic prosthesis", "prosthetic enhancement"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Transgression",
                ipa="/trænzˈɡreʃ.ən/",
                part_of_speech="noun",
                definition_en="An act that goes beyond the bounds of a moral, legal, or established code.",
                definition_vi="Sự vi phạm chuẩn mực, hành vi vượt quá giới hạn đạo đức hoặc pháp luật.",
                context_sentence="Stealing data from his corporate employers was a capital transgression punishable by neural exile.",
                collocations=["moral transgression", "criminal transgression", "pardon a transgression"],
                cefr_level="C2"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Fronted Participial Phrases for Cinematic Atmosphere",
            structure="[Participial Phrase (V-ing / V-ed)], [Main Clause Subject + Verb]",
            explanation_en="Participial clauses placed at the head of a sentence create immediate spatial immersion and vivid sensory compression without verbose coordination.",
            explanation_vi="Mệnh đề phân từ đảo lên đầu câu giúp cô đọng miêu tả cảm giác, vẽ nên bối cảnh hành động dồn dập và điện ảnh mà không cần dùng nhiều liên từ nối rườm rà.",
            exemplar_sentence="Strapped into the cold surgical chair, Case surrendered to the neurotoxin that would sever his link to cyberspace.",
            exam_utility="Significantly enhances IELTS Writing Task 2 and Cambridge C1/C2 Advanced Sentence Variety scores."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="Why was Case neurologically incapacitated by his previous corporate employers?",
                options=[
                    "He failed to encrypt proprietary military databases during a raid.",
                    "He misappropriated confidential data and attempted to sell it independently.",
                    "His nervous system naturally rejected high-bandwidth interface dermatrodes.",
                    "He was captured by Japanese law enforcement officers in Night City."
                ],
                correct_option=1,
                explanation_en="Case committed theft against his employers, who retaliated by poisoning his nervous system with Soviet mycotoxin.",
                explanation_vi="Case đã biển thủ dữ liệu của chính chủ thuê và bị trừng phạt bằng cách phá hủy tế bào thần kinh."
            ),
            PracticeQuestion(
                question_type="Lexical Precision",
                prompt_en="Choose the word closest in meaning to 'ENTROPY' as used in literary descriptions of decaying urban sprawl:",
                options=["Stability", "Degeneration", "Proliferation", "Stagnation"],
                correct_option=1,
                explanation_en="'Degeneration' captures the progressive decline, disorder, and structural rot denoted by entropy.",
                explanation_vi="'Degeneration' nghĩa là sự thoái hóa, suy tàn, đồng nghĩa với entropy trong bối cảnh xã hội suy vi."
            )
        ]
    ),
    ChapterContent(
        number=2,
        part_title_en="PART ONE - CHIBA CITY BLUES",
        part_title_vi="PHẦN MỘT - ĐIỆU BLUES THÀNH PHỐ CHIBA",
        chapter_title_en="Chapter 2: The Coffin Hotel and the Patron",
        chapter_title_vi="Chương 2: Khách sạn tổ kén và Kẻ bảo trợ",
        word_count=4289,
        summary_en=(
            "Molly escorts Case to a high-end luxury suite overlooking Chiba's toxic Tokyo Bay skyline to meet her employer, "
            "a crisply dressed, military-bearing man who introduces himself as Armitage. Armitage possesses enigmatic resources "
            "and an uncanny awareness of Case's medical dossier and psychological vulnerabilities. He makes an astonishing proposition: "
            "in exchange for Case's specialized console cowboy capabilities on an unprecedented black-ops cyberspace mission, "
            "Armitage will finance full neural reconstruction at a secret surgical clinic, micro-grafting healthy nerve tissue to "
            "restore his ability to access the matrix. However, to guarantee absolute loyalty, Armitage secretly implants microscopic "
            "sacs of the same lethal neurotoxin into Case's arteries; if Case fails or defects, the sac walls will dissolve, releasing "
            "the toxin and crippling him permanently. Case accepts the Faustian bargain, takes leave of his tragic memories with Linda Lee, "
            "and boards a suborbital flight to the Sprawl with Molly and Armitage."
        ),
        summary_vi=(
            "Molly hộ tống Case đến một căn phòng khách sạn thượng lưu sang trọng nhìn ra đường chân trời vịnh Tokyo mờ đục khói độc để diện kiến "
            "ông chủ của cô: một người đàn ông mang phong thái quân nhân nghiêm nghị, ăn vận chỉn chu tự xưng là Armitage. Armitage sở hữu tiềm lực "
            "tài chính khổng lồ cùng hồ sơ y khoa và tâm lý chi tiết đáng sợ về Case. Ông ta đưa ra một đề nghị không tưởng: để đổi lấy kỹ năng "
            "đột nhập ma trận siêu việt của Case cho một chiến dịch đen tối mật, Armitage sẽ chi trả toàn bộ chi phí phẫu thuật tái tạo thần kinh vi phẫu, "
            "ghép mô thần kinh khỏe mạnh để phục hồi hoàn toàn khả năng lướt sóng ma trận của Case. Tuy nhiên, nhằm đảm bảo lòng trung thành tuyệt đối, "
            "Armitage đã ngầm cấy vào thành động mạch của Case những túi vi nang chứa chính độc tố thần kinh hủy diệt; nếu Case phản bội hoặc chậm trễ, "
            "lớp vỏ vi nang sẽ tan biến, phóng thích chất độc làm anh liệt vĩnh viễn. Case chấp nhận bản giao kèo kiểu Faust này, bỏ lại sau lưng ký ức "
            "đau thương về Linda Lee, và bước lên chuyến bay cận quỹ đạo hướng về đại đô thị Sprawl cùng Molly và Armitage."
        ),
        literary_analysis_en=(
            "Chapter 2 centers on the classic cyberpunk theme of the 'Faustian bargain' mediated through biomedical control. "
            "Armitage embodies the cold, faceless authority of disembodied military-corporate power. The contrast between Case's cramped "
            "'coffin' sleeping capsule in Cheap Hotel and Armitage's pristine high-altitude suite dramatizes the extreme socio-economic stratification "
            "of Gibson's future. Biological flesh ('the meat') is exposed as fundamentally fragile and subject to biochemical hostage-taking."
        ),
        literary_analysis_vi=(
            "Chương 2 tập trung vào chủ đề kinh điển của thể loại cyberpunk: 'bản giao kèo của quỷ Faust' thông qua sự kiểm soát công nghệ y sinh. "
            "Armitage hiện thân cho quyền lực phi nhân tính, lạnh lùng của giới quân phiệt - tài phiệt tập đoàn. Sự đối lập giữa buồng ngủ 'tổ kén' chật hẹp "
            "của Case tại khách sạn rẻ tiền và căn suite xa hoa trên cao của Armitage thể hiện sâu sắc sự phân hóa giai cấp tột cùng. Thân xác sinh học "
            "('the meat') hiện lên mong manh và bị biến thành con mấu thí nghiệm bằng công nghệ sinh hóa."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="Coffin Hotel",
                category="Urban Geography",
                explanation_en="Extremely compact modular sleeping capsules popular in crowded cyberpunk metropolitan hubs, providing minimal shelter.",
                explanation_vi="Mô hình khách sạn khoang con nhộng tối giản cực kỳ thịnh hành ở các đô thị tương lai đông đúc, chỉ đủ không gian nằm ngủ.",
                cultural_impact="Anticipated Japan's modern capsule hotel culture and minimalist modular micro-apartments."
            ),
            CyberpunkTerm(
                term="Toxin Sacs / Bio-leash",
                category="Biomedical Coercion",
                explanation_en="Micro-encapsulated biochemical implants placed into an operative's vascular system to enforce absolute compliance under threat of timed dissolution.",
                explanation_vi="Các túi độc vi nang cấy thẳng vào mạch máu đối tượng như một sợi dây xích sinh học vô hình, ép tuân lệnh tuyệt đối.",
                cultural_impact="Influenced countless sci-fi tropes including Suicide Squad and cyberpunk espionage narratives."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Coercion",
                ipa="/koʊˈɜːr.ʒən/",
                part_of_speech="noun",
                definition_en="The practice of persuading someone to do something by using force or threats.",
                definition_vi="Sự cưỡng bức, ép buộc bằng đe dọa hoặc vũ lực.",
                context_sentence="Armitage relied on biochemical coercion to compel Case's absolute obedience.",
                collocations=["under coercion", "biochemical coercion", "state coercion"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Faustian",
                ipa="/ˈfaʊ.sti.ən/",
                part_of_speech="adjective",
                definition_en="Done for present gain without regard for future cost or consequences; selling one's soul for power.",
                definition_vi="Mang tính chất đổi chác linh hồn vì quyền lợi trước mắt bất chấp hậu quả thảm khốc.",
                context_sentence="Case enters into a Faustian pact: he recovers his nervous system but surrenders bodily autonomy.",
                collocations=["Faustian bargain", "Faustian pact", "Faustian dilemma"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Disseminate",
                ipa="/dɪˈsem.ɪ.neɪt/",
                part_of_speech="verb",
                definition_en="To spread or disperse information, knowledge, or substances widely.",
                definition_vi="Phổ biến, truyền bá rộng rãi thông tin hoặc gieo rắc chất thể.",
                context_sentence="If the micro-capsule walls dissolved, the neurotoxin would disseminate throughout his bloodstream.",
                collocations=["disseminate information", "disseminate propaganda", "disseminate widely"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Mycotoxin",
                ipa="/ˌmaɪ.kəʊˈtɒk.sɪn/",
                part_of_speech="noun",
                definition_en="A toxic substance produced by a fungus, frequently utilized in bio-warfare fiction.",
                definition_vi="Độc tố do vi nấm sản sinh, thường dùng trong vũ khí sinh học thần kinh.",
                context_sentence="The wartime mycotoxin had selectively destroyed the synapses responsible for matrix connection.",
                collocations=["lethal mycotoxin", "fungal mycotoxin", "mycotoxin exposure"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Suborbital",
                ipa="/sʌbˈɔː.bɪ.təl/",
                part_of_speech="adjective",
                definition_en="Relating to a trajectory that travels to the edge of space without completing a full orbital rotation.",
                definition_vi="Cận quỹ đạo (bay lên tầng rìa không gian nhưng chưa đi hết một vòng quỹ đạo trái đất).",
                context_sentence="The trio boarded a suborbital flight spanning the Pacific Ocean toward the eastern seaboard sprawl.",
                collocations=["suborbital flight", "suborbital trajectory", "suborbital vehicle"],
                cefr_level="C1"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Conditional Clauses with Implied Threat (Inversion / Ellipsis)",
            structure="Should + Subject + Verb, [Threat / Consequence]",
            explanation_en="Using inverted conditional structures creates formal gravitas, legalistic precision, and ominous tension in high-stakes dialogue.",
            explanation_vi="Cấu trúc đảo ngữ điều kiện loại 1 (Should + S + V) tạo sắc thái trang trọng, đanh thép và đầy tính răn đe trong các tình huống giao kèo áp chế.",
            exemplar_sentence="Should Case deviate from the mission parameters, the biochemical bond will dissolve within sixty seconds.",
            exam_utility="Crucial for scoring Band 8.0+ in IELTS Writing Grammatical Range and Cambridge C2 Proficiency exams."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Sentence Transformation",
                prompt_en="Rewrite: 'If Case disobeys Armitage, the toxin capsules will disintegrate.' using inverted conditional (Should).",
                options=[
                    "Should Case disobey Armitage, the toxin capsules will disintegrate.",
                    "If Case should disobey Armitage, the toxin capsules would disintegrate.",
                    "Did Case disobey Armitage, the toxin capsules will disintegrate.",
                    "Should Case disobeys Armitage, the toxin capsules will disintegrate."
                ],
                correct_option=0,
                explanation_en="Inverted first conditional replaces 'if' with 'Should' followed by the bare infinitive verb.",
                explanation_vi="Đảo ngữ câu điều kiện loại 1 dùng 'Should + S + V nguyên thể', không chia động từ."
            ),
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="What mechanism ensures Case cannot simply take his cured nervous system and flee Armitage?",
                options=[
                    "An explosive micro-collar welded around his throat.",
                    "Time-release toxin sacs implanted in his arteries that require regular anti-enzyme injections.",
                    "A behavioral tracking chip that delivers crippling electric shocks.",
                    "A psychic bond maintained by Molly Millions."
                ],
                correct_option=1,
                explanation_en="Armitage placed microscopic biochemical enzyme capsules in his bloodstream that will rupture unless periodically neutralized.",
                explanation_vi="Armitage cấy các túi vi nang độc tố vào động mạch của Case, cần tiêm chất kháng enzyme định kỳ mới không vỡ."
            )
        ]
    )
]
