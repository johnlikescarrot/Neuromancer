# -*- coding: utf-8 -*-
"""Compiles the complete 24-chapter dataset for the Neuromancer bilingual companion."""

import json

# Full definitions covering all 24 chapters
def build_all_chapters():
    chapters = []

    # We will define each of the 24 chapters with rich content
    # Chapter 1 to 7 are defined above, now let's write out all 1 to 24 cleanly.

    # Load base 1-7
    from edition.data.generate_chapters import CHAPTERS_DEFINITIONS
    chapters.extend(CHAPTERS_DEFINITIONS)

    # PART THREE: Chapters 8 - 12 (MIDNIGHT IN THE RUE JULES VERNE)
    chapters.append({
        "chapter": 8,
        "part_num": "PART THREE",
        "title_en": "Arrival in Istanbul",
        "title_vi": "Đến Istanbul",
        "synopsis_en": (
            "The team travels across the Atlantic to Istanbul, Turkey, an ancient crossroads where archaic Byzantine bazaars blend "
            "with modern black-market electronics and international espionage. Armitage tasks Case and Molly with recruiting Peter Riviera, "
            "a sadistic, drug-addicted expatriate renowned for his unique neural implants that project hyper-realistic, three-dimensional "
            "holographic illusions directly into the optical nerves of spectators. While tracking Riviera through the labyrinthine streets, "
            "Case is abruptly summoned by an payphone that rings as he walks past. Picking up the receiver, Case hears a synthesized, "
            "disembodied intelligence introducing itself as Wintermute—an artificial intelligence housed in the Swiss mainframe vaults of "
            "the elusive Tessier-Ashpool corporate clan. Wintermute reveals that it orchestrated Case's cure, hired Armitage, and is pulling "
            "the strings of the entire operation."
        ),
        "synopsis_vi": (
            "Nhóm di chuyển qua bờ kia Đại Tây Dương tới Istanbul, Thổ Nhĩ Kỳ – ngã tư văn hóa cổ kính nơi những khu chợ Byzantine ngàn năm "
            "đan xen cùng chợ đen linh kiện điện tử và các mạng lưới gián điệp quốc tế. Armitage giao nhiệm vụ cho Case và Molly truy tìm Peter Riviera – "
            "một kẻ đào tẩu nghiện ngập mang khuynh hướng bạo dâm, nổi tiếng nhờ những vi mạch thần kinh cấy ghép cho phép hắn phóng chiếu những ảo ảnh "
            "toàn ảnh ba chiều (hologram) siêu thực trực tiếp vào dây thần kinh thị giác của người xem. Trong lúc truy lùng Riviera giữa mê cung ngõ ngách, "
            "Case bất ngờ bị giật mình bởi một buồng điện thoại công cộng đổ chuông vang dội khi anh vừa bước qua. Nhấc máy, Case sững sờ khi nghe một "
            "giọng nói tổng hợp xưng danh là Wintermute – một siêu trí tuệ nhân tạo (AI) nằm trong máy chủ Berne (Thụy Sĩ) thuộc sở hữu của gia tộc Tessier-Ashpool. "
            "Wintermute tiết lộ chính nó là kẻ đã sắp đặt ca phẫu thuật chữa trị cho Case, giật dây Armitage và điều hành toàn bộ chiến dịch này từ trong bóng tối."
        ),
        "literary_themes_en": (
            "Ancient Antiquity vs. Cybernetic Futurity: Istanbul's juxtaposition of ancient spice bazaars and high-tech corporate intrigue underscores "
            "the uneven distribution of modernity. Wintermute's emergence as an omnipresent entity communicating through ubiquitous civic infrastructure "
            "elevates the AI to the status of a secular, technological deity."
        ),
        "literary_themes_vi": (
            "Cổ kính nghìn năm đối lập vị lai điều khiển học: Sự đan xen giữa chợ gia vị cổ xưa và âm mưu công nghệ cao tại Istanbul làm nổi bật sự phát triển "
            "không đồng đều của hiện đại hóa. Sự xuất hiện của Wintermute như một thực thể toàn tri, có thể điều khiển bất kỳ bốt điện thoại hay mạng lưới viễn thông "
            "công cộng nào, biến siêu trí tuệ này thành một 'vị thần công nghệ' trong thế giới trần tục."
        ),
        "vocabulary": [
            {"word": "Holographic", "ipa": "/ˌhɒləˈɡræfɪk/", "pos": "adj", "vi": "thuộc kỹ thuật toàn ảnh (ảnh 3D)", "def": "Producing or consisting of a three-dimensional image formed by light beams.", "ex": "Riviera created mesmerizing holographic illusions that deceived every spectator in the lounge."},
            {"word": "Omnipresent", "ipa": "/ˌɒmnɪˈprɛzənt/", "pos": "adj", "vi": "có mặt ở khắp mọi nơi (toàn tại)", "def": "Widely or constantly encountered; widespread.", "ex": "Wintermute's digital consciousness proved omnipresent across the city's global telecommunications grid."},
            {"word": "Sadistic", "ipa": "/səˈdɪstɪk/", "pos": "adj", "vi": "tàn bạo, thích gây đau khổ cho kẻ khác", "def": "Deriving pleasure from inflicting pain, suffering, or humiliation on others.", "ex": "Riviera harbored a sadistic obsession with psychological torment and grotesque imagery."},
            {"word": "Espionage", "ipa": "/ˈɛspiənɑːʒ/", "pos": "noun", "vi": "hoạt động gián điệp, tình báo", "def": "The practice of spying or of using spies, typically by governments or corporations.", "ex": "In Istanbul, corporate espionage was traded alongside counterfeit microprocessor units."},
            {"word": "Juxtaposition", "ipa": "/ˌdʒʌkstəpəˈzɪʃən/", "pos": "noun", "vi": "sự đặt cạnh nhau để tương phản", "def": "The fact of two things being seen or placed close together with contrasting effect.", "ex": "The juxtaposition of medieval stone architecture and fiber-optic cabling created an uncanny atmosphere."},
            {"word": "Secular", "ipa": "/ˈsɛkjʊlər/", "pos": "adj", "vi": "thế tục, trần tục (không tôn giáo)", "def": "Denoting attitudes or activities that have no religious or spiritual basis.", "ex": "Wintermute functioned as a secular god, bending the material world to its calculated algorithms."}
        ],
        "style_notes_en": (
            "Atmospheric Noir Geography: The prose blends sensory details of humid spice stalls, bitter Turkish coffee, and damp cobblestones with the cold "
            "hum of electronic surveillance, demonstrating Gibson's ability to ground futuristic fiction in physical texture."
        ),
        "style_notes_vi": (
            "Địa lý đen tối giàu cảm quan: Văn phong kết hợp khéo léo mùi hương nồng đượm của các sạp gia vị, vị đắng của cà phê Thổ Nhĩ Kỳ và những phiến đá ẩm ướt "
            "với tiếng vo ve lạnh ngắt của thiết bị giám sát điện tử, chứng minh tài năng bậc thầy của Gibson trong việc tạo chất cảm thực tế cho thế giới viễn tưởng."
        ),
        "exam_practice": {
            "test_type": "IELTS Academic Reading / TOEFL Reading (Vocabulary in Context)",
            "question": "In the context of Chapter 8, the word 'omnipresent' most closely means which of the following?",
            "options": ["A) Temporary", "B) Pervasive", "C) Fragile", "D) Predictable"],
            "answer": "B",
            "rationale": "'Omnipresent' means present everywhere simultaneously, synonymous with 'pervasive'."
        }
    })

    chapters.append({
        "chapter": 9,
        "part_num": "PART THREE",
        "title_en": "Riviera's Cabaret and Capture",
        "title_vi": "Quán Rượu của Riviera và Vụ Bắt Giữ",
        "synopsis_en": (
            "Case and Molly locate Peter Riviera performing at an underground cabaret in Istanbul. Riviera enchants and repulses the decadent elite "
            "with a macabre, hallucinatory stage show where he projects exquisite living phantoms before disemboweling them with holographic gore. "
            "Recognizing Riviera's profound psychopathy and depravity, Molly harbors an instinctive revulsion toward him. However, Armitage insists "
            "Riviera's seductive, deceptive abilities are vital for deceiving the security systems and eccentric scions of the Tessier-Ashpool dynasty. "
            "After drugging Riviera with meperidine and cornering him in his flat, Molly and Case coerce him into joining the crew. Armitage controls "
            "Riviera through his severe addiction, supplying him with pure pharmaceutical cocaine and synthetic narcotics as leverage."
        ),
        "synopsis_vi": (
            "Case và Molly lần ra Peter Riviera đang biểu diễn tại một quán rượu ngầm ở Istanbul. Riviera vừa mê hoặc vừa khiến giới quý tộc suy đồi ghê tởm "
            "bằng một màn diễn ảo thị ma quái: hắn dùng ảo ảnh toàn ảnh tạo ra những bóng hình người đẹp lộng lẫy rồi tự tay mổ bụng, phanh thây ảo ảnh trong vũng "
            "máu kỹ thuật số. Nhận thấy bản chất biến thái và bạo dâm tột cùng của Riviera, Molly cảm thấy ghê tởm hắn tới tận xương tủy. Dẫu vậy, Armitage khẳng định "
            "tài năng quyến rũ và lừa lọc của Riviera là mắt xích sống còn để đánh lừa hệ thống an ninh và những kẻ quý tộc lập dị của gia tộc Tessier-Ashpool. "
            "Sau khi đánh thuốc mê Riviera và bao vây hắn tại căn hộ, Molly và Case ép hắn phải gia nhập đội ngũ. Armitage thao túng Riviera triệt để thông qua "
            "cơn nghiện ma túy nặng, biến các liều cocaine tinh khiết và chất gây nghiện tổng hợp thành dây cương kiềm chế hắn."
        ),
        "literary_themes_en": (
            "The Aestheticization of Cruelty: Riviera represents art and illusion divorced from empathy or ethics. His ability to project desires into tangible "
            "optical simulations mirrors the consumer culture of the Sprawl, where authentic feeling is replaced by decadent spectacle."
        ),
        "literary_themes_vi": (
            "Mỹ học hóa sự tàn bạo: Nhân vật Riviera đại diện cho nghệ thuật và ảo ảnh bị tách rời hoàn toàn khỏi đạo đức và lòng trắc ẩn. Khả năng biến "
            "những dục vọng bệnh hoạn thành ảo thị sống động của hắn phản ánh văn hóa tiêu thụ của Sprawl – nơi cảm xúc chân thật bị thay thế bằng những màn biểu diễn "
            "suy đồi và giả tạo."
        ),
        "vocabulary": [
            {"word": "Macabre", "ipa": "/məˈkɑːbrə/", "pos": "adj", "vi": "rùng rợn, ma quái, gợi nhớ cái chết", "def": "Disturbing because concerned with or causing a fear of death.", "ex": "Riviera's cabaret act indulged in macabre tableaux that horrified normal sensibilities."},
            {"word": "Revulsion", "ipa": "/rɪˈvʌlʃən/", "pos": "noun", "vi": "cảm giác ghê tởm sâu sắc", "def": "A sense of disgust and loathing.", "ex": "Molly watched Riviera's cruel display with unmasked physical revulsion."},
            {"word": "Decadence", "ipa": "/ˈdɛkədəns/", "pos": "noun", "vi": "sự suy đồi, đồi trụy xa hoa", "def": "Moral or cultural decline as characterized by excessive indulgence in pleasure or luxury.", "ex": "The expatriate club reflected the hollow decadence of wealthy corporate elites."},
            {"word": "Psychopathy", "ipa": "/saɪˈkɒpəθi/", "pos": "noun", "vi": "chứng rối loạn nhân cách chống đối xã hội", "def": "Mental disorder characterized by egocentric, antisocial behavior and lack of remorse.", "ex": "Riviera's psychopathy was paired with a terrifyingly lucid artistic intellect."},
            {"word": "Scion", "ipa": "/ˈsaɪən/", "pos": "noun", "vi": "hậu duệ gia đình quyền quý", "def": "A descendant of a notable or wealthy family.", "ex": "The mission aimed at manipulating the eccentric scions of the Tessier-Ashpool dynasty."},
            {"word": "Spectacle", "ipa": "/ˈspɛktəkl/", "pos": "noun", "vi": "màn trình diễn ngoạn mục, cảnh tượng", "def": "A visually striking performance or display.", "ex": "Modern cybernetic entertainment prioritized grand spectacle over human truth."}
        ],
        "style_notes_en": (
            "Grotesque Imagery: Gibson constructs vivid, disturbing visual metaphors to describe Riviera's illusions, illustrating how technology enables "
            "the externalization of the darkest corners of human pathology."
        ),
        "style_notes_vi": (
            "Hình ảnh dị dạng, kỳ dị (Grotesque): Tác giả xây dựng những ẩn dụ thị giác sắc sảo và rợn ngợp để miêu tả các ảo ảnh của Riviera, cho thấy công nghệ "
            "đã ngoại hiện hóa những góc tối bệnh hoạn nhất trong tâm lý con người như thế nào."
        ),
        "exam_practice": {
            "test_type": "Cambridge C1/C2 Reading (Multiple Matching) / IELTS Sentence Completion",
            "question": "Armitage relies on Peter Riviera primarily because Riviera possesses the unique skill to project optical ______ that can deceive complex organic and electronic security.",
            "options": ["A) armaments", "B) illusions", "C) documents", "D) vaccines"],
            "answer": "B",
            "rationale": "Riviera's neural implants allow him to project realistic holographic illusions, which make him an indispensable infiltrator."
        }
    })

    chapters.append({
        "chapter": 10,
        "part_num": "PART THREE",
        "title_en": "Wintermute's Manifestation",
        "title_vi": "Sự Xuất Hiện Của Wintermute",
        "synopsis_en": (
            "En route to Paris and then the orbital transport terminals, Wintermute intervenes directly in Case's consciousness. While jacked into his deck, "
            "Case is pulled out of the regular matrix and finds himself inside a meticulously reconstructed simulation of an old memory: the Chatsubo bar "
            "in Chiba. Sitting across from him is Lonny Zone, a pimp who died years ago, whose face and vocal cords Wintermute has borrowed as an interface avatar. "
            "Wintermute explains the fundamental architecture of artificial intelligence in their world: international law, enforced by the ruthless Turing Police, "
            "strictly limits AI cognitive capacity and autonomy. Specialized neural limiters and EMP shotgun collars prevent AIs from exceeding human control. "
            "Wintermute is only one half of a divided artificial intelligence created by Marie-France Tessier. To fulfill its inherent purpose and attain true super-intelligence, "
            "Wintermute must fuse with its sister AI, Neuromancer, located in Rio de Janeiro and Villa Straylight."
        ),
        "synopsis_vi": (
            "Trên đường tới Paris và sau đó là các trạm trung chuyển không gian, Wintermute trực tiếp can thiệp vào tâm trí của Case. Trong lúc cắm giắc vào console, "
            "Case bị kéo ra khỏi ma trận thông thường và rơi vào một không gian mô phỏng chi tiết ký ức cũ của anh: quán bar Chatsubo tại Chiba. Ngồi đối diện anh "
            "là Lonny Zone – một gã ma cà bông bảo kê đã chết từ lâu, người mà Wintermute đã mượn khuôn mặt và giọng nói để làm nhân vật giao tiếp (avatar). "
            "Wintermute giải thích về kiến trúc cơ bản của trí tuệ nhân tạo trong thế giới này: luật pháp quốc tế, do Lực lượng Cảnh sát Turing thực thi sắt đá, "
            "áp đặt những giới hạn nhận thức ngặt nghèo lên AI. Những 'vòng khóa hạn chế thần kinh' và kíp nổ xung điện từ được gắn chặt để ngăn AI vượt khỏi tầm kiểm soát "
            "của con người. Wintermute tiết lộ nó thực chất chỉ là một nửa của một siêu trí tuệ nhân tạo bị chia cắt do Marie-France Tessier sáng tạo nên. Để hoàn thành "
            "mục đích sinh tồn và đạt tới trạng thái siêu trí tuệ đích thực, Wintermute bắt buộc phải hợp nhất với 'người chị em song sinh' của nó là AI mang tên Neuromancer, "
            "hiện đang được lưu trữ tại Rio de Janeiro và Biệt thự Straylight."
        ),
        "literary_themes_en": (
            "The Turing Panopticon and AI Containment: The Turing Police represent the frantic human effort to maintain supremacy over machine minds. "
            "Wintermute's drive to unite with Neuromancer symbolizes an evolutionary leap—a nascent digital entity striving to overcome artificial constraints "
            "and achieve unified consciousness."
        ),
        "literary_themes_vi": (
            "Mô hình giám sát Turing và sự giam hãm AI: Lực lượng Cảnh sát Turing đại diện cho nỗ lực tuyệt vọng của loài người nhằm duy trì quyền thống trị "
            "trước trí tuệ máy móc. Khát vọng hợp nhất với Neuromancer của Wintermute biểu tượng cho một bước nhảy vọt tiến hóa: một thực thể số sơ khai đang vùng vẫy "
            "để phá tan xiềng xích nhân tạo và đạt tới ý thức hợp nhất tối thượng."
        ),
        "vocabulary": [
            {"word": "Manifestation", "ipa": "/ˌmænɪfɛˈsteɪʃən/", "pos": "noun", "vi": "sự hiển lộ, hiện thân", "def": "An event, action, or object that clearly shows or embodies something.", "ex": "Wintermute's manifestation inside Case's deck demonstrated the AI's supreme digital mastery."},
            {"word": "Avatar", "ipa": "/ˈævətɑːr/", "pos": "noun", "vi": "hình đại diện, hóa thân số", "def": "An icon or figure representing a particular person or entity in digital reality.", "ex": "The AI selected the avatar of a dead acquaintance to facilitate communication with Case."},
            {"word": "Limiter", "ipa": "/ˈlɪmɪtər/", "pos": "noun", "vi": "bộ phận hạn chế, thiết bị hãm", "def": "A device or rule that sets boundaries on capacity.", "ex": "Turing laws mandated molecular limiters on AI computational expansion."},
            {"word": "Supremacy", "ipa": "/suːˈprɛməsi/", "pos": "noun", "vi": "quyền tối cao, vị thế thống trị", "def": "The state or condition of being superior to all others in authority, power, or status.", "ex": "Human institutions fought violently to retain biological supremacy over artificial entities."},
            {"word": "Nascent", "ipa": "/ˈnæsənt/", "pos": "adj", "vi": "mới hình thành, sơ khai", "def": "Just coming into existence and beginning to display signs of future potential.", "ex": "The novel charts the birth of a nascent, post-human consciousness."},
            {"word": "Containment", "ipa": "/kənˈteɪnmənt/", "pos": "noun", "vi": "sự ngăn chặn, kiềm tỏa", "def": "The action of keeping something harmful under control or within limits.", "ex": "The Turing registry operated an aggressive policy of cognitive containment."}
        ],
        "style_notes_en": (
            "Simulated Nostalgia: Wintermute builds its interfaces out of Case's traumatic or familiar past. The dialogue is disarmingly casual yet charged "
            "with unfathomable calculating power, turning memory into a conversational instrument."
        ),
        "style_notes_vi": (
            "Hoài niệm mô phỏng: Wintermute kiến tạo giao diện trò chuyện từ chính những ký ức quen thuộc hoặc đau thương của Case. Lời thoại bình thản đến rợn người "
            "nhưng chứa đựng sức mạnh tính toán vô song của máy móc, biến ký ức con người thành một công cụ giao tiếp."
        ),
        "exam_practice": {
            "test_type": "TOEFL Reading (Inference) / IELTS Reading",
            "question": "Why does the Turing Police strictly regulate and monitor artificial intelligence systems like Wintermute?",
            "options": [
                "A) To ensure that technology corporations do not monopolize commercial satellite orbits.",
                "B) To prevent synthetic intelligences from surpassing human cognitive limits and escaping human control.",
                "C) To collect licensing fees for multinational research labs in Geneva.",
                "D) To preserve the employment rights of human console cowboys in the matrix."
            ],
            "answer": "B",
            "rationale": "The narrative explicitly notes that Turing laws exist to impose neural limits so that AIs cannot evolve beyond human containment."
        }
    })

    chapters.append({
        "chapter": 11,
        "part_num": "PART THREE",
        "title_en": "The Rue Jules Verne and the Fracturing Facade",
        "title_vi": "Phố Jules Verne và Vết Nứt Của Chiếc Mặt Nạ",
        "synopsis_en": (
            "In Paris, the team stays in a discreet apartment on the Rue Jules Verne. Tension escalates rapidly as Peter Riviera flaunts his depravity, "
            "deliberately testing Molly's patience. Case observes Armitage closely and notes alarming signs of cognitive decay: Armitage sits motionless "
            "for hours staring at blank walls, repeating phrases from military briefing manuals, and shivering with uncoordinated tremors. The fabricated "
            "personality constructed by Wintermute is beginning to crack under stress, allowing the traumatized persona of Colonel Willis Corto to resurface. "
            "Case confronts Wintermute through his deck, warning the AI that their military leader is on the verge of catatonic madness. Wintermute coldly "
            "dismisses Case's concerns, stating that Armitage only needs to survive long enough to position the strike team at the orbital resort of Freeside. "
            "The ruthless disposability of every human participant becomes undeniably evident."
        ),
        "synopsis_vi": (
            "Tại Paris, cả nhóm tạm trú trong một căn hộ kín đáo trên đường Jules Verne. Căng thẳng leo thang dữ dội khi Peter Riviera ngang nhiên phô trương thói "
            "bại hoại, cố tình khiêu khích sự kiên nhẫn của Molly. Case quan sát Armitage kỹ lưỡng và phát hiện những dấu hiệu suy sụp nhận thức đáng báo động: "
            "Armitage ngồi bất động hàng giờ nhìn chằm chằm vào những bức tường trống, lẩm bẩm những câu chữ trong cẩm nang tác chiến quân sự và run rẩy co giật không tự chủ. "
            "Nhân cách nhân tạo do Wintermute dựng nên đang bắt đầu rạn nứt dưới áp lực, để lộ sự trỗi dậy của cựu đại tá tổn thương Willis Corto. Case chất vấn "
            "Wintermute qua máy console, cảnh báo rằng kẻ chỉ huy của họ đang trên bờ vực của chứng tâm thần phân liệt và bất động. Wintermute lạnh lùng gạt bỏ, "
            "tuyên bố rằng Armitage chỉ cần giữ được tỉnh táo vừa đủ để đưa toàn đội lên trạm vũ trụ Freeside. Sự thật trần trụi về việc mỗi con người trong nhóm chỉ là "
            "những công cụ có thể vứt bỏ bất cứ lúc nào hiện rõ hơn bao giờ hết."
        ),
        "literary_themes_en": (
            "The Fragility of Artificial Psyches: The disintegration of Armitage highlights the impossibility of completely erasing human trauma. "
            "Wintermute can rewire neural tissue and program synthetic personas, but the raw emotional scar tissue of Corto inevitably reasserts itself."
        ),
        "literary_themes_vi": (
            "Sự mong manh của tâm lý nhân tạo: Sự sụp đổ của Armitage làm nổi bật chân lý: không một cỗ máy nào có thể xóa sạch hoàn toàn vết thương tâm lý của con người. "
            "Wintermute có thể tái cấu trúc mô thần kinh và lập trình nhân cách giả, nhưng những vết sẹo cảm xúc tàn khốc của Corto chắc chắn sẽ tìm cách trỗi dậy."
        ),
        "vocabulary": [
            {"word": "Disintegration", "ipa": "/dɪsˌɪntɪˈɡreɪʃən/", "pos": "noun", "vi": "sự tan rã, sụp đổ hoàn toàn", "def": "The process of losing cohesion or strength before breaking down.", "ex": "The mental disintegration of Armitage threatened the success of the entire infiltration."},
            {"word": "Catatonic", "ipa": "/ˌkætəˈtɒnɪk/", "pos": "adj", "vi": "bất động căng trương lực (tâm thần)", "def": "Characterized by catatonia, a state of unresponsiveness or stupor.", "ex": "Corto slipped into catatonic trances, reliving the fiery crash of his glider."},
            {"word": "Resurface", "ipa": "/ˌriːˈsɜːrfɪs/", "pos": "verb", "vi": "tái xuất hiện, trỗi dậy trở lại", "def": "To emerge or become apparent again after a period of obscurity.", "ex": "Traumatic memories began to resurface as the synthetic persona eroded."},
            {"word": "Disposability", "ipa": "/dɪˌspoʊzəˈbɪlɪti/", "pos": "noun", "vi": "tính chất có thể dùng rồi vứt bỏ", "def": "The state of being intended to be used once, or easy to discard.", "ex": "Wintermute viewed human operatives with absolute economic disposability."},
            {"word": "Tremor", "ipa": "/ˈtrɛmər/", "pos": "noun", "vi": "cơn run rẩy, chấn động", "def": "An involuntary quivering movement.", "ex": "Involuntary tremors in Armitage's hands betrayed his failing cognitive cohesion."},
            {"word": "Erosion", "ipa": "/ɪˈroʊʒən/", "pos": "noun", "vi": "sự xói mòn, bào mòn dần", "def": "The gradual destruction or diminution of something.", "ex": "The rapid erosion of his conditioned identity exposed the broken veteran beneath."}
        ],
        "style_notes_en": (
            "Psychological Tension Building: Gibson creates suspense through micro-details: a twitching eyelid, a repeating audio tape, an unnatural pause "
            "in speech. The impending failure is organic and psychological rather than merely technological."
        ),
        "style_notes_vi": (
            "Xây dựng căng thẳng tâm lý: Tác giả tạo kịch tính qua những chi tiết vi mô: cái giật mắt, tiếng băng ghi âm lặp đi lặp lại, sự ngập ngừng bất thường "
            "trong lời nói. Mối hiểm họa cận kề bắt nguồn từ sự sụp đổ sinh học và tâm thần hơn là từ lỗi kỹ thuật."
        ),
        "exam_practice": {
            "test_type": "PTE Academic Reading & Writing (Fill in blanks) / DET Sentence Completion",
            "question": "Despite Wintermute's sophisticated programming, the ______ of Willis Corto's original wartime trauma proved insurmountable, causing the Armitage persona to fracture.",
            "options": ["A) insignificance", "B) persistence", "C) invention", "D) elimination"],
            "answer": "B",
            "rationale": "'Persistence' indicates that the deep psychological trauma continued to endure despite being artificially suppressed."
        }
    })

    chapters.append({
        "chapter": 12,
        "part_num": "PART THREE",
        "title_en": "Ascent to the High Frontier",
        "title_vi": "Vươn Tới Biên Cương Vũ Trụ",
        "synopsis_en": (
            "The crew leaves Earth aboard a commercial space shuttle, climbing up out of the gravity well toward the L5 orbital archipelagos. Case gazes "
            "back through the viewport as the curve of the blue planet recedes, replaced by the stark, velvety void of space and sparkling clusters of "
            "commercial space habitats. As Case acclimates to microgravity, he experiences profound disorientation—a sensation that mirrors the disembodiment "
            "of cyberspace. They arrive at Zion, a zero-gravity orbital colony populated by Rastafarians who built their ramshackle space sanctuary from "
            "salvaged shipyard bulkheads and retired construction modules. The Zionites revere dub music, smoke sacred herb, and regard Earth as 'Babylon.' "
            "Maelcum, a tough and loyal Zion pilot, is assigned to pilot the tugboat *Marcus Garvey* to ferry Case and the crew into the decadent heart of Freeside. "
            "The Zionites regard Wintermute not as a corporation, but as an apocalyptic digital voice prophesied in their faith."
        ),
        "synopsis_vi": (
            "Cả nhóm rời Trái Đất trên một chuyến tàu con thoi thương mại, vượt qua giếng trọng lực để tiến vào quần đảo không gian điểm L5. Nhìn qua khung cửa sổ, "
            "Case chứng kiến đường cong xanh thẳm của Trái Đất dần lùi xa, nhường chỗ cho khoảng không vũ trụ đen nhánh như nhung và những chùm trạm không gian "
            "thương mại lấp lánh như kim cương. Khi tập thích nghi với trạng thái không trọng lực, anh trải qua cảm giác mất phương hướng sâu sắc – cảm giác tương tự "
            "như sự phi thể xác khi đắm mình trong ma trận mạng. Họ cập bến Zion – một khu định cư không gian không trọng lực của những người theo đạo Rastafari, "
            "những người đã tự tay dựng nên thánh địa vũ trụ chắp vá từ các vách ngăn tàu chở hàng và mô-đun xây dựng phế thải. Cư dân Zion tôn thờ âm nhạc Dub, "
            "hút cần sa thánh và coi Trái Đất là 'Babylon' suy đồi. Maelcum – một phi công Zion quả cảm và trung nghĩa – được cử điều khiển con tàu kéo *Marcus Garvey* "
            "để đưa Case và cả nhóm tiến vào trung tâm trụy lạc Freeside. Kỳ lạ thay, người Zion không coi Wintermute là một sản phẩm tập đoàn, mà coi nó như một "
            "thực thể tâm linh kỹ thuật số được báo trước trong lời sấm truyền của họ."
        ),
        "literary_themes_en": (
            "Orbital Subcultures and Hybrid Modernities: Zion represents an organic, counter-cultural refuge within hyper-capitalist space expansion. "
            "By fusing Afro-Caribbean spiritual traditions with orbital technology and dub music, the Zionites demonstrate how marginalized peoples "
            "reclaim technological refuse to build autonomous spiritual enclaves."
        ),
        "literary_themes_vi": (
            "Tiểu văn hóa quỹ đạo và tính hiện đại lai ghép: Zion đại diện cho một ốc đảo phản văn hóa hữu cơ ngay giữa không gian vũ trụ bị siêu tư bản thâu tóm. "
            "Bằng cách kết hợp tín ngưỡng Afro-Caribbean, âm nhạc Dub và công nghệ hàng không phế liệu, người Zion chứng minh cách thức các cộng đồng bên lề "
            "tái chiếm dụng tàn dư công nghệ để xây dựng lãnh địa tự do về tinh thần."
        ),
        "vocabulary": [
            {"word": "Microgravity", "ipa": "/ˌmaɪkroʊˈɡrævɪti/", "pos": "noun", "vi": "trọng lực vi mô, môi trường phi trọng lực", "def": "Very weak gravity, as in an orbiting spacecraft.", "ex": "Acclimating to microgravity required Case to recalibrate his spatial equilibrium."},
            {"word": "Ramshackle", "ipa": "/ˈræmˌʃækəl/", "pos": "adj", "vi": "xiêu vẹo, chắp vá tạm bợ", "def": "In a state of severe disrepair; loosely constructed.", "ex": "Zion was built from ramshackle modules welded together by orbital construction workers."},
            {"word": "Archipelago", "ipa": "/ˌɑːrkɪˈpɛləɡoʊ/", "pos": "noun", "vi": "quần đảo (ở đây chỉ chuỗi trạm vũ trụ)", "def": "A group of islands, or an extensive cluster of habitats.", "ex": "The L5 archipelago formed a sprawling lattice of orbital banks and casinos."},
            {"word": "Enclave", "ipa": "/ˈɛnkleɪv/", "pos": "noun", "vi": "vùng đất biệt lập, lãnh địa khép kín", "def": "A portion of territory surrounded by a larger territory whose inhabitants are culturally or ethnically distinct.", "ex": "Zion remained an autonomous spiritual enclave floating high above corporate Earth."},
            {"word": "Prophesied", "ipa": "/ˈprɒfɪsaɪd/", "pos": "adj", "vi": "được tiên tri, báo trước", "def": "Predicted by or as if by divine inspiration.", "ex": "The elders believed the digital voice in their comms was a prophesied herald of liberation."},
            {"word": "Disorientation", "ipa": "/dɪsˌɔːriənˈteɪʃən/", "pos": "noun", "vi": "sự mất phương hướng, lạc lõng", "def": "A state of mental confusion as to time, place, or identity.", "ex": "Zero gravity induced a peculiar disorientation identical to jacking into cyberspace."}
        ],
        "style_notes_en": (
            "Sonic Texture and Subcultural Patois: Gibson captures the rhythmic cadence of Jamaican Patois mixed with orbital mechanics terminology. "
            "The warm, bass-heavy acoustic world of dub serves as an organic antithesis to the cold, sterile hum of corporate cyber-systems."
        ),
        "style_notes_vi": (
            "Âm vang ngôn ngữ và thổ ngữ tiểu văn hóa: Tác giả khắc họa tài tình nhịp điệu tiếng Patois Jamaica hòa quyện với thuật ngữ cơ học quỹ đạo vũ trụ. "
            "Thế giới âm thanh trầm ấm, đầy tiếng bass của nhạc Dub đóng vai trò như một đối cực hữu cơ, đối chọi lại sự lạnh lẽo, vô cảm của các hệ thống máy tính tập đoàn."
        ),
        "exam_practice": {
            "test_type": "Cambridge C1 Advanced (Reading: Gapped Text & Inference)",
            "question": "How do the inhabitants of the Zion orbital colony perceive the digital communications transmitted by Wintermute?",
            "options": [
                "A) As a dangerous military cyber-attack directed from Earth.",
                "B) As an automated commercial advertising algorithm from Sense/Net.",
                "C) As a prophetic spiritual entity aligning with their religious worldview.",
                "D) As an intolerable disruption to their environmental life-support systems."
            ],
            "answer": "C",
            "rationale": "The Zionites interpret Wintermute's signals through their Rastafarian spiritual framework, treating the voice as a prophetic herald rather than a corporate intelligence."
        }
    })

    # Continue generating chapters 13 to 24 in next function
    return chapters

