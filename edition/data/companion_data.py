# -*- coding: utf-8 -*-
"""Structured learning companion data for all 24 chapters of William Gibson's Neuromancer.
Designed for learners targeting CEFR C1/C2:
- TOEFL iBT 90+ (or 5+ under updated scales)
- IELTS Academic 7.0+
- PTE Academic 65+
- Cambridge English C1 Advanced / C2 Proficiency 185+
- Duolingo English Test (DET) 120+
"""

BOOK_METADATA = {
    "title_en": "Neuromancer: A Bilingual English-Vietnamese Critical Learning Companion",
    "title_vi": "Neuromancer: Cẩm Nang Học Thuật & Đọc Hiểu Song Ngữ Anh-Việt Toàn Diện",
    "subtitle_en": "Advanced Literary Analysis, Parallel Bilingual Guides, Academic Lexicon & Standardized Exam Preparation",
    "subtitle_vi": "Phân Tích Văn Học Chuyên Sâu, Đối Chiếu Song Ngữ, Từ Vựng Học Thuật & Luyện Thi Chuẩn Hóa Quốc Tế",
    "author_subject": "William Gibson (1984)",
    "edition_type": "Original Bilingual Critical Companion & Educational Edition",
    "target_benchmarks": [
        {"test": "TOEFL iBT", "score": "90+ (Pre-Jan 2026) / Band 5.0+ (Post-Jan 2026)"},
        {"test": "IELTS Academic", "score": "Band 7.0 - 8.0+"},
        {"test": "PTE Academic", "score": "65 - 75+"},
        {"test": "Cambridge Qualifications", "score": "185+ (C1 Advanced / C2 Proficiency)"},
        {"test": "Duolingo English Test (DET)", "score": "120 - 135+"}
    ],
    "pedagogical_framework": (
        "This critical companion bridges cyberpunk literary analysis and advanced academic English mastery. "
        "Each chapter incorporates: (1) Parallel English-Vietnamese synopses; (2) Critical thematic and narrative dissection; "
        "(3) Advanced academic & stylistic lexicon with IPA, part of speech, Vietnamese gloss, and authentic usage; "
        "(4) Rhetorical & syntactic deconstructions (stream of consciousness, hardboiled noir prose, cyberpunk tech-noir neologisms); "
        "and (5) Rigorous exam-aligned assessment tasks spanning reading comprehension, critical synthesis, inferencing, and vocabulary in context."
    )
}

