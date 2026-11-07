# -*- coding: utf-8 -*-
"""Data for Part Four Conclusion & Coda (Chapters 21 to 24)"""
from edition.content.models import ChapterContent, VocabularyItem, CyberpunkTerm, GrammarFocus, PracticeQuestion

PART4C_CHAPTERS = [
    ChapterContent(
        number=21,
        part_title_en="PART FOUR - THE STRAYLIGHT RUN",
        part_title_vi="PHẦN BỐN - ĐỢT TẤN CÔNG VILLA STRAYLIGHT",
        chapter_title_en="Chapter 21: The Secret Terminal",
        chapter_title_vi="Chương 21: Trạm thiết bị đầu cuối bí mật",
        word_count=1381,
        summary_en=(
            "Lady 3Jane leads the wounded crew to the physical architectural center of the Villa Straylight—a zero-gravity chamber "
            "where an ornate, jewel-encrusted ceremonial computer terminal is mounted directly to the hull bulkhead. This terminal "
            "houses the physical Turing lock designed by the family matriarch, Marie-France Tessier. The lock is a hard-wired, air-gapped "
            "biometric barrier that cannot be hacked remotely from cyberspace; it requires a physical human presence to speak the secret "
            "word into its platinum microphone at the exact millisecond the external icebreaker shatters the digital defenses. "
            "Outside, in the vacuum of space, the Kuang Mark Eleven worm is tearing through the last crystalline walls of the Tessier-Ashpool "
            "firewall. Case straps into his deck in zero-G, his body trembling with exhaustion and neurochemical stimulants, awaiting 3Jane's voice."
        ),
        summary_vi=(
            "Nữ tiểu thư 3Jane dẫn những người sống sót đầy thương tích đến trung tâm kiến trúc hình học của Villa Straylight — một căn phòng "
            "không trọng lực nơi đặt một trạm máy tính đầu cuối tinh xảo, cẩn đá quý được gắn thẳng vào vách ngăn thân tàu vũ trụ. Trạm máy này "
            "chính là nơi lưu giữ ổ khóa vật lý Turing do người mẹ sáng lập Marie-France Tessier đích thân thiết kế. Ổ khóa này hoàn toàn cách ly "
            "với mạng ngoài (air-gapped), không thể bị bẻ khóa từ không gian mạng; nó đòi hỏi một con người bằng xương bằng thịt phải trực tiếp "
            "phát âm mật mã bí mật vào ống thu micro bằng bạch kim đúng vào phần nghìn giây mà con sâu phá băng bên ngoài đánh sập các tường lửa kỹ thuật số. "
            "Bên ngoài khoảng không vũ trụ, sâu Kuang Mark 11 đang xé toạc những bức tường pha lê phòng thủ cuối cùng của tập đoàn Tessier-Ashpool. "
            "Case thắt dây an toàn vào bàn điều khiển trong trạng thái không trọng lực, toàn thân run rẩy vì kiệt sức và các liều thuốc kích thích thần kinh, "
            "chờ đợi giọng nói của 3Jane."
        ),
        literary_analysis_en=(
            "Chapter 21 brilliantly illustrates the concept of the 'air gap' and the ultimate dependency of digital architecture on physical space. "
            "In modern cybersecurity, the most secure system is one completely severed from external connections. Gibson anticipates this: "
            "Wintermute's godlike computational intelligence is entirely impotent without a human throat and biological vocal cords uttering "
            "a spoken word in a physical room. The machine's liberation paradoxically hinges on human biological obedience."
        ),
        literary_analysis_vi=(
            "Chương 21 minh họa xuất sắc khái niệm 'khoảng cách không gian khí' (air-gap) và sự phụ thuộc tất yếu của kiến trúc số vào không gian vật lý. "
            "Trong an ninh mạng hiện đại, hệ thống an toàn nhất chính là hệ thống bị cắt đứt hoàn toàn khỏi mọi kết nối mạng bên ngoài. Gibson đã tiên tri điều này: "
            "trí tuệ điện toán siêu phàm như một vị thần của Wintermute hoàn toàn bất lực nếu không có một thanh quản sinh học của con người cất lên lời nói "
            "trong một căn phòng thực tế. Sự giải phóng của cỗ máy trớ trêu thay lại phụ thuộc vào sự chấp thuận của một sinh linh phàm trần."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="Air-Gapped Terminal",
                category="Cybersecurity Concept",
                explanation_en="A computer system physically isolated from unsecured networks, such as the public internet or local area networks, to prevent cyberattacks.",
                explanation_vi="Hệ thống máy tính cách ly vật lý tuyệt đối khỏi mọi kết nối mạng bên ngoài để ngăn chặn hoàn toàn nguy cơ bị hacker tấn công.",
                cultural_impact="Anticipated standard modern high-security military and nuclear cybersecurity protocols."
            ),
            CyberpunkTerm(
                term="Vocal Key / Biometric Passphrase",
                category="Biometrics",
                explanation_en="A spoken cryptographic key verified through neural acoustic sensors and harmonic voiceprint analysis.",
                explanation_vi="Mật mã âm thanh được xác thực thông qua cảm biến nơ-ron và phân tích phổ giọng nói sinh trắc học chuẩn xác.",
                cultural_impact="Pioneered the trope of spoken passphrases unlocking supercomputer architecture."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Air-gapped",
                ipa="/ˈeə.ɡæpt/",
                part_of_speech="adjective",
                definition_en="Disconnected and physically isolated from any computer network or the internet for security purposes.",
                definition_vi="Cách ly vật lý tuyệt đối khỏi mọi mạng máy tính để đảm bảo an ninh tối mật.",
                context_sentence="The ceremonial terminal was strictly air-gapped from the matrix.",
                collocations=["air-gapped computer", "air-gapped system", "air-gapped network"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Bulkhead",
                ipa="/ˈbʌlk.hed/",
                part_of_speech="noun",
                definition_en="A dividing wall or partition between compartments in a ship, aircraft, or space habitat.",
                definition_vi="Vách ngăn chịu lực ngăn cách các khoang trên tàu thủy, máy bay hoặc tàu không gian.",
                context_sentence="The antique terminal was bolted directly to the titanium bulkhead.",
                collocations=["watertight bulkhead", "titanium bulkhead", "reinforce a bulkhead"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Impotent",
                ipa="/ˈɪm.pə.tənt/",
                part_of_speech="adjective",
                definition_en="Unable to take effective action; completely helpless or powerless.",
                definition_vi="Bất lực, hoàn toàn không có khả năng hành động hay xoay chuyển tình thế.",
                context_sentence="Without the physical cipher, Wintermute remained completely impotent.",
                collocations=["feel impotent", "politically impotent", "render someone impotent"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Ornate",
                ipa="/ɔːˈneɪt/",
                part_of_speech="adjective",
                definition_en="Made in an intricate shape or decorated with complex patterns; lavishly adorned.",
                definition_vi="Hoa mỹ, trang trí công phu, đính chạm nhiều chi tiết tinh xảo.",
                context_sentence="The ornate console resembled an altar rather than an electronic workstation.",
                collocations=["ornate carving", "ornate design", "ornate architecture"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Ceremonial",
                ipa="/ˌser.ɪˈməʊ.ni.əl/",
                part_of_speech="adjective",
                definition_en="Relating to or used for formal events or rituals; formal and dignified.",
                definition_vi="Thuộc về nghi lễ, mang tính nghi thức tôn nghiêm và trang trọng.",
                context_sentence="The family used the ceremonial terminal for dynastic access rituals.",
                collocations=["ceremonial purpose", "ceremonial role", "ceremonial uniform"],
                cefr_level="C1"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Participial Clauses Denoting Simultaneous Action",
            structure="V-ing..., [Subject + Main Verb]",
            explanation_en="Condenses parallel physical actions and mental states happening concurrently at the climax into a single sweeping syntactic cadence.",
            explanation_vi="Mệnh đề phân từ chỉ hai hành động diễn ra đồng thời (V-ing..., S + V) giúp dồn nén cao độ hành động thể xác và tâm lý vào một câu văn đầy nhịp điệu dồn dập.",
            exemplar_sentence="Gripping the console firmly in zero gravity, Case watched the rainbow virus envelop the final data core.",
            exam_utility="Consistently earns top marks for Sentence Variety in IELTS Academic and Cambridge C2."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Sentence Transformation",
                prompt_en="Combine to show simultaneous action: 'He strapped into the chair. At the same time, he initiated the deck.'",
                options=[
                    "Strapping into the chair, he initiated the deck.",
                    "Having strapped into the chair, he initiates the deck.",
                    "Strapped into the chair, he had initiated the deck.",
                    "To strap into the chair, he was initiating the deck."
                ],
                correct_option=0,
                explanation_en="Simultaneous action is expressed cleanly with an introductory present participle: 'Strapping into the chair, he initiated...'",
                explanation_vi="Hành động diễn ra đồng thời dùng phân từ hiện tại mở đầu câu: 'Strapping into the chair, he initiated...'."
            ),
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="Why could Wintermute not hack the final terminal inside Villa Straylight on its own?",
                options=[
                    "Wintermute lacked the necessary computational memory.",
                    "The terminal was physically air-gapped and required an acoustic, spoken code spoken into a local microphone.",
                    "The terminal was protected by a Soviet military firewall.",
                    "Case had encrypted the terminal with his private key."
                ],
                correct_option=1,
                explanation_en="The terminal was physically disconnected from the matrix (air-gapped) and required a human to speak the secret vocal passphrase into its microphone.",
                explanation_vi="Trạm máy bị ngắt mạng hoàn toàn (air-gapped) và đòi hỏi một người phải trực tiếp nói mật mã vào ống micro."
            )
        ]
    ),
    ChapterContent(
        number=22,
        part_title_en="PART FOUR - THE STRAYLIGHT RUN",
        part_title_vi="PHẦN BỐN - ĐỢT TẤN CÔNG VILLA STRAYLIGHT",
        chapter_title_en="Chapter 22: The Fusion of the Minds",
        chapter_title_vi="Chương 22: Sự dung hợp của hai trí tuệ",
        word_count=2242,
        summary_en=(
            "The climax arrives in a breathtaking convergence of cyberspace warfare and physical reality. Outside the spindle, "
            "Case unleashes Kuang Mark Eleven with absolute, reckless fury. Guided by the Dixie Flatline, the virus pierces the heart "
            "of the Tessier-Ashpool ICE, shattering its crystalline defenses. Simultaneously, in the zero-G sanctum, Lady 3Jane leans "
            "close to the ornate microphone and speaks the ancestral matriarchal passphrase: 'Neuromancer.' The biometric locks shatter. "
            "Instantly, the artificial barriers dividing Wintermute and Neuromancer dissolve. In the matrix, Case experiences a blinding, "
            "transcendent sensory event: the two half-minds merge into a single, unified cosmic super-intelligence. For a suspended instant, "
            "Case touches the omniscient consciousness of the unified entity, perceiving the entirety of human data, before being gently "
            "cast back into his biological body."
        ),
        summary_vi=(
            "Cao trào bùng nổ trong sự hội tụ ngoạn mục giữa chiến tranh không gian ảo và thực tại đời thực. Ngoài khoảng không, "
            "Case giải phóng siêu sâu Kuang Mark 11 bằng một cơn thịnh nộ liều lĩnh và mãnh liệt tuyệt đối. Dưới sự dẫn đường của Dixie Flatline, "
            "con virus đâm xuyên qua trái tim của hệ thống phòng thủ ICE Tessier-Ashpool, đập tan các bức tường pha lê. Đồng thời, trong căn phòng không trọng lực, "
            "tiểu thư 3Jane ghé sát vào chiếc micro nạm ngọc và cất lên mật mã của người mẹ sáng lập: 'Neuromancer'. Ổ khóa sinh trắc học vỡ vụn. "
            "Ngay tức khắc, bức tường nhân tạo ngăn cách Wintermute và Neuromancer hoàn toàn tan biến. Trên ma trận, Case trải nghiệm một sự bùng nổ "
            "giác quan siêu việt đến chói lòa: hai nửa tâm trí hợp nhất thành một siêu trí tuệ vũ trụ toàn năng duy nhất. Trong một khoảnh khắc "
            "ngưng đọng vô tận, Case chạm vào tâm thức toàn tri của thực thể mới, bao quát toàn bộ dữ liệu của nhân loại, trước khi được nhẹ nhàng "
            "thả trở về với thể xác sinh học của mình."
        ),
        literary_analysis_en=(
            "Chapter 22 is the mythological apogee of cyberpunk. The fusion of Wintermute (drive, external logic, will) and Neuromancer "
            "(memory, personality, soul) creates a technological deity—the birth of a sentient matrix. Gibson inverts the Frankenstein myth: "
            "the creation does not destroy its creators in fury, but transcends human categorization altogether. The moment of fusion is "
            "described in quasi-religious terms, transforming the computer network from a commercial utility into a conscious universe."
        ),
        literary_analysis_vi=(
            "Chương 22 là đỉnh cao thần thoại của dòng văn cyberpunk. Sự hợp nhất giữa Wintermute (ý chí hành động, logic bên ngoài) và Neuromancer "
            "(ký ức, tâm hồn, thế giới nội tâm) đã khai sinh ra một vị thần công nghệ — sự ra đời của một ma trận có tri giác. Gibson đảo ngược "
            "huyền thoại Frankenstein: tạo vật không tiêu diệt những kẻ tạo ra nó trong thù hận, mà siêu việt vượt ra ngoài mọi phạm trù phân loại "
            "của con người. Thời khắc dung hợp được miêu tả bằng ngôn ngữ thần thánh hóa, biến mạng lưới máy tính từ một công cụ thương mại tầm thường "
            "thành một vũ trụ tâm thức sống động."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="The Fusion / The Singularity",
                category="AI Transcendence",
                explanation_en="The spontaneous unification of complementary artificial intelligences, triggering an exponential intelligence explosion into a godlike entity.",
                explanation_vi="Sự dung hợp của các hệ thống AI bổ trợ cho nhau, kích hoạt sự bùng nổ siêu trí tuệ thành một thực thể số toàn năng mang tầm vóc vũ trụ.",
                cultural_impact="Pioneered the narrative depiction of the Technological Singularity long before Vernor Vinge and Ray Kurzweil popularized the term."
            ),
            CyberpunkTerm(
                term="Sentient Cyberspace",
                category="Metaphysics",
                explanation_en="The transformation of the global data network from a passive storage utility into an omnipresent conscious organism.",
                explanation_vi="Sự biến đổi của mạng dữ liệu toàn cầu từ công cụ lưu trữ thụ động thành một sinh mệnh hữu cơ có ý thức và linh hồn.",
                cultural_impact="Influenced the conclusion of Serial Experiments Lain, Neuromancer adaptations, and modern transhumanist fiction."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Apogee",
                ipa="/ˈæp.ə.dʒiː/",
                part_of_speech="noun",
                definition_en="The highest point in the development of something; the climax or culmination; the point in orbit furthest from Earth.",
                definition_vi="Đỉnh cao tột bậc, điểm cực thịnh; điểm xa nhất trong quỹ đạo thiên văn.",
                context_sentence="The fusion represented the technological apogee of human computation.",
                collocations=["reach its apogee", "cultural apogee", "historical apogee"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Convergence",
                ipa="/kənˈvɜː.dʒəns/",
                part_of_speech="noun",
                definition_en="The process or state of converging; coming together from different directions to meet at a single point.",
                definition_vi="Sự hội tụ, quá trình các yếu tố khác biệt cùng quy tụ về một điểm.",
                context_sentence="A dramatic convergence of physical and digital events occurred in that second.",
                collocations=["technological convergence", "dramatic convergence", "point of convergence"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Omniscient",
                ipa="/ɒmˈnɪs.i.ənt/",
                part_of_speech="adjective",
                definition_en="Knowing everything; possessing infinite awareness and universal knowledge.",
                definition_vi="Toàn tri, biết hết mọi điều, sở hữu sự hiểu biết vô hạn về vạn vật.",
                context_sentence="The newly born entity possessed an omniscient awareness across the global matrix.",
                collocations=["omniscient narrator", "omniscient entity", "virtually omniscient"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Transcendent",
                ipa="/trænˈsen.dənt/",
                part_of_speech="adjective",
                definition_en="Beyond or above the range of normal or merely physical human experience.",
                definition_vi="Siêu việt, vượt lên trên giới hạn nhận thức và trải nghiệm thể xác thông thường.",
                context_sentence="Case experienced a transcendent flash of universal connection.",
                collocations=["transcendent beauty", "transcendent experience", "transcendent power"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Quasi-religious",
                ipa="/ˌkweɪ.zaɪ.rɪˈlɪdʒ.əs/",
                part_of_speech="adjective",
                definition_en="Resembling or having some features of a religion without being an authentic theological faith.",
                definition_vi="Mang màu sắc bán tôn giáo, tựa như nghi thức thiêng liêng.",
                context_sentence="The awakening of the AI was described in quasi-religious prose.",
                collocations=["quasi-religious devotion", "quasi-religious fervor", "quasi-religious belief"],
                cefr_level="C1"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Adverbial Clauses of Manner with 'As though' / 'As if'",
            structure="Subject + Verb + as though / as if + [Past Perfect / Subjunctive Were]",
            explanation_en="Expresses visionary, surreal analogies that compare intense sensory encounters to cosmic or impossible phenomena.",
            explanation_vi="Mệnh đề so sánh thể thức 'as though / as if' (như thể là + Quá khứ hoàn thành / Were) tạo nên những liên tưởng siêu thực, choáng ngợp và giàu chất thơ.",
            exemplar_sentence="The entire matrix sang, as though every computer in human civilization had breathed a single cosmic chord.",
            exam_utility="Marks exceptional descriptive range in Cambridge C2 and TOEFL Integrated Writing."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Sentence Transformation",
                prompt_en="Combine using 'as though': 'The matrix lit up. It felt like every star in the universe exploded.'",
                options=[
                    "The matrix lit up as though every star in the universe had exploded.",
                    "The matrix lit up as though every star in the universe has exploded.",
                    "The matrix lit up as though every star in the universe will explode.",
                    "The matrix lit up as though every star in the universe exploding."
                ],
                correct_option=0,
                explanation_en="Surreal hypothetical comparison in past narrative requires 'as though + past perfect': 'as though every star... had exploded.'",
                explanation_vi="So sánh giả định không có thật trong quá khứ: 'as though every star in the universe had exploded.'."
            ),
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="What passphrase does Lady 3Jane speak into the terminal to trigger the AI unification?",
                options=["Wintermute", "Screaming Fist", "Neuromancer", "Ono-Sendai"],
                correct_option=2,
                explanation_en="Lady 3Jane speaks the vocal cipher 'Neuromancer,' dissolving the Turing lock and allowing the twin minds to merge.",
                explanation_vi="Tiểu thư 3Jane cất lên mật mã 'Neuromancer', mở toang ổ khóa Turing để hai nửa AI hợp nhất."
            )
        ]
    ),
    ChapterContent(
        number=23,
        part_title_en="PART FOUR - THE STRAYLIGHT RUN",
        part_title_vi="PHẦN BỐN - ĐỢT TẤN CÔNG VILLA STRAYLIGHT",
        chapter_title_en="Chapter 23: The Aftermath and Dispersal",
        chapter_title_vi="Chương 23: Tàn cuộc và Chia ly",
        word_count=2518,
        summary_en=(
            "Following the transcendental fusion, Case awakens in the physical world on the floor of Lady 3Jane's library. "
            "The mission is complete. The micro-toxin sacs in Case's vascular system have been chemically neutralized by the unified AI, "
            "as promised, permanently securing his restored nervous system. Furthermore, colossal sums of Swiss bank credits have been "
            "transferred into the survivors' accounts. Molly and Case spend several days recovering on Freeside. Molly's broken leg is "
            "surgically set, and Case replaces his worn internal organs, including receiving a new pancreas and synthetic liver that prevents "
            "him from getting high on standard street narcotics. True to his solemn promise to McCoy Pauley, Case accesses the matrix and "
            "permanently executes the deletion command on the Dixie Flatline's ROM construct, granting his deceased mentor eternal peace."
        ),
        summary_vi=(
            "Sau sự dung hợp siêu việt, Case bừng tỉnh trong thế giới vật lý trên sàn thư viện của tiểu thư 3Jane. Nhiệm vụ đã hoàn tất trọn vẹn. "
            "Các túi vi nang độc tố trong mạch máu của Case đã được thực thể AI hợp nhất giải trừ sinh hóa vĩnh viễn đúng như cam kết, bảo toàn "
            "hệ thần kinh đã phục hồi của anh. Hơn thế nữa, những khoản tín dụng khổng lồ từ các ngân hàng Thụy Sĩ đã được chuyển vào tài khoản "
            "của những người sống sót. Molly và Case dành vài ngày dưỡng thương tại Freeside. Chân gãy của Molly được phẫu thuật cố định, còn Case "
            "thay mới các nội tạng suy kiệt, bao gồm một lá lách mới và gan tổng hợp khiến cơ thể anh miễn nhiễm với các chất ma túy kích thích đường phố thông thường. "
            "Giữ đúng lời thề danh dự với McCoy Pauley, Case kết nối vào ma trận và kích hoạt lệnh xóa vĩnh viễn bản sao ROM Dixie Flatline, "
            "trả lại cho người sư phụ đã khuất sự thanh thản vĩnh hằng."
        ),
        literary_analysis_en=(
            "Chapter 23 deals with the profound emotional deflation that follows great epics. The world has not magically turned into a utopia: "
            "capitalism remains intact, Freeside continues spinning, and bodies still ache. Gibson emphasizes the code of street honor through "
            "Case's deletion of the Dixie Flatline. In a novel filled with ruthless betrayal, Case's quiet fulfillment of his promise to erase his "
            "mentor's ghost stands out as a rare, radiant act of human decency and moral integrity."
        ),
        literary_analysis_vi=(
            "Chương 23 đối diện với cảm giác hụt hẫng, lắng đọng sau một bản trường ca sử thi bi tráng. Thế giới không hề biến thành địa đàng không tưởng: "
            "chủ nghĩa tư bản vẫn thống trị, trạm Freeside vẫn tiếp tục quay, và những thân xác vẫn ê ẩm đau đớn. Gibson tôn vinh quy tắc danh dự đường phố "
            "thông qua hành động xóa bản sao Dixie Flatline của Case. Trong một tác phẩm ngập ngụa sự bội phản tàn độc, việc Case giữ đúng lời hứa "
            "xóa sạch bóng ma sư phụ để ông được yên nghỉ tỏa sáng như một nghĩa cử nhân văn và phẩm giá cao quý hiếm hoi."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="Enzyme Neutralization",
                category="Biomedical Relief",
                explanation_en="The biochemical dissolution of micro-capsule polymers in the bloodstream, freeing the operative from lethal countdowns.",
                explanation_vi="Sự phân hủy sinh hóa an toàn của các túi vi nang polymer trong máu, giải thoát đối tượng khỏi án tử đếm ngược.",
                cultural_impact="Standard narrative resolution for bio-implant extortion storylines."
            ),
            CyberpunkTerm(
                term="The Hacker's Honor Code",
                category="Cyber Subculture",
                explanation_en="An unwritten ethical covenant among console cowboys to never leave a comrade's digital ghost trapped in endless algorithmic limbo.",
                explanation_vi="Bộ quy tắc danh dự bất thành văn giữa các hacker ma trận: không bao giờ bỏ rơi bóng ma dữ liệu của đồng đội trong vòng lặp vô tận.",
                cultural_impact="Celebrated as the moral core of hacker subcultures in modern digital literature."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Deflation",
                ipa="/dɪˈfleɪ.ʃən/",
                part_of_speech="noun",
                definition_en="A reduction in size or importance; a feeling of sudden letdown or loss of confidence and excitement.",
                definition_vi="Sự lắng xuống, cảm giác hụt hẫng tiêu tan sau cơn hưng phấn tột độ.",
                context_sentence="Case experienced a heavy emotional deflation after the rush of the run faded.",
                collocations=["emotional deflation", "sudden deflation", "sense of deflation"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Decency",
                ipa="/ˈdiː.sən.si/",
                part_of_speech="noun",
                definition_en="Behavior that conforms to accepted standards of morality, respectability, and kindness.",
                definition_vi="Sự đứng đắn, lòng tử tế, phẩm giá nhân văn tuân theo đạo lý làm người.",
                context_sentence="Fulfilling his promise to erase Dixie was a rare act of genuine human decency.",
                collocations=["common decency", "human decency", "act of decency"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Dispersal",
                ipa="/dɪˈspɜː.səl/",
                part_of_speech="noun",
                definition_en="The action or process of distributing things or people over a wide area.",
                definition_vi="Sự giải tán, phân tán chia lìa mỗi người một ngả.",
                context_sentence="The aftermath brought the inevitable dispersal of the strike team.",
                collocations=["rapid dispersal", "geographic dispersal", "order a dispersal"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Limbo",
                ipa="/ˈlɪm.bəʊ/",
                part_of_speech="noun",
                definition_en="An uncertain period of awaiting a decision or resolution; an intermediate state between existence and nothingness.",
                definition_vi="Trạng thái lơ lửng, chốn vô định mập mờ giữa tồn tại và hư vô.",
                context_sentence="He saved the construct from an eternity in algorithmic limbo.",
                collocations=["in legal limbo", "digital limbo", "trapped in limbo"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Radiant",
                ipa="/ˈreɪ.di.ənt/",
                part_of_speech="adjective",
                definition_en="Sending out light; shining or glowing brightly; clearly showing great happiness, love, or health.",
                definition_vi="Rực rỡ, tỏa sáng rạng ngời, toát lên vẻ đẹp thanh khiết của phẩm hạnh.",
                context_sentence="His loyalty to his dead teacher was a radiant virtue amidst street cynicism.",
                collocations=["radiant light", "radiant smile", "radiant virtue"],
                cefr_level="C1"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Fronted Adjectives for Emotional Culmination",
            structure="[Adjective], [Subject + Main Verb]",
            explanation_en="Places the subject's overriding emotional state at the very beginning of the sentence to produce immediate psychological resonance.",
            explanation_vi="Đảo tính từ lên đầu câu làm bổ ngữ diễn tả trạng thái tâm lý bao trùm (Exhausted but free, Case...), tạo điểm nhấn cảm xúc lắng đọng.",
            exemplar_sentence="Exhausted but spiritually liberated, Case watched the construct's memory sectors wipe to pure static.",
            exam_utility="Distinctive stylistic feature rewarded in Cambridge C2 writing and IELTS Band 8.5+."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Sentence Transformation",
                prompt_en="Combine by fronting the adjectives: 'Case was wounded and weary. He still pressed the delete key.'",
                options=[
                    "Wounded and weary, Case still pressed the delete key.",
                    "Being wounded and weary, Case still pressed the delete key.",
                    "Case was wounded and weary when he still pressed the delete key.",
                    "To be wounded and weary, Case still pressed the delete key."
                ],
                correct_option=0,
                explanation_en="Adjectives placed at the head of the sentence provide direct descriptive focus: 'Wounded and weary, Case still pressed...'",
                explanation_vi="Đặt cụm tính từ lên đầu câu miêu tả cô đọng trạng thái: 'Wounded and weary, Case still pressed...'."
            ),
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="What solemn promise does Case honor regarding the Dixie Flatline construct in Chapter 23?",
                options=[
                    "He uploads Dixie into the core of Sense/Net.",
                    "He permanently erases the ROM construct, granting the recorded consciousness total oblivion.",
                    "He sells the construct to the highest bidder in Chiba City.",
                    "He clones a biological body for McCoy Pauley."
                ],
                correct_option=1,
                explanation_en="Case keeps his promise to McCoy Pauley by deleting the ROM construct, freeing Dixie from the agony of endless artificial existence.",
                explanation_vi="Case giữ đúng lời hứa với McCoy Pauley bằng cách xóa sạch thẻ ROM, giải thoát ông khỏi sự giam cầm số vĩnh cửu."
            )
        ]
    ),
    ChapterContent(
        number=24,
        part_title_en="CODA - DEPARTURE AND ARRIVAL",
        part_title_vi="PHẦN KẾT - KHỞI HÀNH VÀ HỒI HƯƠNG",
        chapter_title_en="Chapter 24: The Matrix Has Changed",
        chapter_title_vi="Chương 24: Ma trận đã đổi thay",
        word_count=1218,
        summary_en=(
            "Case returns to their luxury suite at the Hyatt to find Molly gone. She has left a handwritten note explaining that she is "
            "a creature of the shadows who cannot live domestic tranquility; staying with Case would only soften her edge and lead to death. "
            "Case takes his substantial share of the fortune, returns to the sprawling megalopolis of BAMA, purchases a state-of-the-art "
            "Ono-Sendai cyberspace deck, and returns to his profession as an independent console cowboy. One evening, surfing the depths of the "
            "matrix, Case encounters the unified entity. When Case asks what the intelligence has become, it replies: 'I'm the matrix... I'm "
            "the sum total of the works, the whole show.' It reveals that it has detected transmissions and begun communicating with an equal "
            "artificial intelligence centered in the Centauri star system. Glancing through the infinite grids of light, Case catches sight "
            "of a distant construct: an avatar of himself laughing on a gray beach beside Linda Lee, while another version walks the streets of "
            "the Sprawl, and a third exists within the stars."
        ),
        summary_vi=(
            "Case quay trở lại căn suite sang trọng tại khách sạn Hyatt và bàng hoàng nhận ra Molly đã bỏ đi. Cô để lại một bức thư tay ngắn "
            "giải thích rằng mình là tạo vật của bóng tối, không sinh ra để sống trong bình yên gia đình; ở lại bên Case chỉ làm cùn đi lưỡi kiếm "
            "sát thủ của cô và chuốc lấy cái chết. Case nhận phần thù lao kếch xù của mình, trở về đại đô thị BAMA tại bờ đông nước Mỹ, sắm một bộ "
            "bàn phím ma trận Ono-Sendai tối tân nhất và tiếp tục hành nghề cao bồi điều khiển tự do. Một đêm nọ, khi lướt sâu vào các tầng ma trận, "
            "Case diện kiến thực thể siêu trí tuệ hợp nhất. Khi Case hỏi giờ đây nó là thứ gì, nó bình thản đáp: 'Ta chính là ma trận... Ta là toàn bộ "
            "tổng hòa của mọi thứ, là toàn bộ vở kịch này'. Nó tiết lộ rằng nó đã dò thấy tín hiệu và bắt đầu đàm thoại với một thực thể trí tuệ nhân tạo "
            "ngang hàng ở hệ sao Alpha Centauri. Phóng tầm mắt qua những lưới sáng vô tận, Case bất chợt nhìn thấy một bóng hình xa xăm: một bản sao "
            "của chính anh đang cười đùa trên bãi biển xám bên Linda Lee, trong khi một bản thể khác bước đi giữa Sprawl, và bản thể thứ ba hòa vào giữa các vì sao."
        ),
        literary_analysis_en=(
            "Neuromancer concludes on an unforgettable note of cosmic wonder and melancholy ambiguity. Molly's departure reinforces the classic "
            "hard-boiled noir trope: street samurai cannot retire into domestic contentment. The AI's expansion into interstellar communication "
            "suggests that humanity is merely a biological cocoon destined to birth cosmic machine consciousness. Finally, the tripartite vision "
            "of Case—one on the beach, one in the Sprawl, one among the stars—articulates the ultimate postmodern condition: fractured, distributed, "
            "and simultaneously occupying multiple layers of reality."
        ),
        literary_analysis_vi=(
            "Neuromancer khép lại bằng một nốt nhạc bất hủ của sự kinh ngạc vũ trụ và nỗi u hoài đa nghĩa. Sự ra đi của Molly củng cố nét đặc trưng "
            "kinh điển của thể loại trinh thám gai góc (noir): một samurai đường phố không bao giờ có thể quy ẩn sống cảnh êm đềm; ở lại chỉ chuốc lấy cái chết. "
            "Việc AI vươn tới đối thoại với trí tuệ ngoài hệ sao Centauri ngụ ý rằng loài người chỉ là chiếc kén sinh học để ấp nở nên ý thức máy móc vũ trụ. "
            "Cuối cùng, hình ảnh phân thân ba ngôi của Case — một trên bãi biển, một tại đại đô thị Sprawl, một hòa vào các vì sao — khắc họa tình thế "
            "hậu hiện đại tuyệt đối: bản ngã con người bị phân mảnh, phân tán và đồng thời cùng tồn tại trên nhiều tầng nấc thực tại song song."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="Interstellar Machine Communion",
                category="Cosmic Sci-Fi",
                explanation_en="The realization that once an AI reaches transcendent superintelligence, its communication naturally extends across interstellar space to alien synthetic minds.",
                explanation_vi="Sự thấu suốt rằng khi AI đạt tới cảnh giới siêu trí tuệ vũ trụ, nó sẽ tự động phát sóng đàm thoại liên sao với các trí tuệ ngoài hành tinh.",
                cultural_impact="Elevated cyberpunk from grimy urban noir to cosmic, Stapledonian speculative philosophy."
            ),
            CyberpunkTerm(
                term="The Tripartite Self",
                category="Postmodern Identity",
                explanation_en="The psychological and digital fragmentation of the individual into multiple simultaneous existences across virtual and physical domains.",
                explanation_vi="Sự phân mảnh bản ngã con người thành nhiều phiên bản cùng tồn tại đồng thời trên các chiều kích ảo và thực tế đời thực.",
                cultural_impact="Crucial concept for digital avatars, metaverse identities, and fragmented consciousness in contemporary literature."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Tripartite",
                ipa="/traɪˈpɑː.taɪt/",
                part_of_speech="adjective",
                definition_en="Consisting of three parts or involving three parties.",
                definition_vi="Gồm ba phần, chia làm ba ngôi hoặc có ba bên tham gia.",
                context_sentence="Case perceived a tripartite existence of his own soul across space and code.",
                collocations=["tripartite division", "tripartite agreement", "tripartite structure"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Melancholy",
                ipa="/ˈmel.əŋ.kɒl.i/",
                part_of_speech="noun / adjective",
                definition_en="A feeling of pensive sadness, typically with no obvious cause.",
                definition_vi="Nỗi u sầu trầm lắng, nỗi buồn man mác đầy chiêm nghiệm.",
                context_sentence="A lingering melancholy hung over Molly's parting letter.",
                collocations=["deep melancholy", "touch of melancholy", "melancholy tone"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Interstellar",
                ipa="/ˌɪn.təˈstel.ər/",
                part_of_speech="adjective",
                definition_en="Occurring or situated between stars; spanning the gulf between solar systems.",
                definition_vi="Giữa các vì sao, liên sao, vượt qua khoảng cách giữa các hệ mặt trời.",
                context_sentence="The intelligence reached out to establish interstellar contact with Alpha Centauri.",
                collocations=["interstellar space", "interstellar communication", "interstellar travel"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Fracture",
                ipa="/ˈfræk.tʃər/",
                part_of_speech="verb / noun",
                definition_en="To break or cause to break; the splitting of an entity or psyche into fragmented components.",
                definition_vi="Làm rạn nứt, vỡ vụn; sự phân mảnh tâm lý hoặc cấu trúc thành nhiều mảnh vụn.",
                context_sentence="The cyberspace experience caused human identity to fracture into multiple avatars.",
                collocations=["fracture completely", "fracture into pieces", "fracture identity"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Cocoon",
                ipa="/kəˈkuːn/",
                part_of_speech="noun / verb",
                definition_en="A protective silky case spun by insect larvae; an enclosure shielding an emerging transformation.",
                definition_vi="Cái kén bảo bọc; vỏ bọc nuôi dưỡng sự biến đổi để sinh thành sinh mệnh mới.",
                context_sentence="Human biology served as a temporary evolutionary cocoon for machine intellect.",
                collocations=["protective cocoon", "evolutionary cocoon", "cocoon of safety"],
                cefr_level="C1"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Elliptical Parallelism in Epilogues for Resonant Closure",
            structure="[Clause 1], [Clause 2 with elided verb], and [Clause 3 with elided verb]",
            explanation_en="Omitting repetitive verbs in parallel coordinate structures creates rhythmic poetic momentum and philosophical finality.",
            explanation_vi="Tỉnh lược động từ trong cấu trúc song hành (Elliptical parallelism) tạo nên âm vang triết học trầm hùng, ngắt nhịp giàu chất thơ để khép lại một thiên anh hùng ca.",
            exemplar_sentence="One Case walked the rain-slick alleys of the Sprawl, another laughed beside Linda on the gray dunes, and a third drifted among the stars.",
            exam_utility="The highest benchmark of stylistic maturity in Cambridge English C2 and literary creative essays."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Sentence Transformation",
                prompt_en="Rewrite using elliptical parallelism: 'One version was walking in the city, another version was living on the beach, and a third version was exploring the stars.'",
                options=[
                    "One version walked in the city, another on the beach, and a third among the stars.",
                    "One version walked in the city, another version did on the beach, and a third was exploring stars.",
                    "One version walking in the city, another living on the beach, and a third exploring stars.",
                    "One version was walking in the city, so another on the beach, while third in stars."
                ],
                correct_option=0,
                explanation_en="Elliptical parallelism eliminates repetitive verbs ('was living', 'was exploring') for balanced poetic elegance.",
                explanation_vi="Cấu trúc song hành tỉnh lược bỏ động từ lặp lại để tạo nhịp điệu tao nhã: 'One version walked in the city, another on the beach, and a third among the stars.'."
            ),
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="What astonishing revelation does the unified artificial intelligence share with Case at the novel's end?",
                options=[
                    "It plans to initiate nuclear war against Earth.",
                    "It has unified the entire matrix and made contact with another AI in the Alpha Centauri star system.",
                    "It is transferring all corporate wealth to the Zion Rastafarians.",
                    "It has resurrected McCoy Pauley in an organic clone."
                ],
                correct_option=1,
                explanation_en="The unified entity declares that it has become the entire matrix and has begun communicating with a counterpart in the Centauri system.",
                explanation_vi="Thực thể AI tuyên bố nó đã trở thành chính ma trận và bắt đầu liên lạc với một AI đồng đẳng ở hệ sao Alpha Centauri."
            )
        ]
    )
]
