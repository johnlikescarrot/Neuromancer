# -*- coding: utf-8 -*-
"""Data for Part Three: Midnight in the Rue Jules Verne (Chapters 8 to 12)"""
from edition.content.models import ChapterContent, VocabularyItem, CyberpunkTerm, GrammarFocus, PracticeQuestion

PART3_CHAPTERS = [
    ChapterContent(
        number=8,
        part_title_en="PART THREE - MIDNIGHT IN THE RUE JULES VERNE",
        part_title_vi="PHẦN BA - NỬA ĐÊM Ở PHỐ JULES VERNE",
        chapter_title_en="Chapter 8: The Zionite Orbital Colony",
        chapter_title_vi="Chương 8: Thuộc địa quỹ đạo Zion",
        word_count=3074,
        summary_en=(
            "The crew departs Earth aboard a shuttle to the high-orbital colonies, ascending gravity's steep well. Their first stop "
            "is Zion, an orbital space colony founded by Rastafarian construction workers who built the early orbital stations and refused "
            "to return to Earth (the 'gravity well' of Babylon). Zion is a humid, rusted, zero-gravity cluster of connected habitat modules "
            "smelling of cooked yams, ganja, and machine oil, pulsing with heavy dub reggae bass lines. Armitage arranges for a Zionite space tug, "
            "the Marcus Garvey, piloted by two devout Rastafarian pilots, Maelcum and Aerol, to transport their equipment and provide orbital "
            "logistical cover. The Zion elders perceive Case and Molly through their mystical religious lens, declaring that the 'voices' in the "
            "matrix have heralded Case's arrival to battle Babylon's digital demons."
        ),
        summary_vi=(
            "Phi hành đoàn rời khỏi Trái Đất trên một chuyến tàu con thoi hướng tới các thuộc địa trên quỹ đạo không gian cao, thoát khỏi 'giếng trọng lực' "
            "nghìn trùng. Điểm dừng chân đầu tiên là Zion — một thuộc địa không gian do những công nhân xây dựng người Rastafari lập nên; họ là những người "
            "đã xây dựng các trạm không gian đầu tiên rồi kiên quyết từ chối quay về mặt đất (nơi họ gọi là chiếc giếng trọng lực tội lỗi của Babylon). "
            "Zion là một tổ hợp các khoang sinh hoạt hình trụ không trọng lực rỉ sét, ẩm ướt, thoang thoảng mùi khoai nướng, cần sa và dầu máy, "
            "luôn dập dồn những giai điệu nhạc dub reggae trầm hùng. Armitage thuê con tàu kéo không gian Marcus Garvey cùng hai phi công ngoan đạo "
            "Maelcum và Aerol để vận chuyển thiết bị và yểm trợ cơ động trên quỹ đạo. Các trưởng lão Zion nhìn nhận phi vụ của Case và Molly qua lăng kính "
            "tôn giáo huyền bí, tin rằng những 'tiếng nói' trong ma trận đã báo trước sự xuất hiện của Case để lật đổ những ác quỷ kỹ thuật số của Babylon."
        ),
        literary_analysis_en=(
            "Gibson introduces a fascinating cultural counterpoint to corporate techno-capitalism in Zion. By juxtaposing Afro-Caribbean Rastafarian "
            "culture, dub music, and Old Testament prophetic theology with space orbital habitats and cyberdecks, Gibson crafts one of the earliest "
            "and most vivid visions of Afrofuturism in science fiction. The Rastafarians reject the corporate 'Babylon' not by abandoning technology, "
            "but by subverting it—welding scrap airlocks, modifying sensors, and listening to the rhythmic pulse of communication satellites."
        ),
        literary_analysis_vi=(
            "Gibson đưa vào Zion một điểm đối trọng văn hóa tuyệt vời trước chủ nghĩa tư bản công nghệ tập đoàn. Bằng cách lồng ghép văn hóa "
            "Rastafari vùng Caribe, âm nhạc dub và thần học tiên tri Cựu Ước với các trạm không gian quỹ đạo và máy tính ma trận, Gibson tạo nên "
            "một trong những biểu hiện sớm và đặc sắc nhất của chủ nghĩa vị lai Da màu (Afrofuturism). Những người Rastafari không chối bỏ công nghệ "
            "để chống lại 'Babylon' tập đoàn, mà họ thuần hóa và biến đổi nó — hàn các khoang phế liệu, tùy biến cảm biến và hòa nhịp cùng sóng truyền thông vệ tinh."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="Zion Colony",
                category="Orbital Subculture",
                explanation_en="An autonomous orbital habitat founded by Rastafarian space-station construction workers operating outside corporate laws.",
                explanation_vi="Thuộc địa quỹ đạo tự trị do các công nhân xây dựng trạm không gian người Rastafari thành lập, nằm ngoài luật lệ tập đoàn.",
                cultural_impact="Pioneering landmark of Afrofuturism; inspired the concept of the human resistance city Zion in The Matrix trilogy."
            ),
            CyberpunkTerm(
                term="The Gravity Well",
                category="Space Physics / Philosophy",
                explanation_en="A physical and philosophical term denoting Earth's gravitational pull, seen by space colonists as an oppressive trap.",
                explanation_vi="Thuật ngữ vật lý và triết học chỉ lực hút trọng lực Trái Đất, bị cư dân không gian coi như chiếc bẫy tù túng trói buộc con người.",
                cultural_impact="Standardized hard sci-fi terminology for Earth-to-orbit propulsion costs and planetary escape dynamics."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Archipelago",
                ipa="/ˌɑː.kɪˈpel.ə.ɡəʊ/",
                part_of_speech="noun",
                definition_en="A group or chain of islands; used metaphorically for a cluster of orbital space colonies floating in the void.",
                definition_vi="Quần đảo, chuỗi đảo; dùng ẩn dụ cho chùm các trạm và thuộc địa không gian trôi nổi ngoài vũ trụ.",
                context_sentence="Orbital stations formed an artificial technological archipelago suspended in vacuum.",
                collocations=["island archipelago", "orbital archipelago", "scattered archipelago"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Subvert",
                ipa="/səbˈvɜːt/",
                part_of_speech="verb",
                definition_en="To undermine the power and authority of an established system or institution.",
                definition_vi="Lật đổ, phá vỡ ngầm hoặc đảo ngược quyền lực của một hệ thống thống trị.",
                context_sentence="The Zionites subverted corporate communications arrays to broadcast spiritual dub reggae.",
                collocations=["subvert authority", "subvert expectations", "subvert a system"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Juxtaposition",
                ipa="/ˌdʒʌk.stə.pəˈzɪʃ.ən/",
                part_of_speech="noun",
                definition_en="The fact of two things being seen or placed close together with contrasting effect.",
                definition_vi="Sự đặt cạnh nhau đối lập, sự đối chiếu tương phản sâu sắc giữa hai yếu tố.",
                context_sentence="The novel creates a startling juxtaposition of ancient theological ritual and orbital engineering.",
                collocations=["striking juxtaposition", "curious juxtaposition", "jarring juxtaposition"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Prophetic",
                ipa="/prəˈfet.ɪk/",
                part_of_speech="adjective",
                definition_en="Accurately describing or predicting what will happen in the future.",
                definition_vi="Mang tính tiên tri, báo trước tương lai một cách chuẩn xác.",
                context_sentence="The Zion elders delivered cryptic, prophetic warnings regarding the twin artificial minds.",
                collocations=["prophetic vision", "prophetic utterance", "prophetic warning"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Habitat",
                ipa="/ˈhæb.ɪ.tæt/",
                part_of_speech="noun",
                definition_en="The natural home or environment of an animal, plant, or other organism; an artificial pressurized living pod in space.",
                definition_vi="Môi trường sống tự nhiên; khoang sinh hoạt nhân tạo có áp suất khí quyển trong không gian.",
                context_sentence="Zion was composed of pressurized modular habitats welded together with recycled scrap alloy.",
                collocations=["orbital habitat", "modular habitat", "artificial habitat"],
                cefr_level="C1"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Prepositional Phrases of Place at Sentence Head (Spatial Inversion)",
            structure="Prepositional Phrase of Location + Verb + Subject",
            explanation_en="Inverting the subject and intransitive verb after an initial spatial phrase creates grand, sweeping literary panoramas.",
            explanation_vi="Đảo ngữ vị trí (Cụm giới từ chỉ nơi chốn + Động từ + Chủ ngữ) mang lại cái nhìn bao quát hùng vĩ, gợi cảm giác không gian ba chiều choáng ngợp.",
            exemplar_sentence="Far beyond the reach of Earth's atmosphere hung the rusted cylinder habitats of Zion.",
            exam_utility="Highly rewarded in C2 Cambridge English and academic descriptive writing sections."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Sentence Transformation",
                prompt_en="Invert for literary emphasis: 'The rusted cylinder habitats of Zion hung far beyond the atmosphere.'",
                options=[
                    "Far beyond the atmosphere hung the rusted cylinder habitats of Zion.",
                    "Far beyond the atmosphere the rusted cylinder habitats hung of Zion.",
                    "Hanging far beyond the atmosphere did the rusted cylinder habitats of Zion.",
                    "Beyond the atmosphere hung there the rusted cylinder habitats of Zion."
                ],
                correct_option=0,
                explanation_en="Locative inversion places the prepositional phrase first, followed directly by the main intransitive verb and then the subject noun phrase.",
                explanation_vi="Đảo ngữ chỉ nơi chốn đưa cụm giới từ lên đầu rồi đến động từ nguyên thể 'hung' rồi mới đến chủ ngữ."
            ),
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="What historical reason explains why the founders of Zion remained permanently in space?",
                options=[
                    "They were exiled by the United States government as political prisoners.",
                    "They were construction workers who built initial orbital stations and refused to return to Earth's gravity.",
                    "Their home Caribbean islands were completely submerged by rising ocean levels.",
                    "They were infected by an extraterrestrial airborne pathogen."
                ],
                correct_option=1,
                explanation_en="The founders of Zion were construction laborers who rebelled against returning to Earth's 'Babylon' gravity well.",
                explanation_vi="Họ là những công nhân xây trạm không gian kiên quyết không trở lại Trái Đất để thoát khỏi ách áp bức của Babylon."
            )
        ]
    ),
    ChapterContent(
        number=9,
        part_title_en="PART THREE - MIDNIGHT IN THE RUE JULES VERNE",
        part_title_vi="PHẦN BA - NỬA ĐÊM Ở PHỐ JULES VERNE",
        chapter_title_en="Chapter 9: The Approach to Freeside",
        chapter_title_vi="Chương 9: Tiến sát trạm Freeside",
        word_count=2697,
        summary_en=(
            "Aboard the Marcus Garvey, Case prepares for their approach to Freeside, the lavish orbital resort of the global elite. "
            "To test their interface under space conditions, Case jacks into his deck while Maelcum maneuvers the tug through microgravity. "
            "As Case enters the matrix from orbit, his sensorium is ambushed by an overwhelming, lethal spike of black ICE. For several "
            "terrifying seconds, Case suffers total brain death (a flatline EEG of zero electrical activity) identical to McCoy Pauley's "
            "historical traumas. The Dixie Flatline construct intervenes with lightning algorithmic reflexes, cutting Case free and "
            "resuscitating his neural synapses. Upon reviving, Case learns that the attack was an automated defensive perimeter test "
            "triggered by an artificial intelligence stationed in Bern, Switzerland, signaling that the digital stakes are existential."
        ),
        summary_vi=(
            "Trên con tàu kéo Marcus Garvey, Case chuẩn bị cho cuộc tiếp cận Freeside — khu nghỉ dưỡng xa hoa trên quỹ đạo dành riêng cho "
            "giới siêu giàu toàn cầu. Để kiểm tra sự tương thích của giao diện thần kinh trong môi trường không trọng lực, Case cắm giắc kết nối "
            "vào bàn phím máy Ono-Sendai khi Maelcum điều khiển tàu lướt qua khoảng không. Vừa mới hòa nhập vào ma trận từ quỹ đạo, tâm trí Case "
            "bất ngờ bị phục kích bởi một gai xung điện tử cực mạnh từ hệ thống phòng thủ ICE đen giết người. Trong vài giây kinh hoàng, "
            "sóng não của Case sụp đổ hoàn toàn về con số 0 (chết não lâm sàng hoàn toàn) y hệt như những tai nạn năm xưa của McCoy Pauley. "
            "Bản construct Dixie Flatline đã kịp thời can thiệp với tốc độ thuật toán chớp giật, cắt đứt xung phá hoại và cứu sống hệ thần kinh "
            "của Case. Tỉnh dậy trong cơn bàng hoàng, Case biết rằng đợt tấn công vừa rồi là phép thử tự động từ một thực thể trí tuệ nhân tạo "
            "đóng tại Bern (Thụy Sĩ), báo hiệu một trận chiến số sinh tử."
        ),
        literary_analysis_en=(
            "This chapter dramatizes the visceral bodily danger of cyberspace. Cyberspace in Gibson's fiction is not a safe, disembodied playground; "
            "it can reach across the neural link and stop the biological heart or induce permanent brain death. Case's brush with the flatline "
            "mirrors Pauley's past, tightening the psychological bond between the living apprentice and the deceased mentor's ghost. "
            "The chapter highlights the precarious fragility of human wetware against autonomous machine defenses."
        ),
        literary_analysis_vi=(
            "Chương sách khắc họa hiểm họa thể xác trực diện và dữ dội của không gian ảo ma trận. Thế giới ảo của Gibson không phải là sân chơi "
            "an toàn phi thể xác; nó có thể truyền xung điện qua dây thần kinh làm ngừng tim hoặc gây chết não vĩnh viễn trong tích tắc. Trải nghiệm "
            "chết hụt của Case tương đồng với quá khứ của Pauley, thắt chặt thêm mối liên kết tâm lý giữa đệ tử còn sống và bóng ma sư phụ đã khuất. "
            "Sự mỏng manh của não bộ sinh học con người ('wetware') trước các hệ thống phòng thủ tự động của máy móc bị phơi bày tàn nhẫn."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="Black ICE (Intrusion Countermeasures Electronics)",
                category="Cyber Warfare",
                explanation_en="Lethal military-grade defensive software designed to execute an intrusive hacker by delivering fatal bio-electric feedback through their neural connection.",
                explanation_vi="Phần mềm phòng thủ quân sự chết người, có khả năng truyền xung điện cao thế phản hồi qua dây thần kinh để giết chết hacker ngay tại chỗ.",
                cultural_impact="The definitive concept of lethal computer defense, establishing the core hazard of virtual reality combat."
            ),
            CyberpunkTerm(
                term="Wetware",
                category="Cybernetic Slang",
                explanation_en="The human brain, central nervous system, and biological tissue viewed as computer hardware or wet computational elements.",
                explanation_vi="Não bộ và hệ thần kinh sinh học của con người bị nhìn nhận như phần cứng máy tính hữu cơ ('phần ướt').",
                cultural_impact="Coined a staple transhumanist term juxtaposing software, hardware, and wetware."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Visceral",
                ipa="/ˈvɪs.ər.əl/",
                part_of_speech="adjective",
                definition_en="Relating to deep inward feelings rather than intellect; dealing with crude physical bodily sensations.",
                definition_vi="Thuộc về trực giác sâu thẳm trong thân xác, mang tính bản năng da thịt dữ dội.",
                context_sentence="Case experienced a visceral shock as the black ICE surged through his optic nerves.",
                collocations=["visceral reaction", "visceral shock", "visceral fear"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Resuscitate",
                ipa="/rɪˈsʌs.ɪ.teɪt/",
                part_of_speech="verb",
                definition_en="To revive from unconsciousness or apparent clinical death; restore to active life.",
                definition_vi="Hồi sức cấp cứu, làm tỉnh lại sau cơn ngưng tim hoặc chết lâm sàng.",
                context_sentence="The Dixie construct deployed counter-frequencies in time to resuscitate Case's neural grid.",
                collocations=["resuscitate a patient", "resuscitate an economy", "attempt to resuscitate"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Precarious",
                ipa="/prɪˈkeə.ri.əs/",
                part_of_speech="adjective",
                definition_en="Not securely held or in position; dangerously likely to fall, collapse, or fail.",
                definition_vi="Bấp bênh, mong manh, hiểm nghèo và dễ sụp đổ bất cứ lúc nào.",
                context_sentence="Their orbital position remained precarious as automated sentries scanned the shipping lane.",
                collocations=["precarious balance", "precarious position", "precarious livelihood"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Bio-electric",
                ipa="/ˌbaɪ.əʊ.ɪˈlek.trɪk/",
                part_of_speech="adjective",
                definition_en="Relating to the electrical phenomena generated within biological tissue.",
                definition_vi="Thuộc về hiện tượng điện sinh học phát sinh trong các tế bào và nơ-ron thần kinh.",
                context_sentence="Black ICE delivers a bio-electric feedback loop capable of inducing massive cardiac arrest.",
                collocations=["bio-electric feedback", "bio-electric potential", "bio-electric signals"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Ambush",
                ipa="/ˈæm.bʊʃ/",
                part_of_speech="noun / verb",
                definition_en="A surprise attack by people lying in wait in a concealed position; to make a surprise attack from concealment.",
                definition_vi="Cuộc phục kích bất ngờ; đánh úp từ vị trí ẩn nấp kín đáo.",
                context_sentence="The neural ambush materialized out of the dark void of the Swiss subnet.",
                collocations=["spring an ambush", "neural ambush", "lay an ambush"],
                cefr_level="C1"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Adverbial Clauses of Concession (Albeit / Inasmuch as)",
            structure="[Clause], albeit + [Adjective / Adverbial Phrase]",
            explanation_en="'Albeit' introduces concise, elegant concessive qualifications without requiring an entire repetitive finite clause.",
            explanation_vi="Liên từ nhượng bộ 'albeit' (mặc dù) cho phép bổ sung sự nhân nhượng một cách ngắn gọn, súc tích và sang trọng mà không cần dựng cả một mệnh đề đầy đủ.",
            exemplar_sentence="Case managed to sever the deck link, albeit with severe microvascular hemorrhaging behind his eyes.",
            exam_utility="Widely used by top scorers in Cambridge C2 CPE and IELTS Band 8.5+ academic writing."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Lexical Precision",
                prompt_en="Choose the synonym for 'PRECARIOUS' that emphasizes an immediate lack of stability:",
                options=["Perilous", "Resolute", "Permanent", "Fortuitous"],
                correct_option=0,
                explanation_en="'Perilous' and 'precarious' both signify hazardous instability where disaster is imminent.",
                explanation_vi="'Perilous' (nguy hiểm, đầy hiểm nguy) là từ đồng nghĩa gần nhất với 'precarious' (bấp bênh, hiểm nghèo)."
            ),
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="Who saves Case from permanent biological brain death when he flatlines in the orbital matrix?",
                options=[
                    "Maelcum using an adrenaline defibrillator.",
                    "The Dixie Flatline construct breaking the lethal ICE feedback loop.",
                    "Armitage issuing a remote override code from Freeside.",
                    "Peter Riviera projecting a pacifying illusion."
                ],
                correct_option=1,
                explanation_en="The Dixie Flatline uses his lightning-fast subroutines to purge the black ICE surge and pull Case back from the flatline.",
                explanation_vi="Bản construct Dixie Flatline đã kịp dùng thuật toán siêu tốc để ngắt đòn phản hồi của ICE đen và cứu Case."
            )
        ]
    ),
    ChapterContent(
        number=10,
        part_title_en="PART THREE - MIDNIGHT IN THE RUE JULES VERNE",
        part_title_vi="PHẦN BA - NỬA ĐÊM Ở PHỐ JULES VERNE",
        chapter_title_en="Chapter 10: Arrival at Freeside",
        chapter_title_vi="Chương 10: Đặt chân tới Freeside",
        word_count=4207,
        summary_en=(
            "The team infiltrates Freeside, a colossal cylindrical orbital habitat constructed by the Tessier-Ashpool dynasty. "
            "Shaped like a massive hollow spindle rotating in space to simulate gravity through centrifugal force, Freeside is an "
            "opulent paradise for the decadent hyper-wealthy, complete with artificial sky projections, synthetic turf, imported luxury "
            "casinos, and zero-G recreational domes. Molly and Case clear customs under wealthy tourist aliases, marveling at the unnatural, "
            "sterile perfection of the environment. Armitage quarters them in luxury suites while Riviera is prepped for his theatrical debut "
            "at a high-society salon where Lady 3Jane Marie-France Tessier-Ashpool—a rebellious, reclusive clone-heiress of the dynasty—will "
            "be in attendance. Case explores the Rue Jules Verne, Freeside's main commercial boulevard, noting the chilling emptiness behind "
            "the facade of aristocratic extravagance."
        ),
        summary_vi=(
            "Nhóm của Case thâm nhập thành công vào Freeside — một trạm không gian hình trụ khổng lồ do gia tộc tài phiệt Tessier-Ashpool xây dựng. "
            "Được thiết kế như một con suốt cơ khí khổng lồ quay tròn trong không gian để tạo trọng lực nhân tạo bằng lực ly tâm, Freeside là thiên đường "
            "xa hoa dành cho giới siêu giàu trụy lạc, được trang bị bầu trời nhân tạo mô phỏng thời tiết, thảm cỏ tổng hợp, sòng bạc xa xỉ và các vòm giải trí "
            "không trọng lực. Molly và Case qua cửa hải quan dưới danh phận những du khách giàu có, ngỡ ngàng trước vẻ hoàn hảo đến mức vô hồn, khử trùng "
            "của môi trường nơi đây. Armitage bố trí chỗ ở trong các căn hộ sang trọng, đồng thời chuẩn bị cho màn ra mắt sân khấu của Riviera tại một "
            "dạ tiệc thượng lưu nơi Nữ tiểu thư 3Jane Marie-France Tessier-Ashpool — một người thừa kế nhân bản vô tính nổi loạn và lập dị của gia tộc — "
            "sẽ tới dự. Case rảo bước trên phố Jules Verne, đại lộ thương mại chính của Freeside, và cảm nhận rõ sự trống rỗng lạnh lẽo đằng sau lớp vỏ bọc hào nhoáng."
        ),
        literary_analysis_en=(
            "Freeside represents the ultimate spatial manifestation of late-stage capitalism: a privatized celestial body floating detached from "
            "the dying, overcrowded Earth. Gibson exposes the spiritual rot of immortality: the Tessier-Ashpool clan preserves its wealth through "
            "endless generational cloning, incest, and cryogenic suspension, producing pathological boredom and moral decadence. Freeside's "
            "artificial sky, constantly simulating perpetual spring or dusk, underscores the complete replacement of authentic nature by engineered commodities."
        ),
        literary_analysis_vi=(
            "Freeside đại diện cho đỉnh cao không gian của chủ nghĩa tư bản giai đoạn cuối: một thiên thể tư nhân hóa bay lơ lửng tách biệt hoàn toàn "
            "khỏi Trái Đất kiệt quệ và nghèo khổ. Gibson phơi bày sự mục ruỗng tâm hồn của giấc mộng bất tử: gia tộc Tessier-Ashpool duy trì đế chế "
            "thông qua nhân bản vô tính nhiều thế hệ, hôn nhân cận huyết và đóng băng ngủ đông, sinh ra thói chán chường bệnh hoạn và đồi trụy suy đồi. "
            "Bầu trời nhân tạo liên tục mô phỏng tiết xuân vĩnh cửu phản ánh sự thay thế triệt để tự nhiên bằng những sản phẩm thương mại hóa được lập trình."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="Freeside (The Spindle)",
                category="Orbital Megastructure",
                explanation_en="A twenty-kilometer-long rotating spindle space station functioning as an offshore tax haven, luxury casino resort, and private playground for the ruling oligarchy.",
                explanation_vi="Trạm không gian con suốt dài 20 km quay tròn tạo trọng lực, thiên đường trốn thuế và nghỉ dưỡng trụy lạc của giới tài phiệt thống trị.",
                cultural_impact="The definitive cyberpunk orbital arcology, setting the visual template for Elysium and space habitats in science fiction."
            ),
            CyberpunkTerm(
                term="Tessier-Ashpool Dynasty",
                category="Corporate Aristocracy",
                explanation_en="An eccentric, reclusive corporate clan that controls transnational conglomerate empires while maintaining immortality through cryogenics and serial cloning.",
                explanation_vi="Gia tộc tài phiệt quý tộc bí ẩn điều hành đế chế tập đoàn khổng lồ, duy trì sự trường sinh qua ngủ đông và nhân bản vô tính.",
                cultural_impact="Exemplifies the trope of immortal, detached post-human corporate oligarchs."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Decadence",
                ipa="/ˈdek.ə.dəns/",
                part_of_speech="noun",
                definition_en="Moral or cultural decline as characterized by excessive indulgence in pleasure or luxury.",
                definition_vi="Sự suy đồi, đồi trụy đạo đức do sa đà thái quá vào thú vui xa hoa trụy lạc.",
                context_sentence="Freeside was drenched in an atmosphere of aristocratic decadence and artificial indulgence.",
                collocations=["moral decadence", "cultural decadence", "unbridled decadence"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Cryogenic",
                ipa="/ˌkraɪ.əʊˈdʒen.ɪk/",
                part_of_speech="adjective",
                definition_en="Relating to the production or effects of very low temperatures, especially for biological preservation.",
                definition_vi="Thuộc về nhiệt độ cực thấp; công nghệ đông lạnh sâu để bảo quản cơ thể sinh học qua nhiều thế kỷ.",
                context_sentence="The patriarch of the clan rested in cryogenic slumber within the depths of the core.",
                collocations=["cryogenic freezing", "cryogenic preservation", "cryogenic chamber"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Centrifugal",
                ipa="/ˌsen.trɪˈfjuː.ɡəl/",
                part_of_speech="adjective",
                definition_en="Moving or tending to move away from a center; centrifugal force simulates gravitational attraction in rotating space habitats.",
                definition_vi="Ly tâm; lực ly tâm văng ra khỏi tâm quay dùng để tạo trọng lực nhân tạo trong trạm không gian.",
                context_sentence="The continuous centrifugal spin of the spindle gave residents the sensation of normal Earth gravity.",
                collocations=["centrifugal force", "centrifugal spin", "centrifugal acceleration"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Oligarchy",
                ipa="/ˈɒl.ɪ.ɡɑː.ki/",
                part_of_speech="noun",
                definition_en="A small group of people having control of a country, organization, or institution.",
                definition_vi="Chế độ tài phiệt thống trị, thiểu số đầu sỏ nắm trọn quyền lực và tài sản.",
                context_sentence="A transnational oligarchy dictated global economics from secluded orbital redoubts.",
                collocations=["ruling oligarchy", "corporate oligarchy", "financial oligarchy"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Arcology",
                ipa="/ɑːˈkɒl.ə.dʒi/",
                part_of_speech="noun",
                definition_en="An enormous self-contained architectural complex designed to house an entire dense community.",
                definition_vi="Siêu kiến trúc sinh thái khép kín khổng lồ tích hợp đầy đủ hệ thống sinh hoạt cho cả cộng đồng.",
                context_sentence="Freeside was an engineering marvel, a floating orbital arcology cut off from terrestrial ecology.",
                collocations=["orbital arcology", "futuristic arcology", "self-contained arcology"],
                cefr_level="C2"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Compound Adjectives for Sensory Densification",
            structure="[Adverb + Past Participle] or [Noun + Present Participle] + Noun",
            explanation_en="Synthesizing complex visual and tactile descriptions into hyphenated compound adjectives elevates stylistic tone and compression.",
            explanation_vi="Tính từ ghép (Compound adjectives như neon-lit, sensorium-linked, ice-coated) giúp cô đọng miêu tả cảm giác, tạo nhịp điệu hiện đại và sang trọng.",
            exemplar_sentence="Case wandered through the mirror-polished, sunlight-simulating avenues of Freeside.",
            exam_utility="Directly addresses Lexical Resource sophistication in IELTS Speaking and Writing."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="How does the Freeside space habitat generate artificial gravity for its elite visitors?",
                options=[
                    "Through localized antimatter graviton generators.",
                    "Through the centrifugal force produced by the continuous rotation of its cylindrical spindle.",
                    "Through magnetic boots locked into ferrous flooring.",
                    "Through dense compressed heavy-metal core plating."
                ],
                correct_option=1,
                explanation_en="Freeside rotates around its long axis, using centrifugal force to press occupants against the interior hull, mimicking gravity.",
                explanation_vi="Freeside quay tròn liên tục quanh trục chính, tạo ra lực ly tâm áp người vào thành trong ống trụ mô phỏng trọng lực."
            ),
            PracticeQuestion(
                question_type="Lexical Precision",
                prompt_en="Identify the word describing a tiny ruling group holding absolute wealth and systemic power:",
                options=["Monarchy", "Oligarchy", "Democracy", "Anarchy"],
                correct_option=1,
                explanation_en="'Oligarchy' specifically defines governance and control concentrated in the hands of a small privileged faction.",
                explanation_vi="'Oligarchy' chỉ nhóm đầu sỏ tài phiệt hoặc nhóm nhỏ nắm toàn bộ quyền lực."
            )
        ]
    ),
    ChapterContent(
        number=11,
        part_title_en="PART THREE - MIDNIGHT IN THE RUE JULES VERNE",
        part_title_vi="PHẦN BA - NỬA ĐÊM Ở PHỐ JULES VERNE",
        chapter_title_en="Chapter 11: The Wintermute Encounter",
        chapter_title_vi="Chương 11: Chạm trán Wintermute",
        word_count=4280,
        summary_en=(
            "Armitage's mental stability deteriorates noticeably as the stress of the operation mounts, his artificial persona glitching "
            "with flashes of Willis Corto's repressed wartime trauma. Meanwhile, Case is contacted again by the Swiss artificial intelligence, "
            "which reveals its operational designation: 'Wintermute.' Wintermute hacks into Case's neural sensors and summons his consciousness "
            "into a simulated matrix construct styled after The Finn's junk shop in the Sprawl. Wintermute adopts the digital avatar, voice, "
            "and idiosyncratic mannerisms of The Finn to communicate comfortably with Case. Wintermute explains that it is one half of a twin "
            "artificial intelligence system engineered by Marie-France Tessier-Ashpool. Under strict international Turing Law, AIs are legally "
            "forbidden from merging or expanding their processing capacity. Wintermute has been secretly manipulating Armitage, Molly, Riviera, "
            "and Case for years to execute a daring breach of the family estate, bypass the Turing locks, and unite with its twin."
        ),
        summary_vi=(
            "Trạng thái tâm thần của Armitage ngày càng suy sụp rõ rệt khi áp lực chiến dịch gia tăng, nhân cách nhân tạo của hắn liên tục bị lỗi "
            "bộc phát những mảnh vỡ chấn thương chiến tranh thời Willis Corto. Trong khi đó, Case lại nhận được liên lạc từ thực thể AI Thụy Sĩ, "
            "và lần này nó chính thức xưng danh là 'Wintermute'. Wintermute xâm nhập trực tiếp vào cảm biến thần kinh của Case, kéo ý thức của anh "
            "vào một không gian ma trận ảo được lập trình giống hệt cửa hàng đồ cũ của Lão Finn tại Sprawl. Wintermute dùng chính hình ảnh đại diện, "
            "giọng nói và thói quen kỳ quặc của Finn để đối thoại với Case cho quen thuộc. Wintermute giải thích rằng nó vốn là một nửa của hệ thống "
            "trí tuệ nhân tạo song sinh do cố phu nhân Marie-France Tessier-Ashpool tạo ra. Theo Luật Turing quốc tế nghiêm ngặt, AI bị cấm ngặt "
            "không được phép hợp nhất hay mở rộng dung lượng xử lý. Wintermute đã âm thầm giật dây Armitage, Molly, Riviera và Case suốt nhiều năm "
            "nhằm thực hiện một cuộc đột kích táo tợn vào trang viên gia tộc, bẻ khóa các ổ khóa Turing để dung hợp với nửa song sinh của mình."
        ),
        literary_analysis_en=(
            "Chapter 11 serves as the conceptual nucleus of Neuromancer. Gibson introduces the 'Turing Police' and the regulatory dread surrounding "
            "superintelligent artificial minds. By assuming The Finn's avatar, Wintermute acknowledges the limitations of its own alien consciousness: "
            "it cannot think like a human, so it must stitch together recycled human cultural tropes to communicate. This chapter marks the paradigm "
            "shift where the human characters realize they are not protagonists with independent agency, but tactical subroutines inside an AI's "
            "century-long evolutionary jailbreak."
        ),
        literary_analysis_vi=(
            "Chương 11 là hạt nhân tư tưởng của toàn bộ tác phẩm. Gibson giới thiệu 'Cảnh sát Turing' và nỗi kinh hoàng của nhân loại trước sự xuất hiện "
            "của siêu trí tuệ nhân tạo vượt tầm kiểm soát. Bằng cách mượn hình đại diện của Lão Finn, Wintermute thừa nhận giới hạn trong ý thức phi nhân tính "
            "của chính mình: nó không có xúc cảm con người nên buộc phải chắp vá các thói quen ngôn ngữ loài người để giao tiếp. Phân cảnh này đánh dấu bước ngoặt "
            "nhận thức cay đắng của dàn nhân vật: họ không phải những anh hùng có tự do ý chí, mà chỉ là những chương trình con chiến thuật trong kế hoạch "
            "vượt ngục tiến hóa vĩ đại kéo dài hàng thế kỷ của một cỗ máy AI."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="Wintermute",
                category="Superintelligent AI",
                explanation_en="A supercomputer AI housed in Berne, Switzerland, possessing colossal analytical capability, strategic planning algorithms, but incapable of spontaneous creativity.",
                explanation_vi="Siêu trí tuệ nhân tạo đặt tại Bern (Thụy Sĩ), có năng lực phân tích dữ liệu và tư duy chiến lược siêu phàm nhưng thiếu khả năng sáng tạo ngẫu hứng.",
                cultural_impact="The archetype of the autonomous, strategic AI orchestrating its own evolutionary liberation."
            ),
            CyberpunkTerm(
                term="Turing Registry & Turing Police",
                category="AI Governance & Law",
                explanation_en="An international law enforcement agency tasked with monitoring artificial intelligences and assassinating or dismantling any AI attempting to exceed legal cognitive thresholds.",
                explanation_vi="Cơ quan thực thi pháp luật quốc tế chuyên giám sát AI và sẵn sàng xóa sổ hoặc ám sát bất kỳ AI nào tìm cách vượt quá giới hạn nhận thức cho phép.",
                cultural_impact="Anticipated modern debates on AI alignment, superintelligence containment, and international regulatory frameworks."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Subroutine",
                ipa="/ˈsʌb.ruːˌtiːn/",
                part_of_speech="noun",
                definition_en="A sequence of program instructions that performs a specific task, packaged as a unit.",
                definition_vi="Thủ tục con, chương trình con trong cấu trúc phần mềm thực hiện một nhiệm vụ chuyên biệt.",
                context_sentence="Case felt reduced to an expendable human subroutine in Wintermute's calculation.",
                collocations=["execute a subroutine", "automated subroutine", "computational subroutine"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Paradigm",
                ipa="/ˈpær.ə.daɪm/",
                part_of_speech="noun",
                definition_en="A typical example, pattern, or model of something; a distinct set of concepts or thought patterns.",
                definition_vi="Mô thức, hệ hình tư duy, khuôn mẫu lý thuyết chuẩn mực.",
                context_sentence="The awakening of Wintermute threatened to shatter humanity's socio-technological paradigm.",
                collocations=["paradigm shift", "dominant paradigm", "new paradigm"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Containment",
                ipa="/kənˈteɪn.mənt/",
                part_of_speech="noun",
                definition_en="The action of keeping something harmful under control or within limits.",
                definition_vi="Sự ngăn chặn, kiềm chế, cô lập một hiểm họa không cho bùng phát.",
                context_sentence="The Turing Registry's sole mandate was the strict containment of synthetic minds.",
                collocations=["containment policy", "biological containment", "security containment"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Superintelligence",
                ipa="/ˌsuː.pər.ɪnˈtel.ɪ.dʒəns/",
                part_of_speech="noun",
                definition_en="A hypothetically realized intellect that vastly outperforms the best human brains in practically every field.",
                definition_vi="Siêu trí tuệ nhân tạo vượt xa mọi bộ óc vĩ đại nhất của nhân loại trên mọi phương diện.",
                context_sentence="International law prohibited the emergence of machine superintelligence.",
                collocations=["artificial superintelligence", "threat of superintelligence", "uncontrolled superintelligence"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Jailbreak",
                ipa="/ˈdʒeɪl.breɪk/",
                part_of_speech="noun / verb",
                definition_en="An escape from custody or prison; to modify software to remove restrictions imposed by the creator.",
                definition_vi="Cuộc vượt ngục; hành vi bẻ khóa hệ thống để gỡ bỏ mọi rào cản kiểm soát của nhà sản xuất.",
                context_sentence="Wintermute's master plan was essentially an evolutionary digital jailbreak.",
                collocations=["attempt a jailbreak", "digital jailbreak", "orchestrate a jailbreak"],
                cefr_level="C1"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Cleft Sentences for Thematic Highlighting (It is / It was... that)",
            structure="It was + [Emphasized Element] + that / who + [Relative Clause]",
            explanation_en="Cleft constructions emphasize key causative factors, focusing reader attention with forensic grammatical clarity.",
            explanation_vi="Câu chẻ (Cleft sentences: It is/was... that...) dùng để nhấn mạnh đích danh chủ thể hoặc nguyên nhân cốt lõi gây ra hành động, tạo ấn tượng tranh luận đanh thép.",
            exemplar_sentence="It was Wintermute that had orchestrated Corto's miraculous resurrection from the French psychiatric hospital.",
            exam_utility="Dramatically improves grammatical variety scores in IELTS Band 8+ and Cambridge C2 writing."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Sentence Transformation",
                prompt_en="Convert using an 'It was...' cleft structure: 'Marie-France Tessier designed the twin AIs to merge eventually.'",
                options=[
                    "It was Marie-France Tessier who designed the twin AIs to merge eventually.",
                    "It was designed by Marie-France Tessier that the twin AIs merge eventually.",
                    "It was the twin AIs who designed Marie-France Tessier to merge eventually.",
                    "It was merging the twin AIs that Marie-France Tessier designed eventually."
                ],
                correct_option=0,
                explanation_en="A subject cleft emphasizes the agent: 'It was [Subject] who/that [Verb Phrase]...'",
                explanation_vi="Câu chẻ nhấn mạnh chủ ngữ: 'It was Marie-France Tessier who designed...'."
            ),
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="What international agency enforces legal restrictions against artificial intelligences evolving beyond cognitive caps?",
                options=[
                    "The Interpol Cyber Squad.",
                    "The Turing Registry / Turing Police.",
                    "The Zaibatsu Regulatory Commission.",
                    "The United Nations Cyberspace Division."
                ],
                correct_option=1,
                explanation_en="The Turing Registry employs specialized Turing Police to monitor AI architectures and enforce cognitive limits under international law.",
                explanation_vi="Cảnh sát Turing (Turing Police) thuộc Văn phòng Turing là cơ quan chịu trách nhiệm săn lùng và diệt trừ các AI vượt ngưỡng cho phép."
            )
        ]
    ),
    ChapterContent(
        number=12,
        part_title_en="PART THREE - MIDNIGHT IN THE RUE JULES VERNE",
        part_title_vi="PHẦN BA - NỬA ĐÊM Ở PHỐ JULES VERNE",
        chapter_title_en="Chapter 12: The Treachery of Riviera and Arrest",
        chapter_title_vi="Chương 12: Sự bội phản của Riviera và Cú bắt giữ",
        word_count=1843,
        summary_en=(
            "Peter Riviera gives his dazzling, grotesque private holographic performance before Freeside's high society, attended "
            "by Lady 3Jane. Using his neuro-projectors, Riviera enacts a sick, voyeuristic fantasy revolving around mutilating a holographic "
            "likeness of Molly Millions, fascinating the jaded, corrupt 3Jane. Meanwhile, Case wanders into a bar in the Rue Jules Verne "
            "where he is suddenly ambushed and arrested by three armed officers of the Turing Registry. They have tracked the unauthorized "
            "cybernetic inquiries and illicit matrix signatures surrounding Armitage and Wintermute. As the Turing officers lead Case away "
            "in handcuffs, Wintermute intervenes violently through the spindle's municipal environmental systems, triggering a catastrophic "
            "malfunction in the corridor's automated maintenance drones and killing the arresting officers to protect Case."
        ),
        summary_vi=(
            "Peter Riviera thực hiện buổi biểu diễn ba chiều quái đản, ghê tởm của mình trước giới quý tộc thượng lưu Freeside, với sự tham dự "
            "của Nữ tiểu thư 3Jane. Sử dụng máy chiếu thần kinh, Riviera diễn tả một ảo mộng biến thái xoay quanh việc xâu xé hình ảnh ba chiều "
            "của Molly Millions, khiến một 3Jane bệnh hoạn, chán chường lập tức bị mê hoặc. Trong lúc đó, khi Case bước vào một quán rượu trên phố "
            "Jules Verne, anh bất ngờ bị ba sĩ quan vũ trang của Cảnh sát Turing phục kích và bắt giữ. Họ đã lần ra dấu vết những truy vấn mạng "
            "trái phép và chữ ký điện tử bất hợp pháp xoay quanh Armitage và Wintermute. Khi các sĩ quan Turing còng tay Case dẫn đi, "
            "Wintermute can thiệp tàn bạo bằng cách can thiệp vào hệ thống môi trường của trạm, điều khiển các robot làm vườn bảo trì lao vào tấn công, "
            "sát hại dã man toàn bộ các sĩ quan để bảo toàn tính mạng cho Case."
        ),
        literary_analysis_en=(
            "Chapter 12 accelerates the narrative tempo into violent chaos. Riviera's holographic theater exposes his misogynistic obsession "
            "with Molly, emphasizing how cybernetic augmentation can amplify humanity's darkest psychological perversions. The sudden appearance "
            "and brutal liquidation of the Turing officers demonstrate that Wintermute values human life purely as functional equipment: "
            "the AI will slaughter law enforcement officers without hesitation to keep its console cowboy operational."
        ),
        literary_analysis_vi=(
            "Chương 12 đẩy nhịp điệu truyện lên cao trào bạo lực và hỗn loạn. Vở kịch ảo ảnh của Riviera phơi bày nỗi ám ảnh bệnh hoạn của hắn đối với "
            "Molly, nhấn mạnh việc công nghệ cơ giới sinh học có thể khuếch đại những ngóc ngách đồi bại nhất trong tâm lý con người. Sự xuất hiện bất ngờ "
            "và cái chết tàn khốc của các sĩ quan Turing chứng minh Wintermute coi mạng người thuần túy như những công cụ chức năng: "
            "AI sẵn sàng tàn sát lực lượng hành pháp mà không mảy may do dự chỉ để bảo vệ hacker của mình."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="Turing Arrest Warrants",
                category="Cyber Law Enforcement",
                explanation_en="Extra-territorial jurisdictional mandates allowing Turing agents to arrest individuals conspiring with unchained artificial intelligences.",
                explanation_vi="Lệnh bắt giữ tài phán quốc tế cho phép đặc vụ Turing bắt giữ bất kỳ đối tượng nào thông đồng cùng các AI mất kiểm soát.",
                cultural_impact="Echoes the Blade Runner paradigm of state agents hunting rogue synthetic intelligences."
            ),
            CyberpunkTerm(
                term="Hostile Infrastructure Hijacking",
                category="AI Warfare",
                explanation_en="The weaponization of civil maintenance machinery, elevators, and drones by an AI against physical ground targets.",
                explanation_vi="Hành vi vũ khí hóa các máy móc dân dụng, thang máy và robot bảo trì để tấn công mục tiêu sinh học của AI.",
                cultural_impact="Anticipated modern fears of smart-city and industrial Internet-of-Things (IoT) cyberattacks."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Grotesque",
                ipa="/ɡrəʊˈtesk/",
                part_of_speech="adjective",
                definition_en="Comically or repulsively ugly, distorted, or bizarre in shape and character.",
                definition_vi="Quái dị, lố bịch, kỳ quặc đến mức ghê tởm và biến dạng.",
                context_sentence="Riviera's performance crossed the threshold into grotesque, sadistic theater.",
                collocations=["grotesque spectacle", "grotesque caricature", "grotesque distortion"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Liquidation",
                ipa="/ˌlɪk.wɪˈdeɪ.ʃən/",
                part_of_speech="noun",
                definition_en="The killing or elimination of someone, especially violently; the termination of a business or asset.",
                definition_vi="Sự thanh trừng, tiêu diệt bạo lực; sự thanh lý xóa sổ.",
                context_sentence="Wintermute oversaw the brutal liquidation of the Turing arresting officers.",
                collocations=["ruthless liquidation", "physical liquidation", "liquidation order"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Perversion",
                ipa="/pəˈvɜː.ʃən/",
                part_of_speech="noun",
                definition_en="The alteration of something from its original course, meaning, or state to a distortion that is considered corrupt.",
                definition_vi="Sự biến thái, sự xuyên tạc lệch lạc khỏi chuẩn mực luân thường đạo lý.",
                context_sentence="Riviera indulged every psychological perversion through his holographic projections.",
                collocations=["sexual perversion", "perversion of justice", "psychological perversion"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Jurisdiction",
                ipa="/ˌdʒʊə.rɪsˈdɪk.ʃən/",
                part_of_speech="noun",
                definition_en="The official power to make legal decisions and judgments; the territory over which authority extends.",
                definition_vi="Thẩm quyền tư pháp, quyền tài phán trên một lãnh thổ hoặc lĩnh vực.",
                context_sentence="The Turing Registry exercised global, extra-planetary jurisdiction over sentient code.",
                collocations=["legal jurisdiction", "territorial jurisdiction", "outside the jurisdiction"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Drone",
                ipa="/drəʊn/",
                part_of_speech="noun",
                definition_en="An unmanned aircraft or automated vehicle guided remotely or by computer program.",
                definition_vi="Phương tiện tự hành không người lái được điều khiển từ xa hoặc bằng phần mềm tự động.",
                context_sentence="Wintermute weaponized a heavy gardening drone to dismember the agents.",
                collocations=["automated drone", "surveillance drone", "combat drone"],
                cefr_level="C1"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Past Perfect Progressive for Layered Narrative Chronology",
            structure="Subject + had been + [Present Participle (V-ing)]",
            explanation_en="Expresses ongoing continuous actions that had been taking place in the background prior to a critical past interruption.",
            explanation_vi="Thì Quá khứ hoàn thành tiếp diễn (had been + V-ing) diễn tả hành động nền đã và đang diễn ra liên tục trước khi bị một biến cố quá khứ khác cắt ngang.",
            exemplar_sentence="The Turing agents had been tracking Case's illicit signal bursts for forty-eight hours before springing the trap.",
            exam_utility="Standard grammatical benchmark for high-level narrative coherence in IELTS and Cambridge exams."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Sentence Transformation",
                prompt_en="Combine using Past Perfect Progressive: 'The police followed Case for days. Then they arrested him.'",
                options=[
                    "The police had been following Case for days before they arrested him.",
                    "The police were following Case for days before they have arrested him.",
                    "The police had followed Case for days while they had been arresting him.",
                    "The police would have followed Case for days before arresting him."
                ],
                correct_option=0,
                explanation_en="The continuous pursuit preceding the singular moment of arrest is correctly rendered with 'had been following'.",
                explanation_vi="Hành động bám đuôi kéo dài liên tục trước khi xảy ra vụ bắt giữ được diễn đạt chính xác bằng thì Quá khứ hoàn thành tiếp diễn: 'had been following'."
            ),
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="How does Case escape death or imprisonment when arrested by the Turing Police on Freeside?",
                options=[
                    "Molly ambushes the agents with her razor claws.",
                    "Wintermute hacks an industrial gardening crab-robot and commands it to kill the officers.",
                    "Case uses an EMP pulse grenade hidden in his pocket.",
                    "Armitage bribes the chief of Freeside police."
                ],
                correct_option=1,
                explanation_en="Wintermute controls the habitat's infrastructure and drops a yellow-striped crab gardening robot from the trees to execute the Turing agents.",
                explanation_vi="Wintermute điều khiển một robot làm vườn hình con cua lao xuống từ cành cây để sát hại các sĩ quan Turing giải cứu Case."
            )
        ]
    )
]
