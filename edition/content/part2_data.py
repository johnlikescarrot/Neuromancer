# -*- coding: utf-8 -*-
"""Data for Part Two: The Shopping Expedition (Chapters 3 to 7)"""
from edition.content.models import ChapterContent, VocabularyItem, CyberpunkTerm, GrammarFocus, PracticeQuestion

PART2_CHAPTERS = [
    ChapterContent(
        number=3,
        part_title_en="PART TWO - THE SHOPPING EXPEDITION",
        part_title_vi="PHẦN HAI - CHUYẾN SĂN HÀNG",
        chapter_title_en="Chapter 3: The Sprawl and The Finn",
        chapter_title_vi="Chương 3: Đại đô thị Sprawl và Lão Finn",
        word_count=3651,
        summary_en=(
            "Arriving in the BAMA sprawl (Boston-Atlanta Metropolitan Axis), Case is overwhelmed by the familiar sensory assault "
            "of home—a monolithic geodesic megacity spanning hundreds of miles under climate-controlled domes. Armitage installs "
            "the team in a loft in the cheap industrial fringes of Metro Newark. Molly leads Case to Metro Holografix, a cluttered, "
            "grimy electronics shop operated by 'The Finn,' an idiosyncratic fence, hacker, and hardware technician who tests and "
            "tunes cyberspace consoles, cybernetics, and military gear. Armitage requires customized hacking hardware and a broadcast "
            "rig capable of interfacing Molly's physical sensory feed (simstim) directly with Case's cyberdeck. While the Finn inspects "
            "their custom Ono-Sendai Cyberspace 7 deck, Case contemplates the vast underground economy that fuels illegal net runs."
        ),
        summary_vi=(
            "Đặt chân đến đại đô thị BAMA (Trục đô thị khổng lồ kéo dài từ Boston tới Atlanta), Case bị choáng ngợp bởi sự bùng nổ giác quan "
            "quen thuộc của quê nhà — một siêu cấu trúc mái vòm trắc địa khép kín trải dài hàng trăm dặm với khí hậu điều hòa nhân tạo. "
            "Armitage bố trí nhóm tại một căn gác xép cũ kỹ thuộc rìa khu công nghiệp nghèo nàn Metro Newark. Molly dẫn Case đến tiệm "
            "Metro Holografix, một cửa hàng linh kiện điện tử bừa bộn, nhem nhuốc của 'The Finn' — một tay tiêu thụ đồ gian kiêm kỹ thuật viên "
            "phần cứng quái dị chuyên hiệu chỉnh bàn điều khiển ma trận, thiết bị cơ giới sinh học và khí tài quân sự. Armitage yêu cầu lắp đặt "
            "hệ thống phần cứng xâm nhập tùy biến và một bộ thu phát tín hiệu đặc biệt cho phép đồng bộ trực tiếp luồng cảm giác thực tế của Molly "
            "(simstim) vào cỗ máy cyberdeck của Case. Khi Finn kiểm tra chiếc Ono-Sendai Cyberspace 7, Case trầm ngâm trước quy mô khổng lồ "
            "của nền kinh tế ngầm nuôi sống những vụ đột nhập mạng phi pháp."
        ),
        literary_analysis_en=(
            "Chapter 3 introduces the quintessential megalopolis of science fiction: the Sprawl. Gibson dismantles traditional pastoral American "
            "geography, replacing state borders with a continuous corporate-dominated urban hive. The character of The Finn grounds the text's "
            "visionary technology in gritty material realism: computers here are not sleek utopian tools, but greasy, secondhand machinery "
            "smelling of fried solder and ozone."
        ),
        literary_analysis_vi=(
            "Chương 3 giới thiệu đại đô thị kiểu mẫu của văn học khoa học viễn tưởng: the Sprawl. Gibson xóa bỏ hoàn toàn ranh giới địa lý "
            "truyền thống của nước Mỹ, thay bằng một tổ hợp đô thị khổng lồ bị các tập đoàn chi phối dưới vòm che nhân tạo. Nhân vật Finn kéo "
            "công nghệ viễn tưởng trở về hiện thực trần trụi: máy tính ở đây không phải công cụ không tưởng bóng bẩy, mà là đống đồ cũ nhờn dầu, "
            "bốc mùi khói hàn chì và khí ozone."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="The Sprawl (BAMA)",
                category="Urban Geography",
                explanation_en="The Boston-Atlanta Metropolitan Axis: an uninterrupted urban conglomerate encased under geodesic environmental domes.",
                explanation_vi="Trục đô thị Boston-Atlanta: dải siêu đô thị liên tục bờ đông nước Mỹ nằm dưới các mái vòm khí hậu nhân tạo.",
                cultural_impact="The definitive model of twenty-first-century megalopolises in speculative worldbuilding."
            ),
            CyberpunkTerm(
                term="Simstim (Simulated Stimulation)",
                category="Neural Media",
                explanation_en="A mass entertainment technology allowing a user to inhabit and experience another person's complete sensory apparatus in real time.",
                explanation_vi="Công nghệ truyền thông đại chúng cho phép người dùng trải nghiệm trọn vẹn toàn bộ 5 giác quan của người khác trong thời gian thực.",
                cultural_impact="Precursor to neural recording, brain-computer broadcasting, and neural link media concepts."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Geodesic",
                ipa="/ˌdʒiː.əʊˈdes.ɪk/",
                part_of_speech="adjective",
                definition_en="Relating to the shortest possible line between two points on a curved surface; denoting curved architectural domes built from interlocking geometric polygons.",
                definition_vi="Thuộc trắc địa; hình vòm kiến trúc tạo bởi các đa giác hình học đan xen chịu lực.",
                context_sentence="Massive geodesic domes shielded the Sprawl from toxic exterior weather patterns.",
                collocations=["geodesic dome", "geodesic structure", "geodesic design"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Monolithic",
                ipa="/ˌmɒn.əˈlɪθ.ɪk/",
                part_of_speech="adjective",
                definition_en="Massive, uniform, solid, and virtually unyielding in size or organizational structure.",
                definition_vi="Khổng lồ, đơn khối, đồ sộ và đồng nhất không thể lay chuyển.",
                context_sentence="Corporate arcologies stood as monolithic reminders of transnational capitalism.",
                collocations=["monolithic power", "monolithic architecture", "monolithic entity"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Conglomerate",
                ipa="/kənˈɡlɒm.ər.ət/",
                part_of_speech="noun",
                definition_en="A large corporation made up of several different companies that operate in diversified fields.",
                definition_vi="Tập đoàn đa ngành, khối liên hợp kinh tế quy mô toàn cầu.",
                context_sentence="The multi-national zaibatsu had consolidated into inescapable economic conglomerates.",
                collocations=["multinational conglomerate", "media conglomerate", "corporate conglomerate"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Idiosyncratic",
                ipa="/ˌɪd.i.ə.sɪŋˈkræt.ɪk/",
                part_of_speech="adjective",
                definition_en="Distinctive, peculiar, or unique to an individual person's character or temperament.",
                definition_vi="Kỳ quặc, độc đáo, mang nét đặc thù riêng biệt của một cá nhân.",
                context_sentence="The Finn was an idiosyncratic hoarder whose expertise with antique decks was legendary.",
                collocations=["idiosyncratic behavior", "idiosyncratic style", "idiosyncratic approach"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Fence",
                ipa="/fens/",
                part_of_speech="noun",
                definition_en="An intermediary who buys and sells stolen goods for criminal profit.",
                definition_vi="Kẻ trung gian tiêu thụ tài sản phi pháp, trùm tiêu thụ đồ ăn cắp.",
                context_sentence="Behind his shop facade, the Finn operated as a premier fence for black-market military electronics.",
                collocations=["act as a fence", "criminal fence", "fencing operation"],
                cefr_level="C1"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Absolute Clauses for Descriptive Compression",
            structure="[Noun + Participle / Adjective / Prepositional Phrase], [Main Clause]",
            explanation_en="Absolute constructions provide background circumstances and sensory details independent of the main grammatical subject, creating sophisticated literary flow.",
            explanation_vi="Mệnh đề tuyệt đối (Noun + Participle) cung cấp bối cảnh phụ và chi tiết giác quan độc lập với chủ ngữ chính, giúp câu văn đạt độ tao nhã và chuẩn mực văn học cao.",
            exemplar_sentence="His eyes fixed on the green monitor, his fingers twitching above the Ono-Sendai keys, Case re-entered the matrix.",
            exam_utility="Demonstrates top-tier grammatical mastery required for IELTS Writing Band 8.5+ and Cambridge C2 CPE."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Lexical Precision",
                prompt_en="Which word is the closest synonym for 'MONOLITHIC' in the context of urban megastructures?",
                options=["Colossal", "Fragile", "Decentralized", "Ephemeral"],
                correct_option=0,
                explanation_en="'Colossal' emphasizes gigantic, massive scale, capturing the essence of monolithic architecture.",
                explanation_vi="'Colossal' đồng nghĩa với quy mô khổng lồ, đồ sộ của cấu trúc nguyên khối."
            ),
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="What technical apparatus does The Finn configure to connect Case with Molly?",
                options=[
                    "A direct optical cable welded between their temples.",
                    "A simstim broadcast transceiver allowing Case to experience Molly's sensory feedback.",
                    "A voice synthesizer imitating Molly's auditory frequency.",
                    "An automated sub-neural combat reflex chip."
                ],
                correct_option=1,
                explanation_en="The Finn installs a simstim broadcast rig so Case can ride along in Molly's sensorium while she infiltrates physical sites.",
                explanation_vi="Finn lắp đặt bộ thu phát simstim để Case có thể cảm nhận trọn vẹn mọi giác quan của Molly từ xa."
            )
        ]
    ),
    ChapterContent(
        number=4,
        part_title_en="PART TWO - THE SHOPPING EXPEDITION",
        part_title_vi="PHẦN HAI - CHUYẾN SĂN HÀNG",
        chapter_title_en="Chapter 4: The Infiltration of Sense/Net",
        chapter_title_vi="Chương 4: Đột nhập tập đoàn Sense/Net",
        word_count=5032,
        summary_en=(
            "Armitage reveals their immediate target: the corporate headquarters of media titan Sense/Net, situated in the Sprawl. "
            "Deep inside their subterranean security vaults lies a construct containing the digitized personality, skills, and consciousness "
            "of the late legendary console cowboy McCoy Pauley, known as the 'Dixie Flatline.' Pauley was Case's former mentor, famous "
            "for surviving three flatline EEGs while hacking military ICE. To breach Sense/Net's ultra-secure facility, Armitage hires "
            "the Modern Panther Moderns—a subcultural gang of techno-nihilistic pranksters and reality-hackers led by Lupus Yonderboy. "
            "The Panthers unleash a chaotic, media-jamming diversionary terrorist hoax, spraying mimetic camouflage, simulated terrorist "
            "broadcasts, and panic gas throughout the building. Amid the mayhem, Molly slips inside, neutralizes guards, and locates "
            "the Flatline's ROM construct, while Case monitors her sensorium via simstim and hacks local security feeds."
        ),
        summary_vi=(
            "Armitage hé lộ mục tiêu tác chiến trước mắt: trụ sở tập đoàn truyền thông khổng lồ Sense/Net tại Sprawl. "
            "Sâu trong hầm an ninh ngầm của họ lưu giữ một bản cấu trúc (construct) nạp toàn bộ nhân cách, kỹ năng và ý thức số hóa của "
            "huyền thoại cao bồi điều khiển đã khuất McCoy Pauley, biệt danh 'Dixie Flatline' (Đường Não Phẳng). Pauley từng là sư phụ "
            "của Case, người nổi tiếng với kỷ lục sống sót sau ba lần điện não đồ phẳng lì (chết não lâm sàng) khi phá tường lửa quân sự ICE. "
            "Để đột nhập cơ sở tuyệt mật của Sense/Net, Armitage thuê băng Panther Moderns — một nhóm giang hồ vị lai hư vô theo chủ nghĩa "
            "phá vỡ thực tại do Lupus Yonderboy cầm đầu. Nhóm Panthers tạo nên một màn nghi binh hỗn loạn bằng tin tức giả, khí gas hoảng loạn "
            "và ngụy trang quang học. Giữa cảnh hỗn loạn, Molly thâm nhập vào sâu bên trong, hạ gục bảo vệ và đánh cắp thành công mô-đun ROM "
            "chứa ý thức của Dixie Flatline, trong khi Case theo sát từng cử động qua liên kết giác quan simstim."
        ),
        literary_analysis_en=(
            "Chapter 4 brilliantly dramatizes the concept of 'information warfare.' The Panther Moderns illustrate Gibson's premise that in a "
            "media-saturated future, weaponized disinformation, sensory overloading, and synthetic panic are more destructive than conventional "
            "ballistics. Furthermore, the introduction of the Dixie Flatline construct initiates the novel's philosophical interrogation into the "
            "nature of consciousness: is a recorded ROM matrix with preserved memories truly human, or merely an elaborate mirror of a dead ghost?"
        ),
        literary_analysis_vi=(
            "Chương 4 khắc họa sống động chiến tranh thông tin (information warfare). Băng Panther Moderns minh chứng cho nhận định của Gibson: "
            "trong một tương lai bão hòa truyền thông, thông tin giả bị vũ khí hóa và sự gây nhiễu giác quan còn tàn phá ghê gớm hơn súng đạn "
            "quy ước. Thêm vào đó, việc giới thiệu bản ý thức Dixie Flatline mở ra cuộc vấn đáp triết học sâu sắc: liệu một mô-đun ROM ghi nhớ "
            "ký ức có phải là con người thật sự, hay chỉ là cái bóng ma thuật toán của một linh hồn đã chết?"
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="ROM Construct",
                category="AI & Consciousness",
                explanation_en="A read-only memory matrix encoding the complete neural connectome, memories, and personality algorithms of a deceased person.",
                explanation_vi="Bản ghi nhớ chỉ đọc (ROM) số hóa toàn bộ hệ thống kết nối nơ-ron, ký ức và tính cách của một người đã qua đời.",
                cultural_impact="Foundational concept for digital mind cloning, transhumanist consciousness uploading, and AI ethics."
            ),
            CyberpunkTerm(
                term="Panther Moderns",
                category="Subculture & Insurgency",
                explanation_en="An avant-garde nihilistic youth subculture utilizing sensory disorientation, mimetic suits, and media sabotage to destabilize corporate institutions.",
                explanation_vi="Tiểu văn hóa thanh niên hư vô vị lai dùng bộ đồ tàng hình đổi màu, tin giả và gây nhiễu truyền thông để quậy phá tập đoàn.",
                cultural_impact="Pioneered the 'culture jamming' and visual aesthetics of cyber-gothic street insurgencies."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Mimetic",
                ipa="/mɪˈmet.ɪk/",
                part_of_speech="adjective",
                definition_en="Relating to, characterized by, or exhibiting mimicry or imitation of the surrounding environment.",
                definition_vi="Mang tính chất mô phỏng, bắt chước hoặc biến màu hòa lẫn với môi trường.",
                context_sentence="The Panther Moderns wore mimetic polycarbon cloaks that refracted surrounding ambient light.",
                collocations=["mimetic camouflage", "mimetic polycarbon", "mimetic faculty"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Disinformation",
                ipa="/ˌdɪs.ɪn.fəˈmeɪ.ʃən/",
                part_of_speech="noun",
                definition_en="False information deliberately spread in order to deceive, mislead, or disorient people or organizations.",
                definition_vi="Thông tin sai lệch có chủ đích, tin giả được gieo rắc nhằm đánh lừa dư luận hoặc hệ thống phòng vệ.",
                context_sentence="By broadcasting conflicting tactical disinformation, the Panthers paralyzed Sense/Net security.",
                collocations=["tactical disinformation", "spread disinformation", "disinformation campaign"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Construct",
                ipa="/ˈkɒn.strʌkt/",
                part_of_speech="noun",
                definition_en="An artificial, highly complex conceptual, digital, or psychological model built to replicate personality.",
                definition_vi="Cấu trúc nhân tạo, bản sao kỹ thuật số phức hợp mô phỏng ý thức và nhân cách.",
                context_sentence="The Dixie Flatline was not an organic man, but a preserved digital construct on a magnetic substrate.",
                collocations=["digital construct", "neural construct", "personality construct"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Flatline",
                ipa="/ˈflæt.laɪn/",
                part_of_speech="noun / verb",
                definition_en="An electrical tracing (as on an EEG or ECG) showing no electrical activity, indicating clinical or biological death; to cease living or functioning.",
                definition_vi="Đường điện não/điện tim nằm ngang thẳng đơ (chứng tỏ chết não/ngừng tim lâm sàng); trạng thái sụp đổ hoàn toàn.",
                context_sentence="McCoy Pauley earned his moniker by recovering after his brainwaves had flatlined three times.",
                collocations=["flatline EEG", "flatline trace", "suffer a flatline"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Subterranean",
                ipa="/ˌsʌb.təˈreɪ.ni.ən/",
                part_of_speech="adjective",
                definition_en="Existing, situated, or operating below the surface of the earth; underground.",
                definition_vi="Nằm ngầm dưới lòng đất, thuộc tầng sâu bên dưới bề mặt.",
                context_sentence="Sense/Net safeguarded its prized neural assets in subterranean blast-proof bunkers.",
                collocations=["subterranean vault", "subterranean passage", "subterranean bunker"],
                cefr_level="C1"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Nominalization for Formal Information Density",
            structure="Converting verbs and adjectives into abstract nouns (e.g., infiltrate -> infiltration)",
            explanation_en="Nominalization compresses narrative actions into abstract concepts, increasing academic precision and syntactic weight.",
            explanation_vi="Danh từ hóa (Nominalization) biến các động từ hành động thành khái niệm trừu tượng, gia tăng mật độ thông tin học thuật và tính học thuật sắc sảo.",
            exemplar_sentence="The instantaneous orchestration of the diversion facilitated Molly's undetected extraction of the construct.",
            exam_utility="Essential for achieving Band 8.5+ in IELTS Writing Lexical Resource and Grammatical Range criteria."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="What makes the Dixie Flatline construct exceptionally valuable to Case and Armitage?",
                options=[
                    "He holds the private bank encryption keys to the Swiss orbital bank.",
                    "He was an unrivaled hacker whose digitized reflex algorithms can bypass military-grade cyber ICE.",
                    "He is the original biological designer of the Ono-Sendai terminal.",
                    "He possesses the physical blueprints to the Sense/Net skyscraper."
                ],
                correct_option=1,
                explanation_en="McCoy Pauley was Case's mentor and the greatest deck jockey alive, whose stored instincts can break impenetrable firewalls.",
                explanation_vi="Dixie Flatline là huyền thoại hacker có phản xạ và thuật toán vô song để phá vỡ các bức tường lửa ICE quân sự."
            ),
            PracticeQuestion(
                question_type="Lexical Precision",
                prompt_en="Which term refers to clothing or materials capable of imitating surrounding surfaces for optical stealth?",
                options=["Monolithic", "Mimetic", "Suborbital", "Geodesic"],
                correct_option=1,
                explanation_en="'Mimetic' denotes adaptive imitation, precisely matching the stealth chameleon fabrics used by the Panthers.",
                explanation_vi="'Mimetic' chỉ sự mô phỏng thích nghi thị giác để tàng hình."
            )
        ]
    ),
    ChapterContent(
        number=5,
        part_title_en="PART TWO - THE SHOPPING EXPEDITION",
        part_title_vi="PHẦN HAI - CHUYẾN SĂN HÀNG",
        chapter_title_en="Chapter 5: Awakening the Ghost",
        chapter_title_vi="Chương 5: Đánh thức hồn ma kỹ thuật số",
        word_count=2806,
        summary_en=(
            "Following the heist, Molly receives emergency postoperative wound treatment at an anonymous modular medical clinic "
            "near Baltimore. Case sets up the stolen Sense/Net construct, plugging the Dixie Flatline's ROM card into his deck. "
            "Upon boot-up, the digitized voice of McCoy Pauley responds with uncanny, folksy nonchalance. When Case informs him that "
            "his physical body has been dead for years, the construct accepts its disembodied algorithmic existence with grim, dark humor. "
            "Case connects Dixie into the matrix, and together they initiate a reconnaissance run across transatlantic networks to probe "
            "corporate registries in London. The Flatline demonstrates astonishing hacking speed, cutting effortlessly through standard "
            "commercial ICE, proving that his electronic reflexes remain lethally sharp."
        ),
        summary_vi=(
            "Sau vụ cướp táo tợn, Molly được sơ cứu vết thương tại một phòng khám y tế con nhộng giấu tên gần Baltimore. "
            "Case lắp đặt thẻ nhớ chứa bản ý thức Dixie Flatline vào máy Ono-Sendai. Khi khởi động, giọng nói điện tử của McCoy Pauley vang lên "
            "với phong thái bình thản kỳ lạ. Khi Case thông báo rằng cơ thể sinh học của ông đã chết nhiều năm trước, bản construct chấp nhận "
            "thực tại thuật toán không thân xác của mình bằng sự hài hước đen tối, cay đắng. Case kết nối Dixie vào ma trận, và cả hai cùng nhau "
            "mở một đợt do thám xuyên Đại Tây Dương, thăm dò các máy chủ dữ liệu tập đoàn tại London. Flatline thể hiện tốc độ phá mã kinh hoàng, "
            "xuyên thủng các bức tường ICE thương mại như chém bùn, chứng minh phản xạ điện tử của ông vẫn sắc bén chết người."
        ),
        literary_analysis_en=(
            "The dialogue between Case and the Dixie Flatline is one of the emotional and philosophical summits of the novel. Gibson explores "
            "the Cartesian split between body and mind taken to its extreme: pure cognition without flesh ('meat'). Yet, the Flatline's existence "
            "is tragic; lacking the biological capacity to evolve or create new organic memories, he repeatedly asks Case to promise to erase his "
            "ROM construct once the job is finished, expressing a desire for absolute cessation rather than digital purgatory."
        ),
        literary_analysis_vi=(
            "Cuộc đối thoại giữa Case và Dixie Flatline là một trong những đỉnh cao triết học và cảm xúc của cuốn tiểu thuyết. Gibson đào sâu vào "
            "thuyết nhị nguyên Descartes giữa thể xác và tâm trí bị đẩy đến cực hạn: nhận thức thuần túy không cần da thịt ('the meat'). Tuy nhiên, "
            "sự tồn tại của Flatline mang đậm màu sắc bi kịch: vì bị giới hạn trong bộ nhớ chỉ đọc ROM không thể nảy sinh ký ức mới, ông liên tục xin "
            "Case hãy hứa sẽ xóa sạch mô-đun của mình sau khi phi vụ kết thúc, thà tan biến vĩnh viễn còn hơn chịu cảnh giam cầm bất tận trong luyện ngục số."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="ICE (Intrusion Countermeasures Electronics)",
                category="Cyber Defense",
                explanation_en="Sophisticated security software programs that protect corporate and military databases from unauthorized cyberspace intrusion.",
                explanation_vi="Các phần mềm bảo mật phòng thủ mạng cực kỳ phức tạp dùng để bảo vệ máy chủ tập đoàn khỏi hacker ma trận.",
                cultural_impact="Pioneered the ubiquitous sci-fi term for defensive firewalls, popularized across computer security terminology."
            ),
            CyberpunkTerm(
                term="Neural Connectome / Brain Emulation",
                category="Transhumanism",
                explanation_en="The complete mapping of neural connections within a biological brain, transcribed into synthetic read/write architecture.",
                explanation_vi="Bản đồ liên kết nơ-ron toàn diện của não bộ sinh học được sao chép hoàn chỉnh vào kiến trúc điện toán bán dẫn.",
                cultural_impact="Direct antecedent of current neurological research into whole brain emulation."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Nonchalance",
                ipa="/ˌnɒn.ʃəl.əns/",
                part_of_speech="noun",
                definition_en="The trait of remaining calm, casual, and seemingly unconcerned in stressful situations.",
                definition_vi="Sự thờ ơ, bình thản, điềm nhiên trước biến cố hoặc hoàn cảnh căng thẳng.",
                context_sentence="Dixie greeted the grim news of his own biological death with disarming nonchalance.",
                collocations=["feigned nonchalance", "studied nonchalance", "air of nonchalance"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Substrate",
                ipa="/ˈsʌb.streɪt/",
                part_of_speech="noun",
                definition_en="An underlying substance, layer, or surface upon which an organism or technology develops and operates.",
                definition_vi="Chất nền, tầng vật chất cơ bản nâng đỡ cấu trúc hoặc lưu trữ dữ liệu.",
                context_sentence="Pauley's consciousness was trapped on a silicon substrate, unable to experience biological change.",
                collocations=["silicon substrate", "physical substrate", "organic substrate"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Purgatory",
                ipa="/ˈpɜː.ɡə.tər.i/",
                part_of_speech="noun",
                definition_en="A place or state of temporary suffering, expiation, or limbo.",
                definition_vi="Chốn luyện ngục; trạng thái đau khổ dằn vặt lơ lửng không lối thoát.",
                context_sentence="Remaining locked in a static ROM state was a perpetual digital purgatory for the hacker.",
                collocations=["living purgatory", "endless purgatory", "consigned to purgatory"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Cessation",
                ipa="/sesˈeɪ.ʃən/",
                part_of_speech="noun",
                definition_en="A bringing or coming to an end; a temporary or complete halt.",
                definition_vi="Sự đình chỉ, chấm dứt hoàn toàn một trạng thái hoặc quá trình.",
                context_sentence="The construct pleaded for the eventual cessation of its electronic simulation.",
                collocations=["permanent cessation", "call for a cessation", "immediate cessation"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Reconnaissance",
                ipa="/rɪˈkɒn.ɪ.səns/",
                part_of_speech="noun",
                definition_en="Military observation of a region to locate an enemy or ascertain strategic features.",
                definition_vi="Sự trinh sát, do thám địa bàn hoặc hệ thống phòng ngự của đối phương.",
                context_sentence="Their preliminary reconnaissance of European data banks revealed ominous ice configurations.",
                collocations=["conduct reconnaissance", "aerial reconnaissance", "reconnaissance mission"],
                cefr_level="C1"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Subjunctive Mood in Demands and Formal Requests",
            structure="Demand / Propose / Request + that + Subject + [Bare Infinitive]",
            explanation_en="Expressing urgency, contractual mandates, or existential entreaties using the subjunctive mood reflects high grammatical sophistication.",
            explanation_vi="Thể giả định (Subjunctive mood) dùng sau các động từ yêu cầu, đề nghị (demand/request that + S + V nguyên thể) diễn tả mệnh lệnh hoặc thỉnh cầu dứt khoát.",
            exemplar_sentence="Dixie demanded that Case erase his construct immediately upon completion of the heist.",
            exam_utility="Consistently evaluated in IELTS Academic Reading/Writing and Cambridge English C1/C2 exams."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Sentence Transformation",
                prompt_en="Complete: 'It is essential that Case _____ (not reveal) the construct's true identity to Armitage.'",
                options=["does not reveal", "not reveal", "will not reveal", "not to reveal"],
                correct_option=1,
                explanation_en="In formal subjunctive syntax following 'essential that', the negative bare infinitive 'not reveal' is required.",
                explanation_vi="Cấu trúc giả định 'It is essential that + S + (not) V-infinitive' yêu cầu dùng 'not reveal'."
            ),
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="Why does the Dixie Flatline desire his ROM construct to be erased after the run?",
                options=[
                    "He fears that Sense/Net agents will torture him physically.",
                    "He is angry at Case for resurrecting him.",
                    "He realizes his artificial state is a static, frozen existence unable to learn or genuinely live.",
                    "He wants to protect Case from corporate prosecution."
                ],
                correct_option=2,
                explanation_en="Dixie knows that without biological life or mutable memory, his consciousness is trapped in an agonizing, frozen loop.",
                explanation_vi="Dixie hiểu rằng trạng thái ROM tĩnh không thể tạo ký ức hay thực sự sống, chỉ là vòng lặp số bị giam cầm."
            )
        ]
    ),
    ChapterContent(
        number=6,
        part_title_en="PART TWO - THE SHOPPING EXPEDITION",
        part_title_vi="PHẦN HAI - CHUYẾN SĂN HÀNG",
        chapter_title_en="Chapter 6: Unmasking Armitage",
        chapter_title_vi="Chương 6: Lột mặt nạ Armitage",
        word_count=1449,
        summary_en=(
            "Distrusting Armitage's fabricated identity, Case and the Flatline use their network access to conduct deep counter-intelligence. "
            "They uncover that 'Armitage' does not officially exist in corporate or civic databases. Digging deeper into classified military archives, "
            "they trace his biometric profile back to Colonel Willis Corto, a former US special forces commander who led a disastrous covert "
            "strike mission known as 'Screaming Fist' during a past Russian-American conflict. Corto's assault glider was shot down over Soviet "
            "airspace by EMP weaponry, leaving his entire strike unit slaughtered and Corto physically mutilated, blind, and catatonically "
            "psychotic. Someone—some unimaginable entity with immense resources—rescued Corto from an asylum, rebuilt his mangled body, "
            "and constructed a fragile artificial persona over his shattered psyche named 'Armitage.' Case realizes that Armitage is not "
            "the ultimate mastermind of the operation, but merely an unstable meat-puppet manipulated by an unseen puppet master."
        ),
        summary_vi=(
            "Nghi ngờ danh tính giả mạo của Armitage, Case và Flatline dùng quyền truy cập mạng bí mật để tiến hành phản gián quy mô sâu. "
            "Họ phát hiện cái tên 'Armitage' hoàn toàn không tồn tại trên bất kỳ dữ liệu công dân hay tập đoàn nào. Đào sâu vào kho lưu trữ quân sự "
            "tuyệt mật, họ lần ra hồ sơ sinh trắc học của hắn: hắn chính là Đại tá Willis Corto, cựu chỉ huy lực lượng đặc nhiệm Hoa Kỳ trong "
            "chiến dịch mật 'Screaming Fist' (Cú Đấm Thét Gào) thảm khốc thời chiến tranh với Liên Xô. Tàu lượn tác chiến của Corto từng bị vũ khí "
            "xung điện từ EMP bắn hạ trên không phận Xô Viết, toàn bộ đồng đội bị tiêu diệt, còn Corto bị thương tật cụt tứ chi, mù lòa và chấn thương "
            "tâm thần phân liệt nặng nề. Một thế lực bí ẩn không tưởng với tiềm lực vô biên đã giải cứu Corto khỏi viện tâm thần, tái tạo cơ thể nát vụn "
            "và đắp lên tâm trí vỡ vụn của hắn một nhân cách nhân tạo mỏng manh mang tên 'Armitage'. Case bàng hoàng nhận ra Armitage không phải "
            "kẻ chủ mưu, mà chỉ là một con rối thịt bị điều khiển bởi một bàn tay vô hình ghê gớm hơn nhiều."
        ),
        literary_analysis_en=(
            "Chapter 6 shifts the genre tone towards psychological horror and geopolitical conspiracy. The revelation of Willis Corto deconstructs "
            "the myth of the stoic military leader. In Gibson's universe, the military apparatus is disposable, discarded by transnational corporate "
            "interests. Corto's reconstructed identity illustrates identity fluidity and trauma: a human mind can be rewritten, partitioned, "
            "and deployed as a programmable weapon just as easily as computer software."
        ),
        literary_analysis_vi=(
            "Chương 6 chuyển hướng sang màu sắc kinh dị tâm lý và thuyết âm mưu địa chính trị. Sự thật về Willis Corto đập tan ảo tưởng về hình mẫu "
            "chỉ huy quân sự kiên định. Trong thế giới của Gibson, bộ máy quân đội chỉ là công cụ tiêu hao bị giới tài phiệt tập đoàn vứt bỏ sau khi xong việc. "
            "Nhân cách tái tạo của Corto minh họa sự mong manh và dễ bị ghi đè của bản ngã con người: tâm trí có thể bị lập trình, phân vùng và triển khai "
            "như một thứ vũ khí phần mềm."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="Operation Screaming Fist",
                category="Military Lore",
                explanation_en="A disastrous covert cyber-warfare infiltration mission by US forces against Soviet military installations using gliders and early combat decks.",
                explanation_vi="Chiến dịch xâm nhập tác chiến mạng tuyệt mật của quân đội Mỹ nhắm vào căn cứ Liên Xô, kết thúc bằng thảm họa bị quét sạch.",
                cultural_impact="Echoes Vietnam War trauma transposed into electronic cyberwarfare mythology."
            ),
            CyberpunkTerm(
                term="Constructed Persona / Meat-Puppet",
                category="Psychological Reprogramming",
                explanation_en="A synthetic personality overlaid on a severely traumatized brain via hypnotic conditioning and neuro-chemical therapy.",
                explanation_vi="Nhân cách nhân tạo được cài đè lên bộ não chấn thương qua liệu pháp thôi miên và can thiệp sinh hóa thần kinh.",
                cultural_impact="Major influence on the Manchurian Candidate-style cyberpunk tropes."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Catatonic",
                ipa="/ˌkæt.əˈtɒn.ɪk/",
                part_of_speech="adjective",
                definition_en="Appearing to be in a daze or stupor; characterized by unresponsiveness and muscular rigidity.",
                definition_vi="Bất động đờ đẫn, rơi vào trạng thái đờ người mất phản ứng do sang chấn tâm thần cực độ.",
                context_sentence="Following the EMP strike, Corto was left in a catatonic, unresponsive vegetative state.",
                collocations=["catatonic stupor", "catatonic state", "virtually catatonic"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Biometric",
                ipa="/ˌbaɪ.əʊˈmet.rɪk/",
                part_of_speech="adjective",
                definition_en="Relating to the statistical analysis of unique physiological or biological characteristics.",
                definition_vi="Thuộc về sinh trắc học (nhận diện cá nhân qua vân tay, mống mắt, ADN).",
                context_sentence="Case matched Armitage's biometric retinal patterns to the forgotten military file of Colonel Corto.",
                collocations=["biometric scan", "biometric data", "biometric verification"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Puppet master",
                ipa="/ˈpʌp.ɪt ˌmɑː.stər/",
                part_of_speech="noun",
                definition_en="A person or entity that secretly controls other people or events from behind the scenes.",
                definition_vi="Kẻ giật dây, đạo diễn bí mật đứng sau thao túng mọi sự việc.",
                context_sentence="Armitage was not the architect of the conspiracy, merely a puppet manipulated by an unseen puppet master.",
                collocations=["shadowy puppet master", "political puppet master", "unseen puppet master"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Mutilate",
                ipa="/ˈmjuː.tɪ.leɪt/",
                part_of_speech="verb",
                definition_en="To inflict a violent and disfiguring injury on someone's body.",
                definition_vi="Làm tàn phế, hủy hoại thân thể một cách tàn nhẫn.",
                context_sentence="Wartime laser fire had mutilated Corto's limbs and blinded his vision.",
                collocations=["severely mutilate", "mutilated body", "mutilate beyond recognition"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Disinformation",
                ipa="/ˌdɪs.ɪn.fəˈmeɪ.ʃən/",
                part_of_speech="noun",
                definition_en="Intentionally false information fabricated to obscure an underlying truth.",
                definition_vi="Thông tin sai lạc được ngụy tạo có chủ ý để che đậy sự thật.",
                context_sentence="Armitage's spotless corporate background was an elaborate construct of military disinformation.",
                collocations=["disinformation network", "peddle disinformation", "counter disinformation"],
                cefr_level="C1"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Passive Voice with Reporting Verbs for Objective Distance",
            structure="It is widely believed that... / Subject + is understood to have been + Past Participle",
            explanation_en="Distances the narrator from unverified claims, providing an authoritative, clinical tone suitable for investigative and academic prose.",
            explanation_vi="Thể bị động khách quan với động từ tường thuật (Subject + is understood to have been + V3) tạo sắc thái trung lập, khách quan trong phân tích điều tra.",
            exemplar_sentence="Colonel Corto is understood to have been recruited by an unknown intelligence entity following his evacuation.",
            exam_utility="Crucial for TOEFL Integrated Writing and IELTS Academic Task 2 neutrality criteria."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="What historical tragedy broke Willis Corto's original psyche before he became 'Armitage'?",
                options=[
                    "A laboratory fire in Sense/Net headquarters.",
                    "The failure of Operation Screaming Fist over Soviet territory.",
                    "A street brawl in Chiba City involving Molly Millions.",
                    "A failed cyber raid against the Bank of Berne."
                ],
                correct_option=1,
                explanation_en="Corto led Operation Screaming Fist, where his glider was shot down, destroying his unit and his mental stability.",
                explanation_vi="Corto chỉ huy chiến dịch Screaming Fist thảm họa, tàu bị bắn hạ khiến ông tàn phế và mất trí."
            ),
            PracticeQuestion(
                question_type="Lexical Precision",
                prompt_en="Choose the word most opposite in meaning to 'CATATONIC':",
                options=["Comatose", "Hyperactive", "Lethargic", "Torpid"],
                correct_option=1,
                explanation_en="'Catatonic' describes complete immobility and stupor; 'Hyperactive' represents excessive, vibrant activity.",
                explanation_vi="'Catatonic' là bất động đờ đẫn; từ trái nghĩa là 'Hyperactive' (hoạt động quá mức)."
            )
        ]
    ),
    ChapterContent(
        number=7,
        part_title_en="PART TWO - THE SHOPPING EXPEDITION",
        part_title_vi="PHẦN HAI - CHUYẾN SĂN HÀNG",
        chapter_title_en="Chapter 7: Istanbul and The Illusionist",
        chapter_title_vi="Chương 7: Istanbul và Kẻ tạo ảo ảnh",
        word_count=4108,
        summary_en=(
            "The team travels across Europe to Istanbul, Turkey, an ancient crossroads where decaying Ottoman architecture contrasts "
            "with modern electronic bazaars. Their objective is to recruit Peter Riviera, a depraved, drug-addicted psychopath with a "
            "unique cybernetic talent: sophisticated bio-luminescent holographic projection implants that allow him to cast hyper-realistic "
            "optical illusions directly from his mind into physical space. Riviera uses his talents for sadistic, voyeuristic cabaret performances. "
            "Molly and Case locate Riviera in a seedy cabaret, and Armitage forces him into service using a combination of extortion and the "
            "promise of high-grade medicinal cocaine. Meanwhile, Case is contacted through a public payphone bank in Istanbul by an uncanny, "
            "omnipresent entity possessing artificial intelligence traits, revealing that the true patron orchestrating the entire mission "
            "is not human."
        ),
        summary_vi=(
            "Nhóm của Case bay qua châu Âu tới Istanbul (Thổ Nhĩ Kỳ), ngã tư giao thoa cổ kính nơi kiến trúc Ottoman rêu phong tương phản gay gắt "
            "với những khu chợ linh kiện điện tử sầm uất. Mục tiêu tuyển mộ lần này là Peter Riviera — một kẻ bệnh hoạn, nghiện ma túy nặng "
            "nhưng sở hữu năng lực cơ giới sinh học độc nhất vô nhị: các thiết bị cấy ghép chiếu hình ba chiều (hologram) phát quang sinh học, "
            "cho phép hắn phóng chiếu những ảo ảnh thị giác sống động như thật từ tâm trí ra không gian bên ngoài. Riviera dùng tài năng này cho "
            "những buổi biểu diễn ảo giác biến thái, tàn bạo tại các quán rượu bẩn thỉu. Molly và Case tóm gọn Riviera, và Armitage ép hắn vào đội "
            "bằng sự tống tiền kết hợp mồi nhử cocaine y tế tinh khiết. Cùng lúc đó, khi bước qua dãy bốt điện thoại công cộng tại Istanbul, "
            "từng chiếc điện thoại bất ngờ đồng loạt reo lên: một thực thể trí tuệ nhân tạo toàn năng đã liên lạc trực tiếp với Case, tiết lộ rằng "
            "kẻ bảo trợ thực sự đứng sau toàn bộ chiến dịch này không phải là con người."
        ),
        literary_analysis_en=(
            "Istanbul serves as the geographical hinge connecting Western cyber-capitalism with Eurasian history. Gibson uses Riviera to "
            "interrogate the dark aestheticization of technology: Riviera's cybernetic art is not redemptive or liberating, but narcissistic, "
            "cruel, and sexually predatory. The eerie sequence where public telephones ring sequentially as Case walks past marks the dramatic "
            "manifestation of the artificial intelligence (Wintermute), highlighting the complete vulnerability of human communication grids."
        ),
        literary_analysis_vi=(
            "Istanbul đóng vai trò như bản lề địa lý kết nối chủ nghĩa tư bản số phương Tây với lịch sử huyền bí Á-Âu. Gibson sử dụng nhân vật Riviera "
            "để tra vấn mặt tối của nghệ thuật công nghệ: tài năng ảo ảnh của Riviera không mang tính cứu chuộc hay khai phóng, mà ích kỷ, bệnh hoạn "
            "và tàn bạo. Phân cảnh rùng rợn khi các buồng điện thoại công cộng thi nhau đổ chuông từng chiếc một khi Case bước qua đánh dấu sự lộ diện "
            "đầu tiên của thực thể trí tuệ nhân tạo (Wintermute), phơi bày sự bất lực của con người trước mạng lưới truyền thông số."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="Holographic Projection Implants",
                category="Cybernetic Art & Deception",
                explanation_en="Micro-lasers and epidermal projectors wired into the visual cortex allowing the user to project tangible-looking illusions into space.",
                explanation_vi="Hệ thống máy chiếu vi điểm cấy ghép nối thẳng vào vỏ não thị giác, cho phép phóng chiếu ảo ảnh quang học siêu thực.",
                cultural_impact="Anticipated augmented reality (AR) projection systems and tactile holographic illusion narratives."
            ),
            CyberpunkTerm(
                term="Autonomous AI Network Control",
                category="AI Omnipresence",
                explanation_en="An artificial intelligence possessing unauthorized backdoors into telecommunication switches, manipulating civilian hardware at will.",
                explanation_vi="Khả năng của AI thâm nhập cổng sau viễn thông toàn cầu, điều khiển các thiết bị điện toán ngoại vi theo ý muốn.",
                cultural_impact="Iconic cyberpunk trope of an omnipresent digital deity watching over physical reality."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Depraved",
                ipa="/dɪˈpreɪvd/",
                part_of_speech="adjective",
                definition_en="Morally corrupt; wicked or perverted.",
                definition_vi="Đồi bại, biến chất, sa đọa về mặt đạo đức.",
                context_sentence="Riviera channeled his depraved fantasies into horrifyingly realistic holographic performances.",
                collocations=["depraved criminal", "depraved mind", "morally depraved"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Holographic",
                ipa="/ˌhɒl.əˈɡræf.ɪk/",
                part_of_speech="adjective",
                definition_en="Relating to or produced using holograms (three-dimensional photographic projections).",
                definition_vi="Thuộc về ảnh ba chiều, kỹ thuật tạo hình không gian nổi bằng ánh sáng laser.",
                context_sentence="Riviera manipulated holographic wavelengths to weave convincing optical illusions.",
                collocations=["holographic display", "holographic projection", "holographic image"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Extortion",
                ipa="/ɪkˈstɔː.ʃən/",
                part_of_speech="noun",
                definition_en="The practice of obtaining something, especially money, through force, threats, or blackmail.",
                definition_vi="Sự tống tiền, ép buộc chiếm đoạt bằng đe dọa hoặc áp lực phi pháp.",
                context_sentence="Armitage relied on extortion, holding incriminating Turkish police files over Riviera.",
                collocations=["attempted extortion", "guilty of extortion", "extortion racket"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Omnipresent",
                ipa="/ˌɒm.nɪˈprez.ənt/",
                part_of_speech="adjective",
                definition_en="Widely or constantly encountered; widespread or constantly present everywhere.",
                definition_vi="Có mặt khắp mọi nơi, hiện diện toàn năng ở khắp chốn cùng một lúc.",
                context_sentence="The hidden intelligence seemed omnipresent, manipulating every switchboard in the city.",
                collocations=["omnipresent threat", "omnipresent surveillance", "omnipresent entity"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Crossroads",
                ipa="/ˈkrɒs.rəʊdz/",
                part_of_speech="noun",
                definition_en="An intersection or meeting point of different cultures, trade routes, or historical eras.",
                definition_vi="Ngã tư đường, giao lộ lịch sử nơi các nền văn minh và dòng giao thương gặp nhau.",
                context_sentence="Istanbul functioned as an ancient cultural crossroads now retrofitted with fiber-optic relays.",
                collocations=["cultural crossroads", "at a historic crossroads", "geographical crossroads"],
                cefr_level="C1"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Correlative Conjunctions for Balanced Rhetorical Emphasis",
            structure="Not only [Auxiliary + Subject + Verb]... but [Subject] also [Verb]",
            explanation_en="Inverting after 'Not only' produces dramatic pacing and heightened stylistic sophistication in descriptive exposition.",
            explanation_vi="Đảo ngữ với liên từ tương quan 'Not only + trợ động từ + S + V ... but also' tạo điểm nhấn kịch tính và tăng tính liên kết hùng hồn cho bài viết.",
            exemplar_sentence="Not only did the entity infiltrate the telecommunication switch, but it also addressed Case by his alias.",
            exam_utility="Consistently earns top marks for cohesion and sentence variety in IELTS and PTE Academic essays."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Sentence Transformation",
                prompt_en="Rewrite: 'Riviera projected illusions and he also manipulated people emotionally.' using 'Not only'.",
                options=[
                    "Not only Riviera projected illusions, but also he manipulated people emotionally.",
                    "Not only did Riviera project illusions, but he also manipulated people emotionally.",
                    "Not only was Riviera projecting illusions, but also manipulating people.",
                    "Not only had Riviera projected illusions, but did he manipulate people."
                ],
                correct_option=1,
                explanation_en="'Not only' at the beginning of a clause requires subject-auxiliary inversion: 'Not only did Riviera project...'",
                explanation_vi="Đầu mệnh đề dùng 'Not only' phải đảo trợ động từ lên trước chủ ngữ: 'Not only did Riviera project...'."
            ),
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="What chilling phenomenon occurs as Case walks through Istanbul after recruiting Riviera?",
                options=[
                    "A flock of cybernetic seagulls tracks his precise coordinates.",
                    "Every public telephone he passes rings sequentially once.",
                    "His Ono-Sendai terminal catches fire in his luggage.",
                    "Armitage's toxin sacs prematurely release poison into his blood."
                ],
                correct_option=1,
                explanation_en="A hidden AI demonstrates its terrifying control over civil networks by making a line of public payphones ring one by one as Case walks past.",
                explanation_vi="Thực thể AI bí ẩn thị uy sức mạnh viễn thông bằng cách khiến từng bốt điện thoại lần lượt đổ chuông khi Case bước qua."
            )
        ]
    )
]