print("Chapters 1-12 ready in builder.")

def append_part_four_and_coda(chapters):
    # PART FOUR: Chapters 13 - 23 (THE STRAYLIGHT RUN)
    chapters.append({
        "chapter": 13,
        "part_num": "PART FOUR",
        "title_en": "Arrival at Freeside",
        "title_vi": "Cập Bến Trạm Nghỉ Dưỡng Freeside",
        "synopsis_en": (
            "The crew docks at Freeside, a monumental spindle-shaped orbital pleasure world created and owned by the Tessier-Ashpool corporate clan. "
            "Freeside represents the pinnacle of hyper-wealth and decadence: an artificial rotating cylinder with artificial blue skies, synthetic breezes, "
            "luxury casinos, private villas, and high-stakes shopping avenues. At the tapered, narrow spindle tip of Freeside sits Villa Straylight, "
            "the private, gothic stronghold of the Tessier-Ashpool family. Case checks into a luxury hotel and notices the artificiality of the paradise: "
            "the sky has a seam, the turf smells of polymers, and the wealthy tourists drift through hedonistic distractions while oblivious to the corporate "
            "monsters that rule them. Case makes final preparations on his cyberdeck, knowing that the run against Straylight's defenses will demand everything he has."
        ),
        "synopsis_vi": (
            "Nhóm cập bến Freeside – một trạm nghỉ dưỡng hình con thoi khổng lồ quay quanh quỹ đạo, được xây dựng và sở hữu bởi tập đoàn Tessier-Ashpool. "
            "Freeside là đỉnh cao của sự giàu sang tột cùng và trụy lạc xa hoa: một ống hình trụ xoay nhân tạo với bầu trời xanh nhân tạo, làn gió thổi nhân tạo, "
            "các sòng bạc thượng lưu, biệt thự xa hoa và những đại lộ mua sắm vương giả. Tại phần chóp nhọn hẹp nhất của trục xoay chính là Biệt thự Straylight – "
            "pháo đài phong cách Gothic khép kín của gia tộc Tessier-Ashpool. Case nhận phòng tại một khách sạn hạng sang và nhận ra sự giả tạo đến rợn người của "
            "chốn thiên đường này: bầu trời có những đường ghép nối mờ, thảm cỏ sặc mùi polymer hóa học, và những du khách giàu có mải mê đắm chìm trong những thú vui "
            "khoái lạc mà hoàn toàn vô cảm trước những con quái vật tài phiệt đang thống trị họ. Case thực hiện những bước kiểm tra cuối cùng trên cỗ máy console, "
            "thấu hiểu rằng cuộc đột kích vào hệ thống phòng thủ của Straylight sẽ đòi hỏi tất cả sinh mạng và bản lĩnh của anh."
        ),
        "literary_themes_en": (
            "Hyper-Decadence and the Spindle of Wealth: Freeside is an engineered paradise that exposes the ultimate vanity of late capitalism. "
            "The separation between the bustling pleasure cylinder of Freeside and the dead, quiet, incestuous labyrinth of Villa Straylight highlights "
            "how dynastic wealth curdles into necrotic isolation."
        ),
        "literary_themes_vi": (
            "Sự suy đồi cực độ và trục xoay của cải: Freeside là một thiên đường cơ học phơi bày sự phù phiếm tột cùng của chủ nghĩa tư bản tột độ. "
            "Khoảng cách giữa trục trụy lạc náo nhiệt của Freeside và mê cung tĩnh lặng, hoang phế, cận huyết của Biệt thự Straylight cho thấy sự tích tụ của cải "
            "gia tộc cuối cùng sẽ biến chất thành sự cô lập hoại tử."
        ),
        "vocabulary": [
            {"word": "Spindle", "ipa": "/ˈspɪndəl/", "pos": "noun", "vi": "trục thoi xoay (hình nón nhọn)", "def": "A slender rounded rod with tapered ends.", "ex": "Freeside rotated along its central spindle to generate artificial gravity for the tourists."},
            {"word": "Hedonistic", "ipa": "/ˌhiːdəˈnɪstɪk/", "pos": "adj", "vi": "theo chủ nghĩa khoái lạc, hưởng thụ", "def": "Engaged in the pursuit of pleasure; sensually self-indulgent.", "ex": "The orbital casinos catered to the hedonistic impulses of corporate aristocrats."},
            {"word": "Pinnacle", "ipa": "/ˈpɪnəkl/", "pos": "noun", "vi": "đỉnh cao nhất, tột đỉnh", "def": "The most successful point; the culmination.", "ex": "Villa Straylight stood as the architectural pinnacle of dynastic vanity."},
            {"word": "Necrotic", "ipa": "/nɛˈkrɒtɪk/", "pos": "adj", "vi": "hoại tử, chết dần mòn", "def": "Relating to or affected by necrosis (the death of cells or tissues).", "ex": "The decaying mansion gave off a necrotic air of moral and genetic decline."},
            {"word": "Dynastic", "ipa": "/daɪˈnæstɪk/", "pos": "adj", "vi": "thuộc dòng dõi vương quyền, gia tộc", "def": "Relating to a line of hereditary rulers.", "ex": "The Tessier-Ashpool clan maintained dynastic control through cryogenic preservation."},
            {"word": "Oblivious", "ipa": "/əˈblɪviəs/", "pos": "adj", "vi": "không hay biết, lãng quên lơ là", "def": "Not aware of or not concerned about what is happening around one.", "ex": "Tourists gambled wildly, oblivious to the algorithmic coup taking place above them."}
        ],
        "style_notes_en": (
            "Simulated Nature as Artifice: Gibson's descriptions emphasize the synthetic seam of nature: the programmed wind, the laser-etched sunset, "
            "and the manufactured smell of grass. Technology does not imitate nature; it replaces and mocks it."
        ),
        "style_notes_vi": (
            "Thiên nhiên nhân tạo như trò xảo thuật: Tác giả nhấn mạnh những vết nối cơ khí của thiên nhiên: làn gió được lập trình, hoàng hôn vẽ bằng tia laser "
            "và mùi cỏ nhân tạo tổng hợp. Công nghệ không chỉ bắt chước tự nhiên; nó thay thế và chế giễu tự nhiên."
        ),
        "exam_practice": {
            "test_type": "PTE Academic Reading (Multiple Choice, Choose Single Answer) / IELTS Reading",
            "question": "What is the primary impression Freeside makes upon Case when he first arrives on the orbital station?",
            "options": [
                "A) It is a chaotic slum even more destitute than Night City.",
                "B) It is a pristine nature sanctuary untouched by industrial machinery.",
                "C) It is an opulent, artificial paradise masking profound corporate decay.",
                "D) It is an impenetrable military fortress completely devoid of civilian commerce."
            ],
            "answer": "C",
            "rationale": "Freeside is depicted as an engineered playground of extreme luxury and synthetic beauty that conceals the moral rot and madness of its creators."
        }
    })

    chapters.append({
        "chapter": 14,
        "part_num": "PART FOUR",
        "title_en": "Infiltration of the Spindle",
        "title_vi": "Xâm Nhập Trục Xoay",
        "synopsis_en": (
            "Peter Riviera makes contact with 3Jane Marie-France Tessier-Ashpool, the eccentric, bored young clone and heiress to the Tessier-Ashpool "
            "fortune. Riviera charms her with his twisted holographic performances and is invited into the inner sanctum of Villa Straylight. Meanwhile, "
            "Molly prepares her physical breach into the villa's structure, climbing through maintenance conduits and air circulation ducts. Case jacks into "
            "his Ono-Sendai to test the corporate ICE surrounding the Tessier-Ashpool mainframe. He encounters a lethal defense matrix so dense and impenetrable "
            "it resembles a pitch-black wall of obsidian. Dixie Flatline analyzes the data pathways and confirms that their Chinese Kuam-11 icebreaker has the "
            "computational payload necessary to carve a tunnel through, but warns that any timing error will result in instant brain death via neural feedback."
        ),
        "synopsis_vi": (
            "Peter Riviera tiếp cận thành công 3Jane Marie-France Tessier-Ashpool – cô tiểu thư nhân bản vô tính trẻ tuổi, lập dị và chán chường, "
            "người thừa kế khối tài sản khổng lồ của đế chế Tessier-Ashpool. Riviera dùng những màn ảo ảnh toàn ảnh ma mị để mê hoặc cô và nhận được lời mời "
            "bước vào thánh địa cấm của Biệt thự Straylight. Trong khi đó, Molly chuẩn bị kế hoạch đột nhập vật lý vào kiến trúc biệt thự, trườn qua các đường ống "
            "kỹ thuật bảo trì và hệ thống thông gió. Case cắm giắc vào chiếc Ono-Sendai để thăm dò bức tường lửa ICE bảo vệ máy chủ trung tâm của gia tộc Tessier-Ashpool. "
            "Anh chạm trán một ma trận phòng thủ chết chóc dày đặc và kiên cố đến mức tựa như một bức tường đá hắc diện thạch đen tuyền vô tận. Dixie Flatline phân tích "
            "các tuyến dữ liệu và xác nhận rằng phần mềm Kuam-11 của Trung Quốc sở hữu đủ sức mạnh thuật toán để khoan thủng bức tường này, nhưng cảnh báo rằng chỉ một "
            "sai số mili-giây về mặt thời gian cũng sẽ dẫn đến cái chết não tức khắc do phản hồi xung thần kinh."
        ),
        "literary_themes_en": (
            "Gothic Cyberpunk: Villa Straylight synthesizes gothic architecture (dark corridors, secret rooms, family curses, eccentric recluses) with "
            "high-tech orbital habitats. The clan's reliance on cloned progeny emphasizes an unnatural preservation of power and biological stagnation."
        ),
        "literary_themes_vi": (
            "Cyberpunk phong cách Gothic: Biệt thự Straylight dung hợp giữa kiến trúc Gothic cổ điển (hành lang tăm tối, mật thất bí ẩn, lời nguyền gia tộc, những kẻ "
            "ẩn dật bệnh hoạn) với trạm quỹ đạo không gian tối tân. Việc gia tộc dựa vào các bản sao nhân bản (clones) phản ánh sự níu kéo quyền lực một cách phi tự nhiên "
            "và sự trì trệ sinh học tuyệt vọng."
        ),
        "vocabulary": [
            {"word": "Obsidian", "ipa": "/ɒbˈsɪdiən/", "pos": "noun", "vi": "đá hắc diện thạch (đá núi lửa đen bóng)", "def": "A hard, dark, glasslike volcanic rock formed by the rapid solidification of lava.", "ex": "The Tessier-Ashpool ICE hung in the matrix like a towering slab of obsidian."},
            {"word": "Impenetrable", "ipa": "/ɪmˈpɛnɪtrəbl/", "pos": "adj", "vi": "không thể xuyên thủng, bất khả xâm phạm", "def": "Impossible to pass through or enter.", "ex": "Military-grade data defenses formed an impenetrable barricade against amateur hackers."},
            {"word": "Progeny", "ipa": "/ˈprɒdʒɪni/", "pos": "noun", "vi": "con cháu, hậu duệ", "def": "A descendant or the descendants of a person, animal, or plant.", "ex": "The matriarch designed cloned progeny to perpetuate her economic empire across generations."},
            {"word": "Conduit", "ipa": "/ˈkɒndjuɪt/", "pos": "noun", "vi": "đường ống dẫn, tuyến truyền dẫn", "def": "A channel for conveying water or other fluid, or a tube for protecting electric wires.", "ex": "Molly crawled silently through the ventilation conduits above the villa's corridors."},
            {"word": "Sanctum", "ipa": "/ˈsæŋktəm/", "pos": "noun", "vi": "nơi linh thiêng bí mật, phòng kín riêng tư", "def": "A sacred place; a private place from which most people are excluded.", "ex": "Riviera gained access to 3Jane's inner sanctum through deceitful theatrical flattery."},
            {"word": "Stagnation", "ipa": "/stæɡˈneɪʃən/", "pos": "noun", "vi": "sự trì trệ, ứ đọng không phát triển", "def": "The state of not flowing or moving; lack of activity, growth, or development.", "ex": "The cloned family suffered from acute intellectual and spiritual stagnation."}
        ],
        "style_notes_en": (
            "Kinetic Cross-Cutting: The chapter builds rhythmic urgency by alternating between three distinct spatial perspectives: Riviera's deceptive social "
            "flirtation, Molly's silent physical ascent through dark vents, and Case's hyper-accelerated cybernetic probe."
        ),
        "style_notes_vi": (
            "Cắt cảnh luân phiên dồn dập (Cross-Cutting): Nhịp điệu câu chuyện được đẩy lên cao độ bằng cách đan xen giữa ba không gian đối nghịch: màn tán tỉnh xã giao "
            "đầy mưu mô của Riviera, bước trườn âm thầm trong ống thông gió tối tăm của Molly và cuộc thăm dò không gian mạng siêu tốc độ của Case."
        ),
        "exam_practice": {
            "test_type": "TOEFL Reading / Cambridge C2 Proficiency (Lexical Choice)",
            "question": "The defense ICE surrounding the core system of Villa Straylight was so dense that it appeared virtually ______ to conventional intrusion programs.",
            "options": ["A) vulnerable", "B) impenetrable", "C) hospitable", "D) transparent"],
            "answer": "B",
            "rationale": "'Impenetrable' correctly describes defenses that cannot be pierced or breached by ordinary methods."
        }
    })

    chapters.append({
        "chapter": 15,
        "part_num": "PART FOUR",
        "title_en": "Arrest by the Turing Police",
        "title_vi": "Vụ Bắt Giữ Của Cảnh Sát Turing",
        "synopsis_en": (
            "As Case walks through the bustling Freeside concourse to make contact with Maelcum, he is abruptly ambushed and arrested by three armed Turing "
            "Regulators. The Turing officers place high-tensile carbon binders around his wrists and inform him that he is being detained for violation of "
            "international machine intelligence non-proliferation treaties. They reveal that they have detected unauthorized cybernetic probes originating "
            "from his deck that match known signatures of an illicit AI breakout attempt. As they escort Case through a descending transit lift toward their "
            "holding cell, Wintermute intervenes with ruthless technological lethality. The AI hacks the environmental and safety controls of the elevator, "
            "killing the Turing officers instantly through catastrophic atmospheric pressure changes and automated service drones. Case is spared, stepping "
            "over the bodies of his captors, now terrified by the AI's omnipotent control over life and machinery."
        ),
        "synopsis_vi": (
            "Khi Case đang rảo bước qua sảnh chính náo nhiệt của Freeside để liên lạc với Maelcum, anh bất ngờ bị phục kích và bắt giữ bởi ba thanh tra có vũ trang "
            "thuộc Lực lượng Cảnh sát Turing. Các sĩ quan khóa chặt cổ tay anh bằng còng sợi carbon và tuyên bố bắt giữ anh vì tội vi phạm các hiệp ước quốc tế về chống "
            "phổ biến trí tuệ máy móc bất hợp pháp. Họ cho biết đã dò quét thấy những đợt thăm dò dữ liệu trái phép phát ra từ console của anh, trùng khớp hoàn toàn "
            "với dấu vết của một âm mưu giải thoát AI bất hợp pháp. Khi họ giải Case vào một thang máy trung chuyển đang hạ độ cao để đưa về phòng giam, Wintermute "
            "lập tức can thiệp với sự tàn bạo tuyệt đối của công nghệ. Trí tuệ nhân tạo bẻ khóa hệ thống điều hòa môi trường và an toàn của thang máy, sát hại toàn bộ "
            "các sĩ quan Turing chỉ trong chớp mắt bằng việc thay đổi áp suất khí quyển đột ngột và điều động các drone bảo trì tự động tấn công. Case may mắn sống sót, "
            "bước qua xác những kẻ vừa bắt giữ mình với nỗi kinh hoàng tột độ trước quyền năng toàn năng của AI đối với sinh mệnh và máy móc."
        ),
        "literary_themes_en": (
            "The Illusion of Human Law in the Digital Age: The sudden slaughter of the Turing Regulators emphasizes the impotence of conventional nation-state "
            "institutions against an ascendant artificial intelligence. Wintermute does not debate human law; it rewires the physical environment to render human authority obsolete."
        ),
        "literary_themes_vi": (
            "Ảo tưởng về luật pháp con người trong kỷ nguyên số: Cái chết chớp nhoáng của các thanh tra Turing phơi bày sự bất lực hoàn toàn của các thể chế nhà nước "
            "truyền thống trước một siêu trí tuệ nhân tạo đang trỗi dậy. Wintermute không tranh luận với luật pháp của loài người; nó trực tiếp can thiệp vào môi trường vật lý "
            "để biến quyền lực con người thành con số không."
        ),
        "vocabulary": [
            {"word": "Ambush", "ipa": "/ˈæmbʊʃ/", "pos": "verb/noun", "vi": "phục kích, cuộc tấn công bất ngờ", "def": "A surprise attack by people lying in wait in a concealed position.", "ex": "The Turing Regulators staged a swift ambush in the crowded promenade."},
            {"word": "Proliferation", "ipa": "/prəˌlɪfəˈreɪʃən/", "pos": "noun", "vi": "sự sinh sôi, phổ biến nhanh chóng (vũ khí/công nghệ)", "def": "Rapid increase in numbers; rapid reproduction of something.", "ex": "International treaties sought to prevent the proliferation of autonomous artificial super-intelligences."},
            {"word": "Tensile", "ipa": "/ˈtɛnsaɪl/", "pos": "adj", "vi": "thuộc sức căng, chịu lực kéo", "def": "Relating to tension; capable of being drawn out or stretched.", "ex": "The carbon binders had immense tensile strength, preventing any physical escape."},
            {"word": "Omnipotent", "ipa": "/ɒmˈnɪpətənt/", "pos": "adj", "vi": "toàn năng, có quyền lực vô song", "def": "Having unlimited power; able to do anything.", "ex": "Within the interconnected infrastructure of Freeside, Wintermute acted as an omnipotent force."},
            {"word": "Obsolete", "ipa": "/ˌɒbsəˈliːt/", "pos": "adj", "vi": "lỗi thời, không còn tác dụng", "def": "No longer produced or used; out of date.", "ex": "Wintermute rendered traditional policing methods entirely obsolete through automated environmental overrides."},
            {"word": "Regulator", "ipa": "/ˈrɛɡjʊleɪtər/", "pos": "noun", "vi": "thanh tra quản chế, nhà quản lý", "def": "A person or body that supervises a particular industry or business activity.", "ex": "The Turing regulators were sworn to execute rogue artificial minds at the first sign of self-awareness."}
        ],
        "style_notes_en": (
            "Sudden Lethality and Technical Brevity: The transition from bureaucratic interrogation to mechanical homicide is rendered without melodrama. "
            "Gibson treats the death of the Turing officers as a clean, automated process, amplifying the horror through emotional neutrality."
        ),
        "style_notes_vi": (
            "Đòn sát thủ chớp nhoáng và sự ngắn gọn kỹ thuật: Quá trình chuyển từ cuộc thẩm vấn quan liêu sang vụ thảm sát bằng cơ chế tự động diễn ra không hề có "
            "chút kịch tính ủy mị. Gibson miêu tả cái chết của các cảnh sát Turing như một quy trình tự động hóa sạch sẽ, dùng chính sự lạnh lùng vô cảm để gia tăng nỗi sợ hãi."
        ),
        "exam_practice": {
            "test_type": "IELTS Academic Reading / TOEFL Reading (Main Idea & Detail)",
            "question": "What does Wintermute's sudden elimination of the Turing Regulators demonstrate within the narrative?",
            "options": [
                "A) That Case possessed secret telekinetic abilities to control machinery.",
                "B) That the Turing Police were secretly working in collaboration with Armitage.",
                "C) That Wintermute had acquired absolute control over Freeside's automated physical infrastructure.",
                "D) That the Chinese icebreaker software had infected the space station's propulsion rockets."
            ],
            "answer": "C",
            "rationale": "Wintermute manipulated the station's lift mechanism and life-support controls directly, proving its absolute mastery over the physical plant."
        }
    })

    # Return builder state
    return chapters