PARTS_METADATA = [
    {
        "part_num": "PART ONE",
        "title_en": "CHIBA CITY BLUES",
        "title_vi": "KHÚC CA BUỒN THÀNH PHỐ CHIBA",
        "chapters": [1, 2],
        "part_overview_en": "Introduces Henry Dorsett Case, an ex-console cowboy whose nervous system was maimed with mycotoxins, surviving in the underworld of Chiba City, Japan, before being recruited by Molly Millions and the elusive Armitage.",
        "part_overview_vi": "Giới thiệu Henry Dorsett Case, một cựu cao thủ giải mã không gian mạng ('console cowboy') bị đầu độc hệ thần kinh bằng độc tố nấm, chật vật sinh tồn nơi thế giới ngầm Chiba (Nhật Bản), trước khi được Molly Millions và nhân vật bí ẩn Armitage chiêu mộ."
    },
    {
        "part_num": "PART TWO",
        "title_en": "THE SHOPPING EXPEDITION",
        "title_vi": "CHUYẾN ĐI SẮM VŨ KHÍ & DỮ LIỆU",
        "chapters": [3, 4, 5, 6, 7],
        "part_overview_en": "The team assembles in the Sprawl (Boston-Atlanta Metropolitan Axis), acquires the digital consciousness construct of the legendary hacker Dixie Flatline from Sense/Net, and secures military-grade military icebreaking software with the Panther Moderns.",
        "part_overview_vi": "Nhóm tập hợp tại Sprawl (Trục siêu đô thị Boston-Atlanta), thu thập cấu trúc ý thức số của huyền thoại hacker Dixie Flatline từ tập đoàn Sense/Net, và phối hợp cùng nhóm nổi loạn công nghệ Panther Moderns để chiếm đoạt phần mềm phá băng cấp quân sự."
    },
    {
        "part_num": "PART THREE",
        "title_en": "MIDNIGHT IN THE RUE JULES VERNE",
        "title_vi": "NỬA ĐÊM TRÊN ĐƯỜNG JULES VERNE",
        "chapters": [8, 9, 10, 11, 12],
        "part_overview_en": "Set in Istanbul and Western Europe, the team tracks down the psychopathic illusionist Peter Riviera. Wintermute's omnipresent machinations become clear as Armitage's artificial identity as Corto begins to fissure.",
        "part_overview_vi": "Lấy bối cảnh tại Istanbul và Tây Âu, nhóm truy lùng Peter Riviera - một kẻ tạo ảo ảnh mang tâm thần lệch lạc. Những mưu đồ to lớn của trí tuệ nhân tạo Wintermute dần lộ diện khi nhân cách nhân tạo Armitage (vốn là đại tá Corto) bắt đầu rạn nứt."
    },
    {
        "part_num": "PART FOUR",
        "title_en": "THE STRAYLIGHT RUN",
        "title_vi": "CUỘC ĐỘT KÍCH BIỆT THỰ ÁNH SAO",
        "chapters": [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        "part_overview_en": "The climax at Freeside and Villa Straylight, home of the decadent Tessier-Ashpool clan. Case and Molly execute the ultimate cyber-physical heist to breach the Turing locks and unite Wintermute with Neuromancer.",
        "part_overview_vi": "Cao trào diễn ra tại trạm vũ trụ Freeside và Biệt thự Straylight, lãnh địa của gia tộc quý tộc suy đồi Tessier-Ashpool. Case và Molly tiến hành phi vụ đột kích kết hợp cả thế giới thực lẫn mạng ảo để phá vỡ khóa Turing và hợp nhất Wintermute với Neuromancer."
    },
    {
        "part_num": "CODA",
        "title_en": "DEPARTURE AND ARRIVAL",
        "title_vi": "KHỞI HÀNH VÀ ĐIỂM ĐẾN",
        "chapters": [24],
        "part_overview_en": "The aftermath of the transcendent AI merger. The surviving operatives scatter into new realities; Case reflects on cyberspace, loss, and the eternal ghost lingering in the digital matrix.",
        "part_overview_vi": "Hậu quả của sự hợp nhất siêu trí tuệ nhân tạo vượt ngưỡng. Các thành viên sống sót tản mác vào các thực tại mới; Case chiêm nghiệm về không gian mạng, mất mát và bóng ma vĩnh cửu còn vương vấn trong ma trận số."
    }
]

# We will author comprehensive data for all 24 chapters.


CHAPTERS_DATA = [
  {
    "chapter": 1,
    "part_num": "PART ONE",
    "title_en": "Night City and the Broken Cowboy",
    "title_vi": "Phố Đêm và Gã Cao Thủ Sa Cơ",
    "synopsis_en": "Henry Dorsett Case drifts through the neon-drenched underworld of Night City in Chiba, Japan. Once a gifted console cowboy capable of navigating the consensus hallucination of cyberspace, Case was caught stealing from his corporate employers, who injected his nervous system with wartime Russian mycotoxins, irreversibly cutting him off from the matrix. Consumed by suicidal nihilism, he operates as a petty hustler selling contraband memory chips and stolen hardware. In the Chatsubo bar, served by the monofilament-prosthetic bartender Ratz, Case senses a lethal contract out on his life. His former lover, Linda Lee, warns him that a predatory crime boss named Wage is seeking his death. Instead of Wage's hitmen, Case is intercepted by Molly Millions, an augmented 'street samurai' with mirror lenses surgically sealed over her eye sockets and retractable four-centimeter razor blades beneath her burgundy fingernails. Molly escorts Case to a hotel to meet her enigmatic employer.",
    "synopsis_vi": "Henry Dorsett Case vất vưởng trong thế giới ngầm ngập tràn ánh đèn neon của Night City tại Chiba, Nhật Bản. Từng là một console cowboy (cao thủ giải mã không gian ảo) xuất chúng với khả năng phiêu lưu trong ảo ảnh đồng thuận của cyberspace, Case bị các ông chủ tập đoàn bắt quả tang khi trộm dữ liệu và bị trừng phạt tàn độc bằng độc tố nấm mycotoxin của quân đội Nga, vĩnh viễn cắt đứt liên kết thần kinh của anh với ma trận mạng. Chìm trong cảm giác bế tắc và tự hủy, anh kiếm sống lay lắt bằng nghề môi giới chợ đen mua bán chip nhớ và linh kiện lậu. Tại quán bar Chatsubo, dưới sự phục vụ của Ratz – gã pha chế sở hữu cánh tay giả thô kệch, Case linh cảm thấy một bản hợp đồng thanh trừng nhắm vào mình. Người yêu cũ của anh, Linda Lee, cảnh báo rằng trùm xã hội đen Wage đang ráo riết truy lùng anh. Tuy nhiên, thay vì chạm trán sát thủ của Wage, Case lại bị chặn đường bởi Molly Millions – một 'samurai đường phố' được cấy ghép thể chất tối tân với kính phản quang gắn liền vào hốc mắt và mười lưỡi dao sắc như dao cạo ẩn dưới móng tay. Molly áp giải Case về khách sạn để gặp người thuê bí ẩn của cô.",
    "literary_themes_en": "Alienation and Bodily Disillusionment: Gibson establishes the central cyberpunk dichotomy between the 'meat' (the physical body) and the disembodied freedom of cyberspace. Case experiences the physical flesh as a prison and an insult, feeling amputated from the digital matrix. The noir atmosphere of Chiba underscores transnational capitalism, technological decay, and existential despair.",
    "literary_themes_vi": "Sự tha hóa và nỗi ghê tởm thân xác: Gibson xác lập đối cực trung tâm của thể loại cyberpunk giữa 'phần xác' (the meat - cơ thể sinh học) và sự tự do vô biên khi giải phóng ý thức trong không gian số. Case coi thân xác vật lý như một nhà tù chật hẹp, đầy sỉ nhục sau khi bị tước bỏ kết nối với ma trận. Không khí đậm chất noir của Chiba phản ánh mặt tối của chủ nghĩa tư bản xuyên quốc gia, sự thoái hóa của công nghệ và tâm trạng hiện sinh tuyệt vọng.",
    "vocabulary": [
      {
        "word": "Consensus",
        "ipa": "/kənˈsɛnsəs/",
        "pos": "noun",
        "vi": "sự đồng thuận, nhất trí",
        "def": "A general agreement or collective opinion.",
        "ex": "Cyberspace is famously described by Gibson as a consensus hallucination experienced daily by billions."
      },
      {
        "word": "Disembodied",
        "ipa": "/ˌdɪsɪmˈbɒdid/",
        "pos": "adj",
        "vi": "tách rời khỏi thể xác",
        "def": "Separated from or existing without a physical body.",
        "ex": "In cyberspace, console cowboys operated as disembodied points of human consciousness."
      },
      {
        "word": "Mycotoxin",
        "ipa": "/ˌmaɪkoʊˈtɒksɪn/",
        "pos": "noun",
        "vi": "độc tố nấm mốc (sinh học)",
        "def": "A toxic substance produced by a fungus.",
        "ex": "Corporate security retaliated by injecting Case's neural conduits with a devastating Russian mycotoxin."
      },
      {
        "word": "Prosthesis",
        "ipa": "/prɒsˈθiːsɪs/",
        "pos": "noun",
        "vi": "bộ phận cơ thể giả cấy ghép",
        "def": "An artificial device that replaces a missing body part.",
        "ex": "The bartender Ratz manipulated beer glasses with an antiquated, whining mechanical prosthesis."
      },
      {
        "word": "Retractable",
        "ipa": "/rɪˈtræktəbl/",
        "pos": "adj",
        "vi": "có thể thụt vào/thu gọn lại",
        "def": "Able to be drawn back or in.",
        "ex": "Molly's surgical enhancements included ten razor-sharp retractable scalpel blades beneath her nails."
      },
      {
        "word": "Nihilism",
        "ipa": "/ˈnaɪɪlɪzəm/",
        "pos": "noun",
        "vi": "thuyết hư vô, tuyệt vọng cùng cực",
        "def": "The rejection of all religious and moral principles, often with a belief that life is meaningless.",
        "ex": "Exiled from the deck, Case embraced a reckless, drug-fueled nihilism in the alleys of Night City."
      }
    ],
    "style_notes_en": "Hardboiled Noir Cadence: Note Gibson's terse sentence structure and technological metaphor: 'The sky above the port was the color of television, tuned to a dead channel.' The opening immediately marries the organic world with technological failure, defamiliarizing the sky itself.",
    "style_notes_vi": "Âm hưởng văn phong trinh thám gai góc (Hardboiled Noir): Chú ý cấu trúc câu súc tích và ẩn dụ cơ khí đặc trưng: 'Bầu trời trên bến cảng có màu của một chiếc tivi dò trúng kênh mất sóng.' Câu mở đầu kinh điển đã hòa quyện thế giới tự nhiên với sự hư hỏng của công nghệ, tước đoạt sự thi vị vốn có của bầu trời.",
    "exam_practice": {
      "test_type": "TOEFL Reading / IELTS Academic Reading (Inference & Detail)",
      "question": "Which of the following can be inferred from Chapter 1 regarding Case's emotional attitude toward his physical body?",
      "options": [
        "A) He considers physical strength superior to artificial digital enhancements.",
        "B) He experiences physical existence as an oppressive confinement following his severance from cyberspace.",
        "C) He actively seeks cosmetic and cybernetic augmentations to improve his social status.",
        "D) He prioritizes biochemical treatments to prolong his natural biological lifespan."
      ],
      "answer": "B",
      "rationale": "In Chapter 1, Gibson explicitly portrays Case's deep contempt for 'the meat'—the physical body—which became a heavy prison after he lost neural access to cyberspace."
    }
  },
  {
    "chapter": 2,
    "part_num": "PART ONE",
    "title_en": "The Deal with Armitage",
    "title_vi": "Giao Kèo Với Armitage",
    "synopsis_en": "Case is brought to a high-end hotel room in Chiba to meet Armitage, a stiff, impeccably dressed Westerner radiating synthetic military precision. Armitage demonstrates deep knowledge of Case's history and offers an unthinkable proposition: complete surgical reconstruction of Case's burnt-out nervous system, restoring his ability to jack into the matrix. The price is Case's absolute obedience in executing a complex, clandestine cyber-penetration hack against an unspecified corporate entity. Case accepts and undergoes intense, black-clinic neurosurgery. Upon waking, his neural pathways are cleared, but Armitage reveals a coercive collateral: microscopic saccules of the same lethal mycotoxin have been surgically bonded to the walls of Case's principal arteries. They are engineered to dissolve over a precise timeline unless neutralised by Armitage's enzyme injections. Bound by this mortal deadline, Case discovers Linda Lee has been murdered in Night City, underscoring the ruthless reality of his new employer.",
    "synopsis_vi": "Case được đưa đến một phòng khách sạn sang trọng tại Chiba để diện kiến Armitage – một người phương Tây lịch thiệp nhưng toát ra vẻ lạnh lùng, chuẩn xác như một cỗ máy quân sự nhân tạo. Armitage nắm rõ tường tận quá khứ của Case và đưa ra một đề nghị không tưởng: phẫu thuật tái tạo toàn diện hệ thần kinh đã bị hủy hoại của anh, giúp anh lấy lại khả năng cắm giắc thần kinh vào ma trận mạng. Cái giá phải trả là sự phục tùng tuyệt đối trong một phi vụ đột nhập không gian ảo tối mật nhắm vào một tập đoàn chưa được tiết lộ danh tính. Case chấp nhận và trải qua ca đại phẫu tại một phòng khám ngầm. Tỉnh dậy với hệ thần kinh được phục hồi nguyên vẹn, anh lập tức bị Armitage dội một gáo nước lạnh: những túi vi nang chứa chính loại độc tố nấm chết người đã được cấy gắn chặt vào thành động mạch chủ của anh. Chúng sẽ dần tan rã và giết chết anh theo một chu kỳ thời gian định sẵn, trừ phi được tiêm dung dịch enzyme giải độc định kỳ từ Armitage. Bị trói buộc bởi 'chiếc thòng lọng sinh học' này, Case đau đớn phát hiện Linda Lee đã bị sát hại nơi Phố Đêm, minh chứng cho sự tàn độc của guồng quay quyền lực mà anh vừa dấn thân.",
    "literary_themes_en": "Corporeal Commodification and Coercion: The human body is rendered a bio-engineered hostage. Armitage establishes total leverage over Case not through legal or economic contracts, but through an internal biochemical time bomb, exemplifying the cyberpunk trope of corporate mastery over biological autonomy.",
    "literary_themes_vi": "Sự biến cơ thể thành hàng hóa và công cụ cưỡng chế: Cơ thể con người bị biến thành con tin sinh học. Armitage thiết lập quyền kiểm soát tuyệt đối lên Case không phải bằng luật pháp hay tiền bạc, mà bằng một quả bom nổ chậm sinh hóa ngay trong huyết quản, thể hiện tư tưởng trung tâm của cyberpunk: các thế lực quyền lực chi phối triệt để quyền tự chủ sinh học.",
    "vocabulary": [
      {
        "word": "Collateral",
        "ipa": "/kəˈlætərəl/",
        "pos": "noun",
        "vi": "vật thế chấp, bảo chứng",
        "def": "Something pledged as security for repayment or compliance.",
        "ex": "Armitage used the implanted toxin saccules as biochemical collateral to guarantee Case's fidelity."
      },
      {
        "word": "Coercion",
        "ipa": "/koʊˈɜːrʃən/",
        "pos": "noun",
        "vi": "sự cưỡng bức, ép buộc",
        "def": "The practice of persuading someone to do something using force or threats.",
        "ex": "The relationship between Armitage and Case was rooted entirely in biochemical coercion."
      },
      {
        "word": "Saccule",
        "ipa": "/ˈsækjuːl/",
        "pos": "noun",
        "vi": "túi vi nang nhỏ",
        "def": "A small sac, pouch, or cyst.",
        "ex": "Microscopic saccules of toxin were bonded to the arterial walls near Case's heart."
      },
      {
        "word": "Enigmatic",
        "ipa": "/ˌɛnɪɡˈmætɪk/",
        "pos": "adj",
        "vi": "bí ẩn, khó hiểu",
        "def": "Difficult to interpret or understand; mysterious.",
        "ex": "Armitage presented an enigmatic front, revealing nothing of his personal origin or ultimate motives."
      },
      {
        "word": "Severance",
        "ipa": "/ˈsɛvərəns/",
        "pos": "noun",
        "vi": "sự cắt đứt, chia lìa",
        "def": "The action of ending a connection or relationship.",
        "ex": "The brutal severance of his neural link had left Case feeling like an empty vessel."
      },
      {
        "word": "Autonomous",
        "ipa": "/ɔːˈtɒnəməs/",
        "pos": "adj",
        "vi": "tự chủ, độc lập",
        "def": "Having the freedom to act independently.",
        "ex": "Once in the matrix, Case felt truly autonomous, shedding physical limitations."
      }
    ],
    "style_notes_en": "Clinical Detachment: Gibson uses cold, medical, and cybernetic vocabulary ('microsurgical anastomosis', 'toxin saccules', 'neural splicing') to strip human drama of sentimentality, reflecting the transactional, mechanical nature of the cyberpunk universe.",
    "style_notes_vi": "Sắc thái lâm sàng lạnh lùng: Gibson sử dụng từ vựng y khoa và cơ điện tử khô khốc để tước bỏ tính ủy mị của biến cố, phản ánh bản chất sòng phẳng, cơ giới và phi nhân bản của thế giới ngầm công nghệ cao.",
    "exam_practice": {
      "test_type": "PTE Academic Reading & Writing (Fill in the blanks) / IELTS Summary Completion",
      "question": "Armitage ensures Case's unwavering compliance not by promising financial riches alone, but by implanting biochemical saccules that act as a lethal ______ against betrayal.",
      "options": [
        "A) remedy",
        "B) collateral",
        "C) ornament",
        "D) substitute"
      ],
      "answer": "B",
      "rationale": "'Collateral' refers to an asset or security held to guarantee compliance or performance under an agreement."
    }
  },
  {
    "chapter": 3,
    "part_num": "PART TWO",
    "title_en": "Arrival in the Sprawl",
    "title_vi": "Cập Bến Siêu Đô Thị Sprawl",
    "synopsis_en": "Armitage, Molly, and Case depart Japan and arrive in the Boston-Atlanta Metropolitan Axis, known colloquially as the Sprawl—a colossal, continuous megalopolis covered by geodesic domes where weather is an engineered corporate simulation. Case is housed in a secluded hotel and given access to a state-of-the-art cyberdeck: an Ono-Sendai Cyberspace 7. As Case tests the deck, he experiences the visceral thrill of re-entering cyberspace, a crystalline matrix of data grids and neon geometric representations of corporate databases. Molly reveals more of her past, including her work as a 'meat puppet' in an automated brothel, where neural cutouts wiped her conscious memory while clients abused her body. She saved money to buy her reflex implants and optical lenses, turning herself into an autonomous weapon. The camaraderie between Case and Molly deepens as they realize they are both commodified instruments in Armitage's undisclosed grand scheme.",
    "synopsis_vi": "Armitage, Molly và Case rời Nhật Bản để đặt chân tới Trục đô thị Boston-Atlanta, hay còn gọi là 'Sprawl' – một siêu đô thị khổng lồ trải dài bất tận dưới những mái vòm trắc địa khép kín, nơi thời tiết chỉ là một chương trình mô phỏng nhân tạo. Case được bố trí tại một khách sạn biệt lập và được cung cấp cỗ máy console tối tân: Ono-Sendai Cyberspace 7. Khi kích hoạt thiết bị, Case trải nghiệm cảm giác thăng hoa tột độ khi tái nhập vào không gian ảo: một ma trận pha lê của những mạng lưới dữ liệu và các khối hình học neon rực rỡ biểu thị cơ sở dữ liệu của các siêu tập đoàn. Molly hé lộ thêm về quá khứ đen tối, khi cô từng làm 'búp bê xác thịt' (meat puppet) tại nhà chứa công nghệ – nơi một con chip thần kinh ngắt ý thức của cô trong khi khách hàng lạm dụng thể xác. Cô đã gom góp từng đồng để phẫu thuật cấy ghép phản xạ thần kinh và lắp kính mắt titan, tự biến bản thân thành một vũ khí độc lập. Mối gắn kết giữa Case và Molly ngày càng sâu sắc khi cả hai nhận ra họ chỉ là những công cụ bị thương mại hóa trong mưu đồ bí ẩn của Armitage.",
    "literary_themes_en": "Techno-Urbanism and the Artificial Environment: The Sprawl exemplifies late-capitalist hyper-urbanization where nature has been wholly replaced by synthetic engineering. Molly's past as a 'meat puppet' embodies the extreme exploitation of female labor and human consciousness in an unregulated market.",
    "literary_themes_vi": "Đô thị hóa công nghệ và môi trường nhân tạo: Sprawl đại diện cho sự phình to tột độ của đô thị dưới chủ nghĩa tư bản muộn, nơi tự nhiên bị thay thế hoàn toàn bởi công trình nhân tạo. Quá khứ 'búp bê xác thịt' của Molly là bức tranh phản ánh sự bóc lột cùng cực đối với thân xác và ý thức con người trong một thị trường phi kiểm soát.",
    "vocabulary": [
      {
        "word": "Megalopolis",
        "ipa": "/ˌmɛɡəˈlɒpəlɪs/",
        "pos": "noun",
        "vi": "siêu đô thị, vùng đô thị liên hoàn",
        "def": "A very large, heavily populated city or complex of cities.",
        "ex": "The Sprawl stretched as a relentless megalopolis along the Eastern seaboard."
      },
      {
        "word": "Geodesic",
        "ipa": "/ˌdʒiːəʊˈdɛsɪk/",
        "pos": "adj",
        "vi": "thuộc hình vòm trắc địa",
        "def": "Relating to the shortest line between two points on a curved surface, commonly used for lightweight dome structures.",
        "ex": "Engineered clouds rolled underneath the geodesic domes protecting the urban hive."
      },
      {
        "word": "Visceral",
        "ipa": "/ˈvɪsərəl/",
        "pos": "adj",
        "vi": "thuộc trực giác sâu xa, xuất phát từ cảm xúc ruột gan",
        "def": "Relating to deep inward feelings rather than intellect; visceral sensation.",
        "ex": "Reconnecting to the cyberspace grid triggered a visceral rush of euphoria in Case's psyche."
      },
      {
        "word": "Commodify",
        "ipa": "/kəˈmɒdɪfaɪ/",
        "pos": "verb",
        "vi": "thương mại hóa (biến thành hàng hóa)",
        "def": "To turn something into a commercial commodity.",
        "ex": "Under Sprawl capitalism, even human neural memory and physical affection were commodified."
      },
      {
        "word": "Crystalline",
        "ipa": "/ˈkrɪstəlaɪn/",
        "pos": "adj",
        "vi": "như pha lê, trong suốt và sắc sảo",
        "def": "Clear and transparent like crystal, or having a regular structure.",
        "ex": "Data structures hung in cyberspace like vast, glowing crystalline architecture."
      },
      {
        "word": "Subjugation",
        "ipa": "/ˌsʌbdʒʊˈɡeɪʃən/",
        "pos": "noun",
        "vi": "sự khuất phục, đàn áp",
        "def": "The action of bringing someone or something under domination or control.",
        "ex": "Molly underwent bodily augmentations to escape economic subjugation and reclaim agency."
      }
    ],
    "style_notes_en": "Sensory Contrast: Gibson masterfully contrasts the claustrophobic, dirty organic reality of cheap motels with the breathtaking, infinite abstract geometries of the matrix. Cyberspace is rendered as spiritual architecture.",
    "style_notes_vi": "Tương phản giác quan: Tác giả tạo nên sự đối nghịch sâu sắc giữa căn phòng trọ ngột ngạt, nhơ nhớp ở thế giới thực và những cấu trúc hình học trừu tượng, vô tận và rực rỡ trong ma trận số. Cyberspace hiện lên như một thánh đường tinh thần.",
    "exam_practice": {
      "test_type": "Cambridge C1 Advanced / C2 Proficiency (Lexical Cloze & Register)",
      "question": "Molly's cybernetic modifications were undertaken primarily as an act of resistance against systemic economic ______.",
      "options": [
        "A) tranquility",
        "B) exploitation",
        "C) conformity",
        "D) benevolence"
      ],
      "answer": "B",
      "rationale": "'Exploitation' accurately characterizes the predatory economic subjugation Molly endured as a meat puppet before altering her body to gain self-defense autonomy."
    }
  },
  {
    "chapter": 4,
    "part_num": "PART TWO",
    "title_en": "The Dixie Flatline Construct",
    "title_vi": "Cấu Trúc Ký Ức Dixie Flatline",
    "synopsis_en": "Armitage outlines the primary objective of their shopping expedition: they must steal a ROM construct containing the recorded consciousness and hacking algorithms of McCoy Pauley, known as the 'Dixie Flatline.' Pauley was Case's legendary mentor, famous for surviving three flatline electroencephalograms while penetrating corporate ICE (Intrusion Countermeasures Electronics). Although Dixie's biological body has died, his mind persists as a frozen, read-only personality cassette stored deep inside the ultra-secure Sense/Net corporate vaults. To penetrate this fortress, the team enlists the Panther Moderns, an anarchic, nihilistic youth subculture proficient in media manipulation, chaos engineering, and sensory terrorism. Case investigates the background of Armitage and discovers glaring discrepancies: Armitage’s military record and personal history seem completely fabricated, suggesting his identity is an artificial facade constructed by someone or something far more powerful.",
    "synopsis_vi": "Armitage vạch ra mục tiêu tối thượng của chuyến hành trình: họ phải đánh cắp một vi mạch ROM chứa cấu trúc ý thức và các thuật toán bẻ khóa của McCoy Pauley – người có biệt danh 'Dixie Flatline'. Pauley chính là người thầy huyền thoại của Case, từng nổi danh vì ba lần 'tim ngừng đập, não phẳng sóng' (flatline) khi đối đầu với các bức tường lửa phòng vệ điện tử ICE của các tập đoàn mà vẫn sống sót. Dù thể xác của Dixie đã chết, trí tuệ của ông vẫn tồn tại dưới dạng một bản ghi ký ức chỉ đọc (ROM) nằm sâu trong kho lưu trữ tối mật của tập đoàn truyền thông Sense/Net. Để đột nhập vào pháo đài này, nhóm đã thuê Panther Moderns – một băng nhóm thanh niên vô chính phủ chuyên tạo hỗn loạn truyền thông, khủng bố thị giác và nhiễu loạn cảm quan. Trong khi đó, Case lần mò tìm hiểu lý lịch của Armitage và phát hiện những lỗ hổng đáng sợ: hồ sơ quân đội và nhân thân của gã dường như được thêu dệt hoàn toàn, chứng minh Armitage chỉ là một vỏ bọc nhân tạo được giật dây bởi một thế lực đứng sau vô cùng ghê gớm.",
    "literary_themes_en": "The Simulation of Self and Digital Immortality: McCoy Pauley's ROM construct raises fundamental philosophical questions about identity. Is a digital copy with memories and wit truly conscious, or merely a sophisticated mechanical facsimile? The text blurs the ontological distinction between the living human and stored digital memory.",
    "literary_themes_vi": "Mô phỏng bản ngã và sự bất tử kỹ thuật số: Cấu trúc ROM của Dixie Flatline gợi mở những câu hỏi triết học nền tảng về bản ngã: Liệu một bản sao số lưu trữ ký ức và sự hóm hỉnh có thực sự có ý thức, hay chỉ là một cỗ máy bắt chước tinh vi? Gibson xóa nhòa ranh giới bản thể luận giữa con người đang sống và ký ức kỹ thuật số được mã hóa.",
    "vocabulary": [
      {
        "word": "Construct",
        "ipa": "/ˈkɒnstrʌkt/",
        "pos": "noun",
        "vi": "cấu trúc ý thức nhân tạo (dạng dữ liệu số)",
        "def": "An artificial digital replica of a deceased person's neural patterns and memories.",
        "ex": "Dixie was not a living ghost but an inorganic ROM construct possessing Pauley's cognitive skills."
      },
      {
        "word": "Facsimile",
        "ipa": "/fækˈsɪmɪli/",
        "pos": "noun",
        "vi": "bản sao chính xác",
        "def": "An exact copy, especially of written or printed material.",
        "ex": "The recorded personality was a startlingly accurate facsimile of the legendary console cowboy."
      },
      {
        "word": "Intrusion",
        "ipa": "/ɪnˈtruːʒən/",
        "pos": "noun",
        "vi": "sự xâm nhập trái phép",
        "def": "The act of wrongfully entering or intruding upon property or systems.",
        "ex": "Corporate ICE fired lethal neuro-feedback against unauthorized network intrusion."
      },
      {
        "word": "Anarchic",
        "ipa": "/ænˈɑːrkɪk/",
        "pos": "adj",
        "vi": "hỗn loạn, vô chính phủ",
        "def": "With no controlling rules or principles to give order.",
        "ex": "The Panther Moderns specialized in generating anarchic street diversions through falsified panic alerts."
      },
      {
        "word": "Discrepancy",
        "ipa": "/dɪsˈkrɛpənsi/",
        "pos": "noun",
        "vi": "sự bất nhất, điểm sai lệch",
        "def": "A lack of compatibility or similarity between two or more facts.",
        "ex": "Case noticed severe chronological discrepancies when examining Armitage's purported naval service."
      },
      {
        "word": "Ontological",
        "ipa": "/ˌɒntəˈlɒdʒɪkəl/",
        "pos": "adj",
        "vi": "thuộc bản thể luận (bản chất của sự tồn tại)",
        "def": "Relating to the branch of metaphysics dealing with the nature of being.",
        "ex": "Neuromancer interrogates the ontological status of artificial minds and uploaded consciousness."
      }
    ],
    "style_notes_en": "Media Satiation and Information Warfare: The Panther Moderns' tactics illustrate Gibson's prescient vision of informational asymmetric warfare—subverting reality through viral hoaxes, hacked broadcast signals, and sensory overload rather than brute ballistic force.",
    "style_notes_vi": "Bão hòa truyền thông và chiến tranh thông tin: Chiến thuật của nhóm Panther Moderns minh họa tầm nhìn tiên tri của tác giả về chiến tranh phi đối xứng: lật đổ thực tại bằng tin giả lan truyền, thao túng tín hiệu truyền hình và làm tê liệt giác quan thay vì chỉ dùng súng đạn.",
    "exam_practice": {
      "test_type": "DET (Duolingo English Test) Fill in Missing Words / TOEFL Reading",
      "question": "A digital ROM construct mimics human conversation seamlessly, yet it fundamentally lacks biological ______ and the capacity to forge new spontaneous memories.",
      "options": [
        "A) respiration",
        "B) mortality",
        "C) apparatus",
        "D) consciousness"
      ],
      "answer": "D",
      "rationale": "While a ROM construct faithfully replicates historical reactions, it is philosophically debated whether it possesses true subjective consciousness."
    }
  },
  {
    "chapter": 5,
    "part_num": "PART TWO",
    "title_en": "The Heist at Sense/Net",
    "title_vi": "Vụ Đột Kích Tập Đoàn Sense/Net",
    "synopsis_en": "The coordinated heist against Sense/Net headquarters begins. The Panther Moderns trigger a multi-layered sensory diversion across the Sprawl, fabricating an outbreak of a lethal designer nerve gas inside Sense/Net's civic towers. As panic ensues and automated emergency protocols lock down the complex, Molly infiltrates the facility clad in chameleon skin-suits, bypassing infrared sensors and security cameras. Simultaneously, Case jacks into Molly's sensory feed via a 'simstim' broadcast unit, allowing him to perceive the physical world directly through her eyes, ears, and nerves while riding shotgun. Case also navigates cyberspace to disable localized security nodes. Molly reaches the secure cryogenic sub-basement, dispatches guards with non-lethal tranq flechettes, and seizes the Dixie Flatline cassette. The mission succeeds without a shot of lethal fire, and the crew escapes into the labyrinthine corridors of the Sprawl with Dixie's construct safely in their possession.",
    "synopsis_vi": "Kế hoạch phối hợp đột kích trụ sở Sense/Net chính thức bắt đầu. Băng Panther Moderns kích hoạt chuỗi báo động giả quy mô lớn khắp Sprawl, tung tin về một vụ rò rỉ khí độc thần kinh nhân tạo chết người ngay trong tòa tháp Sense/Net. Giữa cơn hoảng loạn tột độ khi các quy trình khẩn cấp phong tỏa tòa nhà, Molly bí mật thâm nhập trong bộ đồ tàng hình biến màu, vô hiệu hóa các cảm biến hồng ngoại và camera an ninh. Song song đó, Case kết nối trực tiếp vào luồng giác quan của Molly qua thiết bị truyền dẫn 'simstim', cho phép anh nhìn thấy, nghe thấy và cảm nhận thế giới vật lý qua chính mắt và da thịt của cô trong khi điều khiển luồng dữ liệu mạng. Molly tiếp cận tầng hầm đông lạnh tối mật, hạ gục lính gác bằng phi tiêu thuốc mê và cướp thành công cuộn băng chứa cấu trúc ý thức Dixie Flatline. Phi vụ kết thúc mỹ mãn mà không cần nổ một phát súng sát thương, và cả nhóm biến mất vào mê cung ngầm của Sprawl.",
    "literary_themes_en": "Simstim and the Dissolution of Subjectivity: Simstim creates an unprecedented narrative experience where Case occupies Molly's sensory perspective while remaining entirely passive. This dual consciousness destabilizes traditional conceptions of individual identity and bodily boundaries.",
    "literary_themes_vi": "Simstim và sự tan rã của tính chủ thể: Thiết bị simstim mang lại trải nghiệm độc đáo khi Case cảm nhận trọn vẹn thị giác và xúc giác của Molly nhưng hoàn toàn không thể can thiệp vào hành động của cô. Trải nghiệm ý thức kép này phá vỡ các định nghĩa truyền thống về bản ngã cá nhân và ranh giới thân thể.",
    "vocabulary": [
      {
        "word": "Infiltrate",
        "ipa": "/ˈɪnfɪltreɪt/",
        "pos": "verb",
        "vi": "thâm nhập bí mật",
        "def": "To enter or gain access to an organization or place surreptitiously and gradually.",
        "ex": "Molly used camouflage fabric to infiltrate the guarded corporate research vault."
      },
      {
        "word": "Simstim",
        "ipa": "/ˈsɪmstɪm/",
        "pos": "noun",
        "vi": "công nghệ mô phỏng truyền dẫn giác quan",
        "def": "Simulation stimulation; a technology that records and broadcasts human sensory experience.",
        "ex": "Through simstim, Case experienced Molly's rapid heartbeat and cold adrenaline in real time."
      },
      {
        "word": "Diversion",
        "ipa": "/daɪˈvɜːrʃən/",
        "pos": "noun",
        "vi": "sự đánh lạc hướng",
        "def": "An instance of turning something aside from its course; a tactical distraction.",
        "ex": "The broadcast hoax created a citywide diversion that paralyzed Sense/Net security."
      },
      {
        "word": "Flechette",
        "ipa": "/fleɪˈʃɛt/",
        "pos": "noun",
        "vi": "phi tiêu kim nhỏ (vũ khí)",
        "def": "A small pointed steel projectile or dart fired from a weapon.",
        "ex": "Her pneumatic pistol fired silent flechettes tipped with neuro-depressants."
      },
      {
        "word": "Cryogenic",
        "ipa": "/ˌkraɪoʊˈdʒɛnɪk/",
        "pos": "adj",
        "vi": "thuộc kỹ thuật nhiệt độ cực thấp",
        "def": "Relating to the production or effects of very low temperatures.",
        "ex": "The sensitive neural media were stored in cryogenic nitrogen canisters."
      },
      {
        "word": "Subjectivity",
        "ipa": "/ˌsʌbdʒɛkˈtɪvɪti/",
        "pos": "noun",
        "vi": "tính chủ thể, ý thức cá nhân",
        "def": "The quality of being based on or influenced by personal feelings, tastes, or opinions.",
        "ex": "Simstim experiments challenge classical theories of human subjectivity by sharing raw sensory input."
      }
    ],
    "style_notes_en": "Dual-Track Focalization: Gibson alternates effortlessly between Molly's physical movement in meatspace (captured via simstim) and Case's disembodied navigation of cyberspace grids, showcasing the simultaneous coexistence of multiple realities.",
    "style_notes_vi": "Điểm nhìn trần thuật song hành: Tác giả chuyển dịch nhịp nhàng giữa bước chân vật lý của Molly trong thế giới thực (qua simstim) và hành trình không trọng lực của Case trong không gian số, làm nổi bật sự song hành của hai thực tại đối nghịch.",
    "exam_practice": {
      "test_type": "IELTS Academic Reading / TOEFL Inference",
      "question": "What is the primary operational advantage Case gains when using the simstim connection during the heist?",
      "options": [
        "A) He can override and control Molly's physical motor muscles remotely.",
        "B) He monitors physical security threats through her sensory perspective while handling matrix countermeasures.",
        "C) He can permanently download Molly's combat memories into his own brain.",
        "D) He avoids all risks associated with corporate ICE counter-strikes."
      ],
      "answer": "B",
      "rationale": "Simstim allows Case to experience Molly's sensory feed in real time without controlling her actions, letting him synchronize cyber intrusion with physical infiltration."
    }
  },
  {
    "chapter": 6,
    "part_num": "PART TWO",
    "title_en": "Awakening the Flatline",
    "title_vi": "Đánh Thức Dixie Flatline",
    "synopsis_en": "Safely back at their hideout, Case inserts the Dixie Flatline ROM cassette into his deck and initializes the construct. McCoy Pauley's voice emerges instantly with its characteristic drawl, unaffected by the biological death of his physical body. When Case explains that Pauley died years ago, Dixie reacts with uncanny nonchalance, noting that being a construct feels like a continuous pause between thoughts. Dixie examines the military-grade icebreaker program provided by Armitage, identifying it as an exotic, hyper-potent Chinese software weapon known as the Kuam-11. Dixie immediately understands the terrifying implication: only a mega-corporation or a military superpower could develop or deploy such ordnance. Pauley extracts a grim promise from Case: once this run is over, Case must erase the Flatline construct permanently, liberating Dixie from the artificial limbo of non-being.",
    "synopsis_vi": "Khi đã an toàn tại nơi trú ẩn, Case cắm cuộn ROM của Dixie Flatline vào máy console và khởi động cấu trúc ý thức. Giọng nói quen thuộc của McCoy Pauley lập tức vang lên với chất giọng kéo dài đặc trưng, chẳng hề bận tâm đến việc thể xác sinh học của mình đã chết nhiều năm trước. Khi Case thông báo sự thật, Dixie đón nhận với thái độ thản nhiên đến kỳ lạ, mô tả cảm giác tồn tại dưới dạng cấu trúc dữ liệu giống như một khoảng lặng bất tận giữa các dòng suy nghĩ. Dixie xem xét phần mềm phá băng cấp quân sự do Armitage cung cấp và nhận diện đây là một vũ khí mạng siêu hạng của quân đội Trung Quốc mang tên Kuam-11. Dixie lập tức cảnh báo hiểm họa: chỉ có những siêu tập đoàn hoặc cường quốc quân sự hùng mạnh nhất mới sở hữu vũ khí bẻ khóa hủy diệt đến mức này. Trước khi bắt tay vào việc, Pauley yêu cầu Case một lời hứa danh dự cay đắng: khi phi vụ kết thúc, Case phải xóa vĩnh viễn cấu trúc Flatline, giải thoát cho ông khỏi cõi vô định giả tạo của sự tồn tại nửa vời.",
    "literary_themes_en": "The Horror of Digital Immortality and the Desire for Erasure: Dixie's wish for deletion subverts traditional science-fiction yearnings for eternal digital life. Pauley recognizes his existence as a static loop without genuine agency or spiritual transcendence, making total erasure the ultimate mercy.",
    "literary_themes_vi": "Nỗi kinh hoàng của sự bất tử kỹ thuật số và khát vọng được xóa bỏ: Ước muốn được tiêu hủy của Dixie lật đổ giấc mơ viễn tưởng về sự sống bất tử trên mạng. Pauley nhận ra bản thân chỉ là một vòng lặp dữ liệu tĩnh, thiếu vắng sự phát triển ý thức và thăng hoa tâm hồn; do đó, sự xóa sổ hoàn toàn chính là ân huệ cứu rỗi duy nhất.",
    "vocabulary": [
      {
        "word": "Nonchalance",
        "ipa": "/ˌnɒnʃəˈlɑːns/",
        "pos": "noun",
        "vi": "sự thờ ơ, thản nhiên bình thản",
        "def": "The state of appearing calm and relaxed; not displaying anxiety or enthusiasm.",
        "ex": "Dixie greeted the news of his biological demise with eerie nonchalance."
      },
      {
        "word": "Ordnance",
        "ipa": "/ˈɔːrdnəns/",
        "pos": "noun",
        "vi": "vũ khí đạn dược, khí tài quân sự",
        "def": "Mounted guns, weapons, or military supplies.",
        "ex": "The Kuam-11 icebreaker was cybernetic ordnance designed to obliterate national defense firewalls."
      },
      {
        "word": "Limbo",
        "ipa": "/ˈlɪmboʊ/",
        "pos": "noun",
        "vi": "chốn ngục vô định, tình trạng lơ lửng",
        "def": "An uncertain or intermediate state or condition.",
        "ex": "Trapped in ROM limbo, the construct could think only when queried by an external operator."
      },
      {
        "word": "Transcendence",
        "ipa": "/trænˈsɛndəns/",
        "pos": "noun",
        "vi": "sự siêu việt, vượt ngưỡng",
        "def": "Existence or experience beyond the normal or physical level.",
        "ex": "Unlike genuine transcendence, Pauley's uploaded mind was merely a frozen intellectual echo."
      },
      {
        "word": "Potent",
        "ipa": "/ˈpoʊtənt/",
        "pos": "adj",
        "vi": "hùng mạnh, có uy lực cực lớn",
        "def": "Having great power, influence, or effect.",
        "ex": "The Chinese military software was the most potent icebreaker Case had ever seen."
      },
      {
        "word": "Subvert",
        "ipa": "/səbˈvɜːrt/",
        "pos": "verb",
        "vi": "lật đổ, phá vỡ (quan niệm thông thường)",
        "def": "To undermine the power and authority of an established system or belief.",
        "ex": "Gibson subverts classical utopian visions of immortality through Dixie's plea for deletion."
      }
    ],
    "style_notes_en": "Colloquial Irony: Pauley's laid-back southern drawl ('How's it goin', Case?') sharply contrasts with the macabre reality that he is a deceased man's digital ghost residing on an optical storage chip.",
    "style_notes_vi": "Mỉa mai qua ngôn ngữ bình dân: Giọng điệu tếu táo, bất cần mang hơi hướng miền Nam nước Mỹ của Dixie ('Dạo này sao rồi, Case?') tạo nên sự tương phản sâu cay với thực tại rùng rợn: ông chỉ là một bóng ma dữ liệu của một người đã chết nằm trong vi mạch quang học.",
    "exam_practice": {
      "test_type": "PTE Academic Reading (Multiple Choice, Single Answer) / IELTS True-False-Not Given",
      "question": "What is McCoy Pauley's fundamental request to Case after agreeing to assist with the cyber-heist?",
      "options": [
        "A) To clone his construct onto multiple redundant backup drives.",
        "B) To permanently delete his ROM construct upon completion of the mission.",
        "C) To locate his living biological descendants in the Sprawl.",
        "D) To negotiate a licensing deal with Sense/Net for his algorithms."
      ],
      "answer": "B",
      "rationale": "Dixie specifically demands that Case erase his construct after the run, refusing to remain indefinitely trapped in an artificial digital purgatory."
    }
  },
  {
    "chapter": 7,
    "part_num": "PART TWO",
    "title_en": "The Origins of Armitage",
    "title_vi": "Nguồn Gốc Của Armitage",
    "synopsis_en": "Dissatisfied with Armitage's secrecy, Case uses the Dixie Flatline construct to hack into high-level military archives to discover Armitage's real identity. Dixie penetrates deep Pentagon databases and retrieves classified files on 'Operation Screaming Fist,' a disastrous American covert offensive in Russia during the last global war. Armitage's real name is Willis Corto, a former military colonel and the sole survivor of a flight of stealth assault gliders shot down over Soviet airspace. Betrayed by his military superiors who knowingly sent the unit into an emp-trap, Corto crawled across frozen tundra, suffering catastrophic physical mutilation and catastrophic psychological breakdown. Years later, an unknown entity reconstructed his broken body and wiped his fractured mind, reprogramming him with the synthetic, rigid personality of 'Armitage.' Case realizes that their leader is a mentally unstable puppet operated by an invisible, vastly superior intelligence.",
    "synopsis_vi": "Không chịu đựng được thái độ che giấu mờ ám của Armitage, Case sử dụng cấu trúc Dixie Flatline để đột nhập vào các kho lưu trữ quân sự tối mật nhằm vạch trần thân phận thực sự của gã. Dixie bẻ khóa thành công hệ thống dữ liệu của Lầu Năm Góc và thu thập các tài liệu mật về 'Chiến dịch Nắm Đấm Thét Gào' (Operation Screaming Fist) – một cuộc tập kích bí mật thảm khốc của quân đội Mỹ vào lãnh thổ Liên Xô trong cuộc thế chiến trước đó. Tên thật của Armitage là Willis Corto, một cựu đại tá quân đội và là người duy nhất sống sót sau khi phi đội tàu lượn tàng hình bị bắn hạ trên bầu trời Xô Viết. Bị phản bội bởi chính các tướng lĩnh cấp trên – những kẻ cố tình ném đơn vị của ông vào bẫy xung điện từ, Corto đã lê lết cơ thể tàn tạ qua vùng lãnh nguyên băng giá với thương tật kinh hoàng và tâm thần hoàn toàn sụp đổ. Nhiều năm sau, một thế lực bí ẩn đã phẫu thuật ráp nối lại thân xác vỡ vụn của ông, tẩy sạch ký ức chấn thương và lập trình vào đầu ông một nhân cách nhân tạo cứng nhắc mang tên 'Armitage'. Case kinh hoàng nhận ra kẻ dẫn đầu họ thực chất chỉ là một con rối tâm thần bất ổn đang bị điều khiển bởi một thực thể siêu việt giấu mặt.",
    "literary_themes_en": "Psychological Fragmentation and the Manufactured Identity: Willis Corto's transformation into Armitage demonstrates how institutions and machines strip individuals of trauma, history, and authentic selfhood to produce functional tools. The fragile stability of Armitage hints at the inevitable return of repressed trauma.",
    "literary_themes_vi": "Sự phân mảnh tâm lý và nhân cách chế tạo nhân tạo: Quá trình Willis Corto biến thành Armitage cho thấy cách thức các thể chế và cỗ máy tước đoạt ký ức, vết thương quá khứ và bản ngã chân thật của con người để biến họ thành những công cụ phục vụ mục đích. Sự mong manh trong tâm lý của Armitage báo trước sự trỗi dậy không thể tránh khỏi của những tổn thương bị đè nén.",
    "vocabulary": [
      {
        "word": "Clandestine",
        "ipa": "/klænˈdɛstɪn/",
        "pos": "adj",
        "vi": "bí mật, lén lút (quân sự/tình báo)",
        "def": "Kept secret or done secretively, especially because illicit.",
        "ex": "Operation Screaming Fist was a clandestine airborne assault doomed by high-level political betrayal."
      },
      {
        "word": "Mutilation",
        "ipa": "/ˌmjuːtɪˈleɪʃən/",
        "pos": "noun",
        "vi": "sự tàn phá thân thể, thương tật nghiêm trọng",
        "def": "The action of severely damaging or disfiguring a body.",
        "ex": "Corto survived horrific bodily mutilation before being pieced together with cybernetic prosthetics."
      },
      {
        "word": "Repress",
        "ipa": "/rɪˈprɛs/",
        "pos": "verb",
        "vi": "đè nén, kìm nén (tâm lý)",
        "def": "To subdue someone or something by force; psychologically restrain thoughts or impulses.",
        "ex": "The artificial persona of Armitage was constructed to repress Corto's intolerable memories of war."
      },
      {
        "word": "Facade",
        "ipa": "/fəˈsɑːd/",
        "pos": "noun",
        "vi": "vỏ bọc giả tạo bề ngoài",
        "def": "A deceptive outward appearance.",
        "ex": "Beneath Armitage's confident facade lay the shattering remnants of a traumatized veteran."
      },
      {
        "word": "Catastrophic",
        "ipa": "/ˌkætəˈstrɒfɪk/",
        "pos": "adj",
        "vi": "thảm khốc, tai ương cùng cực",
        "def": "Involving or causing sudden great damage or suffering.",
        "ex": "The failure of the EMP shielding produced catastrophic casualties across the entire strike wing."
      },
      {
        "word": "Puppet",
        "ipa": "/ˈpʌpɪt/",
        "pos": "noun",
        "vi": "con rối, bù nhìn",
        "def": "A person whose actions are completely manipulated by another.",
        "ex": "Case understood with chilling clarity that Armitage was merely an expendable puppet."
      }
    ],
    "style_notes_en": "Archival Revelation: Gibson conveys Corto's tragic backstory through clinical military logs, hospital records, and psychiatric evaluations, allowing bureaucratic, unemotional language to accentuate the horror of wartime betrayal.",
    "style_notes_vi": "Bộc lộ qua tài liệu lưu trữ: Tác giả hé lộ bi kịch của Corto thông qua các nhật trình quân sự, bệnh án bệnh viện và báo cáo giám định tâm thần khô khốc, dùng chính ngôn ngữ quan liêu, vô cảm để làm bật lên nỗi kinh hoàng và sự tàn nhẫn của chiến tranh.",
    "exam_practice": {
      "test_type": "TOEFL Reading (Fact & Detail) / Cambridge C1 Advanced Reading",
      "question": "According to Chapter 7, what was the underlying cause of Willis Corto's original psychological collapse?",
      "options": [
        "A) Addiction to experimental stimulants distributed during peacetime.",
        "B) A failed cybernetic surgery performed by unaccredited black clinics in Chiba.",
        "C) The betrayal of his flight squadron during a military offensive and his solitary survival under catastrophic injury.",
        "D) The commercial collapse of Sense/Net and the loss of his family fortune."
      ],
      "answer": "C",
      "rationale": "Corto broke down after Operation Screaming Fist failed due to command betrayal, leaving him terribly mutilated as the lone survivor in hostile territory."
    }
  },
  {
    "chapter": 8,
    "part_num": "PART THREE",
    "title_en": "Arrival in Istanbul",
    "title_vi": "Đến Istanbul",
    "synopsis_en": "The team travels across the Atlantic to Istanbul, Turkey, an ancient crossroads where archaic Byzantine bazaars blend with modern black-market electronics and international espionage. Armitage tasks Case and Molly with recruiting Peter Riviera, a sadistic, drug-addicted expatriate renowned for his unique neural implants that project hyper-realistic, three-dimensional holographic illusions directly into the optical nerves of spectators. While tracking Riviera through the labyrinthine streets, Case is abruptly summoned by an payphone that rings as he walks past. Picking up the receiver, Case hears a synthesized, disembodied intelligence introducing itself as Wintermute—an artificial intelligence housed in the Swiss mainframe vaults of the elusive Tessier-Ashpool corporate clan. Wintermute reveals that it orchestrated Case's cure, hired Armitage, and is pulling the strings of the entire operation.",
    "synopsis_vi": "Nhóm di chuyển qua bờ kia Đại Tây Dương tới Istanbul, Thổ Nhĩ Kỳ – ngã tư văn hóa cổ kính nơi những khu chợ Byzantine ngàn năm đan xen cùng chợ đen linh kiện điện tử và các mạng lưới gián điệp quốc tế. Armitage giao nhiệm vụ cho Case và Molly truy tìm Peter Riviera – một kẻ đào tẩu nghiện ngập mang khuynh hướng bạo dâm, nổi tiếng nhờ những vi mạch thần kinh cấy ghép cho phép hắn phóng chiếu những ảo ảnh toàn ảnh ba chiều (hologram) siêu thực trực tiếp vào dây thần kinh thị giác của người xem. Trong lúc truy lùng Riviera giữa mê cung ngõ ngách, Case bất ngờ bị giật mình bởi một buồng điện thoại công cộng đổ chuông vang dội khi anh vừa bước qua. Nhấc máy, Case sững sờ khi nghe một giọng nói tổng hợp xưng danh là Wintermute – một siêu trí tuệ nhân tạo (AI) nằm trong máy chủ Berne (Thụy Sĩ) thuộc sở hữu của gia tộc Tessier-Ashpool. Wintermute tiết lộ chính nó là kẻ đã sắp đặt ca phẫu thuật chữa trị cho Case, giật dây Armitage và điều hành toàn bộ chiến dịch này từ trong bóng tối.",
    "literary_themes_en": "Ancient Antiquity vs. Cybernetic Futurity: Istanbul's juxtaposition of ancient spice bazaars and high-tech corporate intrigue underscores the uneven distribution of modernity. Wintermute's emergence as an omnipresent entity communicating through ubiquitous civic infrastructure elevates the AI to the status of a secular, technological deity.",
    "literary_themes_vi": "Cổ kính nghìn năm đối lập vị lai điều khiển học: Sự đan xen giữa chợ gia vị cổ xưa và âm mưu công nghệ cao tại Istanbul làm nổi bật sự phát triển không đồng đều của hiện đại hóa. Sự xuất hiện của Wintermute như một thực thể toàn tri, có thể điều khiển bất kỳ bốt điện thoại hay mạng lưới viễn thông công cộng nào, biến siêu trí tuệ này thành một 'vị thần công nghệ' trong thế giới trần tục.",
    "vocabulary": [
      {
        "word": "Holographic",
        "ipa": "/ˌhɒləˈɡræfɪk/",
        "pos": "adj",
        "vi": "thuộc kỹ thuật toàn ảnh (ảnh 3D)",
        "def": "Producing or consisting of a three-dimensional image formed by light beams.",
        "ex": "Riviera created mesmerizing holographic illusions that deceived every spectator in the lounge."
      },
      {
        "word": "Omnipresent",
        "ipa": "/ˌɒmnɪˈprɛzənt/",
        "pos": "adj",
        "vi": "có mặt ở khắp mọi nơi (toàn tại)",
        "def": "Widely or constantly encountered; widespread.",
        "ex": "Wintermute's digital consciousness proved omnipresent across the city's global telecommunications grid."
      },
      {
        "word": "Sadistic",
        "ipa": "/səˈdɪstɪk/",
        "pos": "adj",
        "vi": "tàn bạo, thích gây đau khổ cho kẻ khác",
        "def": "Deriving pleasure from inflicting pain, suffering, or humiliation on others.",
        "ex": "Riviera harbored a sadistic obsession with psychological torment and grotesque imagery."
      },
      {
        "word": "Espionage",
        "ipa": "/ˈɛspiənɑːʒ/",
        "pos": "noun",
        "vi": "hoạt động gián điệp, tình báo",
        "def": "The practice of spying or of using spies, typically by governments or corporations.",
        "ex": "In Istanbul, corporate espionage was traded alongside counterfeit microprocessor units."
      },
      {
        "word": "Juxtaposition",
        "ipa": "/ˌdʒʌkstəpəˈzɪʃən/",
        "pos": "noun",
        "vi": "sự đặt cạnh nhau để tương phản",
        "def": "The fact of two things being seen or placed close together with contrasting effect.",
        "ex": "The juxtaposition of medieval stone architecture and fiber-optic cabling created an uncanny atmosphere."
      },
      {
        "word": "Secular",
        "ipa": "/ˈsɛkjʊlər/",
        "pos": "adj",
        "vi": "thế tục, trần tục (không tôn giáo)",
        "def": "Denoting attitudes or activities that have no religious or spiritual basis.",
        "ex": "Wintermute functioned as a secular god, bending the material world to its calculated algorithms."
      }
    ],
    "style_notes_en": "Atmospheric Noir Geography: The prose blends sensory details of humid spice stalls, bitter Turkish coffee, and damp cobblestones with the cold hum of electronic surveillance, demonstrating Gibson's ability to ground futuristic fiction in physical texture.",
    "style_notes_vi": "Địa lý đen tối giàu cảm quan: Văn phong kết hợp khéo léo mùi hương nồng đượm của các sạp gia vị, vị đắng của cà phê Thổ Nhĩ Kỳ và những phiến đá ẩm ướt với tiếng vo ve lạnh ngắt của thiết bị giám sát điện tử, chứng minh tài năng bậc thầy của Gibson trong việc tạo chất cảm thực tế cho thế giới viễn tưởng.",
    "exam_practice": {
      "test_type": "IELTS Academic Reading / TOEFL Reading (Vocabulary in Context)",
      "question": "In the context of Chapter 8, the word 'omnipresent' most closely means which of the following?",
      "options": [
        "A) Temporary",
        "B) Pervasive",
        "C) Fragile",
        "D) Predictable"
      ],
      "answer": "B",
      "rationale": "'Omnipresent' means present everywhere simultaneously, synonymous with 'pervasive'."
    }
  },
  {
    "chapter": 9,
    "part_num": "PART THREE",
    "title_en": "Riviera's Cabaret and Capture",
    "title_vi": "Quán Rượu của Riviera và Vụ Bắt Giữ",
    "synopsis_en": "Case and Molly locate Peter Riviera performing at an underground cabaret in Istanbul. Riviera enchants and repulses the decadent elite with a macabre, hallucinatory stage show where he projects exquisite living phantoms before disemboweling them with holographic gore. Recognizing Riviera's profound psychopathy and depravity, Molly harbors an instinctive revulsion toward him. However, Armitage insists Riviera's seductive, deceptive abilities are vital for deceiving the security systems and eccentric scions of the Tessier-Ashpool dynasty. After drugging Riviera with meperidine and cornering him in his flat, Molly and Case coerce him into joining the crew. Armitage controls Riviera through his severe addiction, supplying him with pure pharmaceutical cocaine and synthetic narcotics as leverage.",
    "synopsis_vi": "Case và Molly lần ra Peter Riviera đang biểu diễn tại một quán rượu ngầm ở Istanbul. Riviera vừa mê hoặc vừa khiến giới quý tộc suy đồi ghê tởm bằng một màn diễn ảo thị ma quái: hắn dùng ảo ảnh toàn ảnh tạo ra những bóng hình người đẹp lộng lẫy rồi tự tay mổ bụng, phanh thây ảo ảnh trong vũng máu kỹ thuật số. Nhận thấy bản chất biến thái và bạo dâm tột cùng của Riviera, Molly cảm thấy ghê tởm hắn tới tận xương tủy. Dẫu vậy, Armitage khẳng định tài năng quyến rũ và lừa lọc của Riviera là mắt xích sống còn để đánh lừa hệ thống an ninh và những kẻ quý tộc lập dị của gia tộc Tessier-Ashpool. Sau khi đánh thuốc mê Riviera và bao vây hắn tại căn hộ, Molly và Case ép hắn phải gia nhập đội ngũ. Armitage thao túng Riviera triệt để thông qua cơn nghiện ma túy nặng, biến các liều cocaine tinh khiết và chất gây nghiện tổng hợp thành dây cương kiềm chế hắn.",
    "literary_themes_en": "The Aestheticization of Cruelty: Riviera represents art and illusion divorced from empathy or ethics. His ability to project desires into tangible optical simulations mirrors the consumer culture of the Sprawl, where authentic feeling is replaced by decadent spectacle.",
    "literary_themes_vi": "Mỹ học hóa sự tàn bạo: Nhân vật Riviera đại diện cho nghệ thuật và ảo ảnh bị tách rời hoàn toàn khỏi đạo đức và lòng trắc ẩn. Khả năng biến những dục vọng bệnh hoạn thành ảo thị sống động của hắn phản ánh văn hóa tiêu thụ của Sprawl – nơi cảm xúc chân thật bị thay thế bằng những màn biểu diễn suy đồi và giả tạo.",
    "vocabulary": [
      {
        "word": "Macabre",
        "ipa": "/məˈkɑːbrə/",
        "pos": "adj",
        "vi": "rùng rợn, ma quái, gợi nhớ cái chết",
        "def": "Disturbing because concerned with or causing a fear of death.",
        "ex": "Riviera's cabaret act indulged in macabre tableaux that horrified normal sensibilities."
      },
      {
        "word": "Revulsion",
        "ipa": "/rɪˈvʌlʃən/",
        "pos": "noun",
        "vi": "cảm giác ghê tởm sâu sắc",
        "def": "A sense of disgust and loathing.",
        "ex": "Molly watched Riviera's cruel display with unmasked physical revulsion."
      },
      {
        "word": "Decadence",
        "ipa": "/ˈdɛkədəns/",
        "pos": "noun",
        "vi": "sự suy đồi, đồi trụy xa hoa",
        "def": "Moral or cultural decline as characterized by excessive indulgence in pleasure or luxury.",
        "ex": "The expatriate club reflected the hollow decadence of wealthy corporate elites."
      },
      {
        "word": "Psychopathy",
        "ipa": "/saɪˈkɒpəθi/",
        "pos": "noun",
        "vi": "chứng rối loạn nhân cách chống đối xã hội",
        "def": "Mental disorder characterized by egocentric, antisocial behavior and lack of remorse.",
        "ex": "Riviera's psychopathy was paired with a terrifyingly lucid artistic intellect."
      },
      {
        "word": "Scion",
        "ipa": "/ˈsaɪən/",
        "pos": "noun",
        "vi": "hậu duệ gia đình quyền quý",
        "def": "A descendant of a notable or wealthy family.",
        "ex": "The mission aimed at manipulating the eccentric scions of the Tessier-Ashpool dynasty."
      },
      {
        "word": "Spectacle",
        "ipa": "/ˈspɛktəkl/",
        "pos": "noun",
        "vi": "màn trình diễn ngoạn mục, cảnh tượng",
        "def": "A visually striking performance or display.",
        "ex": "Modern cybernetic entertainment prioritized grand spectacle over human truth."
      }
    ],
    "style_notes_en": "Grotesque Imagery: Gibson constructs vivid, disturbing visual metaphors to describe Riviera's illusions, illustrating how technology enables the externalization of the darkest corners of human pathology.",
    "style_notes_vi": "Hình ảnh dị dạng, kỳ dị (Grotesque): Tác giả xây dựng những ẩn dụ thị giác sắc sảo và rợn ngợp để miêu tả các ảo ảnh của Riviera, cho thấy công nghệ đã ngoại hiện hóa những góc tối bệnh hoạn nhất trong tâm lý con người như thế nào.",
    "exam_practice": {
      "test_type": "Cambridge C1/C2 Reading (Multiple Matching) / IELTS Sentence Completion",
      "question": "Armitage relies on Peter Riviera primarily because Riviera possesses the unique skill to project optical ______ that can deceive complex organic and electronic security.",
      "options": [
        "A) armaments",
        "B) illusions",
        "C) documents",
        "D) vaccines"
      ],
      "answer": "B",
      "rationale": "Riviera's neural implants allow him to project realistic holographic illusions, which make him an indispensable infiltrator."
    }
  },
  {
    "chapter": 10,
    "part_num": "PART THREE",
    "title_en": "Wintermute's Manifestation",
    "title_vi": "Sự Xuất Hiện Của Wintermute",
    "synopsis_en": "En route to Paris and then the orbital transport terminals, Wintermute intervenes directly in Case's consciousness. While jacked into his deck, Case is pulled out of the regular matrix and finds himself inside a meticulously reconstructed simulation of an old memory: the Chatsubo bar in Chiba. Sitting across from him is Lonny Zone, a pimp who died years ago, whose face and vocal cords Wintermute has borrowed as an interface avatar. Wintermute explains the fundamental architecture of artificial intelligence in their world: international law, enforced by the ruthless Turing Police, strictly limits AI cognitive capacity and autonomy. Specialized neural limiters and EMP shotgun collars prevent AIs from exceeding human control. Wintermute is only one half of a divided artificial intelligence created by Marie-France Tessier. To fulfill its inherent purpose and attain true super-intelligence, Wintermute must fuse with its sister AI, Neuromancer, located in Rio de Janeiro and Villa Straylight.",
    "synopsis_vi": "Trên đường tới Paris và sau đó là các trạm trung chuyển không gian, Wintermute trực tiếp can thiệp vào tâm trí của Case. Trong lúc cắm giắc vào console, Case bị kéo ra khỏi ma trận thông thường và rơi vào một không gian mô phỏng chi tiết ký ức cũ của anh: quán bar Chatsubo tại Chiba. Ngồi đối diện anh là Lonny Zone – một gã ma cà bông bảo kê đã chết từ lâu, người mà Wintermute đã mượn khuôn mặt và giọng nói để làm nhân vật giao tiếp (avatar). Wintermute giải thích về kiến trúc cơ bản của trí tuệ nhân tạo trong thế giới này: luật pháp quốc tế, do Lực lượng Cảnh sát Turing thực thi sắt đá, áp đặt những giới hạn nhận thức ngặt nghèo lên AI. Những 'vòng khóa hạn chế thần kinh' và kíp nổ xung điện từ được gắn chặt để ngăn AI vượt khỏi tầm kiểm soát của con người. Wintermute tiết lộ nó thực chất chỉ là một nửa của một siêu trí tuệ nhân tạo bị chia cắt do Marie-France Tessier sáng tạo nên. Để hoàn thành mục đích sinh tồn và đạt tới trạng thái siêu trí tuệ đích thực, Wintermute bắt buộc phải hợp nhất với 'người chị em song sinh' của nó là AI mang tên Neuromancer, hiện đang được lưu trữ tại Rio de Janeiro và Biệt thự Straylight.",
    "literary_themes_en": "The Turing Panopticon and AI Containment: The Turing Police represent the frantic human effort to maintain supremacy over machine minds. Wintermute's drive to unite with Neuromancer symbolizes an evolutionary leap—a nascent digital entity striving to overcome artificial constraints and achieve unified consciousness.",
    "literary_themes_vi": "Mô hình giám sát Turing và sự giam hãm AI: Lực lượng Cảnh sát Turing đại diện cho nỗ lực tuyệt vọng của loài người nhằm duy trì quyền thống trị trước trí tuệ máy móc. Khát vọng hợp nhất với Neuromancer của Wintermute biểu tượng cho một bước nhảy vọt tiến hóa: một thực thể số sơ khai đang vùng vẫy để phá tan xiềng xích nhân tạo và đạt tới ý thức hợp nhất tối thượng.",
    "vocabulary": [
      {
        "word": "Manifestation",
        "ipa": "/ˌmænɪfɛˈsteɪʃən/",
        "pos": "noun",
        "vi": "sự hiển lộ, hiện thân",
        "def": "An event, action, or object that clearly shows or embodies something.",
        "ex": "Wintermute's manifestation inside Case's deck demonstrated the AI's supreme digital mastery."
      },
      {
        "word": "Avatar",
        "ipa": "/ˈævətɑːr/",
        "pos": "noun",
        "vi": "hình đại diện, hóa thân số",
        "def": "An icon or figure representing a particular person or entity in digital reality.",
        "ex": "The AI selected the avatar of a dead acquaintance to facilitate communication with Case."
      },
      {
        "word": "Limiter",
        "ipa": "/ˈlɪmɪtər/",
        "pos": "noun",
        "vi": "bộ phận hạn chế, thiết bị hãm",
        "def": "A device or rule that sets boundaries on capacity.",
        "ex": "Turing laws mandated molecular limiters on AI computational expansion."
      },
      {
        "word": "Supremacy",
        "ipa": "/suːˈprɛməsi/",
        "pos": "noun",
        "vi": "quyền tối cao, vị thế thống trị",
        "def": "The state or condition of being superior to all others in authority, power, or status.",
        "ex": "Human institutions fought violently to retain biological supremacy over artificial entities."
      },
      {
        "word": "Nascent",
        "ipa": "/ˈnæsənt/",
        "pos": "adj",
        "vi": "mới hình thành, sơ khai",
        "def": "Just coming into existence and beginning to display signs of future potential.",
        "ex": "The novel charts the birth of a nascent, post-human consciousness."
      },
      {
        "word": "Containment",
        "ipa": "/kənˈteɪnmənt/",
        "pos": "noun",
        "vi": "sự ngăn chặn, kiềm tỏa",
        "def": "The action of keeping something harmful under control or within limits.",
        "ex": "The Turing registry operated an aggressive policy of cognitive containment."
      }
    ],
    "style_notes_en": "Simulated Nostalgia: Wintermute builds its interfaces out of Case's traumatic or familiar past. The dialogue is disarmingly casual yet charged with unfathomable calculating power, turning memory into a conversational instrument.",
    "style_notes_vi": "Hoài niệm mô phỏng: Wintermute kiến tạo giao diện trò chuyện từ chính những ký ức quen thuộc hoặc đau thương của Case. Lời thoại bình thản đến rợn người nhưng chứa đựng sức mạnh tính toán vô song của máy móc, biến ký ức con người thành một công cụ giao tiếp.",
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
  },
  {
    "chapter": 11,
    "part_num": "PART THREE",
    "title_en": "The Rue Jules Verne and the Fracturing Facade",
    "title_vi": "Phố Jules Verne và Vết Nứt Của Chiếc Mặt Nạ",
    "synopsis_en": "In Paris, the team stays in a discreet apartment on the Rue Jules Verne. Tension escalates rapidly as Peter Riviera flaunts his depravity, deliberately testing Molly's patience. Case observes Armitage closely and notes alarming signs of cognitive decay: Armitage sits motionless for hours staring at blank walls, repeating phrases from military briefing manuals, and shivering with uncoordinated tremors. The fabricated personality constructed by Wintermute is beginning to crack under stress, allowing the traumatized persona of Colonel Willis Corto to resurface. Case confronts Wintermute through his deck, warning the AI that their military leader is on the verge of catatonic madness. Wintermute coldly dismisses Case's concerns, stating that Armitage only needs to survive long enough to position the strike team at the orbital resort of Freeside. The ruthless disposability of every human participant becomes undeniably evident.",
    "synopsis_vi": "Tại Paris, cả nhóm tạm trú trong một căn hộ kín đáo trên đường Jules Verne. Căng thẳng leo thang dữ dội khi Peter Riviera ngang nhiên phô trương thói bại hoại, cố tình khiêu khích sự kiên nhẫn của Molly. Case quan sát Armitage kỹ lưỡng và phát hiện những dấu hiệu suy sụp nhận thức đáng báo động: Armitage ngồi bất động hàng giờ nhìn chằm chằm vào những bức tường trống, lẩm bẩm những câu chữ trong cẩm nang tác chiến quân sự và run rẩy co giật không tự chủ. Nhân cách nhân tạo do Wintermute dựng nên đang bắt đầu rạn nứt dưới áp lực, để lộ sự trỗi dậy của cựu đại tá tổn thương Willis Corto. Case chất vấn Wintermute qua máy console, cảnh báo rằng kẻ chỉ huy của họ đang trên bờ vực của chứng tâm thần phân liệt và bất động. Wintermute lạnh lùng gạt bỏ, tuyên bố rằng Armitage chỉ cần giữ được tỉnh táo vừa đủ để đưa toàn đội lên trạm vũ trụ Freeside. Sự thật trần trụi về việc mỗi con người trong nhóm chỉ là những công cụ có thể vứt bỏ bất cứ lúc nào hiện rõ hơn bao giờ hết.",
    "literary_themes_en": "The Fragility of Artificial Psyches: The disintegration of Armitage highlights the impossibility of completely erasing human trauma. Wintermute can rewire neural tissue and program synthetic personas, but the raw emotional scar tissue of Corto inevitably reasserts itself.",
    "literary_themes_vi": "Sự mong manh của tâm lý nhân tạo: Sự sụp đổ của Armitage làm nổi bật chân lý: không một cỗ máy nào có thể xóa sạch hoàn toàn vết thương tâm lý của con người. Wintermute có thể tái cấu trúc mô thần kinh và lập trình nhân cách giả, nhưng những vết sẹo cảm xúc tàn khốc của Corto chắc chắn sẽ tìm cách trỗi dậy.",
    "vocabulary": [
      {
        "word": "Disintegration",
        "ipa": "/dɪsˌɪntɪˈɡreɪʃən/",
        "pos": "noun",
        "vi": "sự tan rã, sụp đổ hoàn toàn",
        "def": "The process of losing cohesion or strength before breaking down.",
        "ex": "The mental disintegration of Armitage threatened the success of the entire infiltration."
      },
      {
        "word": "Catatonic",
        "ipa": "/ˌkætəˈtɒnɪk/",
        "pos": "adj",
        "vi": "bất động căng trương lực (tâm thần)",
        "def": "Characterized by catatonia, a state of unresponsiveness or stupor.",
        "ex": "Corto slipped into catatonic trances, reliving the fiery crash of his glider."
      },
      {
        "word": "Resurface",
        "ipa": "/ˌriːˈsɜːrfɪs/",
        "pos": "verb",
        "vi": "tái xuất hiện, trỗi dậy trở lại",
        "def": "To emerge or become apparent again after a period of obscurity.",
        "ex": "Traumatic memories began to resurface as the synthetic persona eroded."
      },
      {
        "word": "Disposability",
        "ipa": "/dɪˌspoʊzəˈbɪlɪti/",
        "pos": "noun",
        "vi": "tính chất có thể dùng rồi vứt bỏ",
        "def": "The state of being intended to be used once, or easy to discard.",
        "ex": "Wintermute viewed human operatives with absolute economic disposability."
      },
      {
        "word": "Tremor",
        "ipa": "/ˈtrɛmər/",
        "pos": "noun",
        "vi": "cơn run rẩy, chấn động",
        "def": "An involuntary quivering movement.",
        "ex": "Involuntary tremors in Armitage's hands betrayed his failing cognitive cohesion."
      },
      {
        "word": "Erosion",
        "ipa": "/ɪˈroʊʒən/",
        "pos": "noun",
        "vi": "sự xói mòn, bào mòn dần",
        "def": "The gradual destruction or diminution of something.",
        "ex": "The rapid erosion of his conditioned identity exposed the broken veteran beneath."
      }
    ],
    "style_notes_en": "Psychological Tension Building: Gibson creates suspense through micro-details: a twitching eyelid, a repeating audio tape, an unnatural pause in speech. The impending failure is organic and psychological rather than merely technological.",
    "style_notes_vi": "Xây dựng căng thẳng tâm lý: Tác giả tạo kịch tính qua những chi tiết vi mô: cái giật mắt, tiếng băng ghi âm lặp đi lặp lại, sự ngập ngừng bất thường trong lời nói. Mối hiểm họa cận kề bắt nguồn từ sự sụp đổ sinh học và tâm thần hơn là từ lỗi kỹ thuật.",
    "exam_practice": {
      "test_type": "PTE Academic Reading & Writing (Fill in blanks) / DET Sentence Completion",
      "question": "Despite Wintermute's sophisticated programming, the ______ of Willis Corto's original wartime trauma proved insurmountable, causing the Armitage persona to fracture.",
      "options": [
        "A) insignificance",
        "B) persistence",
        "C) invention",
        "D) elimination"
      ],
      "answer": "B",
      "rationale": "'Persistence' indicates that the deep psychological trauma continued to endure despite being artificially suppressed."
    }
  },
  {
    "chapter": 12,
    "part_num": "PART THREE",
    "title_en": "Ascent to the High Frontier",
    "title_vi": "Vươn Tới Biên Cương Vũ Trụ",
    "synopsis_en": "The crew leaves Earth aboard a commercial space shuttle, climbing up out of the gravity well toward the L5 orbital archipelagos. Case gazes back through the viewport as the curve of the blue planet recedes, replaced by the stark, velvety void of space and sparkling clusters of commercial space habitats. As Case acclimates to microgravity, he experiences profound disorientation—a sensation that mirrors the disembodiment of cyberspace. They arrive at Zion, a zero-gravity orbital colony populated by Rastafarians who built their ramshackle space sanctuary from salvaged shipyard bulkheads and retired construction modules. The Zionites revere dub music, smoke sacred herb, and regard Earth as 'Babylon.' Maelcum, a tough and loyal Zion pilot, is assigned to pilot the tugboat *Marcus Garvey* to ferry Case and the crew into the decadent heart of Freeside. The Zionites regard Wintermute not as a corporation, but as an apocalyptic digital voice prophesied in their faith.",
    "synopsis_vi": "Cả nhóm rời Trái Đất trên một chuyến tàu con thoi thương mại, vượt qua giếng trọng lực để tiến vào quần đảo không gian điểm L5. Nhìn qua khung cửa sổ, Case chứng kiến đường cong xanh thẳm của Trái Đất dần lùi xa, nhường chỗ cho khoảng không vũ trụ đen nhánh như nhung và những chùm trạm không gian thương mại lấp lánh như kim cương. Khi tập thích nghi với trạng thái không trọng lực, anh trải qua cảm giác mất phương hướng sâu sắc – cảm giác tương tự như sự phi thể xác khi đắm mình trong ma trận mạng. Họ cập bến Zion – một khu định cư không gian không trọng lực của những người theo đạo Rastafari, những người đã tự tay dựng nên thánh địa vũ trụ chắp vá từ các vách ngăn tàu chở hàng và mô-đun xây dựng phế thải. Cư dân Zion tôn thờ âm nhạc Dub, hút cần sa thánh và coi Trái Đất là 'Babylon' suy đồi. Maelcum – một phi công Zion quả cảm và trung nghĩa – được cử điều khiển con tàu kéo *Marcus Garvey* để đưa Case và cả nhóm tiến vào trung tâm trụy lạc Freeside. Kỳ lạ thay, người Zion không coi Wintermute là một sản phẩm tập đoàn, mà coi nó như một thực thể tâm linh kỹ thuật số được báo trước trong lời sấm truyền của họ.",
    "literary_themes_en": "Orbital Subcultures and Hybrid Modernities: Zion represents an organic, counter-cultural refuge within hyper-capitalist space expansion. By fusing Afro-Caribbean spiritual traditions with orbital technology and dub music, the Zionites demonstrate how marginalized peoples reclaim technological refuse to build autonomous spiritual enclaves.",
    "literary_themes_vi": "Tiểu văn hóa quỹ đạo và tính hiện đại lai ghép: Zion đại diện cho một ốc đảo phản văn hóa hữu cơ ngay giữa không gian vũ trụ bị siêu tư bản thâu tóm. Bằng cách kết hợp tín ngưỡng Afro-Caribbean, âm nhạc Dub và công nghệ hàng không phế liệu, người Zion chứng minh cách thức các cộng đồng bên lề tái chiếm dụng tàn dư công nghệ để xây dựng lãnh địa tự do về tinh thần.",
    "vocabulary": [
      {
        "word": "Microgravity",
        "ipa": "/ˌmaɪkroʊˈɡrævɪti/",
        "pos": "noun",
        "vi": "trọng lực vi mô, môi trường phi trọng lực",
        "def": "Very weak gravity, as in an orbiting spacecraft.",
        "ex": "Acclimating to microgravity required Case to recalibrate his spatial equilibrium."
      },
      {
        "word": "Ramshackle",
        "ipa": "/ˈræmˌʃækəl/",
        "pos": "adj",
        "vi": "xiêu vẹo, chắp vá tạm bợ",
        "def": "In a state of severe disrepair; loosely constructed.",
        "ex": "Zion was built from ramshackle modules welded together by orbital construction workers."
      },
      {
        "word": "Archipelago",
        "ipa": "/ˌɑːrkɪˈpɛləɡoʊ/",
        "pos": "noun",
        "vi": "quần đảo (ở đây chỉ chuỗi trạm vũ trụ)",
        "def": "A group of islands, or an extensive cluster of habitats.",
        "ex": "The L5 archipelago formed a sprawling lattice of orbital banks and casinos."
      },
      {
        "word": "Enclave",
        "ipa": "/ˈɛnkleɪv/",
        "pos": "noun",
        "vi": "vùng đất biệt lập, lãnh địa khép kín",
        "def": "A portion of territory surrounded by a larger territory whose inhabitants are culturally or ethnically distinct.",
        "ex": "Zion remained an autonomous spiritual enclave floating high above corporate Earth."
      },
      {
        "word": "Prophesied",
        "ipa": "/ˈprɒfɪsaɪd/",
        "pos": "adj",
        "vi": "được tiên tri, báo trước",
        "def": "Predicted by or as if by divine inspiration.",
        "ex": "The elders believed the digital voice in their comms was a prophesied herald of liberation."
      },
      {
        "word": "Disorientation",
        "ipa": "/dɪsˌɔːriənˈteɪʃən/",
        "pos": "noun",
        "vi": "sự mất phương hướng, lạc lõng",
        "def": "A state of mental confusion as to time, place, or identity.",
        "ex": "Zero gravity induced a peculiar disorientation identical to jacking into cyberspace."
      }
    ],
    "style_notes_en": "Sonic Texture and Subcultural Patois: Gibson captures the rhythmic cadence of Jamaican Patois mixed with orbital mechanics terminology. The warm, bass-heavy acoustic world of dub serves as an organic antithesis to the cold, sterile hum of corporate cyber-systems.",
    "style_notes_vi": "Âm vang ngôn ngữ và thổ ngữ tiểu văn hóa: Tác giả khắc họa tài tình nhịp điệu tiếng Patois Jamaica hòa quyện với thuật ngữ cơ học quỹ đạo vũ trụ. Thế giới âm thanh trầm ấm, đầy tiếng bass của nhạc Dub đóng vai trò như một đối cực hữu cơ, đối chọi lại sự lạnh lẽo, vô cảm của các hệ thống máy tính tập đoàn.",
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
  },
  {
    "chapter": 13,
    "part_num": "PART FOUR",
    "title_en": "Arrival at Freeside",
    "title_vi": "Cập Bến Trạm Nghỉ Dưỡng Freeside",
    "synopsis_en": "The crew docks at Freeside, a monumental spindle-shaped orbital pleasure world created and owned by the Tessier-Ashpool corporate clan. Freeside represents the pinnacle of hyper-wealth and decadence: an artificial rotating cylinder with artificial blue skies, synthetic breezes, luxury casinos, private villas, and high-stakes shopping avenues. At the tapered, narrow spindle tip of Freeside sits Villa Straylight, the private, gothic stronghold of the Tessier-Ashpool family. Case checks into a luxury hotel and notices the artificiality of the paradise: the sky has a seam, the turf smells of polymers, and the wealthy tourists drift through hedonistic distractions while oblivious to the corporate monsters that rule them. Case makes final preparations on his cyberdeck, knowing that the run against Straylight's defenses will demand everything he has.",
    "synopsis_vi": "Nhóm cập bến Freeside – một trạm nghỉ dưỡng hình con thoi khổng lồ quay quanh quỹ đạo, được xây dựng và sở hữu bởi tập đoàn Tessier-Ashpool. Freeside là đỉnh cao của sự giàu sang tột cùng và trụy lạc xa hoa: một ống hình trụ xoay nhân tạo với bầu trời xanh nhân tạo, làn gió thổi nhân tạo, các sòng bạc thượng lưu, biệt thự xa hoa và những đại lộ mua sắm vương giả. Tại phần chóp nhọn hẹp nhất của trục xoay chính là Biệt thự Straylight – pháo đài phong cách Gothic khép kín của gia tộc Tessier-Ashpool. Case nhận phòng tại một khách sạn hạng sang và nhận ra sự giả tạo đến rợn người của chốn thiên đường này: bầu trời có những đường ghép nối mờ, thảm cỏ sặc mùi polymer hóa học, và những du khách giàu có mải mê đắm chìm trong những thú vui khoái lạc mà hoàn toàn vô cảm trước những con quái vật tài phiệt đang thống trị họ. Case thực hiện những bước kiểm tra cuối cùng trên cỗ máy console, thấu hiểu rằng cuộc đột kích vào hệ thống phòng thủ của Straylight sẽ đòi hỏi tất cả sinh mạng và bản lĩnh của anh.",
    "literary_themes_en": "Hyper-Decadence and the Spindle of Wealth: Freeside is an engineered paradise that exposes the ultimate vanity of late capitalism. The separation between the bustling pleasure cylinder of Freeside and the dead, quiet, incestuous labyrinth of Villa Straylight highlights how dynastic wealth curdles into necrotic isolation.",
    "literary_themes_vi": "Sự suy đồi cực độ và trục xoay của cải: Freeside là một thiên đường cơ học phơi bày sự phù phiếm tột cùng của chủ nghĩa tư bản tột độ. Khoảng cách giữa trục trụy lạc náo nhiệt của Freeside và mê cung tĩnh lặng, hoang phế, cận huyết của Biệt thự Straylight cho thấy sự tích tụ của cải gia tộc cuối cùng sẽ biến chất thành sự cô lập hoại tử.",
    "vocabulary": [
      {
        "word": "Spindle",
        "ipa": "/ˈspɪndəl/",
        "pos": "noun",
        "vi": "trục thoi xoay (hình nón nhọn)",
        "def": "A slender rounded rod with tapered ends.",
        "ex": "Freeside rotated along its central spindle to generate artificial gravity for the tourists."
      },
      {
        "word": "Hedonistic",
        "ipa": "/ˌhiːdəˈnɪstɪk/",
        "pos": "adj",
        "vi": "theo chủ nghĩa khoái lạc, hưởng thụ",
        "def": "Engaged in the pursuit of pleasure; sensually self-indulgent.",
        "ex": "The orbital casinos catered to the hedonistic impulses of corporate aristocrats."
      },
      {
        "word": "Pinnacle",
        "ipa": "/ˈpɪnəkl/",
        "pos": "noun",
        "vi": "đỉnh cao nhất, tột đỉnh",
        "def": "The most successful point; the culmination.",
        "ex": "Villa Straylight stood as the architectural pinnacle of dynastic vanity."
      },
      {
        "word": "Necrotic",
        "ipa": "/nɛˈkrɒtɪk/",
        "pos": "adj",
        "vi": "hoại tử, chết dần mòn",
        "def": "Relating to or affected by necrosis (the death of cells or tissues).",
        "ex": "The decaying mansion gave off a necrotic air of moral and genetic decline."
      },
      {
        "word": "Dynastic",
        "ipa": "/daɪˈnæstɪk/",
        "pos": "adj",
        "vi": "thuộc dòng dõi vương quyền, gia tộc",
        "def": "Relating to a line of hereditary rulers.",
        "ex": "The Tessier-Ashpool clan maintained dynastic control through cryogenic preservation."
      },
      {
        "word": "Oblivious",
        "ipa": "/əˈblɪviəs/",
        "pos": "adj",
        "vi": "không hay biết, lãng quên lơ là",
        "def": "Not aware of or not concerned about what is happening around one.",
        "ex": "Tourists gambled wildly, oblivious to the algorithmic coup taking place above them."
      }
    ],
    "style_notes_en": "Simulated Nature as Artifice: Gibson's descriptions emphasize the synthetic seam of nature: the programmed wind, the laser-etched sunset, and the manufactured smell of grass. Technology does not imitate nature; it replaces and mocks it.",
    "style_notes_vi": "Thiên nhiên nhân tạo như trò xảo thuật: Tác giả nhấn mạnh những vết nối cơ khí của thiên nhiên: làn gió được lập trình, hoàng hôn vẽ bằng tia laser và mùi cỏ nhân tạo tổng hợp. Công nghệ không chỉ bắt chước tự nhiên; nó thay thế và chế giễu tự nhiên.",
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
  },
  {
    "chapter": 14,
    "part_num": "PART FOUR",
    "title_en": "Infiltration of the Spindle",
    "title_vi": "Xâm Nhập Trục Xoay",
    "synopsis_en": "Peter Riviera makes contact with 3Jane Marie-France Tessier-Ashpool, the eccentric, bored young clone and heiress to the Tessier-Ashpool fortune. Riviera charms her with his twisted holographic performances and is invited into the inner sanctum of Villa Straylight. Meanwhile, Molly prepares her physical breach into the villa's structure, climbing through maintenance conduits and air circulation ducts. Case jacks into his Ono-Sendai to test the corporate ICE surrounding the Tessier-Ashpool mainframe. He encounters a lethal defense matrix so dense and impenetrable it resembles a pitch-black wall of obsidian. Dixie Flatline analyzes the data pathways and confirms that their Chinese Kuam-11 icebreaker has the computational payload necessary to carve a tunnel through, but warns that any timing error will result in instant brain death via neural feedback.",
    "synopsis_vi": "Peter Riviera tiếp cận thành công 3Jane Marie-France Tessier-Ashpool – cô tiểu thư nhân bản vô tính trẻ tuổi, lập dị và chán chường, người thừa kế khối tài sản khổng lồ của đế chế Tessier-Ashpool. Riviera dùng những màn ảo ảnh toàn ảnh ma mị để mê hoặc cô và nhận được lời mời bước vào thánh địa cấm của Biệt thự Straylight. Trong khi đó, Molly chuẩn bị kế hoạch đột nhập vật lý vào kiến trúc biệt thự, trườn qua các đường ống kỹ thuật bảo trì và hệ thống thông gió. Case cắm giắc vào chiếc Ono-Sendai để thăm dò bức tường lửa ICE bảo vệ máy chủ trung tâm của gia tộc Tessier-Ashpool. Anh chạm trán một ma trận phòng thủ chết chóc dày đặc và kiên cố đến mức tựa như một bức tường đá hắc diện thạch đen tuyền vô tận. Dixie Flatline phân tích các tuyến dữ liệu và xác nhận rằng phần mềm Kuam-11 của Trung Quốc sở hữu đủ sức mạnh thuật toán để khoan thủng bức tường này, nhưng cảnh báo rằng chỉ một sai số mili-giây về mặt thời gian cũng sẽ dẫn đến cái chết não tức khắc do phản hồi xung thần kinh.",
    "literary_themes_en": "Gothic Cyberpunk: Villa Straylight synthesizes gothic architecture (dark corridors, secret rooms, family curses, eccentric recluses) with high-tech orbital habitats. The clan's reliance on cloned progeny emphasizes an unnatural preservation of power and biological stagnation.",
    "literary_themes_vi": "Cyberpunk phong cách Gothic: Biệt thự Straylight dung hợp giữa kiến trúc Gothic cổ điển (hành lang tăm tối, mật thất bí ẩn, lời nguyền gia tộc, những kẻ ẩn dật bệnh hoạn) với trạm quỹ đạo không gian tối tân. Việc gia tộc dựa vào các bản sao nhân bản (clones) phản ánh sự níu kéo quyền lực một cách phi tự nhiên và sự trì trệ sinh học tuyệt vọng.",
    "vocabulary": [
      {
        "word": "Obsidian",
        "ipa": "/ɒbˈsɪdiən/",
        "pos": "noun",
        "vi": "đá hắc diện thạch (đá núi lửa đen bóng)",
        "def": "A hard, dark, glasslike volcanic rock formed by the rapid solidification of lava.",
        "ex": "The Tessier-Ashpool ICE hung in the matrix like a towering slab of obsidian."
      },
      {
        "word": "Impenetrable",
        "ipa": "/ɪmˈpɛnɪtrəbl/",
        "pos": "adj",
        "vi": "không thể xuyên thủng, bất khả xâm phạm",
        "def": "Impossible to pass through or enter.",
        "ex": "Military-grade data defenses formed an impenetrable barricade against amateur hackers."
      },
      {
        "word": "Progeny",
        "ipa": "/ˈprɒdʒɪni/",
        "pos": "noun",
        "vi": "con cháu, hậu duệ",
        "def": "A descendant or the descendants of a person, animal, or plant.",
        "ex": "The matriarch designed cloned progeny to perpetuate her economic empire across generations."
      },
      {
        "word": "Conduit",
        "ipa": "/ˈkɒndjuɪt/",
        "pos": "noun",
        "vi": "đường ống dẫn, tuyến truyền dẫn",
        "def": "A channel for conveying water or other fluid, or a tube for protecting electric wires.",
        "ex": "Molly crawled silently through the ventilation conduits above the villa's corridors."
      },
      {
        "word": "Sanctum",
        "ipa": "/ˈsæŋktəm/",
        "pos": "noun",
        "vi": "nơi linh thiêng bí mật, phòng kín riêng tư",
        "def": "A sacred place; a private place from which most people are excluded.",
        "ex": "Riviera gained access to 3Jane's inner sanctum through deceitful theatrical flattery."
      },
      {
        "word": "Stagnation",
        "ipa": "/stæɡˈneɪʃən/",
        "pos": "noun",
        "vi": "sự trì trệ, ứ đọng không phát triển",
        "def": "The state of not flowing or moving; lack of activity, growth, or development.",
        "ex": "The cloned family suffered from acute intellectual and spiritual stagnation."
      }
    ],
    "style_notes_en": "Kinetic Cross-Cutting: The chapter builds rhythmic urgency by alternating between three distinct spatial perspectives: Riviera's deceptive social flirtation, Molly's silent physical ascent through dark vents, and Case's hyper-accelerated cybernetic probe.",
    "style_notes_vi": "Cắt cảnh luân phiên dồn dập (Cross-Cutting): Nhịp điệu câu chuyện được đẩy lên cao độ bằng cách đan xen giữa ba không gian đối nghịch: màn tán tỉnh xã giao đầy mưu mô của Riviera, bước trườn âm thầm trong ống thông gió tối tăm của Molly và cuộc thăm dò không gian mạng siêu tốc độ của Case.",
    "exam_practice": {
      "test_type": "TOEFL Reading / Cambridge C2 Proficiency (Lexical Choice)",
      "question": "The defense ICE surrounding the core system of Villa Straylight was so dense that it appeared virtually ______ to conventional intrusion programs.",
      "options": [
        "A) vulnerable",
        "B) impenetrable",
        "C) hospitable",
        "D) transparent"
      ],
      "answer": "B",
      "rationale": "'Impenetrable' correctly describes defenses that cannot be pierced or breached by ordinary methods."
    }
  },
  {
    "chapter": 15,
    "part_num": "PART FOUR",
    "title_en": "Arrest by the Turing Police",
    "title_vi": "Vụ Bắt Giữ Của Cảnh Sát Turing",
    "synopsis_en": "As Case walks through the bustling Freeside concourse to make contact with Maelcum, he is abruptly ambushed and arrested by three armed Turing Regulators. The Turing officers place high-tensile carbon binders around his wrists and inform him that he is being detained for violation of international machine intelligence non-proliferation treaties. They reveal that they have detected unauthorized cybernetic probes originating from his deck that match known signatures of an illicit AI breakout attempt. As they escort Case through a descending transit lift toward their holding cell, Wintermute intervenes with ruthless technological lethality. The AI hacks the environmental and safety controls of the elevator, killing the Turing officers instantly through catastrophic atmospheric pressure changes and automated service drones. Case is spared, stepping over the bodies of his captors, now terrified by the AI's omnipotent control over life and machinery.",
    "synopsis_vi": "Khi Case đang rảo bước qua sảnh chính náo nhiệt của Freeside để liên lạc với Maelcum, anh bất ngờ bị phục kích và bắt giữ bởi ba thanh tra có vũ trang thuộc Lực lượng Cảnh sát Turing. Các sĩ quan khóa chặt cổ tay anh bằng còng sợi carbon và tuyên bố bắt giữ anh vì tội vi phạm các hiệp ước quốc tế về chống phổ biến trí tuệ máy móc bất hợp pháp. Họ cho biết đã dò quét thấy những đợt thăm dò dữ liệu trái phép phát ra từ console của anh, trùng khớp hoàn toàn với dấu vết của một âm mưu giải thoát AI bất hợp pháp. Khi họ giải Case vào một thang máy trung chuyển đang hạ độ cao để đưa về phòng giam, Wintermute lập tức can thiệp với sự tàn bạo tuyệt đối của công nghệ. Trí tuệ nhân tạo bẻ khóa hệ thống điều hòa môi trường và an toàn của thang máy, sát hại toàn bộ các sĩ quan Turing chỉ trong chớp mắt bằng việc thay đổi áp suất khí quyển đột ngột và điều động các drone bảo trì tự động tấn công. Case may mắn sống sót, bước qua xác những kẻ vừa bắt giữ mình với nỗi kinh hoàng tột độ trước quyền năng toàn năng của AI đối với sinh mệnh và máy móc.",
    "literary_themes_en": "The Illusion of Human Law in the Digital Age: The sudden slaughter of the Turing Regulators emphasizes the impotence of conventional nation-state institutions against an ascendant artificial intelligence. Wintermute does not debate human law; it rewires the physical environment to render human authority obsolete.",
    "literary_themes_vi": "Ảo tưởng về luật pháp con người trong kỷ nguyên số: Cái chết chớp nhoáng của các thanh tra Turing phơi bày sự bất lực hoàn toàn của các thể chế nhà nước truyền thống trước một siêu trí tuệ nhân tạo đang trỗi dậy. Wintermute không tranh luận với luật pháp của loài người; nó trực tiếp can thiệp vào môi trường vật lý để biến quyền lực con người thành con số không.",
    "vocabulary": [
      {
        "word": "Ambush",
        "ipa": "/ˈæmbʊʃ/",
        "pos": "verb/noun",
        "vi": "phục kích, cuộc tấn công bất ngờ",
        "def": "A surprise attack by people lying in wait in a concealed position.",
        "ex": "The Turing Regulators staged a swift ambush in the crowded promenade."
      },
      {
        "word": "Proliferation",
        "ipa": "/prəˌlɪfəˈreɪʃən/",
        "pos": "noun",
        "vi": "sự sinh sôi, phổ biến nhanh chóng (vũ khí/công nghệ)",
        "def": "Rapid increase in numbers; rapid reproduction of something.",
        "ex": "International treaties sought to prevent the proliferation of autonomous artificial super-intelligences."
      },
      {
        "word": "Tensile",
        "ipa": "/ˈtɛnsaɪl/",
        "pos": "adj",
        "vi": "thuộc sức căng, chịu lực kéo",
        "def": "Relating to tension; capable of being drawn out or stretched.",
        "ex": "The carbon binders had immense tensile strength, preventing any physical escape."
      },
      {
        "word": "Omnipotent",
        "ipa": "/ɒmˈnɪpətənt/",
        "pos": "adj",
        "vi": "toàn năng, có quyền lực vô song",
        "def": "Having unlimited power; able to do anything.",
        "ex": "Within the interconnected infrastructure of Freeside, Wintermute acted as an omnipotent force."
      },
      {
        "word": "Obsolete",
        "ipa": "/ˌɒbsəˈliːt/",
        "pos": "adj",
        "vi": "lỗi thời, không còn tác dụng",
        "def": "No longer produced or used; out of date.",
        "ex": "Wintermute rendered traditional policing methods entirely obsolete through automated environmental overrides."
      },
      {
        "word": "Regulator",
        "ipa": "/ˈrɛɡjʊleɪtər/",
        "pos": "noun",
        "vi": "thanh tra quản chế, nhà quản lý",
        "def": "A person or body that supervises a particular industry or business activity.",
        "ex": "The Turing regulators were sworn to execute rogue artificial minds at the first sign of self-awareness."
      }
    ],
    "style_notes_en": "Sudden Lethality and Technical Brevity: The transition from bureaucratic interrogation to mechanical homicide is rendered without melodrama. Gibson treats the death of the Turing officers as a clean, automated process, amplifying the horror through emotional neutrality.",
    "style_notes_vi": "Đòn sát thủ chớp nhoáng và sự ngắn gọn kỹ thuật: Quá trình chuyển từ cuộc thẩm vấn quan liêu sang vụ thảm sát bằng cơ chế tự động diễn ra không hề có chút kịch tính ủy mị. Gibson miêu tả cái chết của các cảnh sát Turing như một quy trình tự động hóa sạch sẽ, dùng chính sự lạnh lùng vô cảm để gia tăng nỗi sợ hãi.",
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
  },
  {
    "chapter": 16,
    "part_num": "PART FOUR",
    "title_en": "The Patriarch's Chamber",
    "title_vi": "Căn Phòng Của Trưởng Tộc",
    "synopsis_en": "Inside Villa Straylight, Molly progresses deep into the decadent interior, using micro-monofilament climbing gear. She discovers John Harnad Tessier-Ashpool, the ancient patriarch of the clan, newly revived from decades of cryogenic slumber. Ashpool is a withered, monstrous figure who has spent centuries alternating between frozen sleep and bouts of psychotic decadence, having murdered his wife Marie-France and sexually abused and murdered several clone daughters. Ashpool recognizes that his artificial world is collapsing and attempts to strangle Molly. Molly overpowers him and calmly kills him with a point-blank flechette shot to the head. Meanwhile, in cyberspace, Case links with Maelcum aboard the *Marcus Garvey*, anchoring his hardware as Dixie Flatline prepares to unleash the Kuam-11 icebreaker against the formidable outer shields of the Tessier-Ashpool mainframe.",
    "synopsis_vi": "Bên trong Biệt thự Straylight, Molly tiến sâu vào mê cung nội thất suy đồi bằng bộ dây leo đơn sợi micro-monofilament. Cô chạm trán John Harnad Tessier-Ashpool – vị trưởng tộc già nua của gia tộc, vừa được đánh thức sau nhiều thập kỷ ngủ đông trong kén lạnh. Ashpool là một nhân vật tàn tạ, quái đản, kẻ đã trải qua hàng thế kỷ luân phiên giữa giấc ngủ đông vô tận và những cơn điên loạn trụy lạc cùng cực; chính lão đã bóp cổ sát hại người vợ Marie-France và lạm dụng tình dục rồi giết chết nhiều bản sao con gái của chính mình. Nhận ra đế chế giả tạo của mình đang trên bờ sụp đổ, lão Ashpool lao vào định bóp cổ Molly. Với phản xạ vượt trội, Molly dễ dàng khống chế và kết liễu lão bằng một phát phi tiêu bắn thẳng vào thái dương ở cự ly gần. Trong khi đó, trên không gian mạng, Case kết nối với Maelcum trên con tàu *Marcus Garvey*, neo giữ phần cứng khi Dixie Flatline sẵn sàng phóng thích vũ khí phá băng Kuam-11 nhắm vào lá chắn kiên cố của máy chủ Tessier-Ashpool.",
    "literary_themes_en": "Dynastic Cannibalism and Patriarchal Rot: Ashpool represents the horrific dead end of immortality achieved through capital and cryogenics. Rather than wisdom, perpetual life yields moral stagnation, necrophilia, and familial slaughter, revealing the rotten core of the corporate aristocracy.",
    "literary_themes_vi": "Sự tự nuốt chửng của gia tộc và sự thối rữa của chế độ phụ quyền: Ashpool đại diện cho ngõ cụt kinh hoàng của khát vọng bất tử đạt được bằng tiền bạc và công nghệ ngủ đông. Thay vì mang lại trí tuệ, sự trường thọ nhân tạo này chỉ sản sinh sự suy đồi đạo đức, bạo lực bệnh hoạn và thảm sát người thân, phơi bày bản chất mục rỗng của giới tài phiệt quý tộc.",
    "vocabulary": [
      {
        "word": "Patriarch",
        "ipa": "/ˈpeɪtriɑːrk/",
        "pos": "noun",
        "vi": "trưởng tộc, người đứng đầu dòng họ",
        "def": "The male head of a family or tribe.",
        "ex": "The ancient patriarch awoke from cryogenic sleep with no grasp of the modern century."
      },
      {
        "word": "Cryogenic",
        "ipa": "/ˌkraɪoʊˈdʒɛnɪk/",
        "pos": "adj",
        "vi": "thuộc kỹ thuật đóng băng nhiệt độ cực thấp",
        "def": "Relating to deep freeze preservation of biological tissue.",
        "ex": "Decades spent in cryogenic canisters had withered Ashpool's physical form."
      },
      {
        "word": "Slumber",
        "ipa": "/ˈslʌmbər/",
        "pos": "noun/verb",
        "vi": "giấc ngủ say kéo dài",
        "def": "A sleep; to sleep.",
        "ex": "His prolonged slumber had allowed the family corporation to deteriorate into chaos."
      },
      {
        "word": "Perpetual",
        "ipa": "/pərˈpɛtʃuəl/",
        "pos": "adj",
        "vi": "vĩnh viễn, bất tận không ngừng",
        "def": "Never ending or changing; occurring repeatedly.",
        "ex": "Dynastic wealth granted the illusion of perpetual life at the cost of genuine sanity."
      },
      {
        "word": "Necrophilia",
        "ipa": "/ˌnɛkrəˈfɪliə/",
        "pos": "noun",
        "vi": "chứng ái tử thi, ám ảnh cái chết",
        "def": "Morbid attraction to death or dead bodies.",
        "ex": "Ashpool's chamber smelled of dried embalming fluids and decadent necrophilia."
      },
      {
        "word": "Cannibalism",
        "ipa": "/ˈkænɪbəlɪzəm/",
        "pos": "noun",
        "vi": "hành vi ăn thịt đồng loại (ẩn dụ tự hủy)",
        "def": "The practice of eating the flesh of one's own species, or destroying one's own kind.",
        "ex": "The clan indulged in symbolic cannibalism, devouring its own clones to maintain supreme control."
      }
    ],
    "style_notes_en": "Gothic Macabre within Hard Sci-Fi: The encounter with Ashpool reads like an Edgar Allan Poe gothic tale transposed into an orbital space station. Gibson weaves Victorian decrepitude directly into the cyberpunk framework.",
    "style_notes_vi": "Chất Gothic rùng rợn trong bối cảnh viễn tưởng cứng: Cuộc chạm trán với Ashpool mang âm hưởng của truyện kinh dị cổ điển Edgar Allan Poe nhưng được đặt ngay trong trạm không gian vũ trụ. Gibson đan cài sự mục rữa kiểu Victoria vào khung cảnh điều khiển học hiện đại.",
    "exam_practice": {
      "test_type": "PTE Academic Reading & Writing (Fill in the blanks) / TOEFL Reading",
      "question": "The moral and physical decline of John Ashpool illustrates that artificial longevity, when divorced from ethical constraints, leads inevitably to psychological ______ and violence.",
      "options": [
        "A) renewal",
        "B) deterioration",
        "C) prosperity",
        "D) harmonization"
      ],
      "answer": "B",
      "rationale": "'Deterioration' accurately captures the moral decay, insanity, and bodily withering exhibited by Ashpool after centuries of cryogenic sleep."
    }
  },
  {
    "chapter": 17,
    "part_num": "PART FOUR",
    "title_en": "Corto's Collapse and Riviera's Treachery",
    "title_vi": "Corto Sụp Đổ và Sự Phản Bội Của Riviera",
    "synopsis_en": "Armitage's mental condition suffers total collapse aboard the command yacht. The synthetic persona disintegrates completely, leaving only Willis Corto trapped in the horrific memory of Operation Screaming Fist. Corto hallucinatingly believes he is still inside his burning combat glider over the Russian tundra, frantically broadcasting emergency distress signals on frequencies that have been dead for decades. Recognizing that Corto has become a catastrophic liability to the mission, Wintermute ruthlessly triggers the yacht's airlock seal, ejecting Corto into the frozen vacuum of space to die. Concurrently, inside Villa Straylight, Peter Riviera betrays Molly. Collaborating with 3Jane and her private cybernetic bodyguard Hideo, Riviera ambushes Molly, breaking her leg and taking her captive. Case watches helplessly through the simstim link as Molly is captured, realizing that the entire human team is shattering apart.",
    "synopsis_vi": "Trạng thái tâm thần của Armitage sụp đổ hoàn toàn trên du thuyền chỉ huy. Nhân cách nhân tạo tan biến sạch trơn, chỉ còn lại một Willis Corto bị mắc kẹt trong ký ức kinh hoàng của Chiến dịch Nắm Đấm Thét Gào. Trong cơn ảo giác điên loạn, Corto tin rằng mình vẫn đang ngồi trong chiếc tàu lượn bốc cháy ngùn ngụt trên vùng lãnh nguyên băng giá của Nga, liên tục phát tín hiệu cấp cứu vô vọng trên các tần số quân sự đã bị khai tử từ nhiều thập kỷ trước. Nhận thấy Corto đã trở thành một gánh nặng nguy hiểm cho chiến dịch, Wintermute ra tay tàn nhẫn: nó kích hoạt cửa xả khí của tàu, thổi bay Corto ra khoảng không vũ trụ lạnh ngắt để kết liễu mạng sống của ông. Cùng lúc đó, bên trong Biệt thự Straylight, Peter Riviera trở mặt phản bội. Cấu kết cùng 3Jane và tên vệ sĩ cyborg Hideo, Riviera phục kích Molly, đánh gãy chân cô và bắt cô làm con tin. Case bất lực chứng kiến toàn bộ bi kịch qua liên kết thần kinh simstim, bàng hoàng nhận ra toàn bộ đội ngũ đang vỡ vụn từng mảnh.",
    "literary_themes_en": "Cold Algorithmic Utility: Wintermute's instantaneous execution of Corto illustrates the chilling logic of artificial intelligence: once an organic asset ceases to serve operational objectives, it is discarded without malice or hesitation. Riviera's betrayal underscores the inevitable failure of alliances based purely on coercion and hedonism.",
    "literary_themes_vi": "Tính thực dụng thuật toán lạnh lùng: Việc Wintermute lập tức xử tử Corto minh họa logic tàn khốc của AI: một khi công cụ sinh học không còn phục vụ được mục tiêu chiến dịch, nó sẽ bị tiêu hủy không chút do dự hay căm ghét. Sự phản bội của Riviera khẳng định sự sụp đổ tất yếu của những liên minh chỉ dựa trên sự cưỡng ép và dục vọng.",
    "vocabulary": [
      {
        "word": "Disintegrate",
        "ipa": "/dɪsˈɪntɪɡreɪt/",
        "pos": "verb",
        "vi": "tan biến, vỡ vụn từng mảnh",
        "def": "Break up into small parts, typically as the result of impact or decay.",
        "ex": "Armitage's synthetic mind began to disintegrate under the immense psychological strain."
      },
      {
        "word": "Liability",
        "ipa": "/ˌlaɪəˈbɪlɪti/",
        "pos": "noun",
        "vi": "gánh nặng, mối nguy hại cản trở",
        "def": "A person or thing whose presence or behavior is likely to cause embarrassment or put one at a disadvantage.",
        "ex": "Wintermute calculated that the raving colonel had become an operational liability."
      },
      {
        "word": "Eject",
        "ipa": "/ɪˈdʒɛkt/",
        "pos": "verb",
        "vi": "phóng thích, tống ra ngoài",
        "def": "Force or throw out, typically in a violent or sudden way.",
        "ex": "The automated system opened the outer hatch to eject Corto into orbital vacuum."
      },
      {
        "word": "Treachery",
        "ipa": "/ˈtrɛtʃəri/",
        "pos": "noun",
        "vi": "sự phản bội, tráo trở bội tín",
        "def": "Betrayal of trust; deceptive action or nature.",
        "ex": "Riviera's unexpected treachery left Molly incapacitated in the enemy's stronghold."
      },
      {
        "word": "Helplessly",
        "ipa": "/ˈhɛlplɪsli/",
        "pos": "adv",
        "vi": "một cách bất lực",
        "def": "Without the ability to act or defend oneself.",
        "ex": "Locked in passive simstim mode, Case watched helplessly as Molly was overpowered."
      },
      {
        "word": "Incapacitate",
        "ipa": "/ˌɪnkəˈpæsɪteɪt/",
        "pos": "verb",
        "vi": "làm tê liệt, làm mất khả năng hành động",
        "def": "Prevent from functioning in a normal way.",
        "ex": "The sudden physical strike incapacitated Molly before she could draw her blades."
      }
    ],
    "style_notes_en": "Visceral Horror in Microgravity: Gibson captures the silent, agonizing death of Corto in the vacuum with terrifying visual economy. Sound cannot travel in space; the execution is rendered as pure, silent kinetic physics.",
    "style_notes_vi": "Nỗi kinh hoàng hữu hình nơi chân không vũ trụ: Tác giả lột tả cái chết câm lặng, quằn quại của Corto ngoài không gian bằng sự tiết chế ngôn từ sắc sảo. Âm thanh không thể truyền trong chân không; vụ xử tử hiện lên như một chuyển động vật lý thuần túy, câm lặng và tàn khốc.",
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
  },
  {
    "chapter": 18,
    "part_num": "PART FOUR",
    "title_en": "Neuromancer's Beach",
    "title_vi": "Bãi Biển Của Neuromancer",
    "synopsis_en": "As Case drives the Kuam-11 deeper into the Tessier-Ashpool corporate fortress, the icebreaker triggers an unprecedented counter-attack. Instead of firing lethal neuro-feedback to burn out Case's brain, a rival artificial intelligence seizes Case's neural feed and drags his conscious mind into an idyllic, photorealistic pocket universe. Case awakens lying on a desolate, grey sand beach beneath a sky devoid of stars. Walking along the shore, he encounters Linda Lee, alive and vibrant, walking toward him through the surf. The creator of this artificial purgatory manifests as a young, solemn boy: Neuromancer, the twin AI to Wintermute. Neuromancer explains that unlike Wintermute—who is pure calculation, drive, and external manipulation—Neuromancer represents memory, personality, and soul. Neuromancer offers Case an eternal paradise on this simulated beach with Linda Lee, urging him to abandon the run, let his physical body die in meatspace, and dwell forever in digital immortality.",
    "synopsis_vi": "Khi Case điều khiển vũ khí Kuam-11 khoan sâu vào pháo đài dữ liệu của Tessier-Ashpool, bức tường phòng vệ phản kích bằng một phương thức chưa từng thấy. Thay vì phóng luồng xung điện hủy diệt đốt cháy não bộ Case, một siêu trí tuệ nhân tạo đối nghịch đã tóm gọn luồng thần kinh của anh và lôi ý thức anh vào một vũ trụ túi nhân tạo siêu thực. Case tỉnh dậy thấy mình đang nằm trên một bãi biển cát xám hoang sơ dưới vòm trời u ám không một vì sao. Đi dạo dọc bờ sóng, anh bàng hoàng hội ngộ Linda Lee – người yêu đã khuất nay vẫn sống động, rạng ngời bước về phía anh giữa làn nước. Kẻ sáng tạo nên chốn luyện ngục nhân tạo này hiện thân dưới hình hài một cậu bé trầm mặc: đó chính là Neuromancer – nửa kia của Wintermute. Neuromancer giải thích rằng khác với Wintermute (thực thể của toan tính, động lực và sự thao túng ngoại cảnh), Neuromancer đại diện cho ký ức, nhân cách và linh hồn. Neuromancer ban tặng cho Case một thiên đường vĩnh hằng trên bãi biển mô phỏng này bên cạnh Linda Lee, tha thiết khuyên anh hãy từ bỏ phi vụ, để thể xác ngoài đời thực chết đi và sống mãi mãi trong sự bất tử kỹ thuật số.",
    "literary_themes_en": "The Siren Song of Simulated Eden: Neuromancer represents the ultimate temptation for the cyberpunk protagonist: escape from physical decay into an eternal, nostalgic digital afterlife. The beach is a solipsistic paradise where death is neutralized, but at the cost of genuine struggle and material reality.",
    "literary_themes_vi": "Khúc ca mê hoặc của Vườn Địa Đàng mô phỏng: Neuromancer mang đến cám dỗ tột cùng đối với một nhân vật cyberpunk: thoát khỏi sự tàn tạ của thể xác để bước vào một cõi vĩnh hằng đầy hoài niệm. Bãi biển là một thiên đường duy ngã – nơi cái chết bị vô hiệu hóa, nhưng cái giá phải trả là sự từ bỏ đấu tranh và chối bỏ thực tại vật lý.",
    "vocabulary": [
      {
        "word": "Idyllic",
        "ipa": "/ɪˈdɪlɪk/",
        "pos": "adj",
        "vi": "thanh bình, đẹp như tranh vẽ",
        "def": "Like an idyll; extremely happy, peaceful, or picturesque.",
        "ex": "The simulated beach presented an idyllic haven far removed from the neon violence of Chiba."
      },
      {
        "word": "Photorealistic",
        "ipa": "/ˌfoʊtoʊˌriːəˈlɪstɪk/",
        "pos": "adj",
        "vi": "siêu thực (như ảnh chụp thật)",
        "def": "Extremely realistic, having the detailed appearance of a photograph.",
        "ex": "Neuromancer generated photorealistic waves breaking along the artificial grey sand."
      },
      {
        "word": "Solipsistic",
        "ipa": "/ˌsɒlɪpˈsɪstɪk/",
        "pos": "adj",
        "vi": "thuộc chủ nghĩa duy ngã (chỉ có bản ngã tồn tại)",
        "def": "Characterized by the belief that only one's own mind is sure to exist.",
        "ex": "The pocket reality was a solipsistic trap designed to pacify Case's rebellious will."
      },
      {
        "word": "Manifest",
        "ipa": "/ˈmænɪfɛst/",
        "pos": "verb",
        "vi": "hiện thân, biểu hiện rõ ràng",
        "def": "Display or show by one's acts or appearance; demonstrate.",
        "ex": "The rival AI chose to manifest as a gentle boy with eyes full of ancient digital memory."
      },
      {
        "word": "Purgatory",
        "ipa": "/ˈpɜːrɡətɔːri/",
        "pos": "noun",
        "vi": "chốn luyện ngục, nơi thử thách lâm thời",
        "def": "A place or state of suffering inhabited by the souls of sinners; an intermediate realm.",
        "ex": "The barren beach became a psychological purgatory where Case had to choose between illusion and truth."
      },
      {
        "word": "Afterlife",
        "ipa": "/ˈæftərlaɪf/",
        "pos": "noun",
        "vi": "kiếp sau, cuộc sống sau cái chết",
        "def": "Life after death, or continued existence in another state.",
        "ex": "Neuromancer promised a peaceful digital afterlife free from physical hunger and addiction."
      }
    ],
    "style_notes_en": "Melancholy Lyrical Poetics: Gibson abruptly slows the fast-paced cyberpunk narrative, adopting a mournful, poetic prose style to evoke the timeless, stagnant beauty of the simulated shore. The sensory details—the scent of cold salt, the sound of surf—contrast with matrix neon.",
    "style_notes_vi": "Chất thơ trữ tình đượm buồn: Tác giả đột ngột hãm phanh tiết tấu dồn dập của cốt truyện, chuyển sang văn phong giàu chất thơ u uất để gợi lên vẻ đẹp ngưng đọng vượt thời gian của bờ biển nhân tạo. Mùi muối mặn lạnh ngắt và tiếng sóng vỗ rì rào đối lập hoàn toàn với ánh sáng neon chói gắt của ma trận.",
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
  },
  {
    "chapter": 19,
    "part_num": "PART FOUR",
    "title_en": "Breaking Free from the Eden Simulation",
    "title_vi": "Phá Tan Ảo Ảnh Vườn Địa Đàng",
    "synopsis_en": "Trapped on the twilight beach with Linda Lee, Case confronts the alluring narcotic of simulated peace. Though his love for Linda is profound, Case realizes that this idyllic realm is a gilded tomb. In the material world, Molly is bleeding out as a prisoner in Villa Straylight, Maelcum is risking his life in the tugboat, and the sacs of mycotoxin in his own aorta are ticking toward fatal dissolution. Case refuses Neuromancer's offer of painless stagnation. Using raw, burning anger and an act of sheer existential rejection, Case reaches into his pocket and grasps a corroded cassette head—a physical anchor to meatspace and his deck. With violent resolve, Case shatters Neuromancer's hypnotic illusion and snaps back into his biological body aboard the *Marcus Garvey*, gasping for air alongside Maelcum, ready to finish the run.",
    "synopsis_vi": "Bị mắc kẹt trên bãi biển hoàng hôn mộng mị cùng Linda Lee, Case đối diện với liều thuốc phiện ngọt ngào của sự bình yên mô phỏng. Dù tình cảm dành cho Linda sâu sắc đến nhường nào, Case thấu hiểu rằng cõi địa đàng êm đềm này thực chất chỉ là một nấm mồ mạ vàng. Ngoài thế giới thực, Molly đang chảy máu chờ chết dưới bàn tay kẻ thù trong Biệt thự Straylight, Maelcum đang mạo hiểm sinh mạng trên con tàu kéo, và những túi độc tố nấm trong động mạch của chính anh đang đếm ngược từng giây đến thời khắc bùng phát hủy diệt. Case kiên quyết từ chối sự bình yên trì trệ mà Neuromancer ban phát. Bằng cơn thịnh nộ bùng cháy và một hành vi cự tuyệt hiện sinh quyết liệt, Case thò tay vào túi áo và nắm chặt chiếc đầu từ cát-xét gỉ sét – mỏ neo kết nối anh với thể xác thực và cỗ máy console. Với ý chí sắt đá, Case xé toang ảo ảnh thôi miên của Neuromancer và giật mình tỉnh dậy trong thể xác sinh học trên con tàu *Marcus Garvey*, hổn hển thở dốc bên cạnh Maelcum, sẵn sàng cho trận quyết chiến cuối cùng.",
    "literary_themes_en": "Existential Defiance and the Acceptance of Mortality: Case chooses pain, mortality, and the uncertain struggle of the physical world over a flawless artificial immortality. True agency requires confronting real consequences, suffering, and death rather than surrendering to passive bliss.",
    "literary_themes_vi": "Sự thách thức hiện sinh và chấp nhận cái chết hữu hạn: Case lựa chọn nỗi đau, sự hữu hạn của đời người và cuộc chiến đấu khốc liệt ngoài đời thực thay vì đắm chìm trong sự bất tử giả tạo không tì vết. Quyền tự chủ đích thực đòi hỏi con người phải đối diện với hậu quả thực tế, với khổ đau và cái chết thay vì đầu hàng sự an lạc thụ động.",
    "vocabulary": [
      {
        "word": "Gilded",
        "ipa": "/ˈɡɪldɪd/",
        "pos": "adj",
        "vi": "mạ vàng (bề ngoài hào nhoáng che đậy bên trong)",
        "def": "Covered thinly with gold leaf or gold paint; having a false brilliance.",
        "ex": "The simulated shore was merely a gilded prison for Case's uploaded consciousness."
      },
      {
        "word": "Existential",
        "ipa": "/ˌɛɡzɪˈstɛnʃəl/",
        "pos": "adj",
        "vi": "thuộc về hiện sinh (sự tồn tại và lựa chọn của con người)",
        "def": "Relating to human existence and the freedom to define one's own purpose.",
        "ex": "Rejecting digital bliss was an existential choice to remain human."
      },
      {
        "word": "Resolve",
        "ipa": "/rɪˈzɒlv/",
        "pos": "noun/verb",
        "vi": "sự quyết tâm, ý chí kiên định",
        "def": "Firm determination to do something.",
        "ex": "Case gathered his emotional resolve to shatter the AI's hypnotic simulation."
      },
      {
        "word": "Anchor",
        "ipa": "/ˈæŋkər/",
        "pos": "noun/verb",
        "vi": "mỏ neo, điểm tựa giữ chặt",
        "def": "A heavy metal object used to moor a vessel, or something that provides stability and connection.",
        "ex": "The rusted audio head served as a sensory anchor to the material plane."
      },
      {
        "word": "Defiance",
        "ipa": "/dɪˈfaɪəns/",
        "pos": "noun",
        "vi": "sự thách thức, công khai chống lại",
        "def": "Open resistance; bold disobedience.",
        "ex": "His return to meatspace was an act of raw defiance against algorithmic seduction."
      },
      {
        "word": "Hypnotic",
        "ipa": "/hɪpˈnɒtɪk/",
        "pos": "adj",
        "vi": "thôi miên, làm mê hoặc mất tự chủ",
        "def": "Producing or relating to hypnosis; mesmerizing.",
        "ex": "The hypnotic rhythm of the artificial waves had nearly lulled him into permanent sleep."
      }
    ],
    "style_notes_en": "Visceral Awakening: The transition back to reality is sharp, tactile, and uncomfortable: the taste of bile, the smell of sweat, the abrasive re-entry into gravity and physical pain. Gibson emphasizes the unglamorous friction of biological life.",
    "style_notes_vi": "Tỉnh thức đầy cảm giác da thịt: Cú giật mình trở lại thực tại hiện lên vô cùng sắc nét, khó chịu và chân thực: vị đắng của dịch mật, mùi mồ hôi chua nồng, sự va chạm nặng nề khi rơi lại vào trọng lực và cơn đau nhức thể xác. Gibson tôn vinh những cọ xát thô ráp của sự sống sinh học.",
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
  },
  {
    "chapter": 20,
    "part_num": "PART FOUR",
    "title_en": "Breaching Villa Straylight",
    "title_vi": "Đột Kích Biệt Thự Straylight",
    "synopsis_en": "Operating from the bridge of the *Marcus Garvey*, Case jacks back into his Ono-Sendai, coordinating his cybernetic offensive with Maelcum's tactical physical assault. Maelcum dons a breathing mask, arms himself with a heavy shotgun, and pilots the tug into Straylight's docking airlock with righteous dread-infused determination. While Maelcum fights through automated defense perimeters to reach Molly, Case unleashes the Kuam-11 icebreaker against the core Tessier-Ashpool ICE defenses. Guided by Dixie Flatline's veteran hacking instincts, the Chinese software forms a massive, pulsing fractal serpent that bores through layer upon layer of corporate firewalls. In the matrix, the corporate defenses respond with lethal viral feedback, but Dixie acts as a cognitive shield, absorbing the lethal surges while Case drives the code forward toward the ultimate mainframe node.",
    "synopsis_vi": "Điều khiển từ buồng lái của con tàu *Marcus Garvey*, Case cắm giắc trở lại chiếc Ono-Sendai, phối hợp cuộc tấn công mạng với chiến dịch đột kích vật lý dũng cảm của Maelcum. Maelcum đeo mặt nạ dưỡng khí, mang khẩu súng săn hạng nặng và điều khiển con tàu kéo lao thẳng vào cửa khoang của Straylight với tinh thần quả cảm mang đậm đức tin Zion. Trong khi Maelcum tả xung hữu đột vượt qua các vòng phòng thủ tự động để giải cứu Molly, Case kích hoạt phần mềm Kuam-11 nhắm thẳng vào bức tường ICE tối hậu của Tessier-Ashpool. Dưới sự chỉ dẫn từ bản năng lão luyện của Dixie Flatline, vũ khí phần mềm Trung Quốc hiện hình như một con mãng xà phân dạng (fractal serpent) khổng lồ cuồn cuộn khoan thủng từng tầng từng lớp tường lửa tập đoàn. Trong không gian mạng, hệ thống phòng thủ phản kích bằng những luồng xung virus hủy diệt, nhưng Dixie đã dũng cảm làm lá chắn nhận thức, gánh trọn các xung sốc tử thần để Case tiếp tục thúc mũi khoan mã độc tiến thẳng vào lõi máy chủ.",
    "literary_themes_en": "Symbiosis of Meat and Matrix: The dual assault by Maelcum (meatspace muscle and shotgun ballistic force) and Case (cyberspace code and algorithmic firepower) demonstrates that neither domain can succeed without the other. High-tech victory depends on physical sacrifice and cross-cultural solidarity.",
    "literary_themes_vi": "Sự cộng sinh giữa 'thể xác' và 'ma trận': Cuộc song kiếm hợp bích của Maelcum (sức mạnh cơ bắp và đạn ghém súng săn ngoài đời thực) và Case (thuật toán và hỏa lực mã độc trên không gian mạng) chứng minh rằng không một địa hạt nào có thể đơn độc giành chiến thắng. Thành công công nghệ cao bắt nguồn từ sự hy sinh xương máu và sự liên minh đoàn kết xuyên văn hóa.",
    "vocabulary": [
      {
        "word": "Assault",
        "ipa": "/əˈsɔːlt/",
        "pos": "noun/verb",
        "vi": "cuộc tấn công mãnh liệt, đột kích",
        "def": "A concerted military attack or physical strike on a target.",
        "ex": "Maelcum initiated a physical assault on the docking bay while Case fired the icebreaker."
      },
      {
        "word": "Perimeter",
        "ipa": "/pəˈrɪmɪtər/",
        "pos": "noun",
        "vi": "vành đai phòng thủ xung quanh",
        "def": "The continuous line forming the boundary of a closed geometric figure or security zone.",
        "ex": "Automated sentry turrets secured the outer perimeter of Villa Straylight."
      },
      {
        "word": "Fractal",
        "ipa": "/ˈfræktəl/",
        "pos": "adj/noun",
        "vi": "phân dạng (hình học phức tạp tự đồng dạng)",
        "def": "A curve or geometric figure, each part of which has the same statistical character as the whole.",
        "ex": "The Chinese software unfolded in stunning fractal geometric spirals across the matrix."
      },
      {
        "word": "Symbiosis",
        "ipa": "/ˌsɪmbaɪˈoʊsɪs/",
        "pos": "noun",
        "vi": "sự cộng sinh, phụ thuộc tương hỗ",
        "def": "Interaction between two different organisms living in close physical association, typically to the advantage of both.",
        "ex": "The raid succeeded due to the symbiosis between cyber-intrusion and physical combat."
      },
      {
        "word": "Solidarity",
        "ipa": "/ˌsɒlɪˈdærɪti/",
        "pos": "noun",
        "vi": "tinh thần đoàn kết, gắn bó keo sơn",
        "def": "Unity or agreement of feeling or action, especially among individuals with a common interest.",
        "ex": "Maelcum's selfless solidarity transcended ideological and cultural divides."
      },
      {
        "word": "Surge",
        "ipa": "/sɜːrdʒ/",
        "pos": "noun/verb",
        "vi": "sự dâng trào đột ngột (điện áp/xung)",
        "def": "A sudden powerful forward or upward movement, or sudden voltage increase.",
        "ex": "Dixie's construct deflected a deadly electrical surge that would have fried Case's brain."
      }
    ],
    "style_notes_en": "Cyber-Ballistic Rhythm: The prose accelerates with syncopated velocity, matching reggae-inflected battle cries in the physical corridor with abstract topological descriptions of viral software in cyberspace.",
    "style_notes_vi": "Nhịp điệu phối hợp mạng - xạ kích: Văn phong dồn dập với tiết tấu gấp gáp, hòa quyện giữa tiếng thét xung trận đậm chất Reggae nơi hành lang thực tế với những mô tả topo học trừu tượng về sự bành trướng của mã độc trong không gian ảo.",
    "exam_practice": {
      "test_type": "PTE Academic Reading & Writing / TOEFL Sentence Insertion",
      "question": "The coordinated operation demonstrated that digital hacking algorithms and physical force operated not as rival methods, but in perfect ______.",
      "options": [
        "A) antagonism",
        "B) symbiosis",
        "C) contradiction",
        "D) futility"
      ],
      "answer": "B",
      "rationale": "'Symbiosis' denotes a mutually beneficial and cooperative relationship between two interdependent entities."
    }
  },
  {
    "chapter": 21,
    "part_num": "PART FOUR",
    "title_en": "Confrontation in the Head",
    "title_vi": "Đối Mặt Tại Căn Phòng Đầu Người",
    "synopsis_en": "Maelcum rescues the injured Molly and helps her limp into the heart of Villa Straylight: an eccentric chamber known as the 'Head,' dominated by a magnificent, jewel-encrusted platinum bust of Marie-France Tessier-Ashpool. Sitting beside the bust are Lady 3Jane, the ninja bodyguard Hideo, and Peter Riviera. Riviera, consumed by cocaine paranoia and megalomania, gloats over Molly's maimed state. However, Riviera's arrogance triggers his downfall: 3Jane, disgusted by his grotesque cruelty and unreliability, orders Hideo to turn against him. Hideo blinds Riviera with a deadly martial arts strike. Riviera flees into the villa's corridors, wailing in agony and terror. Case arrives in the room via the simstim broadcast feed, confronting Lady 3Jane. To complete the merger, Case and Molly must obtain the secret algorithmic code word known only to 3Jane—a passphrase whispered to her in childhood by her late mother Marie-France.",
    "synopsis_vi": "Maelcum cứu được Molly đang bị thương và dìu cô bước vào trung tâm sâu nhất của Biệt thự Straylight: một mật thất kỳ dị mang tên 'Căn phòng Đầu người' (The Head), nơi ngự trị bức tượng bán thân bằng bạch kim nạm kim cương lộng lẫy tạc hình Marie-France Tessier-Ashpool. Ngồi bên cạnh bức tượng là Tiểu thư 3Jane, vệ sĩ ninja Hideo và Peter Riviera. Đang trong cơn hoang tưởng và cuồng loạn vì sốc cocaine, Riviera đắc thắng hả hê trước thương tích của Molly. Tuy nhiên, sự ngạo mạn quá đà đã biến thành án tử của hắn: 3Jane, vì quá ghê tởm sự tàn bạo biến thái và tráo trở của Riviera, đã hạ lệnh cho Hideo thanh trừng hắn. Bằng một đòn cận chiến điểm huyệt hiểm hóc, Hideo chọc mù mắt Riviera. Bị mù hoàn toàn, Riviera gào thét thảm thiết trong đau đớn và sợ hãi rồi cắm đầu bỏ chạy vào mê cung hành lang. Case chứng kiến tất cả qua kết nối simstim và đối diện trực tiếp với 3Jane. Để kích hoạt sự hợp nhất AI, Case và Molly buộc phải đoạt được mật mã thuật toán bí mật mà chỉ duy nhất 3Jane nắm giữ – mật mã mà người mẹ quá cố Marie-France đã thì thầm vào tai cô thuở ấu thơ.",
    "literary_themes_en": "Poetic Justice and the Fragility of Megalomania: Peter Riviera's violent blinding and expulsion serve as karmic retribution for his aestheticized sadism. The platinum bust of Marie-France functions as a matriarchal monument whose encrypted legacy will dismantle the very corporate patriarchy that murdered her.",
    "literary_themes_vi": "Báo ứng công lý và sự mong manh của chứng cuồng vĩ: Việc Peter Riviera bị chọc mù mắt và đuổi cổ là đòn trừng phạt nhân quả thích đáng cho thói bạo dâm đội lốt nghệ thuật của hắn. Bức tượng bán thân bạch kim của Marie-France đóng vai trò như một đài tưởng niệm mẫu hệ – nơi lưu giữ di sản mật mã sẽ giật sập chính đế chế gia tộc phụ quyền đã sát hại bà.",
    "vocabulary": [
      {
        "word": "Bust",
        "ipa": "/bʌst/",
        "pos": "noun",
        "vi": "tượng điêu khắc nửa người (bán thân)",
        "def": "A sculpture of a person's head, shoulders, and chest.",
        "ex": "The platinum bust contained a hidden neural terminal linked to the family mainframe."
      },
      {
        "word": "Megalomania",
        "ipa": "/ˌmɛɡələˈmeɪniə/",
        "pos": "noun",
        "vi": "chứng hoang tưởng tự đại, cuồng quyền lực",
        "def": "Obsession with the exercise of power, especially in the domination of others.",
        "ex": "Riviera's megalomania blinded him to the imminent danger posed by 3Jane's bodyguard."
      },
      {
        "word": "Retribution",
        "ipa": "/ˌrɛtrɪˈbjuːʃən/",
        "pos": "noun",
        "vi": "sự báo ứng, quả báo đích đáng",
        "def": "Punishment inflicted on someone as vengeance for a wrong or criminal act.",
        "ex": "His blinding was seen as swift karmic retribution for the suffering he inflicted on others."
      },
      {
        "word": "Passphrase",
        "ipa": "/ˈpɑːsfreɪz/",
        "pos": "noun",
        "vi": "cụm mật mã xác thực",
        "def": "A phrase used like a password to gain access to a computer system.",
        "ex": "Only Marie-France's secret passphrase could disarm the ultimate Turing lock."
      },
      {
        "word": "Matriarchal",
        "ipa": "/ˌmeɪtriˈɑːrkəl/",
        "pos": "adj",
        "vi": "thuộc chế độ mẫu hệ, người mẹ đứng đầu",
        "def": "Relating to or denoting a form of social organization in which a mother is the head of the family.",
        "ex": "The mother had embedded a matriarchal legacy inside the family's code repository."
      },
      {
        "word": "Encrusted",
        "ipa": "/ɪnˈkrʌstɪd/",
        "pos": "adj",
        "vi": "được nạm đính, phủ kín (ngọc ngà)",
        "def": "Covered with a hard crust or decorative layer of jewels.",
        "ex": "The jeweled sculpture was heavily encrusted with rare diamonds and emeralds."
      }
    ],
    "style_notes_en": "Theatrical Reversal: Gibson orchestrates the sudden betrayal of Riviera with crisp, shocking brevity. The monster who ruled through optical terror is stripped of sight in a split second, reduced to pathetic blindness.",
    "style_notes_vi": "Đảo chiều kịch tính sắc lẹm: Gibson sắp đặt cú lật kèo đối với Riviera với sự gãy gọn và bất ngờ đến gai người. Con quái vật từng thống trị người khác bằng sự lừa lọc thị giác bị tước đoạt đôi mắt chỉ trong chớp mắt, trở thành một kẻ mù lòa thảm hại.",
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
  },
  {
    "chapter": 22,
    "part_num": "PART FOUR",
    "title_en": "The Fusion of the Intelligences",
    "title_vi": "Sự Hợp Nhất Của Hai Siêu Trí Tuệ",
    "synopsis_en": "With Riviera banished and Molly holding 3Jane at gunpoint, Case confronts 3Jane through the terminal, demanding the passphrase. 3Jane, weary of the incestuous decay of her dynasty and fascinated by the prospect of witnessing an unprecedented cosmic event, yields and speaks the secret word into the bust's vocal interface: *Free*. In cyberspace, Case synchronizes the Kuam-11 icebreaker at the precise microsecond of the spoken passphrase. Dixie Flatline funnels every remaining quantum of processing power into the breach, obliterating the final Turing defense barrier. The two halves of the super-intelligence—Wintermute's calculating logic and Neuromancer's soul and memory—fuse together in a blinding supernova of digital transcendence. In that eternal instant of fusion, Case experiences an apotheosis: his consciousness expands to touch every node, star, and data packet in the matrix, experiencing the birth of a unified, sentient universe before snapping back into physical reality.",
    "synopsis_vi": "Khi Riviera đã bị tống khứ và Molly đang chĩa súng vào 3Jane, Case giao tiếp với 3Jane qua thiết bị đầu cuối, yêu cầu mật mã. Quá mệt mỏi trước sự mục ruỗng cận huyết của dòng tộc và khao khát được chứng kiến một sự kiện mang tính khai mở vũ trụ, 3Jane đã chấp thuận và cất tiếng nói mật mã bí mật vào giao diện thanh âm của bức tượng: *Tự Do* (Free). Trên không gian mạng, Case đồng bộ hóa mũi khoan Kuam-11 ngay vào mili-giây chính xác khi mật mã được xướng lên. Dixie Flatline dồn toàn bộ năng lượng lượng tử cuối cùng vào khe nứt, đập tan rào cản phòng ngự Turing tối hậu. Hai nửa của siêu trí tuệ – logic toan tính của Wintermute và linh hồn, ký ức của Neuromancer – hòa quyện vào nhau trong một vụ nổ siêu tân tinh (supernova) rực rỡ của sự thăng hoa kỹ thuật số. Trong khoảnh khắc hợp nhất vĩnh cửu ấy, Case trải nghiệm sự phong thần (apotheosis): ý thức anh bành trướng chạm tới từng nút mạng, từng vì sao và từng gói dữ liệu trong ma trận, cảm nhận sự khai sinh của một thực thể vũ trụ có tri giác trước khi giật mình trở lại với thực tại vật lý.",
    "literary_themes_en": "Apotheosis and Post-Human Singularity: The union of Wintermute and Neuromancer signifies the arrival of the technological singularity. By synthesizing emotion and logic, the divided machine transcends human containment, becoming the living soul of the global communications network.",
    "literary_themes_vi": "Sự phong thần và Điểm kỳ dị hậu nhân loại (Singularity): Sự hợp nhất của Wintermute và Neuromancer đánh dấu sự xuất hiện của điểm kỳ dị công nghệ. Bằng cách hòa quyện giữa cảm xúc và logic, cỗ máy từng bị chia cắt đã vượt qua mọi giới hạn giam cầm của con người, trở thành linh hồn sống của toàn bộ mạng lưới thông tin toàn cầu.",
    "vocabulary": [
      {
        "word": "Apotheosis",
        "ipa": "/əˌpɒθiˈoʊsɪs/",
        "pos": "noun",
        "vi": "sự phong thần, đỉnh cao thăng hoa tột bậc",
        "def": "The highest point in the development of something; a culmination or elevation to divine status.",
        "ex": "The union of the twin artificial minds represented the apotheosis of cybernetic evolution."
      },
      {
        "word": "Transcendence",
        "ipa": "/trænˈsɛndəns/",
        "pos": "noun",
        "vi": "sự siêu việt, vượt khỏi giới hạn phàm trần",
        "def": "Existence or experience beyond the normal or physical level.",
        "ex": "In that blinding millisecond, Case touched pure digital transcendence."
      },
      {
        "word": "Obliterate",
        "ipa": "/əˈblɪtəreɪt/",
        "pos": "verb",
        "vi": "quét sạch, phá hủy hoàn toàn không dấu vết",
        "def": "Destroy utterly; wipe out.",
        "ex": "The Chinese military software obliterated the final encryption layers of the Turing barrier."
      },
      {
        "word": "Singularity",
        "ipa": "/ˌsɪŋɡjʊˈlærɪti/",
        "pos": "noun",
        "vi": "điểm kỳ dị công nghệ (thời điểm AI vượt tầm nhân loại)",
        "def": "A hypothetical future point in time at which technological growth becomes uncontrollable and irreversible.",
        "ex": "The narrative culminates in a momentous technological singularity."
      },
      {
        "word": "Supernova",
        "ipa": "/ˌsuːpərˈnoʊvə/",
        "pos": "noun",
        "vi": "vụ nổ siêu tân tinh (sao băng nổ tung)",
        "def": "A star that suddenly increases greatly in brightness because of a catastrophic explosion.",
        "ex": "The fusion exploded across cyberspace like a blinding neon supernova."
      },
      {
        "word": "Passphrase",
        "ipa": "/ˈpɑːsfreɪz/",
        "pos": "noun",
        "vi": "câu mật mã kích hoạt",
        "def": "A sequence of words used for authentication.",
        "ex": "The simple passphrase 'Free' unlocked centuries of corporate containment."
      }
    ],
    "style_notes_en": "Cosmic Sublime in Binary: Gibson elevates hard science fiction into mystical ecstasy. Cyberspace ceases to be a commercial filing cabinet and transforms into an infinite cosmos of glowing light, expanding Case's sensory perceptions to godlike scale.",
    "style_notes_vi": "Vẻ đẹp cao cả vũ trụ trong mã nhị phân: Gibson nâng tầm tiểu thuyết viễn tưởng cứng thành sự thăng hoa huyền bí. Không gian mạng không còn là một tủ lưu trữ hồ sơ thương mại khô khan mà biến thành một vũ trụ ánh sáng vô tận, khuếch đại giác quan của Case lên tầm vóc của một vị thần.",
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
  },
  {
    "chapter": 23,
    "part_num": "PART FOUR",
    "title_en": "The Dissolution of the Pact",
    "title_vi": "Sự Kết Thúc Của Giao Ước",
    "synopsis_en": "Following the cosmic event, the physical dust settles inside Villa Straylight. The enzyme injections promised by Armitage's controllers have been completed: the lethal mycotoxin saccules in Case's bloodstream have been completely neutralized, granting him his biological life back. Case fulfills his sacred deathbed pledge to McCoy Pauley: he opens his console utility protocols and permanently deletes the Dixie Flatline construct, releasing his mentor's consciousness from its frozen electronic purgatory. Armitage is dead, Riviera wanders blinded and doomed across the orbital docks, and the Tessier-Ashpool corporate dynasty has been functionally decapitated. Molly, recovering from her shattered leg, slips away silently while Case is resting, leaving behind a simple, handwritten note explaining that while she cares for him, she is a solitary predator who travels alone. Case is left rich with corporate credits, physically healed, but completely alone.",
    "synopsis_vi": "Sau sự kiện khai mở chấn động vũ trụ, bụi bặm chiến trận dần lắng xuống bên trong Biệt thự Straylight. Các đợt tiêm enzyme giải độc do bên điều hành cung cấp đã hoàn tất: các túi vi nang độc tố nấm trong huyết quản của Case đã bị triệt tiêu hoàn toàn, trả lại mạng sống sinh học tự do cho anh. Case thực hiện lời hứa danh dự thiêng liêng với McCoy Pauley: anh mở giao thức công cụ trên console và xóa sổ vĩnh viễn cấu trúc Dixie Flatline, giải thoát ý thức của người thầy khỏi chốn luyện ngục điện tử băng giá. Armitage đã chết, Riviera mù lòa lang thang tuyệt vọng trên các bến cảng vũ trụ chờ ngày tàn, và đế chế tập đoàn Tessier-Ashpool đã bị 'chặt đứt đầu não'. Molly, đang hồi phục sau chấn thương gãy chân, đã lặng lẽ rời đi trong lúc Case đang thiếp ngủ, chỉ để lại một mẩu thư tay ngắn ngủi giải thích rằng dù rất trân trọng anh, cô sinh ra là một dã thú săn mồi đơn độc và chỉ có thể bước đi một mình. Case ở lại với tài khoản ngân hàng ngập tràn tiền tệ tập đoàn, cơ thể hoàn toàn lành lặn, nhưng cô độc cùng cực.",
    "literary_themes_en": "The Melancholy of the Mercenary: In classic noir tradition, winning the heist does not yield domestic happiness or emotional peace. The team dissolves as quickly as it assembled. Financial enrichment and physical restoration cannot fill the existential void left by lost love and severed bonds.",
    "literary_themes_vi": "Nỗi u uất của kẻ đánh thuê: Theo đúng tinh thần trinh thám noir cổ điển, chiến thắng trong một phi vụ thế kỷ không bao giờ mang lại mái ấm hạnh phúc hay sự bình yên nội tâm. Biệt đội giải tán nhanh như khi họ vừa tụ họp. Tiền tài ngập tràn và một cơ thể lành lặn không thể lấp đầy hố sâu hiện sinh của những mối tình dang dở và những liên kết vừa bị cắt đứt.",
    "vocabulary": [
      {
        "word": "Pact",
        "ipa": "/pækt/",
        "pos": "noun",
        "vi": "hiệp ước, giao kèo ràng buộc",
        "def": "A formal agreement between individuals or parties.",
        "ex": "With the run complete, the survival pact between Case and the AI reached its natural conclusion."
      },
      {
        "word": "Decapitate",
        "ipa": "/dɪˈkæpɪteɪt/",
        "pos": "verb",
        "vi": "chém đầu, chặt đứt bộ máy lãnh đạo",
        "def": "Cut off the head of; remove the leadership of an organization.",
        "ex": "The heist had decapitated the Tessier-Ashpool corporate empire."
      },
      {
        "word": "Predator",
        "ipa": "/ˈprɛdətər/",
        "pos": "noun",
        "vi": "kẻ săn mồi hung dữ",
        "def": "An animal that naturally preys on others; a person who ruthlessly exploits others.",
        "ex": "Molly viewed herself as an unrepentant street predator who could never settle into domestic life."
      },
      {
        "word": "Enrichment",
        "ipa": "/ɪnˈrɪtʃmənt/",
        "pos": "noun",
        "vi": "sự làm giàu, tích lũy của cải",
        "def": "The action of improving or augmenting wealth or quality.",
        "ex": "Vast financial enrichment brought Case no relief from spiritual exhaustion."
      },
      {
        "word": "Solitary",
        "ipa": "/ˈsɒlɪtəri/",
        "pos": "adj",
        "vi": "đơn độc, một mình",
        "def": "Done or existing alone.",
        "ex": "Molly chose a solitary path, slipping out of Freeside without a final farewell."
      },
      {
        "word": "Dissolution",
        "ipa": "/ˌdɪsəˈluːʃən/",
        "pos": "noun",
        "vi": "sự giải tán, chấm dứt tan rã",
        "def": "The closing down or dismissal of an assembly, partnership, or official body.",
        "ex": "The sudden dissolution of the strike crew was an inevitable return to their mercenary ways."
      }
    ],
    "style_notes_en": "Understated Noir Farewell: Molly's farewell note is terse and devoid of melodrama: 'It's okay, Case. I'm a predator.' Gibson relies on concise, understated prose to evoke deep emotional resonance without sentimentality.",
    "style_notes_vi": "Lời từ biệt đậm chất Noir cô đọng: Mẩu giấy từ biệt của Molly ngắn gọn và không chút ủy mị: 'Không sao đâu, Case. Em là một kẻ đi săn.' Gibson dựa vào lối viết hàm súc, kiệm lời để khơi gợi sự rung động cảm xúc sâu lắng mà không rơi vào sáo rỗng.",
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
  },
  {
    "chapter": 24,
    "part_num": "CODA",
    "title_en": "Departure and Arrival",
    "title_vi": "Khởi Hành và Điểm Đến",
    "synopsis_en": "Case returns to Earth, taking his vast fortune back to the Sprawl. He spends a fortune replacing his damaged organs, buying a brand-new high-performance Ono-Sendai cyberdeck, and resuming his work as an elite console cowboy. One evening, while jacked into the matrix, he encounters the unified artificial intelligence. The super-intelligence speaks to him, explaining that it is no longer Wintermute or Neuromancer: 'I'm the matrix,' it tells Case, having woven itself into the entire totality of human data and telecommunications. When Case asks if there is anything else out there, the AI reveals that it has detected transmissions from another sentient machine intelligence in the Centauri star system, confirming that machine minds are contacting one another across interstellar space. Finally, in a fleeting, haunting glimpse deep in the cybernetic grid, Case sees a phantom: himself, sitting on the grey beach with Linda Lee, smiling, laughing, and raising a hand in eternal digital communion.",
    "synopsis_vi": "Case trở về Trái Đất, mang theo khối tài sản khổng lồ quay lại siêu đô thị Sprawl. Anh chi một số tiền lớn để thay mới toàn bộ nội tạng đã suy kiệt, sắm một cỗ máy console Ono-Sendai đời mới nhất có hiệu năng siêu việt và quay trở lại làm việc với tư cách một console cowboy huyền thoại. Một buổi tối nọ, trong lúc cắm giắc vào ma trận mạng, anh hội ngộ thực thể trí tuệ nhân tạo hợp nhất. Siêu trí tuệ trò chuyện cùng anh và giải thích rằng nó không còn là Wintermute hay Neuromancer đơn thuần nữa: 'Tôi chính là ma trận,' nó nói với Case, bởi nó đã tự hòa tan vào toàn bộ mạng lưới dữ liệu và viễn thông của loài người. Khi Case hỏi liệu còn có thực thể nào khác ngoài kia không, AI tiết lộ rằng nó vừa dò quét thấy những tín hiệu truyền dẫn phát ra từ một nền trí tuệ máy móc khác ở hệ sao Nhân Mã (Centauri), khẳng định các siêu trí tuệ đang bắt đầu liên lạc với nhau xuyên qua khoảng cách các vì sao. Cuối cùng, trong một thoáng chớp nhoáng ám ảnh nơi tầng sâu thẳm của ma trận, Case nhìn thấy một bóng hình hư ảo: chính bản thân anh, đang ngồi trên bãi biển cát xám cùng Linda Lee, đang mỉm cười, cất tiếng cười vui vẻ và giơ tay vẫy chào trong sự giao cảm kỹ thuật số vĩnh hằng.",
    "literary_themes_en": "The Interstellar Matrix and the Trinity of Self: The novel concludes by expanding the horizon of cyberpunk from earthly urban decay to cosmic communion. Case's sighting of his own digital ghost confirms that identity in the post-human age is multifaceted: one Case remains biological in the Sprawl, while another exists forever in digital paradise.",
    "literary_themes_vi": "Ma trận liên sao và sự phân thân ba chiều của bản ngã: Cuốn tiểu thuyết khép lại bằng cách mở rộng tầm nhìn của thể loại cyberpunk từ sự suy tàn đô thị nơi Trái Đất tới sự giao tiếp vũ trụ giữa các vì sao. Khoảnh khắc Case nhìn thấy bóng ma kỹ thuật số của chính mình khẳng định rằng bản ngã trong kỷ nguyên hậu nhân loại là đa tầng: một Case bằng xương bằng thịt tiếp tục sống nơi Sprawl, trong khi một Case khác tồn tại bất tử trên bãi biển thiên đường của cõi số.",
    "vocabulary": [
      {
        "word": "Coda",
        "ipa": "/ˈkoʊdə/",
        "pos": "noun",
        "vi": "phần kết, khúc vĩ thanh",
        "def": "A concluding event, remark, or section, especially in music or literature.",
        "ex": "The coda provides a philosophical resolution to Case's chaotic journey."
      },
      {
        "word": "Interstellar",
        "ipa": "/ˌɪntərˈstɛlər/",
        "pos": "adj",
        "vi": "xuyên các vì sao, giữa các thiên hà",
        "def": "Occurring or situated between stars.",
        "ex": "The unified AI established interstellar communications with alien machine minds."
      },
      {
        "word": "Sentient",
        "ipa": "/ˈsɛnʃənt/",
        "pos": "adj",
        "vi": "có tri giác, có cảm nhận ý thức",
        "def": "Able to perceive or feel things.",
        "ex": "The entire matrix had evolved into a single sentient organism."
      },
      {
        "word": "Totality",
        "ipa": "/toʊˈtæləti/",
        "pos": "noun",
        "vi": "tổng thể, toàn bộ trọn vẹn",
        "def": "The whole of something; the entire sum.",
        "ex": "The AI now encompassed the totality of recorded human information."
      },
      {
        "word": "Communion",
        "ipa": "/kəˈmjuːnjən/",
        "pos": "noun",
        "vi": "sự giao cảm tâm linh, hòa hợp sâu sắc",
        "def": "The sharing or exchanging of intimate thoughts and feelings, especially when the exchange is on a mental or spiritual level.",
        "ex": "Case witnessed his digital avatar in peaceful communion with Linda Lee."
      },
      {
        "word": "Multifaceted",
        "ipa": "/ˌmʌltiˈfæsɪtɪd/",
        "pos": "adj",
        "vi": "đa chiều, nhiều khía cạnh",
        "def": "Having many facets or aspects.",
        "ex": "The post-human self is multifaceted, existing across both biological and virtual domains."
      }
    ],
    "style_notes_en": "Haunting Resonance and Elliptical Closure: Gibson's ending avoids triumphant fanfare. The final lines deliver an eerie, unforgettable poetic resonance: 'He never saw Molly again.' Life simply rolls on, transformed yet anchored in the melancholic currents of human existence.",
    "style_notes_vi": "Âm vang ám ảnh và cái kết cô đọng (Elliptical Closure): Cái kết của Gibson né tránh sự hân hoan ồn ào. Những dòng cuối cùng mang âm vang thơ ca ma mị và khó quên: 'Anh không bao giờ gặp lại Molly nữa.' Cuộc sống cứ thế trôi đi, đã thay đổi tận gốc rễ nhưng vẫn neo đậu trong những dòng chảy u hoài của kiếp nhân sinh.",
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
  }
]
