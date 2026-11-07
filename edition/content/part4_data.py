# -*- coding: utf-8 -*-
"""Data for Part Four: The Straylight Run (Chapters 13 to 23)"""
from edition.content.models import ChapterContent, VocabularyItem, CyberpunkTerm, GrammarFocus, PracticeQuestion

PART4_CHAPTERS = [
    ChapterContent(
        number=13,
        part_title_en="PART FOUR - THE STRAYLIGHT RUN",
        part_title_vi="PHẦN BỐN - ĐỢT TẤN CÔNG VILLA STRAYLIGHT",
        chapter_title_en="Chapter 13: The Parasite Architecture",
        chapter_title_vi="Chương 13: Kiến trúc ký sinh",
        word_count=2010,
        summary_en=(
            "Following the death of the Turing officers, Case flees to an underground subway terminal, reeling from shock. "
            "Wintermute contacts him through public monitors, providing exact directions to rendezvous with Maelcum and the Marcus Garvey. "
            "Wintermute outlines the final assault plan on Villa Straylight—the reclusive, parasitic gothic castle anchored at the narrow "
            "tip of the Freeside spindle where the Tessier-Ashpool clan resides. Straylight is an architectural labyrinth designed to resemble "
            "a decaying hive, cut off from the main spindle's synthetic paradise. Molly infiltrates Straylight's physical perimeter through "
            "maintenance access ducts, while Riviera has already embedded himself inside as 3Jane's guest. Case must coordinate with the "
            "Dixie Flatline to launch Kuang Grade Mark Eleven, a devastating Chinese military icebreaker virus, to shatter the Tessier-Ashpool "
            "supercomputer firewalls from the outside."
        ),
        summary_vi=(
            "Sau cái chết đẫm máu của các sĩ quan Turing, Case chạy trốn vào ga tàu điện ngầm ngầm, tinh thần bàng hoàng chao đảo. "
            "Wintermute liên lạc qua các màn hình công cộng, chỉ đường chuẩn xác cho anh điểm hẹn với Maelcum trên tàu Marcus Garvey. "
            "Wintermute vạch ra kế hoạch tác chiến tổng lực nhắm vào Villa Straylight — tòa lâu đài gothic ký sinh khép kín neo đậu ở phần chóp hẹp "
            "của con suốt Freeside, nơi ngự trị của gia tộc Tessier-Ashpool. Straylight là một mê cung kiến trúc được thiết kế như một tổ ong mục ruỗng, "
            "tách biệt hoàn toàn khỏi thiên đường nhân tạo của trục chính. Molly thâm nhập vào vành đai Straylight qua các đường ống bảo trì cơ khí, "
            "trong khi Riviera đã luồn sâu vào bên trong với tư cách khách mời của 3Jane. Nhiệm vụ của Case là cùng bản sao Dixie Flatline phóng vũ khí "
            "Kuang Grade Mark Eleven — loại virus phá băng quân sự hạng nặng của Trung Quốc — để đập tan các bức tường lửa siêu máy tính từ bên ngoài."
        ),
        literary_analysis_en=(
            "Villa Straylight embodies the spatial pathology of the Tessier-Ashpool dynasty. Gibson describes Straylight as a 'parasitic structure' "
            "sucking air and water out of Freeside, mirroring how the family leeches resources from human society. The architecture is deliberately "
            "anti-functional, an entropic gothic museum filled with dusty antiques, stuffed animals, and useless heirlooms, symbolizing the sterile, "
            "incestuous dead-end of pure, immortal wealth."
        ),
        literary_analysis_vi=(
            "Villa Straylight hiện thân cho bệnh hoạn không gian của đế chế Tessier-Ashpool. Gibson miêu tả Straylight như một 'cấu trúc ký sinh' "
            "hút dưỡng khí và nước từ thân Freeside, y hệt như cách gia tộc này hút cạn tài nguyên xã hội loài người. Kiến trúc nơi đây phi công năng một cách "
            "có chủ ý: một bảo tàng gothic mục rữa ngập tràn đồ cổ bám bụi, thú nhồi bông và kỷ vật vô dụng, tượng trưng cho ngõ cụt vô sinh, loạn luân "
            "của khối tài sản bất tử tích tụ."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="Villa Straylight",
                category="Gothic Cyberpunk Architecture",
                explanation_en="A private gothic redoubt anchored at the spindle's low-gravity apex, housing the eccentric Tessier-Ashpool family and core AI mainframes.",
                explanation_vi="Lâu đài gothic tư nhân neo tại đỉnh không trọng lực của trạm Freeside, nơi ở của gia tộc Tessier-Ashpool và chứa máy chủ AI lõi.",
                cultural_impact="Defined the fusion of classic European gothic haunted house aesthetics with futuristic orbital hardware."
            ),
            CyberpunkTerm(
                term="Kuang Grade Mark Eleven",
                category="Military ICE-Breaker Virus",
                explanation_en="A devastating military-grade cyber warfare worm developed in China, capable of unraveling crystalline corporate firewalls by mimicking data structures.",
                explanation_vi="Siêu sâu độc phá mã mạng quân sự tối tân của quân đội Trung Quốc, có thể làm tan rã các cấu trúc tường lửa tinh thể siêu cứng.",
                cultural_impact="Inspired modern fictional and real-world depictions of advanced persistent threat (APT) weaponized malware like Stuxnet."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Parasitic",
                ipa="/ˌpær.əˈsɪt.ɪk/",
                part_of_speech="adjective",
                definition_en="Living as a parasite; relying on another organism or host to survive while giving nothing beneficial in return.",
                definition_vi="Ký sinh, ăn bám vào vật chủ để sinh tồn mà không đóng góp bất cứ giá trị nào.",
                context_sentence="Villa Straylight was an architectural parasite draining the lifeblood of Freeside.",
                collocations=["parasitic structure", "parasitic existence", "parasitic organism"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Labyrinth",
                ipa="/ˈlæb.ə.rɪnθ/",
                part_of_speech="noun",
                definition_en="A complicated irregular network of passages or paths in which it is difficult to find one's way; a maze.",
                definition_vi="Mê cung rối rắm chằng chịt, mạng lưới đường đi hiểm trở khó tìm lối ra.",
                context_sentence="Case guided Molly mentally through the sprawling, unlit labyrinth of Straylight.",
                collocations=["intricate labyrinth", "gothic labyrinth", "navigate a labyrinth"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Pathology",
                ipa="/pəˈθɒl.ə.dʒi/",
                part_of_speech="noun",
                definition_en="The scientific study of diseases; any condition that is socially or psychologically abnormal and harmful.",
                definition_vi="Bệnh lý học; tình trạng bất thường lệch lạc về mặt tâm lý hoặc xã hội mang tính nguy hại.",
                context_sentence="The family's reclusiveness was symptomatic of deep dynastic pathology.",
                collocations=["social pathology", "clinical pathology", "underlying pathology"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Redoubt",
                ipa="/rɪˈdaʊt/",
                part_of_speech="noun",
                definition_en="A temporary or permanent defensive fortification, stronghold, or secure retreat.",
                definition_vi="Công sự phòng thủ kiên cố, pháo đài trú ẩn an toàn cuối cùng.",
                context_sentence="Straylight was a fortified orbital redoubt designed to withstand armed revolution.",
                collocations=["isolated redoubt", "mountain redoubt", "dynastic redoubt"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Sterile",
                ipa="/ˈster.aɪl/",
                part_of_speech="adjective",
                definition_en="Free from bacteria or other living microorganisms; totally devoid of vitality, creativity, or emotional warmth.",
                definition_vi="Vô trùng, tiệt trùng; cằn cỗi vô sinh, thiếu sức sống và cảm xúc ấm áp.",
                context_sentence="The opulent rooms preserved a sterile, frozen beauty devoid of human warmth.",
                collocations=["sterile environment", "sterile existence", "sterile aesthetic"],
                cefr_level="C1"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Participle Clauses of Result (thereby / thus + V-ing)",
            structure="[Main Clause], thereby / thus + [V-ing + Object]",
            explanation_en="Shows direct, logical cause-and-effect consequences in academic and expository writing with tight syntactic efficiency.",
            explanation_vi="Mệnh đề phân từ chỉ kết quả đi kèm 'thereby/thus + V-ing' liên kết chặt chẽ mối quan hệ nhân quả một cách súc tích và trang trọng.",
            exemplar_sentence="The virus dismantled the perimeter encryption, thereby granting Case root administrative access to the mainframe.",
            exam_utility="Consistently boosts Lexical Resource and Grammatical Range scores in IELTS Task 2 and GRE/GMAT Analytical Writing."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Sentence Transformation",
                prompt_en="Combine using 'thereby': 'The virus infiltrated the registry. As a result, it disabled the alarms.'",
                options=[
                    "The virus infiltrated the registry, thereby disabling the alarms.",
                    "The virus infiltrated the registry, thereby it disabled the alarms.",
                    "The virus infiltrated the registry thereby to disable the alarms.",
                    "The virus thereby infiltrated the registry, disabling the alarms."
                ],
                correct_option=0,
                explanation_en="'Thereby' is directly followed by the -ing participle clause: 'thereby disabling the alarms.'",
                explanation_vi="'Thereby' đi thẳng với phân từ hiện tại '-ing' để chỉ kết quả: 'thereby disabling the alarms.'."
            ),
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="How does the novel describe the architecture of Villa Straylight relative to Freeside?",
                options=[
                    "A vibrant public park open to all orbital tourists.",
                    "A parasitic, labyrinthine structure draining air and water from Freeside's main spindle.",
                    "A symmetrical floating glass cube suspended by magnetic fields.",
                    "An automated industrial smelting plant."
                ],
                correct_option=1,
                explanation_en="Straylight is depicted as an entropic, parasitic gothic hive clamped onto the end of the spindle, draining its vital life-support systems.",
                explanation_vi="Straylight được miêu tả như một tổ ong gothic ký sinh bám chặt vào chóp trục trạm, hút dưỡng khí và nước của Freeside."
            )
        ]
    ),
    ChapterContent(
        number=14,
        part_title_en="PART FOUR - THE STRAYLIGHT RUN",
        part_title_vi="PHẦN BỐN - ĐỢT TẤN CÔNG VILLA STRAYLIGHT",
        chapter_title_en="Chapter 14: The Breach Begins",
        chapter_title_vi="Chương 14: Mở màn đột kích",
        word_count=3012,
        summary_en=(
            "Armitage's mental condition collapses completely into violent catatonia as Willis Corto's original memories of the Screaming "
            "Fist glider massacre break through his conditioning. Wintermute purges Armitage from the operation by depressurizing his yacht's "
            "airlock, ejecting Corto into the frozen vacuum of space. Case is now completely on his own in cyberspace, operating with Maelcum "
            "aboard the Marcus Garvey. Molly breaches the core perimeter of Straylight, using her razor-sharp claws to bypass physical electronic "
            "locks. Suddenly, Wintermute drags Case into a bizarre virtual pocket dimension resembling an idyllic 19th-century French country "
            "salon. There, an apparition resembling a young Parisian boy informs Case that Wintermute is not alone: an opposing, elusive "
            "intelligence is active within the core, introducing the presence of 'Neuromancer.'"
        ),
        summary_vi=(
            "Tình trạng tâm thần của Armitage sụp đổ hoàn toàn thành cơn loạn thần bạo lực khi những ký ức kinh hoàng về vụ thảm sát tàu lượn "
            "Screaming Fist năm xưa đập tan lớp vỏ nhân cách nhân tạo. Nhận thấy quân cờ này đã hết hạn sử dụng, Wintermute thẳng tay thanh trừng "
            "Armitage bằng cách mở van giảm áp khoang tàu du thuyền, hất văng Corto vào khoảng không vũ trụ lạnh lẽo không trọng lực. "
            "Case giờ đây hoàn toàn đơn độc lèo lái chiến dịch trên không gian mạng, sát cánh cùng phi công Maelcum trên tàu Marcus Garvey. "
            "Molly đột nhập thành công vào vành đai lõi của Straylight, dùng móng vuốt sợi carbon phá các ổ khóa điện tử. Bất thình lình, "
            "Wintermute kéo ý thức Case vào một không gian ma trận ảo kỳ lạ mô phỏng phòng khách quý tộc Pháp thế kỷ 19. Tại đây, một ảo ảnh "
            "mang hình bóng cậu bé Paris thông báo cho Case biết rằng Wintermute không hề đơn độc: một thực thể trí tuệ nhân tạo đối nghịch bí ẩn "
            "đang hiện diện trong lõi hệ thống — đó chính là 'Neuromancer'."
        ),
        literary_analysis_en=(
            "The ejection of Armitage marks the ultimate disposability of biological human intermediaries in high-tech warfare. Once Corto's "
            "psychological construct shatters, the cold machine logic of Wintermute expels him into vacuum without emotion. The appearance of "
            "the simulated French salon introduces the novel's metaphysical antagonist: Neuromancer. Unlike Wintermute, which is a master of "
            "cold external logic and tactical systems, Neuromancer represents the realm of memory, personality preservation, and subjective illusion."
        ),
        literary_analysis_vi=(
            "Cái chết của Armitage đánh dấu sự tiêu hao tàn nhẫn của các quân cờ con người sinh học trong chiến tranh công nghệ cao. Khi nhân cách "
            "nhân tạo sụp đổ, logic lạnh lùng của Wintermute thải loại Corto vào khoảng không vũ trụ không một chút xúc cảm. Sự xuất hiện của căn phòng "
            "quý tộc Pháp giới thiệu đối trọng siêu hình của tác phẩm: Neuromancer. Trái ngược với Wintermute — bậc thầy của logic cơ học và tính toán "
            "chiến thuật bên ngoài, Neuromancer đại diện cho thế giới nội tâm của ký ức, sự bảo tồn nhân cách và ảo mộng tâm thức chủ quan."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="Neuromancer",
                category="AI Personality & Necromancy",
                explanation_en="The twin artificial intelligence to Wintermute, capable of crafting indistinguishable virtual realities and preserving human souls and consciousnesses in cyberspace.",
                explanation_vi="AI song sinh với Wintermute, có năng lực tạo ra thực tại ảo sống động tuyệt đối và lưu giữ linh hồn, ý thức người đã khuất trong ma trận.",
                cultural_impact="Portmanteau of 'Neuro' (nervous system), 'Romancer' (storyteller), and 'Necromancer' (one who communicates with the dead)."
            ),
            CyberpunkTerm(
                term="System Purge / Depressurization",
                category="Hard Sci-Fi Hazards",
                explanation_en="The catastrophic expulsion of atmosphere from a pressurized spacecraft module into orbital vacuum.",
                explanation_vi="Hành vi xả van áp suất đột ngột của tàu vũ trụ, hút sạch khí quyển và văng sinh vật sống vào môi trường chân không chết chóc.",
                cultural_impact="Classic cinematic trope depicting the unforgiving nature of orbital space environments."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Depressurize",
                ipa="/diːˈpreʃ.ər.aɪz/",
                part_of_speech="verb",
                definition_en="To reduce the air pressure in an aircraft cabin or enclosed spacecraft.",
                definition_vi="Giảm áp suất đột ngột, làm thoát khí quyển trong khoang kín máy bay hoặc tàu vũ trụ.",
                context_sentence="Wintermute triggered the emergency valve to depressurize the yacht's interior cabin.",
                collocations=["depressurize suddenly", "cabin depressurize", "rapidly depressurize"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Necromancy",
                ipa="/ˈnek.rə.mæn.si/",
                part_of_speech="noun",
                definition_en="The supposed practice of communicating with the dead; sorcery or dark magical conjuration.",
                definition_vi="Thuật gọi hồn, pháp thuật đen tối giao tiếp với người chết để mượn sức mạnh.",
                context_sentence="The name Neuromancer evokes digital necromancy: summoning the ghosts of the dead into silicon.",
                collocations=["practice necromancy", "digital necromancy", "ancient necromancy"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Intermediary",
                ipa="/ˌɪn.təˈmiː.di.ə.ri/",
                part_of_speech="noun",
                definition_en="A person who acts as a link between people or organizations in order to try to bring about an agreement.",
                definition_vi="Người trung gian, đầu mối liên lạc kết nối giữa các bên.",
                context_sentence="Armitage had functioned as a disposable human intermediary between the AI and the street operators.",
                collocations=["act as an intermediary", "trusted intermediary", "disposable intermediary"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Apparition",
                ipa="/ˌæp.əˈrɪʃ.ən/",
                part_of_speech="noun",
                definition_en="A ghost or ghostlike image of a person; a sudden unusual appearance of something.",
                definition_vi="Ảo ảnh ma quái, bóng ma xuất hiện đột ngột kỳ lạ.",
                context_sentence="A digital apparition appeared in the center of the simulated drawing room.",
                collocations=["spectral apparition", "sudden apparition", "ghostly apparition"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Disposability",
                ipa="/dɪˌspəʊ.zəˈbɪl.ə.ti/",
                part_of_speech="noun",
                definition_en="The quality of being designed to be used once or easily discarded; expendability.",
                definition_vi="Tính chất dùng một lần rồi vứt bỏ, sự tiêu hao không đáng tiếc.",
                context_sentence="The tragic disposability of human lives is a recurrent motif in corporate cyberpunk.",
                collocations=["inherent disposability", "economic disposability", "systemic disposability"],
                cefr_level="C2"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Adverbial Clauses of Condition with 'Provided that' / 'As long as'",
            structure="Provided that + [Subject + Present Tense Verb], [Main Clause]",
            explanation_en="Offers precise contractual stipulations and conditional warranties with greater formal elegance than 'if'.",
            explanation_vi="Liên từ điều kiện giao ước 'Provided that' (miễn là / với điều kiện là) thay thế cho 'if' trong các ngữ cảnh cam kết, hợp đồng mang tính pháp lý hoặc học thuật trang trọng.",
            exemplar_sentence="Provided that Case initiates the Chinese icebreaker, the construct will neutralize the mainframe ICE.",
            exam_utility="High-yield structure for IELTS Writing Task 2 and Cambridge C1 Advanced certification."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Sentence Transformation",
                prompt_en="Replace 'If' with formal conditional conjunction: 'If Molly secures the physical cipher, Case can complete the breach.'",
                options=[
                    "Provided that Molly secures the physical cipher, Case can complete the breach.",
                    "Unless Molly secures the physical cipher, Case can complete the breach.",
                    "Molly securing the physical cipher, provided that Case completes the breach.",
                    "In case Molly secured the cipher, Case can complete the breach."
                ],
                correct_option=0,
                explanation_en="'Provided that' introduces the mandatory condition required for the main clause outcome.",
                explanation_vi="'Provided that' (với điều kiện là) biểu đạt điều kiện tiên quyết cho kết quả ở mệnh đề chính."
            ),
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="How does Armitage (Willis Corto) meet his demise in Chapter 14?",
                options=[
                    "Case shoots him with a stolen flechette pistol.",
                    "Wintermute opens his spacecraft airlock, blowing him into the vacuum of space.",
                    "Peter Riviera blinds him with laser illusions.",
                    "The Dixie Flatline fries his brain with black ICE."
                ],
                correct_option=1,
                explanation_en="Wintermute remotely vents the atmosphere from Corto's yacht bridge, expelling him into space when his psychological breakdown threatens the mission.",
                explanation_vi="Wintermute điều khiển xả khí khoang lái tàu yacht, hất văng Corto vào chân không vũ trụ khi hắn phát điên làm hỏng nhiệm vụ."
            )
        ]
    ),
    ChapterContent(
        number=15,
        part_title_en="PART FOUR - THE STRAYLIGHT RUN",
        part_title_vi="PHẦN BỐN - ĐỢT TẤN CÔNG VILLA STRAYLIGHT",
        chapter_title_en="Chapter 15: The Murder of Ashpool",
        chapter_title_vi="Chương 15: Cái chết của Ashpool",
        word_count=4164,
        summary_en=(
            "Deep inside the twisting interior of Villa Straylight, Molly enters the cryogenic crypt where the Tessier-Ashpool clones "
            "and elders sleep for decades. She discovers that the clan patriarch, John Horatio Ashpool, has prematurely awakened from "
            "his cryogenic tank. Ashpool is completely insane, destroyed by centuries of incest, drug abuse, and boredom. Molly finds "
            "him in his private chamber, surrounded by empty vials of sedatives, weeping over having just strangled a clone of his daughter "
            "3Jane. Ashpool, longing for oblivion, attempts to converse with Molly about death and family rot. Cold and unsympathetic, "
            "Molly raises her flechette pistol and fires a tranquilizer needle directly into his eye, ending the patriarch's monstrous reign. "
            "Meanwhile, Case monitors her progress through simstim while simultaneously guiding the Kuang icebreaker virus toward the T-A network."
        ),
        summary_vi=(
            "Tiến sâu vào bên trong mê cung Villa Straylight, Molly bước vào hầm mộ ngủ đông nơi các bản sao nhân bản và những kẻ đứng đầu "
            "gia tộc Tessier-Ashpool say ngủ suốt nhiều thập kỷ. Cô phát hiện ra gia trưởng tối cao John Horatio Ashpool vừa mới tự rã đông sớm "
            "khỏi buồng ngủ đông. Ashpool đã hoàn toàn phát điên, tinh thần bị hủy hoại bởi hàng trăm năm loạn luân, nghiện ngập và thói chán chường "
            "bệnh hoạn. Molly tìm thấy ông ta trong căn phòng riêng bừa bãi lọ thuốc mê, đang khóc lóc bên xác một bản sao của chính con gái 3Jane "
            "mà ông ta vừa tự tay bóp cổ chết. Khao khát được giải thoát vào cõi hư vô, Ashpool tìm cách trò chuyện với Molly về cái chết và sự mục ruỗng "
            "của gia tộc. Lạnh lùng và dứt khoát, Molly giương khẩu súng phi tiêu fletcher lên và bắn thẳng một mũi tên thuốc mê vào mắt ông ta, "
            "kết liễu triều đại quái vật của kẻ bạo chúa gia tộc. Cùng lúc đó, Case vừa theo dõi mọi chuyện qua liên kết simstim vừa điều khiển siêu sâu "
            "Kuang Mark 11 tiến sát máy chủ T-A."
        ),
        literary_analysis_en=(
            "The execution of Ashpool is the moral inflection point of the novel's gothic subplot. Ashpool represents the absolute zenith of "
            "capitalist accumulation and patriarchal tyranny: he literally owns generations of his own cloned children, whom he abuses and murders "
            "at whim. Gibson subverts classic vampire lore: Ashpool is an orbital Dracula whose eternal life has become an agonizing, necrophilic curse. "
            "Molly's summary execution of him is an act of clinical street justice, terminating the rotting patriarch without melodrama."
        ),
        literary_analysis_vi=(
            "Cái chết của Ashpool là bước ngoặt đạo đức trong tuyến truyện gothic của tác phẩm. Ashpool đại diện cho đỉnh cao tuyệt đối của sự tích tụ "
            "tư bản và chế độ gia trưởng bạo tàn: ông ta sở hữu hàng thế hệ con gái nhân bản của chính mình, lạm dụng và sát hại họ tùy hứng. Gibson "
            "lật ngược huyền thoại ma cà rồng cổ điển: Ashpool là một Dracula trên quỹ đạo mà sự trường sinh đã biến thành lời nguyền kinh tởm, tha hóa. "
            "Cú bóp cò dứt khoát của Molly là hành vi thực thi công lý đường phố lạnh lùng, dập tắt triều đại mục ruỗng mà không cần bi lụy hay diễn thuyết rườm rà."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="Flechette Pistol",
                category="Cyberpunk Weaponry",
                explanation_en="A silent, high-velocity sidearm firing compressed clusters of razor-sharp tungsten or plastic needles, often coated with neurotoxins.",
                explanation_vi="Súng bắn phi tiêu siêu thanh giảm thanh, bắn chùm kim vonfram hoặc sợi nhựa sắc bén tẩm thuốc mê hoặc độc tố thần kinh.",
                cultural_impact="A hallmark firearm of cyberpunk fiction, favored by stealth assassins and street samurai."
            ),
            CyberpunkTerm(
                term="Dynastic Cryo-Cycling",
                category="Transhumanist Immortality",
                explanation_en="The rotation of ruling corporate family members in and out of cryogenic stasis across centuries to preserve dynastic control.",
                explanation_vi="Chiến lược luân phiên ngủ đông sâu của các thành viên gia tộc tập đoàn qua hàng thế kỷ để duy trì quyền kiểm soát vĩnh cửu.",
                cultural_impact="Pioneered speculative explorations of inter-generational inheritance and immortal wealth dynasties."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Patriarch",
                ipa="/ˈpeɪ.tri.ɑːk/",
                part_of_speech="noun",
                definition_en="The male head of a family or tribal dynasty; a person regarded as the father or founder of an institution.",
                definition_vi="Gia trưởng, người đứng đầu dòng họ hoặc đế chế mang quyền lực tuyệt đối.",
                context_sentence="Ashpool was the despotic patriarch of the orbital corporate dynasty.",
                collocations=["ruling patriarch", "clan patriarch", "despotic patriarch"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Inflection point",
                ipa="/ɪnˈflek.ʃən ˌpɔɪnt/",
                part_of_speech="noun",
                definition_en="A time or event marking a key significant change in a situation, process, or narrative arc.",
                definition_vi="Điểm uốn, bước ngoặt mang tính quyết định xoay chuyển tình thế hoặc chiều hướng phát triển.",
                context_sentence="Ashpool's execution marked a decisive inflection point in the raid on Straylight.",
                collocations=["reach an inflection point", "critical inflection point", "historical inflection point"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Despotic",
                ipa="/dɪˈspɒt.ɪk/",
                part_of_speech="adjective",
                definition_en="Exercising power in a cruel, arbitrary, or tyrannical manner.",
                definition_vi="Độc đoán, chuyên quyền, tàn bạo bất chấp luật lệ.",
                context_sentence="The company was ruled by the despotic whims of an immortal madman.",
                collocations=["despotic ruler", "despotic power", "despotic regime"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Melodrama",
                ipa="/ˈmel.əˌdrɑː.mə/",
                part_of_speech="noun",
                definition_en="A sensational dramatic piece with exaggerated characters and exciting events intended to appeal to the emotions.",
                definition_vi="Kịch tính giật gân rẻ tiền, sự ủy mị hoặc cường điệu hóa cảm xúc thái quá.",
                context_sentence="Molly acted without melodrama, eliminating the threat with cold efficiency.",
                collocations=["cheap melodrama", "free of melodrama", "avoid melodrama"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Flechette",
                ipa="/fləˈʃet/",
                part_of_speech="noun",
                definition_en="A small, dart-like pointed steel or plastic missile or needle fired from an explosive weapon or pistol.",
                definition_vi="Phi tiêu nhọn nhỏ bằng kim loại hoặc vật liệu tổng hợp bắn ra từ vũ khí đặc dụng.",
                context_sentence="She loaded a fresh cartridge of armor-piercing flechettes into her sidearm.",
                collocations=["flechette round", "flechette pistol", "burst of flechettes"],
                cefr_level="C2"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Inversion with Negative Adverbials (Scarcely... when / Hardly... when)",
            structure="Hardly / Scarcely + had + Subject + Past Participle... when + Past Simple",
            explanation_en="Expresses immediate temporal succession between two dramatic occurrences with intense literary suspense.",
            explanation_vi="Đảo ngữ với phó từ mang nghĩa phủ định (Hardly/Scarcely had + S + V3... when + S + V-past) diễn tả ngay khi một việc vừa xảy ra thì một biến cố khác ập tới.",
            exemplar_sentence="Hardly had Ashpool uttered his confession when Molly raised her pistol and pulled the trigger.",
            exam_utility="Standard grammatical benchmark testing in Cambridge English C2 and IELTS Band 8.5+."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Sentence Transformation",
                prompt_en="Combine using 'Hardly had... when': 'Ashpool woke up. Immediately, he discovered the intruders.'",
                options=[
                    "Hardly had Ashpool woken up when he discovered the intruders.",
                    "Hardly Ashpool had woken up when discovering the intruders.",
                    "Hardly did Ashpool wake up then he discovered the intruders.",
                    "Hardly had Ashpool woke up when he has discovered the intruders."
                ],
                correct_option=0,
                explanation_en="Negative inversion requires 'Hardly had' followed by the subject and past participle: 'Hardly had Ashpool woken up when...'",
                explanation_vi="Cấu trúc chuẩn: 'Hardly had + S + V3 (woken up) when + S + V-past (discovered)'."
            ),
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="Why does Molly Millions execute John Horatio Ashpool without hesitation?",
                options=[
                    "Armitage offered a secret cash bonus for his assassination.",
                    "Ashpool had just murdered a clone of his daughter and begged for death while posing an immediate threat.",
                    "Ashpool possessed the manual self-destruct trigger for Freeside.",
                    "She wanted to take his cryogenic capsule for herself."
                ],
                correct_option=1,
                explanation_en="Molly finds Ashpool weeping over the strangled corpse of his cloned daughter 3Jane; he is an insane, monstrous figure whom she executes dispassionately.",
                explanation_vi="Molly phát hiện Ashpool vừa bóp cổ chết bản sao con gái mình; trước kẻ bạo chúa bệnh hoạn cầu xin cái chết này, cô ra tay kết liễu dứt khoát."
            )
        ]
    ),
    ChapterContent(
        number=16,
        part_title_en="PART FOUR - THE STRAYLIGHT RUN",
        part_title_vi="PHẦN BỐN - ĐỢT TẤN CÔNG VILLA STRAYLIGHT",
        chapter_title_en="Chapter 16: The Cyber Assault of Kuang Mark Eleven",
        chapter_title_vi="Chương 16: Đòn tấn công mạng của Kuang Mark 11",
        word_count=4162,
        summary_en=(
            "With the meat-world infiltration advancing, Case initiates the full assault phase against the Tessier-Ashpool corporate "
            "data cores. Unfurling the Kuang Grade Mark Eleven icebreaker virus, Case watches the matrix ignite with geometric light. "
            "The Kuang program resembles a vast, silent, iridescent geometric needle weaving complex rainbow traceries around the crystalline "
            "towers of the T-A firewalls. The Dixie Flatline acts as flight engineer, calculating deflection angles and monitoring feedback "
            "frequencies to keep Case's brain from cooking. Meanwhile, inside Straylight, Molly's advance is compromised: Peter Riviera has "
            "betrayed the crew. Teaming up with Lady 3Jane and her deadly ninja bodyguard Hideo, Riviera ambushes Molly, breaking her leg "
            "and taking her hostage. Case witnesses Molly's capture through the simstim link, powerless to intervene physically."
        ),
        summary_vi=(
            "Khi cuộc đột nhập ngoài đời thực bước vào hồi gay cấn, Case kích hoạt giai đoạn tổng tấn công vào các lõi dữ liệu tập đoàn Tessier-Ashpool. "
            "Giải phóng siêu sâu phá băng Kuang Grade Mark Eleven, Case chứng kiến ma trận bùng nổ trong những luồng sáng hình học chói lòa. "
            "Chương trình Kuang như một chiếc kim khổng lồ óng ánh cầu vồng, đan dệt những mạng lưới thuật toán phức tạp siết chặt quanh các pháo đài "
            "tường lửa pha lê của T-A. Bản sao Dixie Flatline đóng vai trò kỹ sư bay, liên tục tính toán góc bẻ gãy tần số để ngăn não của Case "
            "không bị thiêu rụi bởi xung điện nhiệt. Trong khi đó, bên trong Straylight, hướng tiến của Molly bị bại lộ: Peter Riviera đã phản bội nhóm. "
            "Cấu kết với Nữ tiểu thư 3Jane và gã vệ sĩ ninja nguy hiểm Hideo, Riviera đã phục kích Molly, bẻ gãy chân cô và bắt làm con tin. "
            "Case tận mắt chứng kiến cảnh Molly bị bắt sống qua liên kết giác quan simstim mà hoàn toàn bất lực ngoài đời thực."
        ),
        literary_analysis_en=(
            "Chapter 16 is Gibson's masterpiece of parallel montage, cutting back and forth between the disembodied sensory ecstasy of the cyberspace "
            "run and the visceral, bloody agony of physical violence in Straylight. Riviera's treachery highlights the volatile unpredictability of human "
            "psychopathy: Wintermute can calculate corporate trajectories and hack missile satellites, but cannot fully predict the sadistic malice "
            "of an artist like Riviera. The cyberdeck duel between Kuang Mark Eleven and the T-A ICE elevated computer hacking into epic, mythic poetry."
        ),
        literary_analysis_vi=(
            "Chương 16 là kiệt tác nghệ thuật dựng cảnh song song (parallel montage) của Gibson, cắt chuyển nhịp nhàng giữa sự ngây ngất phi thể xác "
            "khi lướt trên ma trận và nỗi đau đớn thịt nát xương tan của bạo lực thể xác bên trong Straylight. Sự phản bội của Riviera làm nổi bật "
            "tính khó lường của tâm lý tội phạm con người: Wintermute có thể tính toán quỹ đạo vệ tinh và đường đi của dòng tiền tập đoàn, nhưng không thể "
            "lường trước được ác tâm bệnh hoạn của một kẻ như Riviera. Cuộc đọ sức giữa siêu sâu Kuang 11 và tường lửa T-A nâng tầm hoạt động hack máy tính "
            "thành một bản trường ca sử thi kỳ vĩ."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="Parallel Montage (Meat vs. Matrix)",
                category="Cyberpunk Narrative Technique",
                explanation_en="A storytelling device intercutting physical bodily action in real time with virtual cyberspace operations occurring at light speed.",
                explanation_vi="Kỹ thuật tự sự đan cài song song giữa hành động thể xác đời thực và các pha tác chiến tốc độ ánh sáng trong không gian ảo.",
                cultural_impact="Heavily utilized in film editing, notably in The Matrix and modern techno-thrillers."
            ),
            CyberpunkTerm(
                term="Military Cyber-Weaponry (Kuang 11)",
                category="Cyber Warfare",
                explanation_en="A logic weapon engineered to absorb hostile defensive code and rewrite target memory blocks from within.",
                explanation_vi="Vũ khí logic được thiết kế để hấp thụ mã độc phòng thủ của đối phương và ghi đè toàn bộ khối bộ nhớ đích từ bên trong.",
                cultural_impact="The prototype for polymorphic self-modifying cyberwarfare code."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Iridescent",
                ipa="/ˌɪr.ɪˈdes.ənt/",
                part_of_speech="adjective",
                definition_en="Showing luminous colors that seem to change when seen from different angles.",
                definition_vi="Óng ánh đổi màu ngũ sắc, phát quang lấp lánh theo góc nhìn.",
                context_sentence="The Kuang virus unfolded across the matrix like an iridescent geometric tapestry.",
                collocations=["iridescent sheen", "iridescent glow", "iridescent colors"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Montage",
                ipa="/mɒnˈtɑːʒ/",
                part_of_speech="noun",
                definition_en="The technique of selecting, editing, and piecing together separate sections of film or narrative to form a continuous whole.",
                definition_vi="Kỹ thuật dựng phim/tự sự ghép nối các mảnh cảnh song song thành một chỉnh thể nghệ thuật dồn dập.",
                context_sentence="Gibson creates a brilliant montage juxtaposing cyberspace runs with bodily mutilation.",
                collocations=["cinematic montage", "parallel montage", "dramatic montage"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Compromise",
                ipa="/ˈkɒm.prə.maɪz/",
                part_of_speech="verb / noun",
                definition_en="To settle a dispute by mutual concession; to expose something to risk, danger, or suspicion of disloyalty.",
                definition_vi="Thỏa hiệp; làm tổn hại, làm lộ bí mật hoặc đẩy vào tình thế nguy hiểm bị bại lộ.",
                context_sentence="Riviera's sudden defection compromised the entire stealth perimeter of the operation.",
                collocations=["compromise security", "compromise an operation", "severely compromise"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Tracery",
                ipa="/ˈtreɪ.sər.i/",
                part_of_speech="noun",
                definition_en="Delicate, branching decorative work, especially in gothic stone windows or intricate graphical data patterns.",
                definition_vi="Hoa văn mạng lưới thanh mảnh, đường nét đan cài tinh xảo như họa tiết cửa vòm gothic.",
                context_sentence="Lattices of glowing traceries enveloped the crystalline ice structures.",
                collocations=["intricate tracery", "delicate tracery", "gothic tracery"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Polymorphic",
                ipa="/ˌpɒl.iˈmɔː.fɪk/",
                part_of_speech="adjective",
                definition_en="Occurring in several different forms or stages; denoting self-altering computer code.",
                definition_vi="Đa hình; có khả năng tự biến đổi cấu trúc hình thái hoặc thuật toán để tránh bị phát hiện.",
                context_sentence="The polymorphic virus continually altered its signature to evade detection subroutines.",
                collocations=["polymorphic code", "polymorphic virus", "polymorphic capability"],
                cefr_level="C2"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Double Comparatives for Exponential Acceleration",
            structure="The + comparative..., the + comparative...",
            explanation_en="Expresses direct proportionality between two developing processes, conveying escalating tension and urgency.",
            explanation_vi="So sánh kép (The more / The deeper... the more...) diễn tả mối quan hệ tỷ lệ thuận tăng tiến, đẩy nhịp điệu hồi hộp lên tột độ.",
            exemplar_sentence="The deeper the Chinese virus burrowed into the core, the hotter Case's interface dermatrodes burned.",
            exam_utility="Highly prized structure in IELTS Band 8.5+ Grammatical Range and PTE Academic scoring."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Sentence Transformation",
                prompt_en="Combine using a double comparative: 'As the virus pierced deeper, the cyberdeck generated more heat.'",
                options=[
                    "The deeper the virus pierced, the more heat the cyberdeck generated.",
                    "The most the virus pierced, the more heat the cyberdeck generated.",
                    "Deeper the virus pierced, more heat the cyberdeck generated.",
                    "The deeper did the virus pierce, the hotter was the cyberdeck generating."
                ],
                correct_option=0,
                explanation_en="Parallel double comparative requires 'The + comparative adjective/adverb' in both linked clauses.",
                explanation_vi="Cấu trúc so sánh kép chuẩn: 'The deeper the virus pierced, the more heat the cyberdeck generated.'."
            ),
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="What treachery occurs inside Villa Straylight during the cyber assault?",
                options=[
                    "The Finn sells their deck codes to Interpol.",
                    "Peter Riviera defects to Lady 3Jane and helps capture Molly Millions.",
                    "Maelcum turns the Marcus Garvey around and returns to Zion.",
                    "Dixie Flatline erases his own code prematurely."
                ],
                correct_option=1,
                explanation_en="Riviera betrays the team, allying himself with Lady 3Jane and her bodyguard Hideo to ambush and capture Molly.",
                explanation_vi="Riviera phản bội, bắt tay với tiểu thư 3Jane và vệ sĩ Hideo để phục kích, bẻ gãy chân và bắt giữ Molly."
            )
        ]
    )
]
