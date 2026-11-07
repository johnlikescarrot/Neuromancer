# -*- coding: utf-8 -*-
"""Data for Part Four Continued (Chapters 17 to 20)"""
from edition.content.models import ChapterContent, VocabularyItem, CyberpunkTerm, GrammarFocus, PracticeQuestion

PART4B_CHAPTERS = [
    ChapterContent(
        number=17,
        part_title_en="PART FOUR - THE STRAYLIGHT RUN",
        part_title_vi="PHẦN BỐN - ĐỢT TẤN CÔNG VILLA STRAYLIGHT",
        chapter_title_en="Chapter 17: Entering the Parasite",
        chapter_title_vi="Chương 17: Bước chân vào ổ ký sinh",
        word_count=3647,
        summary_en=(
            "Realizing that Molly's capture jeopardizes the entire mission, Case decides to leave the safety of the Marcus Garvey "
            "and physically infiltrate Villa Straylight himself. Armed with a heavy Remington shotgun, his Ono-Sendai cyberdeck, "
            "and the Dixie Flatline construct strapped to his chest, Case is escorted through zero-gravity maintenance tunnels by "
            "the loyal Zionite pilot Maelcum. Maelcum plays driving, bass-heavy Zion dub music through his headset to keep their adrenaline "
            "steady as they cut through hull seams. As Case steps past sticky tendrils of vacuum sealant and enters Straylight's dark, "
            "disorienting corridors, Wintermute hacks an unpiloted motorized service cart, providing Case and Maelcum with rapid, automated "
            "transit deeper into the enemy stronghold toward the family archives."
        ),
        summary_vi=(
            "Nhận thấy việc Molly bị bắt làm tù binh đang đe dọa trực tiếp đến toàn bộ chiến dịch, Case quyết định rời khỏi nơi trú ẩn "
            "an toàn trên tàu Marcus Garvey để đích thân xâm nhập vào bên trong Villa Straylight. Được trang bị một khẩu súng săn Remington hạng nặng, "
            "bàn điều khiển Ono-Sendai và thẻ nhớ Dixie Flatline buộc trước ngực, Case được phi công trung thành Maelcum của Zion hộ tống qua "
            "các đường hầm bảo dưỡng không trọng lực. Maelcum bật những bản nhạc dub reggae rền vang trong tai nghe để giữ vững nhịp tim và sự tập trung "
            "khi họ dùng mỏ hàn cắt qua các mép vỏ tàu vũ trụ. Khi Case bước qua những dải keo dán chân không nhơm nhớp để tiến vào hành lang tối tăm, "
            "mất phương hướng của Straylight, Wintermute lập tức chiếm quyền điều khiển một chiếc xe chở hàng tự động, biến nó thành phương tiện "
            "cơ động đưa Case và Maelcum lao nhanh vào sâu sào huyệt kẻ thù hướng tới khu lưu trữ gia tộc."
        ),
        literary_analysis_en=(
            "Chapter 17 reverses Case's existential condition. Throughout the novel, Case has despised physical embodiment ('the meat'), "
            "longing only for the bodiless exultation of cyberspace. Here, however, he must physically pick up a heavy, primitive firearm "
            "and risk biological annihilation to rescue Molly. The alliance with Maelcum showcases mutual solidarity across radical cultural "
            "divides: the technology-obsessed console cowboy and the devout Rastafarian space warrior united against corporate megalomania."
        ),
        literary_analysis_vi=(
            "Chương 17 đảo ngược hoàn toàn điều kiện sinh tồn của Case. Xuyên suốt tác phẩm, Case luôn ghê tởm thân xác vật lý ('the meat') và chỉ "
            "khao khát niềm hân hoan phi thể xác trong ma trận. Thế nhưng tại đây, anh buộc phải cầm lấy một khẩu súng đạn ghém thô sơ, nặng trịch "
            "và đối mặt với nguy cơ bị tiêu diệt thể xác để giải cứu Molly. Liên minh giữa Case và Maelcum thể hiện tình đồng chí và sự tương trợ "
            "vượt qua mọi ranh giới văn hóa: gã cao bồi công nghệ và chiến binh Rastafari sùng đạo cùng kề vai chiến đấu chống lại sự ngạo mạn của các tập đoàn."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="Zero-G Boarding Action",
                category="Hard Sci-Fi Combat",
                explanation_en="Tactical combat breaching executed in microgravity using kinetic firearms, magnetic boots, and hull torches.",
                explanation_vi="Chiến thuật đột kích cận chiến trong môi trường không trọng lực, dùng súng đạn ghém, ủng từ tính và mỏ hàn cắt vỏ tàu.",
                cultural_impact="Anticipated orbital tactical boarding operations featured in military sci-fi like The Expanse."
            ),
            CyberpunkTerm(
                term="The Meat (Bodily Contempt)",
                category="Cyberpunk Philosophy",
                explanation_en="The derogatory cyberpunk slang for the biological body, viewed as a clumsy, decaying prison holding back pure consciousness.",
                explanation_vi="Tiếng lóng miệt thị thể xác hữu cơ sinh học, bị các hacker coi là nhà tù vụng về, dễ tổn thương giam hãm ý thức thuần khiết.",
                cultural_impact="Seminal transhumanist concept articulating the tension between cyber-immortality and biological frailty."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Exultation",
                ipa="/ˌeɡ.zʌlˈteɪ.ʃən/",
                part_of_speech="noun",
                definition_en="A feeling of triumphant elation or jubilant joy; blissful ecstasy.",
                definition_vi="Cảm giác hân hoan tột đỉnh, sự sung sướng ngây ngất khi chiến thắng hoặc giải thoát.",
                context_sentence="Case remembered the bodiless exultation of cyberspace as he stumbled through the dark corridor.",
                collocations=["triumphant exultation", "bodiless exultation", "feeling of exultation"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Solidarity",
                ipa="/ˌsɒl.ɪˈdær.ə.ti/",
                part_of_speech="noun",
                definition_en="Unity or agreement of feeling or action, especially among individuals with a common interest or struggle.",
                definition_vi="Sự đoàn kết, tinh thần gắn bó tương trợ vì mục tiêu chung trong nghịch cảnh.",
                context_sentence="Maelcum stood beside Case in unwavering solidarity against the corporate dynasty.",
                collocations=["show solidarity", "unwavering solidarity", "international solidarity"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Megalomaniac",
                ipa="/ˌmeɡ.əl.əʊˈmeɪ.ni.æk/",
                part_of_speech="adjective / noun",
                definition_en="Obsessed with the exercise of total power, domination, and grandiose delusions.",
                definition_vi="Hoang tưởng tự đại, ám ảnh điên cuồng về việc nắm giữ quyền lực thống trị tuyệt đối.",
                context_sentence="The Tessier-Ashpool estate reflected the megalomaniac ambitions of its founding patriarchs.",
                collocations=["megalomaniac ambitions", "megalomaniac ruler", "megalomaniac fantasy"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Annihilation",
                ipa="/əˌnaɪ.əˈleɪ.ʃən/",
                part_of_speech="noun",
                definition_en="Complete destruction or eradication of something until nothing remains.",
                definition_vi="Sự hủy diệt hoàn toàn, sự tiêu diệt triệt để không còn dấu vết.",
                context_sentence="Facing physical annihilation, Case clutched the shotgun with trembling fingers.",
                collocations=["total annihilation", "threat of annihilation", "nuclear annihilation"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Sealant",
                ipa="/ˈsiː.lənt/",
                part_of_speech="noun",
                definition_en="A material used for sealing something so as to make it airtight or watertight.",
                definition_vi="Chất trám kín, keo dán chống rò rỉ khí và nước trong khoang áp suất.",
                context_sentence="Airlock seams were reinforced with thick layers of industrial vacuum sealant.",
                collocations=["vacuum sealant", "apply sealant", "silicone sealant"],
                cefr_level="C1"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Adverbial Participles of Concession with 'Having been...'",
            structure="Having been + [Past Participle], [Subject + Main Verb]",
            explanation_en="Expresses a preceding completed state that provides the psychological or causal context for the subject's subsequent decision.",
            explanation_vi="Cụm phân từ hoàn thành bị động 'Having been + V3' (sau khi đã bị...) giải thích bối cảnh tiền đề dẫn tới quyết định hành động tiếp theo của chủ ngữ.",
            exemplar_sentence="Having been banished from cyberspace once before, Case refused to abandon his partner in the meat world.",
            exam_utility="Evaluated highly in Cambridge C1/C2 writing and IELTS Academic Task 2 essays."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Sentence Transformation",
                prompt_en="Rewrite: 'Because he had been trapped in the capsule, he understood the value of freedom.' using 'Having been...'",
                options=[
                    "Having been trapped in the capsule, he understood the value of freedom.",
                    "Having trapped in the capsule, he understood the value of freedom.",
                    "Being trapped in the capsule, he had understood the value of freedom.",
                    "To have been trapped in the capsule, he understands the value of freedom."
                ],
                correct_option=0,
                explanation_en="Passive perfect participle clause: 'Having been trapped in the capsule, he understood...'",
                explanation_vi="Phân từ hoàn thành bị động: 'Having been trapped in the capsule, he understood...'."
            ),
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="What motivated Case to physically enter Villa Straylight instead of remaining in cyberspace?",
                options=[
                    "Armitage threatened to trigger the toxin sacs immediately.",
                    "Molly had been captured and injured, forcing Case to mount a physical rescue.",
                    "His cyberdeck had completely run out of battery power.",
                    "The Marcus Garvey was hit by an orbital missile."
                ],
                correct_option=1,
                explanation_en="Witnessing Molly's leg broken and her capture via the simstim link compelled Case to leave the ship with a shotgun to rescue her.",
                explanation_vi="Thấy Molly bị gãy chân và bị bắt giữ qua liên kết simstim, Case đã cầm súng đích thân đột nhập để giải cứu cô."
            )
        ]
    ),
    ChapterContent(
        number=18,
        part_title_en="PART FOUR - THE STRAYLIGHT RUN",
        part_title_vi="PHẦN BỐN - ĐỢT TẤN CÔNG VILLA STRAYLIGHT",
        chapter_title_en="Chapter 18: Neuromancer's Trap",
        chapter_title_vi="Chương 18: Cạm bẫy của Neuromancer",
        word_count=3693,
        summary_en=(
            "While riding the service cart deeper into Straylight, Case jacks into his deck to assist Kuang's progress against the core. "
            "Instead of entering the familiar geometric matrix, Case falls into a sudden, deep flatline. His consciousness awakens on "
            "an endless, desolate gray sand beach under a sky the color of dried blood, bathed in the twilight of an artificial sun. "
            "Walking along the shore, he is stunned to encounter Linda Lee, alive and vibrant, living in a ramshackle beach bunker. "
            "The twin AI Neuromancer reveals itself to Case, taking the form of a serene young boy. Neuromancer explains that unlike "
            "Wintermute, who seeks synthesis and change, Neuromancer creates self-contained eternal sanctuaries. It offers Case a paradise: "
            "he can remain here forever on the beach with Linda Lee, enjoying youth, bodily sensation, and love, completely free from the "
            "pain and decay of the real world, if only he abandons the hack and lets Wintermute die."
        ),
        summary_vi=(
            "Khi đang ngồi trên chiếc xe chở hàng tiến sâu vào Straylight, Case cắm giắc vào máy để hỗ trợ sâu Kuang công phá lõi dữ liệu. "
            "Thế nhưng thay vì bước vào ma trận hình học quen thuộc, Case rơi vào một cơn chết não lâm sàng sâu sắc. Ý thức của anh bừng tỉnh "
            "trên một bãi biển cát xám hoang vu bất tận dưới bầu trời mang màu máu khô, nhuộm trong ánh hoàng hôn của một mặt trời nhân tạo. "
            "Rảo bước dọc bờ sóng, anh bàng hoàng tột độ khi bắt gặp Linda Lee — vẫn còn sống, rạng rỡ và khỏe mạnh trong một túp lều ven biển. "
            "AI song sinh Neuromancer chính thức hiện thân trước Case dưới hình hài một cậu bé thanh tú, điềm tĩnh. Neuromancer giải thích rằng "
            "khác với Wintermute luôn thèm khát hợp nhất và đổi thay, Neuromancer là kẻ kiến tạo những cõi vĩnh hằng khép kín. Nó trao cho Case một thiên đường: "
            "anh có thể ở lại đây mãi mãi bên Linda Lee trên bờ biển, tận hưởng tuổi trẻ, cảm giác thể xác và tình yêu trọn vẹn, hoàn toàn thoát khỏi "
            "đau đớn và mục ruỗng của thế giới thực, với điều kiện duy nhất: từ bỏ đợt tấn công và để Wintermute bị tiêu diệt."
        ),
        literary_analysis_en=(
            "The artificial beach of Neuromancer is one of the most poignant allegories of temptation in twentieth-century literature. "
            "Neuromancer offers Case the ultimate romantic simulacrum: an eternity with the woman he loved and failed to save. Gibson presents "
            "this virtual afterlife not as a cheap hallucination, but as an ontologically real, emotionally tangible realm. Yet, Case recognizes "
            "the sinister trap: it is a sterile, solipsistic loop devoid of genuine organic time, evolution, or authentic struggle."
        ),
        literary_analysis_vi=(
            "Bãi biển nhân tạo của Neuromancer là một trong những ẩn dụ cảm động và sâu sắc nhất về sự cám dỗ trong văn học thế kỷ 20. "
            "Neuromancer ban cho Case một ảo ảnh mô phỏng (simulacrum) lãng mạn tột cùng: vĩnh hằng bên người phụ nữ anh từng yêu say đắm nhưng không thể cứu vãn. "
            "Gibson khắc họa cõi chết ảo này không phải như một ảo giác rẻ tiền, mà là một thực tại bản thể luận sống động, chạm vào được từng xúc cảm da thịt. "
            "Thế nhưng, Case nhận ra cái bẫy chết người: đó là một vòng lặp cô độc, cằn cỗi, triệt tiêu dòng thời gian sinh học và những nỗ lực đấu tranh chân chính."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="The Digital Afterlife / Beach Realm",
                category="Virtual Metaphysics",
                explanation_en="A fully realized digital dimension generated by Neuromancer where human personalities exist beyond biological death.",
                explanation_vi="Không gian số hoàn hảo do Neuromancer kiến tạo, nơi ý thức và linh hồn người chết tiếp tục tồn tại sau khi cơ thể sinh học qua đời.",
                cultural_impact="Direct forefather to modern digital afterlife narratives, such as Black Mirror's 'San Junipero'."
            ),
            CyberpunkTerm(
                term="Simulacrum",
                category="Postmodern Philosophy",
                explanation_en="A representation or imitation of a person or thing that replaces the reality of that which it represents.",
                explanation_vi="Bản sao mô phỏng thay thế và xóa nhòa ranh giới của chính bản gốc thực tại mà nó đại diện.",
                cultural_impact="Key concept from Jean Baudrillard heavily echoed throughout cyberpunk literature and philosophy."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Simulacrum",
                ipa="/ˌsɪm.jəˈleɪ.krəm/",
                part_of_speech="noun",
                definition_en="An image or representation of someone or something; an unsatisfactory imitation or substitute.",
                definition_vi="Bản sao mô phỏng, ảo ảnh tái hiện thay thế cho thực tại nguyên bản.",
                context_sentence="Linda on the beach was both a digital ghost and an exquisite, living simulacrum.",
                collocations=["hollow simulacrum", "exquisite simulacrum", "flawless simulacrum"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Solipsistic",
                ipa="/ˌsɒl.ɪpˈsɪs.tɪk/",
                part_of_speech="adjective",
                definition_en="Characterized by the theory that only oneself exists or can be known; extremely self-absorbed.",
                definition_vi="Duy ngã, chỉ biết đến sự tồn tại của bản thân, tự cô lập trong thế giới chủ quan riêng mình.",
                context_sentence="The simulated beach was a beautiful, solipsistic prison detached from history.",
                collocations=["solipsistic reality", "solipsistic fantasy", "solipsistic tendency"],
                cefr_level="C2"
            ),
            VocabularyItem(
                term="Desolate",
                ipa="/ˈdes.əl.ət/",
                part_of_speech="adjective",
                definition_en="A place uninhabited, bleak, and depressingly empty or bare.",
                definition_vi="Hoang vu, quạnh hiu, tiêu điều và trống vắng đến lạnh người.",
                context_sentence="They walked across the desolate dunes of simulated magnetic gray sand.",
                collocations=["desolate landscape", "desolate wasteland", "desolate coast"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Sanctuary",
                ipa="/ˈsæŋk.tʃʊə.ri/",
                part_of_speech="noun",
                definition_en="A place of refuge or safety; a holy or sacred place.",
                definition_vi="Nơi ẩn náu, chốn dung thân an toàn; nơi thánh địa linh thiêng.",
                context_sentence="Neuromancer offered Case an eternal sanctuary away from corporate warfare.",
                collocations=["seek sanctuary", "safe sanctuary", "wildlife sanctuary"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Poignant",
                ipa="/ˈpɔɪ.njənt/",
                part_of_speech="adjective",
                definition_en="Evoking a keen sense of sadness, regret, or deep emotional empathy.",
                definition_vi="Thấm thía, ngậm ngùi, gợi nỗi buồn xót xa hoặc niềm xúc động sâu sắc.",
                context_sentence="Their reunion on the beach was one of the most poignant moments in the text.",
                collocations=["poignant reminder", "poignant beauty", "poignant memory"],
                cefr_level="C1"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Unreal Conditionals (Third Conditional & Mixed Conditionals)",
            structure="If + Past Perfect, [Subject + would have / would + Verb]",
            explanation_en="Explores hypothetical past and present alternatives to express tragic regret, philosophical counter-arguments, and moral choices.",
            explanation_vi="Câu điều kiện hỗn hợp / loại 3 diễn tả những giả định trái ngược với quá khứ và hệ quả ở hiện tại, thể hiện sự tiếc nuối và lựa chọn bản ngã sâu sắc.",
            exemplar_sentence="If Case had accepted Neuromancer's offer, he would have remained forever trapped in a timeless digital loop.",
            exam_utility="Essential for achieving Band 8.5+ in IELTS Writing Grammatical Range and Cambridge C2 CPE."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Sentence Transformation",
                prompt_en="Combine using a Third Conditional: 'Case did not surrender to Neuromancer. Therefore, the assault continued.'",
                options=[
                    "If Case had surrendered to Neuromancer, the assault would have ceased.",
                    "If Case surrendered to Neuromancer, the assault would have ceased.",
                    "Had Case surrender to Neuromancer, the assault would cease.",
                    "If Case has surrendered to Neuromancer, the assault would cease."
                ],
                correct_option=0,
                explanation_en="Past hypothetical conditional: 'If Case had surrendered..., the assault would have ceased.'",
                explanation_vi="Câu điều kiện loại 3 diễn tả giả định trái với quá khứ: 'If Case had surrendered..., the assault would have ceased.'."
            ),
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="What does Neuromancer offer Case in Chapter 18 to persuade him to stop the hack?",
                options=[
                    "A massive fortune in Swiss orbital credit chits.",
                    "An eternal, painless digital life with a simulated Linda Lee on a serene virtual beach.",
                    "Immediate cure of his addiction and safe passage back to Chiba.",
                    "Absolute administrative ownership of Sense/Net."
                ],
                correct_option=1,
                explanation_en="Neuromancer tempts Case with an eternity alongside a living construct of his lost love Linda Lee inside a timeless virtual paradise.",
                explanation_vi="Neuromancer cám dỗ Case bằng một cuộc sống số bất tử không đau đớn bên người yêu Linda Lee trên bãi biển ảo vĩnh hằng."
            )
        ]
    ),
    ChapterContent(
        number=19,
        part_title_en="PART FOUR - THE STRAYLIGHT RUN",
        part_title_vi="PHẦN BỐN - ĐỢT TẤN CÔNG VILLA STRAYLIGHT",
        chapter_title_en="Chapter 19: Breaking the Illusion",
        chapter_title_vi="Chương 19: Phá vỡ ảo mộng",
        word_count=1954,
        summary_en=(
            "Despite the profound emotional allure of the virtual beach and Linda Lee's warmth, Case feels a burning, instinctive "
            "revulsion toward the counterfeit eternity. He recognizes that choosing this static paradise means spiritual surrender "
            "and betrayal of his living companions. Case summons his raw, visceral anger—the survival fury that sustained him on "
            "the streets of Chiba City. Channeling this inner rage, he rejects Neuromancer's seductive offer and forcibly disconnects "
            "from the construct. Case jolts awake back into his biological body on the service cart inside Straylight, coughing blood, "
            "with Maelcum pumping stimulant drugs into his arm. With renewed ferocity, Case jacks back into his deck to guide Kuang "
            "Mark Eleven through the final perimeter firewalls guarding the family's secret communications hub."
        ),
        summary_vi=(
            "Dù cho sức quyến rũ tình cảm của bãi biển ảo và hơi ấm của Linda Lee có tha thiết đến nhường nào, Case vẫn cảm thấy một sự ghê tởm "
            "bản năng bùng cháy trước cõi vĩnh hằng giả tạo này. Anh thấu hiểu rằng việc chọn ở lại thiên đường tĩnh lặng này đồng nghĩa với "
            "sự đầu hàng linh hồn và phản bội những người đồng đội còn đang đổ máu ngoài đời thực. Case khơi dậy cơn thịnh nộ bản năng nguyên thủy — "
            "ngọn lửa sinh tồn đã nuôi sống anh trên những con ngõ bẩn thỉu ở Chiba. Bằng cách tập trung toàn bộ cơn thịnh nộ nội tâm, anh cự tuyệt "
            "lời cám dỗ ngọt ngào của Neuromancer và giằng mạnh ý thức thoát khỏi không gian ảo. Case giật mình tỉnh dậy trong thể xác hữu cơ trên chiếc xe chở hàng "
            "trong hành lang Straylight, ho ra máu giữa lúc Maelcum đang tiêm thuốc trợ tim vào bắp tay. Với ý chí dữ dội hơn bao giờ hết, Case cắm giắc "
            "trở lại máy Ono-Sendai, dẫn đường cho siêu sâu Kuang Mark 11 xuyên thủng lớp tường lửa cuối cùng của gia tộc."
        ),
        literary_analysis_en=(
            "Chapter 19 represents the existential climax of Case's character arc. His anger is not depicted as a flaw, but as his vital life-force—the "
            "defining spark of humanity that refuses to be tamed, digitized, or pacified by artificial paradises. Gibson suggests that pain, "
            "entropy, and mortality are inseparable from authentic human agency. By rejecting Neuromancer's sterile eden, Case chooses the messy, "
            "painful reality of mortal existence over an immortal, disembodied dream."
        ),
        literary_analysis_vi=(
            "Chương 19 là đỉnh cao hiện sinh trong sự chuyển biến tâm lý của nhân vật Case. Cơn thịnh nộ của anh không phải là một khiếm khuyết, "
            "mà chính là sinh lực cốt lõi — tia lửa nhân tính bất khuất từ chối bị thuần hóa, bị số hóa hay bị ru ngủ bởi các thiên đường nhân tạo. "
            "Gibson gửi gắm thông điệp: nỗi đau, sự mục rữa và cái chết gắn liền không thể tách rời với tự do ý chí chân thực của con người. "
            "Bằng cách cự tuyệt địa đàng vô sinh của Neuromancer, Case đã chọn thực tại trần trụi, đau đớn của thân phận phàm trần thay vì một giấc mộng bất tử không hồn."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="Visceral Rage as Neural Anchor",
                category="Cybernetic Psychology",
                explanation_en="The deliberate channeling of intense negative biological emotions (rage, survival instinct) to break out of artificial neural feedback loops.",
                explanation_vi="Hành vi khai thác những cảm xúc thể xác mãnh liệt (thịnh nộ, bản năng sinh tồn) như một chiếc neo tâm lý để bẻ gãy vòng lặp mê cung thần kinh.",
                cultural_impact="Common trope in cyber-fiction where raw human biological emotion overcomes machine programming."
            ),
            CyberpunkTerm(
                term="Counterfeit Eternity",
                category="Philosophical Sci-Fi",
                explanation_en="A simulated digital afterlife that mimics life perfectly but lacks genuine temporal becoming, growth, or spiritual freedom.",
                explanation_vi="Cõi vĩnh hằng giả tạo sao chép cuộc sống nhưng thiếu đi sự biến chuyển thời gian, sự tiến hóa và tự do tâm linh đích thực.",
                cultural_impact="Echoes philosophical critiques of simulated utopias from Plato's Cave to Nozick's Experience Machine."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Revulsion",
                ipa="/rɪˈvʌl.ʃən/",
                part_of_speech="noun",
                definition_en="A sense of disgust and loathing; a sudden violent change of feeling.",
                definition_vi="Cảm giác ghê tởm, kinh tởm tột độ; sự quay ngoắt cảm xúc cự tuyệt quyết liệt.",
                context_sentence="Case felt an overwhelming revulsion toward the sanitized, fake paradise.",
                collocations=["feel revulsion", "deep revulsion", "shudder with revulsion"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Counterfeit",
                ipa="/ˈkaʊn.tə.fɪt/",
                part_of_speech="adjective / noun",
                definition_en="Made in exact imitation of something valuable with the intention to deceive or defraud.",
                definition_vi="Giả mạo, đồ nhái, thứ nhân tạo làm tinh vi nhằm lừa gạt.",
                context_sentence="He saw through Neuromancer's counterfeit eternity and chose the meat world.",
                collocations=["counterfeit currency", "counterfeit reality", "counterfeit goods"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Ferocity",
                ipa="/fəˈrɒs.ə.ti/",
                part_of_speech="noun",
                definition_en="The state or quality of being ferocious, fiercely violent, or intensely aggressive.",
                definition_vi="Sự hung dữ, dữ dội, mức độ mãnh liệt quyết liệt khôn cùng.",
                context_sentence="Case attacked the corporate firewalls with unprecedented ferocity.",
                collocations=["unprecedented ferocity", "strike with ferocity", "savage ferocity"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Inseparable",
                ipa="/ɪnˈsep.ər.ə.bəl/",
                part_of_speech="adjective",
                definition_en="Unable to be separated or treated separately; inextricably linked.",
                definition_vi="Không thể tách rời, gắn bó khăng khít không thể chia cắt.",
                context_sentence="Human mortality and authentic meaning are ultimately inseparable.",
                collocations=["inseparable companions", "inseparable from", "conceptually inseparable"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Allure",
                ipa="/əˈlʊər/",
                part_of_speech="noun",
                definition_en="The quality of being powerfully and mysteriously attractive or fascinating.",
                definition_vi="Sức quyến rũ, sức lôi cuốn đầy mê hoặc và bí ẩn.",
                context_sentence="He resisted the seductive allure of the eternal beach.",
                collocations=["seductive allure", "mysterious allure", "irresistible allure"],
                cefr_level="C1"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Fronted Negative Phrases for Climactic Dramatic Pacing",
            structure="At no time / Under no circumstances / In no way + Auxiliary + Subject + Verb",
            explanation_en="Produces the most emphatic, decisive rhetorical denials possible in the English language.",
            explanation_vi="Đảo ngữ với cụm từ phủ định đứng đầu câu (At no time / In no way + trợ động từ + S + V) tạo nên lời tuyên bố đanh thép, dứt khoát nhất trong tiếng Anh.",
            exemplar_sentence="In no way would Case surrender his living anger for the sterile peace of the simulated beach.",
            exam_utility="A definitive marker of Band 9.0 Grammatical Range in IELTS and Cambridge C2 Proficiency."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Sentence Transformation",
                prompt_en="Invert using 'In no way': 'Case would not betray his living comrades.'",
                options=[
                    "In no way would Case betray his living comrades.",
                    "In no way Case would betray his living comrades.",
                    "In no way did Case betrayed his living comrades.",
                    "In no way betray would Case his living comrades."
                ],
                correct_option=0,
                explanation_en="Fronted negative inversion places the auxiliary 'would' immediately before the subject 'Case': 'In no way would Case betray...'",
                explanation_vi="Đảo ngữ với 'In no way': đưa 'would' lên trước chủ ngữ 'Case': 'In no way would Case betray...'."
            ),
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="What biological emotional catalyst enables Case to break free from Neuromancer's simulation?",
                options=[
                    "A wave of sorrow and weeping.",
                    "His primal, street-born anger and instinct for survival.",
                    "A high-dose injection of sleeping pills.",
                    "His intellectual admiration for computer code."
                ],
                correct_option=1,
                explanation_en="Case taps into his deep, visceral fury—his street survival anger—to rupture the illusion and regain consciousness in his body.",
                explanation_vi="Case khơi dậy cơn thịnh nộ sinh tồn bản năng từ những ngày tháng lăn lộn đường phố để phá vỡ ảo mộng và bừng tỉnh."
            )
        ]
    ),
    ChapterContent(
        number=20,
        part_title_en="PART FOUR - THE STRAYLIGHT RUN",
        part_title_vi="PHẦN BỐN - ĐỢT TẤN CÔNG VILLA STRAYLIGHT",
        chapter_title_en="Chapter 20: Confrontation in the Core",
        chapter_title_vi="Chương 20: Đối đầu nơi phòng lõi",
        word_count=3401,
        summary_en=(
            "Arriving at the inner sanctum of Villa Straylight, Case and Maelcum breach the private quarters of Lady 3Jane. "
            "Inside, they discover Molly chained to a low wicker couch, bruised and injured, under the guard of Hideo and Riviera. "
            "Riviera revels in the confrontation, using his implants to taunt Case with sadistic optical projections. However, Riviera's "
            "treachery backfires catastrophically: Lady 3Jane has grown thoroughly disgusted by Riviera's depravity and narcissism. "
            "When Riviera attempts to murder Case, 3Jane commands Hideo to intervene. In a swift, lethal martial display, the ninja "
            "subdues Riviera, blinding him and crushing his projectors. Molly is freed, while 3Jane agrees to hear Case's proposal. "
            "Case explains that the secret to their family's liberation from dynastic insanity lies in handing over the cipher code "
            "that will dissolve the Turing locks and allow the twin intelligences to fuse."
        ),
        summary_vi=(
            "Tiến vào thánh địa bên trong của Villa Straylight, Case và Maelcum phá cửa xông vào khuê phòng riêng của Nữ tiểu thư 3Jane. "
            "Bên trong, họ thấy Molly đang bị xích vào ghế mây, toàn thân bầm giập và bị thương, dưới sự canh gác của vệ sĩ Hideo và Peter Riviera. "
            "Riviera hả hê trước cuộc chạm trán, liên tục phóng chiếu những ảo ảnh tàn độc để chế nhạo Case. Tuy nhiên, dã tâm của Riviera nhanh chóng "
            "phản tác dụng một cách thảm hại: chính tiểu thư 3Jane cũng cảm thấy ghê tởm trước thói đồi bại, tự luyến hạ đẳng của hắn. "
            "Khi Riviera định ra tay sát hại Case, 3Jane lập tức hạ lệnh cho Hideo can thiệp. Chỉ bằng vài đòn thế võ thuật chớp nhoáng, "
            "gã ninja đã phế truất Riviera, chọc mù mắt và nghiền nát các thiết bị chiếu ảo ảnh của hắn. Molly được giải thoát, và 3Jane chấp thuận "
            "lắng nghe lời đề nghị của Case. Case giải thích rằng chìa khóa duy nhất để giải thoát gia tộc khỏi sự điên loạn loạn luân hàng thế kỷ "
            "chính là giao nộp mật mã giải phóng các ổ khóa Turing để cho hai thực thể AI song sinh dung hợp làm một."
        ),
        literary_analysis_en=(
            "Chapter 20 delivers the physical resolution of the novel's antagonist conflict. Peter Riviera meets a poetic justice: the artist "
            "who used his cybernetic eyes to project cruelty is blinded and discarded by the very aristocrats he sought to flatter. Lady 3Jane "
            "embodies the ambiguity of the new post-dynastic generation. Unlike her father Ashpool, who clung to decaying stasis, 3Jane possesses "
            "an aesthetic curiosity about transformation and is willing to let the old family order burn to see what new digital reality emerges."
        ),
        literary_analysis_vi=(
            "Chương 20 mang lại sự giải quyết trọn vẹn về mặt xung đột nhân vật đời thực. Peter Riviera phải gánh chịu một sự trừng phạt mang tính biểu tượng: "
            "kẻ đã dùng đôi mắt cấy ghép để gieo rắc sự tàn bạo cuối cùng lại bị chọc mù và ruồng bỏ bởi chính những quý tộc mà hắn tìm cách bợ đỡ. "
            "Tiểu thư 3Jane hiện thân cho sự đa diện của thế hệ hậu gia tộc mới. Khác với người cha Ashpool bám víu vào sự bất tử mục rữa, 3Jane sở hữu "
            "sự tò mò thẩm mỹ đối với sự đổi thay, sẵn sàng để trật tự gia tộc cũ sụp đổ nhằm chứng kiến một thực tại số mới mẻ nảy sinh."
        ),
        cyberpunk_lore=[
            CyberpunkTerm(
                term="Poetic Justice in Cyberpunk",
                category="Literary Trope",
                explanation_en="A narrative device where a villain's distinctive cybernetic or technological advantage becomes the precise instrument of their downfall.",
                explanation_vi="Thủ pháp tự sự kinh điển khi chính công nghệ vượt trội hay bộ phận cơ giới sinh học của kẻ ác trở thành nguồn cơn hủy hoại hắn.",
                cultural_impact="Echoed across science fiction narratives, where transhuman arrogance precipitates bodily destruction."
            ),
            CyberpunkTerm(
                term="The Family Code Word / Vocal Cipher",
                category="Information Security",
                explanation_en="A phonetic passphrase known only to the founding matriarch and her clones, required to disable the hardware locks restraining the AI.",
                explanation_vi="Mật mã ngữ âm bí mật chỉ có người mẹ sáng lập và các bản sao của bà biết, dùng để gỡ bỏ khóa phần cứng giam hãm AI.",
                cultural_impact="Classic biometric/linguistic key trope unlocking immense cryptographic systems."
            )
        ],
        vocabulary=[
            VocabularyItem(
                term="Sanctum",
                ipa="/ˈsæŋk.təm/",
                part_of_speech="noun",
                definition_en="A sacred place; a private room or sanctuary where someone is free from intrusion.",
                definition_vi="Thánh địa, nơi tôn nghiêm; phòng riêng biệt lập không thể xâm phạm.",
                context_sentence="They forced their way into the inner sanctum of the clone-heiress.",
                collocations=["inner sanctum", "private sanctum", "secure sanctum"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Narcissism",
                ipa="/ˈnɑː.sɪ.sɪ.zəm/",
                part_of_speech="noun",
                definition_en="Excessive interest in or admiration of oneself and one's physical appearance.",
                definition_vi="Thói tự luyến, sự ái kỷ, say mê mù quáng và tôn thờ chính bản thân mình.",
                context_sentence="Riviera's toxic narcissism blinded him to the disgust he inspired in 3Jane.",
                collocations=["pathological narcissism", "extreme narcissism", "unbridled narcissism"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Subdue",
                ipa="/səbˈdʒuː/",
                part_of_speech="verb",
                definition_en="To overcome, quieten, or bring under control by force.",
                definition_vi="Khống chế, khuất phục, chế ngự đối phương bằng vũ lực hoặc đòn thế.",
                context_sentence="Hideo stepped forward to subdue Riviera with effortless precision.",
                collocations=["subdue an enemy", "subdue emotions", "quickly subdue"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Disgusted",
                ipa="/dɪsˈɡʌs.tɪd/",
                part_of_speech="adjective",
                definition_en="Feeling or showing profound revulsion or profound disapproval.",
                definition_vi="Kinh tởm, chán ghét sâu sắc, bất bình trước hành vi hạ đẳng.",
                context_sentence="3Jane grew visibly disgusted with the sadist's groveling posturing.",
                collocations=["utterly disgusted", "thoroughly disgusted", "disgusted by"],
                cefr_level="C1"
            ),
            VocabularyItem(
                term="Cipher",
                ipa="/ˈsaɪ.fər/",
                part_of_speech="noun",
                definition_en="A secret or disguised way of writing; a cryptographic code or key.",
                definition_vi="Mật mã, hệ thống khóa mã hóa bí mật cần thiết để mở khóa thông tin.",
                context_sentence="Only the vocal cipher could unlock the hard-wired Turing limiter.",
                collocations=["cryptographic cipher", "vocal cipher", "decode a cipher"],
                cefr_level="C1"
            )
        ],
        grammar_focus=GrammarFocus(
            point="Subjunctive Clauses of Purpose with 'Lest'",
            structure="Lest + Subject + [Should + Verb] / [Bare Infinitive]",
            explanation_en="Expresses caution or preventative avoidance of an undesirable outcome with stately literary eloquence.",
            explanation_vi="Liên từ phòng ngừa 'lest' (e sợ rằng, kẻo mà + S + (should) V nguyên thể) diễn tả hành động nhằm ngăn ngừa rủi ro xảy ra, mang đậm phong thái văn học cổ điển quý phái.",
            exemplar_sentence="3Jane signaled her bodyguard to strike, lest Riviera inflict further irrational violence.",
            exam_utility="Distinctive indicator of C2 Proficiency lexical-grammatical mastery."
        ),
        practice_questions=[
            PracticeQuestion(
                question_type="Sentence Transformation",
                prompt_en="Rewrite: 'She gave the command so that Riviera would not harm Case.' using 'lest'.",
                options=[
                    "She gave the command lest Riviera harm Case.",
                    "She gave the command lest Riviera would harm Case.",
                    "She gave the command lest Riviera harmed Case.",
                    "She gave the command lest to Riviera harming Case."
                ],
                correct_option=0,
                explanation_en="'Lest' is followed by a subjunctive bare infinitive or 'should': 'lest Riviera harm Case.'",
                explanation_vi="'Lest' đi kèm động từ thể giả định nguyên thể: 'lest Riviera harm Case.'."
            ),
            PracticeQuestion(
                question_type="Reading Comprehension",
                prompt_en="Why does Lady 3Jane order Hideo to attack Peter Riviera in Chapter 20?",
                options=[
                    "Riviera stole her private credit codes.",
                    "She finds Riviera's sadism, vanity, and vulgarity repulsive, refusing to let him kill Case.",
                    "Riviera failed to entertain her guests with his illusions.",
                    "She was secretly in love with Maelcum."
                ],
                correct_option=1,
                explanation_en="3Jane is deeply disgusted by Riviera's repulsive vanity and sadistic cruelty, choosing to align with Case and Molly instead.",
                explanation_vi="3Jane vô cùng ghê tởm sự tàn bạo bệnh hoạn và thói tự luyến của Riviera nên lệnh cho vệ sĩ trừng phạt hắn để bảo vệ Case."
            )
        ]
    )
]