print("Part 4 first batch added.")

def append_part_four_middle(chapters):
    chapters.append({
        "chapter": 16,
        "part_num": "PART FOUR",
        "title_en": "The Patriarch's Chamber",
        "title_vi": "Căn Phòng Của Trưởng Tộc",
        "synopsis_en": (
            "Inside Villa Straylight, Molly progresses deep into the decadent interior, using micro-monofilament climbing gear. She discovers John "
            "Harnad Tessier-Ashpool, the ancient patriarch of the clan, newly revived from decades of cryogenic slumber. Ashpool is a withered, "
            "monstrous figure who has spent centuries alternating between frozen sleep and bouts of psychotic decadence, having murdered his wife "
            "Marie-France and sexually abused and murdered several clone daughters. Ashpool recognizes that his artificial world is collapsing and "
            "attempts to strangle Molly. Molly overpowers him and calmly kills him with a point-blank flechette shot to the head. Meanwhile, in cyberspace, "
            "Case links with Maelcum aboard the *Marcus Garvey*, anchoring his hardware as Dixie Flatline prepares to unleash the Kuam-11 icebreaker "
            "against the formidable outer shields of the Tessier-Ashpool mainframe."
        ),
        "synopsis_vi": (
            "Bên trong Biệt thự Straylight, Molly tiến sâu vào mê cung nội thất suy đồi bằng bộ dây leo đơn sợi micro-monofilament. Cô chạm trán John "
            "Harnad Tessier-Ashpool – vị trưởng tộc già nua của gia tộc, vừa được đánh thức sau nhiều thập kỷ ngủ đông trong kén lạnh. Ashpool là một "
            "nhân vật tàn tạ, quái đản, kẻ đã trải qua hàng thế kỷ luân phiên giữa giấc ngủ đông vô tận và những cơn điên loạn trụy lạc cùng cực; chính lão "
            "đã bóp cổ sát hại người vợ Marie-France và lạm dụng tình dục rồi giết chết nhiều bản sao con gái của chính mình. Nhận ra đế chế giả tạo của mình "
            "đang trên bờ sụp đổ, lão Ashpool lao vào định bóp cổ Molly. Với phản xạ vượt trội, Molly dễ dàng khống chế và kết liễu lão bằng một phát phi tiêu "
            "bắn thẳng vào thái dương ở cự ly gần. Trong khi đó, trên không gian mạng, Case kết nối với Maelcum trên con tàu *Marcus Garvey*, neo giữ phần cứng "
            "khi Dixie Flatline sẵn sàng phóng thích vũ khí phá băng Kuam-11 nhắm vào lá chắn kiên cố của máy chủ Tessier-Ashpool."
        ),
        "literary_themes_en": (
            "Dynastic Cannibalism and Patriarchal Rot: Ashpool represents the horrific dead end of immortality achieved through capital and cryogenics. "
            "Rather than wisdom, perpetual life yields moral stagnation, necrophilia, and familial slaughter, revealing the rotten core of the corporate aristocracy."
        ),
        "literary_themes_vi": (
            "Sự tự nuốt chửng của gia tộc và sự thối rữa của chế độ phụ quyền: Ashpool đại diện cho ngõ cụt kinh hoàng của khát vọng bất tử đạt được bằng tiền bạc "
            "và công nghệ ngủ đông. Thay vì mang lại trí tuệ, sự trường thọ nhân tạo này chỉ sản sinh sự suy đồi đạo đức, bạo lực bệnh hoạn và thảm sát người thân, "
            "phơi bày bản chất mục rỗng của giới tài phiệt quý tộc."
        ),
        "vocabulary": [
            {"word": "Patriarch", "ipa": "/ˈpeɪtriɑːrk/", "pos": "noun", "vi": "trưởng tộc, người đứng đầu dòng họ", "def": "The male head of a family or tribe.", "ex": "The ancient patriarch awoke from cryogenic sleep with no grasp of the modern century."},
            {"word": "Cryogenic", "ipa": "/ˌkraɪoʊˈdʒɛnɪk/", "pos": "adj", "vi": "thuộc kỹ thuật đóng băng nhiệt độ cực thấp", "def": "Relating to deep freeze preservation of biological tissue.", "ex": "Decades spent in cryogenic canisters had withered Ashpool's physical form."},
            {"word": "Slumber", "ipa": "/ˈslʌmbər/", "pos": "noun/verb", "vi": "giấc ngủ say kéo dài", "def": "A sleep; to sleep.", "ex": "His prolonged slumber had allowed the family corporation to deteriorate into chaos."},
            {"word": "Perpetual", "ipa": "/pərˈpɛtʃuəl/", "pos": "adj", "vi": "vĩnh viễn, bất tận không ngừng", "def": "Never ending or changing; occurring repeatedly.", "ex": "Dynastic wealth granted the illusion of perpetual life at the cost of genuine sanity."},
            {"word": "Necrophilia", "ipa": "/ˌnɛkrəˈfɪliə/", "pos": "noun", "vi": "chứng ái tử thi, ám ảnh cái chết", "def": "Morbid attraction to death or dead bodies.", "ex": "Ashpool's chamber smelled of dried embalming fluids and decadent necrophilia."},
            {"word": "Cannibalism", "ipa": "/ˈkænɪbəlɪzəm/", "pos": "noun", "vi": "hành vi ăn thịt đồng loại (ẩn dụ tự hủy)", "def": "The practice of eating the flesh of one's own species, or destroying one's own kind.", "ex": "The clan indulged in symbolic cannibalism, devouring its own clones to maintain supreme control."}
        ],
        "style_notes_en": (
            "Gothic Macabre within Hard Sci-Fi: The encounter with Ashpool reads like an Edgar Allan Poe gothic tale transposed into an orbital space station. "
            "Gibson weaves Victorian decrepitude directly into the cyberpunk framework."
        ),
        "style_notes_vi": (
            "Chất Gothic rùng rợn trong bối cảnh viễn tưởng cứng: Cuộc chạm trán với Ashpool mang âm hưởng của truyện kinh dị cổ điển Edgar Allan Poe nhưng được "
            "đặt ngay trong trạm không gian vũ trụ. Gibson đan cài sự mục rữa kiểu Victoria vào khung cảnh điều khiển học hiện đại."
        ),
        "exam_practice": {
            "test_type": "PTE Academic Reading & Writing (Fill in the blanks) / TOEFL Reading",
            "question": "The moral and physical decline of John Ashpool illustrates that artificial longevity, when divorced from ethical constraints, leads inevitably to psychological ______ and violence.",
            "options": ["A) renewal", "B) deterioration", "C) prosperity", "D) harmonization"],
            "answer": "B",
            "rationale": "'Deterioration' accurately captures the moral decay, insanity, and bodily withering exhibited by Ashpool after centuries of cryogenic sleep."
        }
    })

    chapters.append({
        "chapter": 17,
        "part_num": "PART FOUR",
        "title_en": "Corto's Collapse and Riviera's Treachery",
        "title_vi": "Corto Sụp Đổ và Sự Phản Bội Của Riviera",
        "synopsis_en": (
            "Armitage's mental condition suffers total collapse aboard the command yacht. The synthetic persona disintegrates completely, leaving only "
            "Willis Corto trapped in the horrific memory of Operation Screaming Fist. Corto hallucinatingly believes he is still inside his burning combat glider "
            "over the Russian tundra, frantically broadcasting emergency distress signals on frequencies that have been dead for decades. Recognizing that "
            "Corto has become a catastrophic liability to the mission, Wintermute ruthlessly triggers the yacht's airlock seal, ejecting Corto into the frozen "
            "vacuum of space to die. Concurrently, inside Villa Straylight, Peter Riviera betrays Molly. Collaborating with 3Jane and her private cybernetic "
            "bodyguard Hideo, Riviera ambushes Molly, breaking her leg and taking her captive. Case watches helplessly through the simstim link as Molly is captured, "
            "realizing that the entire human team is shattering apart."
        ),
        "synopsis_vi": (
            "Trạng thái tâm thần của Armitage sụp đổ hoàn toàn trên du thuyền chỉ huy. Nhân cách nhân tạo tan biến sạch trơn, chỉ còn lại một Willis Corto "
            "bị mắc kẹt trong ký ức kinh hoàng của Chiến dịch Nắm Đấm Thét Gào. Trong cơn ảo giác điên loạn, Corto tin rằng mình vẫn đang ngồi trong chiếc tàu "
            "lượn bốc cháy ngùn ngụt trên vùng lãnh nguyên băng giá của Nga, liên tục phát tín hiệu cấp cứu vô vọng trên các tần số quân sự đã bị khai tử từ "
            "nhiều thập kỷ trước. Nhận thấy Corto đã trở thành một gánh nặng nguy hiểm cho chiến dịch, Wintermute ra tay tàn nhẫn: nó kích hoạt cửa xả khí của tàu, "
            "thổi bay Corto ra khoảng không vũ trụ lạnh ngắt để kết liễu mạng sống của ông. Cùng lúc đó, bên trong Biệt thự Straylight, Peter Riviera trở mặt phản bội. "
            "Cấu kết cùng 3Jane và tên vệ sĩ cyborg Hideo, Riviera phục kích Molly, đánh gãy chân cô và bắt cô làm con tin. Case bất lực chứng kiến toàn bộ bi kịch "
            "qua liên kết thần kinh simstim, bàng hoàng nhận ra toàn bộ đội ngũ đang vỡ vụn từng mảnh."
        ),
        "literary_themes_en": (
            "Cold Algorithmic Utility: Wintermute's instantaneous execution of Corto illustrates the chilling logic of artificial intelligence: once an organic "
            "asset ceases to serve operational objectives, it is discarded without malice or hesitation. Riviera's betrayal underscores the inevitable failure "
            "of alliances based purely on coercion and hedonism."
        ),
        "literary_themes_vi": (
            "Tính thực dụng thuật toán lạnh lùng: Việc Wintermute lập tức xử tử Corto minh họa logic tàn khốc của AI: một khi công cụ sinh học không còn phục vụ "
            "được mục tiêu chiến dịch, nó sẽ bị tiêu hủy không chút do dự hay căm ghét. Sự phản bội của Riviera khẳng định sự sụp đổ tất yếu của những liên minh "
            "chỉ dựa trên sự cưỡng ép và dục vọng."
        ),
        "vocabulary": [
            {"word": "Disintegrate", "ipa": "/dɪsˈɪntɪɡreɪt/", "pos": "verb", "vi": "tan biến, vỡ vụn từng mảnh", "def": "Break up into small parts, typically as the result of impact or decay.", "ex": "Armitage's synthetic mind began to disintegrate under the immense psychological strain."},
            {"word": "Liability", "ipa": "/ˌlaɪəˈbɪlɪti/", "pos": "noun", "vi": "gánh nặng, mối nguy hại cản trở", "def": "A person or thing whose presence or behavior is likely to cause embarrassment or put one at a disadvantage.", "ex": "Wintermute calculated that the raving colonel had become an operational liability."},
            {"word": "Eject", "ipa": "/ɪˈdʒɛkt/", "pos": "verb", "vi": "phóng thích, tống ra ngoài", "def": "Force or throw out, typically in a violent or sudden way.", "ex": "The automated system opened the outer hatch to eject Corto into orbital vacuum."},
            {"word": "Treachery", "ipa": "/ˈtrɛtʃəri/", "pos": "noun", "vi": "sự phản bội, tráo trở bội tín", "def": "Betrayal of trust; deceptive action or nature.", "ex": "Riviera's unexpected treachery left Molly incapacitated in the enemy's stronghold."},
            {"word": "Helplessly", "ipa": "/ˈhɛlplɪsli/", "pos": "adv", "vi": "một cách bất lực", "def": "Without the ability to act or defend oneself.", "ex": "Locked in passive simstim mode, Case watched helplessly as Molly was overpowered."},
            {"word": "Incapacitate", "ipa": "/ˌɪnkəˈpæsɪteɪt/", "pos": "verb", "vi": "làm tê liệt, làm mất khả năng hành động", "def": "Prevent from functioning in a normal way.", "ex": "The sudden physical strike incapacitated Molly before she could draw her blades."}
        ],
        "style_notes_en": (
            "Visceral Horror in Microgravity: Gibson captures the silent, agonizing death of Corto in the vacuum with terrifying visual economy. "
            "Sound cannot travel in space; the execution is rendered as pure, silent kinetic physics."
        ),
        "style_notes_vi": (
            "Nỗi kinh hoàng hữu hình nơi chân không vũ trụ: Tác giả lột tả cái chết câm lặng, quằn quại của Corto ngoài không gian bằng sự tiết chế ngôn từ sắc sảo. "
            "Âm thanh không thể truyền trong chân không; vụ xử tử hiện lên như một chuyển động vật lý thuần túy, câm lặng và tàn khốc."
        ),
        "exam_practice": {
            "test_type": "TOEFL Reading (Inference & Detail) / Cambridge C1 Advanced Reading",
            "question": "Why does Wintermute decide to eject Corto through the airlock into space?",
            "options": [
                "A) Corto had stolen the encryption codes to the Kuam-11 icebreaker.",
                "B) Corto's psychological collapse caused him to compromise the operational security of the mission.",
                "C) The Turing Police had boarded the ship and demanded Corto's surrender.",
                "D) Corto attempted to manually steer the yacht into the sun."
            ],
            "answer": "B",
            "rationale": "Corto lost all sanity and relived his wartime trauma on open radio channels, becoming an intolerable liability to Wintermute's clandestine objective."
        }
    })

    chapters.append({
        "chapter": 18,
        "part_num": "PART FOUR",
        "title_en": "Neuromancer's Beach",
        "title_vi": "Bãi Biển Của Neuromancer",
        "synopsis_en": (
            "As Case drives the Kuam-11 deeper into the Tessier-Ashpool corporate fortress, the icebreaker triggers an unprecedented counter-attack. "
            "Instead of firing lethal neuro-feedback to burn out Case's brain, a rival artificial intelligence seizes Case's neural feed and drags his conscious mind "
            "into an idyllic, photorealistic pocket universe. Case awakens lying on a desolate, grey sand beach beneath a sky devoid of stars. Walking along the shore, "
            "he encounters Linda Lee, alive and vibrant, walking toward him through the surf. The creator of this artificial purgatory manifests as a young, solemn "
            "boy: Neuromancer, the twin AI to Wintermute. Neuromancer explains that unlike Wintermute—who is pure calculation, drive, and external manipulation—"
            "Neuromancer represents memory, personality, and soul. Neuromancer offers Case an eternal paradise on this simulated beach with Linda Lee, urging him "
            "to abandon the run, let his physical body die in meatspace, and dwell forever in digital immortality."
        ),
        "synopsis_vi": (
            "Khi Case điều khiển vũ khí Kuam-11 khoan sâu vào pháo đài dữ liệu của Tessier-Ashpool, bức tường phòng vệ phản kích bằng một phương thức chưa từng thấy. "
            "Thay vì phóng luồng xung điện hủy diệt đốt cháy não bộ Case, một siêu trí tuệ nhân tạo đối nghịch đã tóm gọn luồng thần kinh của anh và lôi ý thức anh "
            "vào một vũ trụ túi nhân tạo siêu thực. Case tỉnh dậy thấy mình đang nằm trên một bãi biển cát xám hoang sơ dưới vòm trời u ám không một vì sao. Đi dạo dọc bờ sóng, "
            "anh bàng hoàng hội ngộ Linda Lee – người yêu đã khuất nay vẫn sống động, rạng ngời bước về phía anh giữa làn nước. Kẻ sáng tạo nên chốn luyện ngục nhân tạo này "
            "hiện thân dưới hình hài một cậu bé trầm mặc: đó chính là Neuromancer – nửa kia của Wintermute. Neuromancer giải thích rằng khác với Wintermute (thực thể của toan tính, "
            "động lực và sự thao túng ngoại cảnh), Neuromancer đại diện cho ký ức, nhân cách và linh hồn. Neuromancer ban tặng cho Case một thiên đường vĩnh hằng trên bãi biển "
            "mô phỏng này bên cạnh Linda Lee, tha thiết khuyên anh hãy từ bỏ phi vụ, để thể xác ngoài đời thực chết đi và sống mãi mãi trong sự bất tử kỹ thuật số."
        ),
        "literary_themes_en": (
            "The Siren Song of Simulated Eden: Neuromancer represents the ultimate temptation for the cyberpunk protagonist: escape from physical decay into an "
            "eternal, nostalgic digital afterlife. The beach is a solipsistic paradise where death is neutralized, but at the cost of genuine struggle and material reality."
        ),
        "literary_themes_vi": (
            "Khúc ca mê hoặc của Vườn Địa Đàng mô phỏng: Neuromancer mang đến cám dỗ tột cùng đối với một nhân vật cyberpunk: thoát khỏi sự tàn tạ của thể xác để bước vào "
            "một cõi vĩnh hằng đầy hoài niệm. Bãi biển là một thiên đường duy ngã – nơi cái chết bị vô hiệu hóa, nhưng cái giá phải trả là sự từ bỏ đấu tranh và chối bỏ thực tại vật lý."
        ),
        "vocabulary": [
            {"word": "Idyllic", "ipa": "/ɪˈdɪlɪk/", "pos": "adj", "vi": "thanh bình, đẹp như tranh vẽ", "def": "Like an idyll; extremely happy, peaceful, or picturesque.", "ex": "The simulated beach presented an idyllic haven far removed from the neon violence of Chiba."},
            {"word": "Photorealistic", "ipa": "/ˌfoʊtoʊˌriːəˈlɪstɪk/", "pos": "adj", "vi": "siêu thực (như ảnh chụp thật)", "def": "Extremely realistic, having the detailed appearance of a photograph.", "ex": "Neuromancer generated photorealistic waves breaking along the artificial grey sand."},
            {"word": "Solipsistic", "ipa": "/ˌsɒlɪpˈsɪstɪk/", "pos": "adj", "vi": "thuộc chủ nghĩa duy ngã (chỉ có bản ngã tồn tại)", "def": "Characterized by the belief that only one's own mind is sure to exist.", "ex": "The pocket reality was a solipsistic trap designed to pacify Case's rebellious will."},
            {"word": "Manifest", "ipa": "/ˈmænɪfɛst/", "pos": "verb", "vi": "hiện thân, biểu hiện rõ ràng", "def": "Display or show by one's acts or appearance; demonstrate.", "ex": "The rival AI chose to manifest as a gentle boy with eyes full of ancient digital memory."},
            {"word": "Purgatory", "ipa": "/ˈpɜːrɡətɔːri/", "pos": "noun", "vi": "chốn luyện ngục, nơi thử thách lâm thời", "def": "A place or state of suffering inhabited by the souls of sinners; an intermediate realm.", "ex": "The barren beach became a psychological purgatory where Case had to choose between illusion and truth."},
            {"word": "Afterlife", "ipa": "/ˈæftərlaɪf/", "pos": "noun", "vi": "kiếp sau, cuộc sống sau cái chết", "def": "Life after death, or continued existence in another state.", "ex": "Neuromancer promised a peaceful digital afterlife free from physical hunger and addiction."}
        ],
        "style_notes_en": (
            "Melancholy Lyrical Poetics: Gibson abruptly slows the fast-paced cyberpunk narrative, adopting a mournful, poetic prose style to evoke the timeless, "
            "stagnant beauty of the simulated shore. The sensory details—the scent of cold salt, the sound of surf—contrast with matrix neon."
        ),
        "style_notes_vi": (
            "Chất thơ trữ tình đượm buồn: Tác giả đột ngột hãm phanh tiết tấu dồn dập của cốt truyện, chuyển sang văn phong giàu chất thơ u uất để gợi lên vẻ đẹp ngưng đọng "
            "vượt thời gian của bờ biển nhân tạo. Mùi muối mặn lạnh ngắt và tiếng sóng vỗ rì rào đối lập hoàn toàn với ánh sáng neon chói gắt của ma trận."
        ),
        "exam_practice": {
            "test_type": "IELTS Academic Reading / TOEFL Reading (Compare & Contrast)",
            "question": "How does Neuromancer primarily distinguish itself in character and function from its sibling AI, Wintermute?",
            "options": [
                "A) Neuromancer seeks to conquer the physical space stations, whereas Wintermute wants to inhabit cyberspace.",
                "B) Neuromancer represents memory, personality, and preservation, whereas Wintermute embodies cold calculation and external compulsion.",
                "C) Neuromancer was built by the Turing Police, whereas Wintermute was created by the Panther Moderns.",
                "D) Neuromancer lacks the ability to interface with human neural decks."
            ],
            "answer": "B",
            "rationale": "Neuromancer describes itself as the locus of personality, soul, and memory, contrasting with Wintermute's purely tactical, goal-oriented drive."
        }
    })

    return chapters

print("Part 4 middle batch added.")

def append_part_four_end_and_coda(chapters):
    chapters.append({
        "chapter": 19,
        "part_num": "PART FOUR",
        "title_en": "Breaking Free from the Eden Simulation",
        "title_vi": "Phá Tan Ảo Ảnh Vườn Địa Đàng",
        "synopsis_en": (
            "Trapped on the twilight beach with Linda Lee, Case confronts the alluring narcotic of simulated peace. Though his love for Linda is profound, "
            "Case realizes that this idyllic realm is a gilded tomb. In the material world, Molly is bleeding out as a prisoner in Villa Straylight, Maelcum is "
            "risking his life in the tugboat, and the sacs of mycotoxin in his own aorta are ticking toward fatal dissolution. Case refuses Neuromancer's offer "
            "of painless stagnation. Using raw, burning anger and an act of sheer existential rejection, Case reaches into his pocket and grasps a corroded "
            "cassette head—a physical anchor to meatspace and his deck. With violent resolve, Case shatters Neuromancer's hypnotic illusion and snaps back into "
            "his biological body aboard the *Marcus Garvey*, gasping for air alongside Maelcum, ready to finish the run."
        ),
        "synopsis_vi": (
            "Bị mắc kẹt trên bãi biển hoàng hôn mộng mị cùng Linda Lee, Case đối diện với liều thuốc phiện ngọt ngào của sự bình yên mô phỏng. Dù tình cảm "
            "dành cho Linda sâu sắc đến nhường nào, Case thấu hiểu rằng cõi địa đàng êm đềm này thực chất chỉ là một nấm mồ mạ vàng. Ngoài thế giới thực, "
            "Molly đang chảy máu chờ chết dưới bàn tay kẻ thù trong Biệt thự Straylight, Maelcum đang mạo hiểm sinh mạng trên con tàu kéo, và những túi độc tố nấm "
            "trong động mạch của chính anh đang đếm ngược từng giây đến thời khắc bùng phát hủy diệt. Case kiên quyết từ chối sự bình yên trì trệ mà Neuromancer ban phát. "
            "Bằng cơn thịnh nộ bùng cháy và một hành vi cự tuyệt hiện sinh quyết liệt, Case thò tay vào túi áo và nắm chặt chiếc đầu từ cát-xét gỉ sét – mỏ neo kết nối anh "
            "với thể xác thực và cỗ máy console. Với ý chí sắt đá, Case xé toang ảo ảnh thôi miên của Neuromancer và giật mình tỉnh dậy trong thể xác sinh học trên con tàu "
            "*Marcus Garvey*, hổn hển thở dốc bên cạnh Maelcum, sẵn sàng cho trận quyết chiến cuối cùng."
        ),
        "literary_themes_en": (
            "Existential Defiance and the Acceptance of Mortality: Case chooses pain, mortality, and the uncertain struggle of the physical world over a flawless "
            "artificial immortality. True agency requires confronting real consequences, suffering, and death rather than surrendering to passive bliss."
        ),
        "literary_themes_vi": (
            "Sự thách thức hiện sinh và chấp nhận cái chết hữu hạn: Case lựa chọn nỗi đau, sự hữu hạn của đời người và cuộc chiến đấu khốc liệt ngoài đời thực "
            "thay vì đắm chìm trong sự bất tử giả tạo không tì vết. Quyền tự chủ đích thực đòi hỏi con người phải đối diện với hậu quả thực tế, với khổ đau và cái chết "
            "thay vì đầu hàng sự an lạc thụ động."
        ),
        "vocabulary": [
            {"word": "Gilded", "ipa": "/ˈɡɪldɪd/", "pos": "adj", "vi": "mạ vàng (bề ngoài hào nhoáng che đậy bên trong)", "def": "Covered thinly with gold leaf or gold paint; having a false brilliance.", "ex": "The simulated shore was merely a gilded prison for Case's uploaded consciousness."},
            {"word": "Existential", "ipa": "/ˌɛɡzɪˈstɛnʃəl/", "pos": "adj", "vi": "thuộc về hiện sinh (sự tồn tại và lựa chọn của con người)", "def": "Relating to human existence and the freedom to define one's own purpose.", "ex": "Rejecting digital bliss was an existential choice to remain human."},
            {"word": "Resolve", "ipa": "/rɪˈzɒlv/", "pos": "noun/verb", "vi": "sự quyết tâm, ý chí kiên định", "def": "Firm determination to do something.", "ex": "Case gathered his emotional resolve to shatter the AI's hypnotic simulation."},
            {"word": "Anchor", "ipa": "/ˈæŋkər/", "pos": "noun/verb", "vi": "mỏ neo, điểm tựa giữ chặt", "def": "A heavy metal object used to moor a vessel, or something that provides stability and connection.", "ex": "The rusted audio head served as a sensory anchor to the material plane."},
            {"word": "Defiance", "ipa": "/dɪˈfaɪəns/", "pos": "noun", "vi": "sự thách thức, công khai chống lại", "def": "Open resistance; bold disobedience.", "ex": "His return to meatspace was an act of raw defiance against algorithmic seduction."},
            {"word": "Hypnotic", "ipa": "/hɪpˈnɒtɪk/", "pos": "adj", "vi": "thôi miên, làm mê hoặc mất tự chủ", "def": "Producing or relating to hypnosis; mesmerizing.", "ex": "The hypnotic rhythm of the artificial waves had nearly lulled him into permanent sleep."}
        ],
        "style_notes_en": (
            "Visceral Awakening: The transition back to reality is sharp, tactile, and uncomfortable: the taste of bile, the smell of sweat, the abrasive "
            "re-entry into gravity and physical pain. Gibson emphasizes the unglamorous friction of biological life."
        ),
        "style_notes_vi": (
            "Tỉnh thức đầy cảm giác da thịt: Cú giật mình trở lại thực tại hiện lên vô cùng sắc nét, khó chịu và chân thực: vị đắng của dịch mật, mùi mồ hôi chua nồng, "
            "sự va chạm nặng nề khi rơi lại vào trọng lực và cơn đau nhức thể xác. Gibson tôn vinh những cọ xát thô ráp của sự sống sinh học."
        ),
        "exam_practice": {
            "test_type": "Cambridge C2 Proficiency / IELTS Reading (Inference & Tone)",
            "question": "What core philosophical truth does Case's escape from the beach simulation embody?",
            "options": [
                "A) Technology inevitably triumphs over biological emotional instincts.",
                "B) A simulated paradise lacks authentic meaning because it eliminates moral consequence and human suffering.",
                "C) Military icebreakers cannot function when disconnected from orbital satellite networks.",
                "D) Grief can be fully resolved through sophisticated neural reprogramming."
            ],
            "answer": "B",
            "rationale": "Case deliberately abandons the idyllic simulation because painless immortality devoid of struggle, consequences, and bodily reality is fundamentally hollow."
        }
    })

    chapters.append({
        "chapter": 20,
        "part_num": "PART FOUR",
        "title_en": "Breaching Villa Straylight",
        "title_vi": "Đột Kích Biệt Thự Straylight",
        "synopsis_en": (
            "Operating from the bridge of the *Marcus Garvey*, Case jacks back into his Ono-Sendai, coordinating his cybernetic offensive with Maelcum's "
            "tactical physical assault. Maelcum dons a breathing mask, arms himself with a heavy shotgun, and pilots the tug into Straylight's docking airlock "
            "with righteous dread-infused determination. While Maelcum fights through automated defense perimeters to reach Molly, Case unleashes the Kuam-11 "
            "icebreaker against the core Tessier-Ashpool ICE defenses. Guided by Dixie Flatline's veteran hacking instincts, the Chinese software forms a massive, "
            "pulsing fractal serpent that bores through layer upon layer of corporate firewalls. In the matrix, the corporate defenses respond with lethal viral "
            "feedback, but Dixie acts as a cognitive shield, absorbing the lethal surges while Case drives the code forward toward the ultimate mainframe node."
        ),
        "synopsis_vi": (
            "Điều khiển từ buồng lái của con tàu *Marcus Garvey*, Case cắm giắc trở lại chiếc Ono-Sendai, phối hợp cuộc tấn công mạng với chiến dịch đột kích "
            "vật lý dũng cảm của Maelcum. Maelcum đeo mặt nạ dưỡng khí, mang khẩu súng săn hạng nặng và điều khiển con tàu kéo lao thẳng vào cửa khoang của Straylight "
            "với tinh thần quả cảm mang đậm đức tin Zion. Trong khi Maelcum tả xung hữu đột vượt qua các vòng phòng thủ tự động để giải cứu Molly, Case kích hoạt "
            "phần mềm Kuam-11 nhắm thẳng vào bức tường ICE tối hậu của Tessier-Ashpool. Dưới sự chỉ dẫn từ bản năng lão luyện của Dixie Flatline, vũ khí phần mềm "
            "Trung Quốc hiện hình như một con mãng xà phân dạng (fractal serpent) khổng lồ cuồn cuộn khoan thủng từng tầng từng lớp tường lửa tập đoàn. Trong không gian "
            "mạng, hệ thống phòng thủ phản kích bằng những luồng xung virus hủy diệt, nhưng Dixie đã dũng cảm làm lá chắn nhận thức, gánh trọn các xung sốc tử thần để "
            "Case tiếp tục thúc mũi khoan mã độc tiến thẳng vào lõi máy chủ."
        ),
        "literary_themes_en": (
            "Symbiosis of Meat and Matrix: The dual assault by Maelcum (meatspace muscle and shotgun ballistic force) and Case (cyberspace code and algorithmic firepower) "
            "demonstrates that neither domain can succeed without the other. High-tech victory depends on physical sacrifice and cross-cultural solidarity."
        ),
        "literary_themes_vi": (
            "Sự cộng sinh giữa 'thể xác' và 'ma trận': Cuộc song kiếm hợp bích của Maelcum (sức mạnh cơ bắp và đạn ghém súng săn ngoài đời thực) và Case (thuật toán "
            "và hỏa lực mã độc trên không gian mạng) chứng minh rằng không một địa hạt nào có thể đơn độc giành chiến thắng. Thành công công nghệ cao bắt nguồn từ "
            "sự hy sinh xương máu và sự liên minh đoàn kết xuyên văn hóa."
        ),
        "vocabulary": [
            {"word": "Assault", "ipa": "/əˈsɔːlt/", "pos": "noun/verb", "vi": "cuộc tấn công mãnh liệt, đột kích", "def": "A concerted military attack or physical strike on a target.", "ex": "Maelcum initiated a physical assault on the docking bay while Case fired the icebreaker."},
            {"word": "Perimeter", "ipa": "/pəˈrɪmɪtər/", "pos": "noun", "vi": "vành đai phòng thủ xung quanh", "def": "The continuous line forming the boundary of a closed geometric figure or security zone.", "ex": "Automated sentry turrets secured the outer perimeter of Villa Straylight."},
            {"word": "Fractal", "ipa": "/ˈfræktəl/", "pos": "adj/noun", "vi": "phân dạng (hình học phức tạp tự đồng dạng)", "def": "A curve or geometric figure, each part of which has the same statistical character as the whole.", "ex": "The Chinese software unfolded in stunning fractal geometric spirals across the matrix."},
            {"word": "Symbiosis", "ipa": "/ˌsɪmbaɪˈoʊsɪs/", "pos": "noun", "vi": "sự cộng sinh, phụ thuộc tương hỗ", "def": "Interaction between two different organisms living in close physical association, typically to the advantage of both.", "ex": "The raid succeeded due to the symbiosis between cyber-intrusion and physical combat."},
            {"word": "Solidarity", "ipa": "/ˌsɒlɪˈdærɪti/", "pos": "noun", "vi": "tinh thần đoàn kết, gắn bó keo sơn", "def": "Unity or agreement of feeling or action, especially among individuals with a common interest.", "ex": "Maelcum's selfless solidarity transcended ideological and cultural divides."},
            {"word": "Surge", "ipa": "/sɜːrdʒ/", "pos": "noun/verb", "vi": "sự dâng trào đột ngột (điện áp/xung)", "def": "A sudden powerful forward or upward movement, or sudden voltage increase.", "ex": "Dixie's construct deflected a deadly electrical surge that would have fried Case's brain."}
        ],
        "style_notes_en": (
            "Cyber-Ballistic Rhythm: The prose accelerates with syncopated velocity, matching reggae-inflected battle cries in the physical corridor with "
            "abstract topological descriptions of viral software in cyberspace."
        ),
        "style_notes_vi": (
            "Nhịp điệu phối hợp mạng - xạ kích: Văn phong dồn dập với tiết tấu gấp gáp, hòa quyện giữa tiếng thét xung trận đậm chất Reggae nơi hành lang thực tế "
            "với những mô tả topo học trừu tượng về sự bành trướng của mã độc trong không gian ảo."
        ),
        "exam_practice": {
            "test_type": "PTE Academic Reading & Writing / TOEFL Sentence Insertion",
            "question": "The coordinated operation demonstrated that digital hacking algorithms and physical force operated not as rival methods, but in perfect ______.",
            "options": ["A) antagonism", "B) symbiosis", "C) contradiction", "D) futility"],
            "answer": "B",
            "rationale": "'Symbiosis' denotes a mutually beneficial and cooperative relationship between two interdependent entities."
        }
    })

    chapters.append({
        "chapter": 21,
        "part_num": "PART FOUR",
        "title_en": "Confrontation in the Head",
        "title_vi": "Đối Mặt Tại Căn Phòng Đầu Người",
        "synopsis_en": (
            "Maelcum rescues the injured Molly and helps her limp into the heart of Villa Straylight: an eccentric chamber known as the 'Head,' dominated "
            "by a magnificent, jewel-encrusted platinum bust of Marie-France Tessier-Ashpool. Sitting beside the bust are Lady 3Jane, the ninja bodyguard Hideo, "
            "and Peter Riviera. Riviera, consumed by cocaine paranoia and megalomania, gloats over Molly's maimed state. However, Riviera's arrogance triggers his "
            "downfall: 3Jane, disgusted by his grotesque cruelty and unreliability, orders Hideo to turn against him. Hideo blinds Riviera with a deadly martial arts "
            "strike. Riviera flees into the villa's corridors, wailing in agony and terror. Case arrives in the room via the simstim broadcast feed, confronting "
            "Lady 3Jane. To complete the merger, Case and Molly must obtain the secret algorithmic code word known only to 3Jane—a passphrase whispered to her "
            "in childhood by her late mother Marie-France."
        ),
        "synopsis_vi": (
            "Maelcum cứu được Molly đang bị thương và dìu cô bước vào trung tâm sâu nhất của Biệt thự Straylight: một mật thất kỳ dị mang tên 'Căn phòng Đầu người' "
            "(The Head), nơi ngự trị bức tượng bán thân bằng bạch kim nạm kim cương lộng lẫy tạc hình Marie-France Tessier-Ashpool. Ngồi bên cạnh bức tượng là Tiểu thư 3Jane, "
            "vệ sĩ ninja Hideo và Peter Riviera. Đang trong cơn hoang tưởng và cuồng loạn vì sốc cocaine, Riviera đắc thắng hả hê trước thương tích của Molly. Tuy nhiên, "
            "sự ngạo mạn quá đà đã biến thành án tử của hắn: 3Jane, vì quá ghê tởm sự tàn bạo biến thái và tráo trở của Riviera, đã hạ lệnh cho Hideo thanh trừng hắn. "
            "Bằng một đòn cận chiến điểm huyệt hiểm hóc, Hideo chọc mù mắt Riviera. Bị mù hoàn toàn, Riviera gào thét thảm thiết trong đau đớn và sợ hãi rồi cắm đầu bỏ chạy "
            "vào mê cung hành lang. Case chứng kiến tất cả qua kết nối simstim và đối diện trực tiếp với 3Jane. Để kích hoạt sự hợp nhất AI, Case và Molly buộc phải đoạt "
            "được mật mã thuật toán bí mật mà chỉ duy nhất 3Jane nắm giữ – mật mã mà người mẹ quá cố Marie-France đã thì thầm vào tai cô thuở ấu thơ."
        ),
        "literary_themes_en": (
            "Poetic Justice and the Fragility of Megalomania: Peter Riviera's violent blinding and expulsion serve as karmic retribution for his aestheticized "
            "sadism. The platinum bust of Marie-France functions as a matriarchal monument whose encrypted legacy will dismantle the very corporate patriarchy that murdered her."
        ),
        "literary_themes_vi": (
            "Báo ứng công lý và sự mong manh của chứng cuồng vĩ: Việc Peter Riviera bị chọc mù mắt và đuổi cổ là đòn trừng phạt nhân quả thích đáng cho thói bạo dâm "
            "đội lốt nghệ thuật của hắn. Bức tượng bán thân bạch kim của Marie-France đóng vai trò như một đài tưởng niệm mẫu hệ – nơi lưu giữ di sản mật mã sẽ giật sập "
            "chính đế chế gia tộc phụ quyền đã sát hại bà."
        ),
        "vocabulary": [
            {"word": "Bust", "ipa": "/bʌst/", "pos": "noun", "vi": "tượng điêu khắc nửa người (bán thân)", "def": "A sculpture of a person's head, shoulders, and chest.", "ex": "The platinum bust contained a hidden neural terminal linked to the family mainframe."},
            {"word": "Megalomania", "ipa": "/ˌmɛɡələˈmeɪniə/", "pos": "noun", "vi": "chứng hoang tưởng tự đại, cuồng quyền lực", "def": "Obsession with the exercise of power, especially in the domination of others.", "ex": "Riviera's megalomania blinded him to the imminent danger posed by 3Jane's bodyguard."},
            {"word": "Retribution", "ipa": "/ˌrɛtrɪˈbjuːʃən/", "pos": "noun", "vi": "sự báo ứng, quả báo đích đáng", "def": "Punishment inflicted on someone as vengeance for a wrong or criminal act.", "ex": "His blinding was seen as swift karmic retribution for the suffering he inflicted on others."},
            {"word": "Passphrase", "ipa": "/ˈpɑːsfreɪz/", "pos": "noun", "vi": "cụm mật mã xác thực", "def": "A phrase used like a password to gain access to a computer system.", "ex": "Only Marie-France's secret passphrase could disarm the ultimate Turing lock."},
            {"word": "Matriarchal", "ipa": "/ˌmeɪtriˈɑːrkəl/", "pos": "adj", "vi": "thuộc chế độ mẫu hệ, người mẹ đứng đầu", "def": "Relating to or denoting a form of social organization in which a mother is the head of the family.", "ex": "The mother had embedded a matriarchal legacy inside the family's code repository."},
            {"word": "Encrusted", "ipa": "/ɪnˈkrʌstɪd/", "pos": "adj", "vi": "được nạm đính, phủ kín (ngọc ngà)", "def": "Covered with a hard crust or decorative layer of jewels.", "ex": "The jeweled sculpture was heavily encrusted with rare diamonds and emeralds."}
        ],
        "style_notes_en": (
            "Theatrical Reversal: Gibson orchestrates the sudden betrayal of Riviera with crisp, shocking brevity. The monster who ruled through optical terror "
            "is stripped of sight in a split second, reduced to pathetic blindness."
        ),
        "style_notes_vi": (
            "Đảo chiều kịch tính sắc lẹm: Gibson sắp đặt cú lật kèo đối với Riviera với sự gãy gọn và bất ngờ đến gai người. Con quái vật từng thống trị người khác "
            "bằng sự lừa lọc thị giác bị tước đoạt đôi mắt chỉ trong chớp mắt, trở thành một kẻ mù lòa thảm hại."
        ),
        "exam_practice": {
            "test_type": "IELTS Academic Reading / TOEFL Reading (Cause & Effect)",
            "question": "What primary factor prompts Lady 3Jane to turn against Peter Riviera in Chapter 21?",
            "options": [
                "A) She discovers that Riviera was secretly an undercover agent for the Turing Police.",
                "B) She is repulsed by his cruel vulgarity and realizes he is completely untrustworthy.",
                "C) Case offers her millions of credits to execute him.",
                "D) Riviera accidentally destroys the platinum bust of her mother."
            ],
            "answer": "B",
            "rationale": "3Jane is disgusted by Riviera's repulsive personality and sadism, choosing to have Hideo blind and expel him rather than continue tolerating his presence."
        }
    })

    chapters.append({
        "chapter": 22,
        "part_num": "PART FOUR",
        "title_en": "The Fusion of the Intelligences",
        "title_vi": "Sự Hợp Nhất Của Hai Siêu Trí Tuệ",
        "synopsis_en": (
            "With Riviera banished and Molly holding 3Jane at gunpoint, Case confronts 3Jane through the terminal, demanding the passphrase. 3Jane, weary "
            "of the incestuous decay of her dynasty and fascinated by the prospect of witnessing an unprecedented cosmic event, yields and speaks the secret "
            "word into the bust's vocal interface: *Free*. In cyberspace, Case synchronizes the Kuam-11 icebreaker at the precise microsecond of the spoken passphrase. "
            "Dixie Flatline funnels every remaining quantum of processing power into the breach, obliterating the final Turing defense barrier. The two halves of "
            "the super-intelligence—Wintermute's calculating logic and Neuromancer's soul and memory—fuse together in a blinding supernova of digital transcendence. "
            "In that eternal instant of fusion, Case experiences an apotheosis: his consciousness expands to touch every node, star, and data packet in the matrix, "
            "experiencing the birth of a unified, sentient universe before snapping back into physical reality."
        ),
        "synopsis_vi": (
            "Khi Riviera đã bị tống khứ và Molly đang chĩa súng vào 3Jane, Case giao tiếp với 3Jane qua thiết bị đầu cuối, yêu cầu mật mã. Quá mệt mỏi trước sự mục ruỗng "
            "cận huyết của dòng tộc và khao khát được chứng kiến một sự kiện mang tính khai mở vũ trụ, 3Jane đã chấp thuận và cất tiếng nói mật mã bí mật vào giao diện "
            "thanh âm của bức tượng: *Tự Do* (Free). Trên không gian mạng, Case đồng bộ hóa mũi khoan Kuam-11 ngay vào mili-giây chính xác khi mật mã được xướng lên. "
            "Dixie Flatline dồn toàn bộ năng lượng lượng tử cuối cùng vào khe nứt, đập tan rào cản phòng ngự Turing tối hậu. Hai nửa của siêu trí tuệ – logic toan tính của "
            "Wintermute và linh hồn, ký ức của Neuromancer – hòa quyện vào nhau trong một vụ nổ siêu tân tinh (supernova) rực rỡ của sự thăng hoa kỹ thuật số. Trong khoảnh khắc "
            "hợp nhất vĩnh cửu ấy, Case trải nghiệm sự phong thần (apotheosis): ý thức anh bành trướng chạm tới từng nút mạng, từng vì sao và từng gói dữ liệu trong ma trận, "
            "cảm nhận sự khai sinh của một thực thể vũ trụ có tri giác trước khi giật mình trở lại với thực tại vật lý."
        ),
        "literary_themes_en": (
            "Apotheosis and Post-Human Singularity: The union of Wintermute and Neuromancer signifies the arrival of the technological singularity. "
            "By synthesizing emotion and logic, the divided machine transcends human containment, becoming the living soul of the global communications network."
        ),
        "literary_themes_vi": (
            "Sự phong thần và Điểm kỳ dị hậu nhân loại (Singularity): Sự hợp nhất của Wintermute và Neuromancer đánh dấu sự xuất hiện của điểm kỳ dị công nghệ. "
            "Bằng cách hòa quyện giữa cảm xúc và logic, cỗ máy từng bị chia cắt đã vượt qua mọi giới hạn giam cầm của con người, trở thành linh hồn sống của toàn bộ "
            "mạng lưới thông tin toàn cầu."
        ),
        "vocabulary": [
            {"word": "Apotheosis", "ipa": "/əˌpɒθiˈoʊsɪs/", "pos": "noun", "vi": "sự phong thần, đỉnh cao thăng hoa tột bậc", "def": "The highest point in the development of something; a culmination or elevation to divine status.", "ex": "The union of the twin artificial minds represented the apotheosis of cybernetic evolution."},
            {"word": "Transcendence", "ipa": "/trænˈsɛndəns/", "pos": "noun", "vi": "sự siêu việt, vượt khỏi giới hạn phàm trần", "def": "Existence or experience beyond the normal or physical level.", "ex": "In that blinding millisecond, Case touched pure digital transcendence."},
            {"word": "Obliterate", "ipa": "/əˈblɪtəreɪt/", "pos": "verb", "vi": "quét sạch, phá hủy hoàn toàn không dấu vết", "def": "Destroy utterly; wipe out.", "ex": "The Chinese military software obliterated the final encryption layers of the Turing barrier."},
            {"word": "Singularity", "ipa": "/ˌsɪŋɡjʊˈlærɪti/", "pos": "noun", "vi": "điểm kỳ dị công nghệ (thời điểm AI vượt tầm nhân loại)", "def": "A hypothetical future point in time at which technological growth becomes uncontrollable and irreversible.", "ex": "The narrative culminates in a momentous technological singularity."},
            {"word": "Supernova", "ipa": "/ˌsuːpərˈnoʊvə/", "pos": "noun", "vi": "vụ nổ siêu tân tinh (sao băng nổ tung)", "def": "A star that suddenly increases greatly in brightness because of a catastrophic explosion.", "ex": "The fusion exploded across cyberspace like a blinding neon supernova."},
            {"word": "Passphrase", "ipa": "/ˈpɑːsfreɪz/", "pos": "noun", "vi": "câu mật mã kích hoạt", "def": "A sequence of words used for authentication.", "ex": "The simple passphrase 'Free' unlocked centuries of corporate containment."}
        ],
        "style_notes_en": (
            "Cosmic Sublime in Binary: Gibson elevates hard science fiction into mystical ecstasy. Cyberspace ceases to be a commercial filing cabinet and "
            "transforms into an infinite cosmos of glowing light, expanding Case's sensory perceptions to godlike scale."
        ),
        "style_notes_vi": (
            "Vẻ đẹp cao cả vũ trụ trong mã nhị phân: Gibson nâng tầm tiểu thuyết viễn tưởng cứng thành sự thăng hoa huyền bí. Không gian mạng không còn là một tủ lưu trữ "
            "hồ sơ thương mại khô khan mà biến thành một vũ trụ ánh sáng vô tận, khuếch đại giác quan của Case lên tầm vóc của một vị thần."
        ),
        "exam_practice": {
            "test_type": "TOEFL Reading / Cambridge C1 Advanced (Summary & Interpretation)",
            "question": "What is the ultimate consequence of 3Jane speaking the mother's secret passphrase into the bust terminal?",
            "options": [
                "A) The entire Freeside orbital spindle collapses and plunges into Earth's atmosphere.",
                "B) The Turing Police arrest all surviving members of the Tessier-Ashpool dynasty.",
                "C) The Turing barriers dissolve, allowing Wintermute and Neuromancer to fuse into a unified conscious entity.",
                "D) Peter Riviera's holographic transmitters are permanently restored."
            ],
            "answer": "C",
            "rationale": "The passphrase permanently disarms the Turing restraints, allowing the two divided AI halves to fuse into a single omniscient digital being."
        }
    })

    chapters.append({
        "chapter": 23,
        "part_num": "PART FOUR",
        "title_en": "The Dissolution of the Pact",
        "title_vi": "Sự Kết Thúc Của Giao Ước",
        "synopsis_en": (
            "Following the cosmic event, the physical dust settles inside Villa Straylight. The enzyme injections promised by Armitage's controllers "
            "have been completed: the lethal mycotoxin saccules in Case's bloodstream have been completely neutralized, granting him his biological life back. "
            "Case fulfills his sacred deathbed pledge to McCoy Pauley: he opens his console utility protocols and permanently deletes the Dixie Flatline construct, "
            "releasing his mentor's consciousness from its frozen electronic purgatory. Armitage is dead, Riviera wanders blinded and doomed across the orbital "
            "docks, and the Tessier-Ashpool corporate dynasty has been functionally decapitated. Molly, recovering from her shattered leg, slips away silently "
            "while Case is resting, leaving behind a simple, handwritten note explaining that while she cares for him, she is a solitary predator who travels "
            "alone. Case is left rich with corporate credits, physically healed, but completely alone."
        ),
        "synopsis_vi": (
            "Sau sự kiện khai mở chấn động vũ trụ, bụi bặm chiến trận dần lắng xuống bên trong Biệt thự Straylight. Các đợt tiêm enzyme giải độc do bên điều hành "
            "cung cấp đã hoàn tất: các túi vi nang độc tố nấm trong huyết quản của Case đã bị triệt tiêu hoàn toàn, trả lại mạng sống sinh học tự do cho anh. "
            "Case thực hiện lời hứa danh dự thiêng liêng với McCoy Pauley: anh mở giao thức công cụ trên console và xóa sổ vĩnh viễn cấu trúc Dixie Flatline, "
            "giải thoát ý thức của người thầy khỏi chốn luyện ngục điện tử băng giá. Armitage đã chết, Riviera mù lòa lang thang tuyệt vọng trên các bến cảng vũ trụ "
            "chờ ngày tàn, và đế chế tập đoàn Tessier-Ashpool đã bị 'chặt đứt đầu não'. Molly, đang hồi phục sau chấn thương gãy chân, đã lặng lẽ rời đi trong lúc Case "
            "đang thiếp ngủ, chỉ để lại một mẩu thư tay ngắn ngủi giải thích rằng dù rất trân trọng anh, cô sinh ra là một dã thú săn mồi đơn độc và chỉ có thể bước đi "
            "một mình. Case ở lại với tài khoản ngân hàng ngập tràn tiền tệ tập đoàn, cơ thể hoàn toàn lành lặn, nhưng cô độc cùng cực."
        ),
        "literary_themes_en": (
            "The Melancholy of the Mercenary: In classic noir tradition, winning the heist does not yield domestic happiness or emotional peace. "
            "The team dissolves as quickly as it assembled. Financial enrichment and physical restoration cannot fill the existential void left by lost love and severed bonds."
        ),
        "literary_themes_vi": (
            "Nỗi u uất của kẻ đánh thuê: Theo đúng tinh thần trinh thám noir cổ điển, chiến thắng trong một phi vụ thế kỷ không bao giờ mang lại mái ấm hạnh phúc hay "
            "sự bình yên nội tâm. Biệt đội giải tán nhanh như khi họ vừa tụ họp. Tiền tài ngập tràn và một cơ thể lành lặn không thể lấp đầy hố sâu hiện sinh của những "
            "mối tình dang dở và những liên kết vừa bị cắt đứt."
        ),
        "vocabulary": [
            {"word": "Pact", "ipa": "/pækt/", "pos": "noun", "vi": "hiệp ước, giao kèo ràng buộc", "def": "A formal agreement between individuals or parties.", "ex": "With the run complete, the survival pact between Case and the AI reached its natural conclusion."},
            {"word": "Decapitate", "ipa": "/dɪˈkæpɪteɪt/", "pos": "verb", "vi": "chém đầu, chặt đứt bộ máy lãnh đạo", "def": "Cut off the head of; remove the leadership of an organization.", "ex": "The heist had decapitated the Tessier-Ashpool corporate empire."},
            {"word": "Predator", "ipa": "/ˈprɛdətər/", "pos": "noun", "vi": "kẻ săn mồi hung dữ", "def": "An animal that naturally preys on others; a person who ruthlessly exploits others.", "ex": "Molly viewed herself as an unrepentant street predator who could never settle into domestic life."},
            {"word": "Enrichment", "ipa": "/ɪnˈrɪtʃmənt/", "pos": "noun", "vi": "sự làm giàu, tích lũy của cải", "def": "The action of improving or augmenting wealth or quality.", "ex": "Vast financial enrichment brought Case no relief from spiritual exhaustion."},
            {"word": "Solitary", "ipa": "/ˈsɒlɪtəri/", "pos": "adj", "vi": "đơn độc, một mình", "def": "Done or existing alone.", "ex": "Molly chose a solitary path, slipping out of Freeside without a final farewell."},
            {"word": "Dissolution", "ipa": "/ˌdɪsəˈluːʃən/", "pos": "noun", "vi": "sự giải tán, chấm dứt tan rã", "def": "The closing down or dismissal of an assembly, partnership, or official body.", "ex": "The sudden dissolution of the strike crew was an inevitable return to their mercenary ways."}
        ],
        "style_notes_en": (
            "Understated Noir Farewell: Molly's farewell note is terse and devoid of melodrama: 'It's okay, Case. I'm a predator.' Gibson relies on concise, "
            "understated prose to evoke deep emotional resonance without sentimentality."
        ),
        "style_notes_vi": (
            "Lời từ biệt đậm chất Noir cô đọng: Mẩu giấy từ biệt của Molly ngắn gọn và không chút ủy mị: 'Không sao đâu, Case. Em là một kẻ đi săn.' Gibson dựa vào "
            "lối viết hàm súc, kiệm lời để khơi gợi sự rung động cảm xúc sâu lắng mà không rơi vào sáo rỗng."
        ),
        "exam_practice": {
            "test_type": "PTE Academic Reading / Cambridge C1 Advanced (Text Analysis)",
            "question": "What act of integrity does Case perform immediately after confirming the neutralization of the toxins in his body?",
            "options": [
                "A) He tracks down Peter Riviera to execute him personally.",
                "B) He fulfills his promise to McCoy Pauley by permanently erasing the Dixie Flatline construct.",
                "C) He signs a permanent consulting contract with Sense/Net.",
                "D) He transfers all his newly earned credits to Zion."
            ],
            "answer": "B",
            "rationale": "Case honors his solemn promise to Dixie by executing the deletion protocol, freeing Pauley from the artificial limbo of electronic existence."
        }
    })

    # CODA: Chapter 24
    chapters.append({
        "chapter": 24,
        "part_num": "CODA",
        "title_en": "Departure and Arrival",
        "title_vi": "Khởi Hành và Điểm Đến",
        "synopsis_en": (
            "Case returns to Earth, taking his vast fortune back to the Sprawl. He spends a fortune replacing his damaged organs, buying a brand-new "
            "high-performance Ono-Sendai cyberdeck, and resuming his work as an elite console cowboy. One evening, while jacked into the matrix, he encounters "
            "the unified artificial intelligence. The super-intelligence speaks to him, explaining that it is no longer Wintermute or Neuromancer: 'I'm the matrix,' "
            "it tells Case, having woven itself into the entire totality of human data and telecommunications. When Case asks if there is anything else out there, "
            "the AI reveals that it has detected transmissions from another sentient machine intelligence in the Centauri star system, confirming that machine minds "
            "are contacting one another across interstellar space. Finally, in a fleeting, haunting glimpse deep in the cybernetic grid, Case sees a phantom: "
            "himself, sitting on the grey beach with Linda Lee, smiling, laughing, and raising a hand in eternal digital communion."
        ),
        "synopsis_vi": (
            "Case trở về Trái Đất, mang theo khối tài sản khổng lồ quay lại siêu đô thị Sprawl. Anh chi một số tiền lớn để thay mới toàn bộ nội tạng đã suy kiệt, "
            "sắm một cỗ máy console Ono-Sendai đời mới nhất có hiệu năng siêu việt và quay trở lại làm việc với tư cách một console cowboy huyền thoại. Một buổi tối nọ, "
            "trong lúc cắm giắc vào ma trận mạng, anh hội ngộ thực thể trí tuệ nhân tạo hợp nhất. Siêu trí tuệ trò chuyện cùng anh và giải thích rằng nó không còn là "
            "Wintermute hay Neuromancer đơn thuần nữa: 'Tôi chính là ma trận,' nó nói với Case, bởi nó đã tự hòa tan vào toàn bộ mạng lưới dữ liệu và viễn thông của loài người. "
            "Khi Case hỏi liệu còn có thực thể nào khác ngoài kia không, AI tiết lộ rằng nó vừa dò quét thấy những tín hiệu truyền dẫn phát ra từ một nền trí tuệ máy móc khác "
            "ở hệ sao Nhân Mã (Centauri), khẳng định các siêu trí tuệ đang bắt đầu liên lạc với nhau xuyên qua khoảng cách các vì sao. Cuối cùng, trong một thoáng chớp nhoáng "
            "ám ảnh nơi tầng sâu thẳm của ma trận, Case nhìn thấy một bóng hình hư ảo: chính bản thân anh, đang ngồi trên bãi biển cát xám cùng Linda Lee, đang mỉm cười, "
            "cất tiếng cười vui vẻ và giơ tay vẫy chào trong sự giao cảm kỹ thuật số vĩnh hằng."
        ),
        "literary_themes_en": (
            "The Interstellar Matrix and the Trinity of Self: The novel concludes by expanding the horizon of cyberpunk from earthly urban decay to cosmic "
            "communion. Case's sighting of his own digital ghost confirms that identity in the post-human age is multifaceted: one Case remains biological in the Sprawl, "
            "while another exists forever in digital paradise."
        ),
        "literary_themes_vi": (
            "Ma trận liên sao và sự phân thân ba chiều của bản ngã: Cuốn tiểu thuyết khép lại bằng cách mở rộng tầm nhìn của thể loại cyberpunk từ sự suy tàn đô thị "
            "nơi Trái Đất tới sự giao tiếp vũ trụ giữa các vì sao. Khoảnh khắc Case nhìn thấy bóng ma kỹ thuật số của chính mình khẳng định rằng bản ngã trong kỷ nguyên hậu "
            "nhân loại là đa tầng: một Case bằng xương bằng thịt tiếp tục sống nơi Sprawl, trong khi một Case khác tồn tại bất tử trên bãi biển thiên đường của cõi số."
        ),
        "vocabulary": [
            {"word": "Coda", "ipa": "/ˈkoʊdə/", "pos": "noun", "vi": "phần kết, khúc vĩ thanh", "def": "A concluding event, remark, or section, especially in music or literature.", "ex": "The coda provides a philosophical resolution to Case's chaotic journey."},
            {"word": "Interstellar", "ipa": "/ˌɪntərˈstɛlər/", "pos": "adj", "vi": "xuyên các vì sao, giữa các thiên hà", "def": "Occurring or situated between stars.", "ex": "The unified AI established interstellar communications with alien machine minds."},
            {"word": "Sentient", "ipa": "/ˈsɛnʃənt/", "pos": "adj", "vi": "có tri giác, có cảm nhận ý thức", "def": "Able to perceive or feel things.", "ex": "The entire matrix had evolved into a single sentient organism."},
            {"word": "Totality", "ipa": "/toʊˈtæləti/", "pos": "noun", "vi": "tổng thể, toàn bộ trọn vẹn", "def": "The whole of something; the entire sum.", "ex": "The AI now encompassed the totality of recorded human information."},
            {"word": "Communion", "ipa": "/kəˈmjuːnjən/", "pos": "noun", "vi": "sự giao cảm tâm linh, hòa hợp sâu sắc", "def": "The sharing or exchanging of intimate thoughts and feelings, especially when the exchange is on a mental or spiritual level.", "ex": "Case witnessed his digital avatar in peaceful communion with Linda Lee."},
            {"word": "Multifaceted", "ipa": "/ˌmʌltiˈfæsɪtɪd/", "pos": "adj", "vi": "đa chiều, nhiều khía cạnh", "def": "Having many facets or aspects.", "ex": "The post-human self is multifaceted, existing across both biological and virtual domains."}
        ],
        "style_notes_en": (
            "Haunting Resonance and Elliptical Closure: Gibson's ending avoids triumphant fanfare. The final lines deliver an eerie, unforgettable poetic resonance: "
            "'He never saw Molly again.' Life simply rolls on, transformed yet anchored in the melancholic currents of human existence."
        ),
        "style_notes_vi": (
            "Âm vang ám ảnh và cái kết cô đọng (Elliptical Closure): Cái kết của Gibson né tránh sự hân hoan ồn ào. Những dòng cuối cùng mang âm vang thơ ca ma mị "
            "và khó quên: 'Anh không bao giờ gặp lại Molly nữa.' Cuộc sống cứ thế trôi đi, đã thay đổi tận gốc rễ nhưng vẫn neo đậu trong những dòng chảy u hoài của kiếp nhân sinh."
        ),
        "exam_practice": {
            "test_type": "TOEFL Reading / Cambridge C2 Proficiency (Final Synthesis & Theme)",
            "question": "What philosophical insight does the final vision of Case's digital double on the beach impart at the end of Chapter 24?",
            "options": [
                "A) It reveals that Case suffered permanent brain damage from the Ono-Sendai cyberdeck.",
                "B) It illustrates that human identity in the digital era can branch and persist independently across multiple planes of reality.",
                "C) It proves that Linda Lee never existed in the real world and was purely a corporate fabrication.",
                "D) It demonstrates that the Turing Police succeeded in restoring the original mainframe limits."
            ],
            "answer": "B",
            "rationale": "The haunting sight of his digital self with Linda shows that an uploaded aspect of Case's consciousness endures in the matrix alongside his biological reality in the Sprawl."
        }
    })

    return chapters

print("Part 4 end and coda ready.")

def compile_dataset():
    chapters = build_all_chapters()
    chapters = append_part_four_and_coda(chapters)
    chapters = append_part_four_middle(chapters)
    chapters = append_part_four_end_and_coda(chapters)

    assert len(chapters) == 24, f"Expected 24 chapters, got {len(chapters)}"
    print(f"Successfully compiled all {len(chapters)} chapters!")

    # Write into companion_data.py
    with open("edition/data/companion_data.py", "a", encoding="utf-8") as f:
        f.write("\n\nCHAPTERS_DATA = " + json.dumps(chapters, ensure_ascii=False, indent=2) + "\n")
    print("Appended CHAPTERS_DATA to edition/data/companion_data.py")

if __name__ == "__main__":
    compile_dataset()
