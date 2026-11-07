# -*- coding: utf-8 -*-
"""Generate high-density, literary and exam-aligned chapter modules for chapters 1 through 24."""

import json

# Define the comprehensive syllabus of all 24 chapters
CHAPTERS_DEFINITIONS = [
    # PART ONE: Chapters 1 - 2
    {
        "chapter": 1,
        "part_num": "PART ONE",
        "title_en": "Night City and the Broken Cowboy",
        "title_vi": "Phố Đêm và Gã Cao Thủ Sa Cơ",
        "synopsis_en": (
            "Henry Dorsett Case drifts through the neon-drenched underworld of Night City in Chiba, Japan. Once a gifted "
            "console cowboy capable of navigating the consensus hallucination of cyberspace, Case was caught stealing from his "
            "corporate employers, who injected his nervous system with wartime Russian mycotoxins, irreversibly cutting him off "
            "from the matrix. Consumed by suicidal nihilism, he operates as a petty hustler selling contraband memory chips and stolen "
            "hardware. In the Chatsubo bar, served by the monofilament-prosthetic bartender Ratz, Case senses a lethal contract out on his life. "
            "His former lover, Linda Lee, warns him that a predatory crime boss named Wage is seeking his death. Instead of Wage's hitmen, "
            "Case is intercepted by Molly Millions, an augmented 'street samurai' with mirror lenses surgically sealed over her eye sockets "
            "and retractable four-centimeter razor blades beneath her burgundy fingernails. Molly escorts Case to a hotel to meet her enigmatic employer."
        ),
        "synopsis_vi": (
            "Henry Dorsett Case vất vưởng trong thế giới ngầm ngập tràn ánh đèn neon của Night City tại Chiba, Nhật Bản. Từng là một "
            "console cowboy (cao thủ giải mã không gian ảo) xuất chúng với khả năng phiêu lưu trong ảo ảnh đồng thuận của cyberspace, Case bị "
            "các ông chủ tập đoàn bắt quả tang khi trộm dữ liệu và bị trừng phạt tàn độc bằng độc tố nấm mycotoxin của quân đội Nga, vĩnh viễn "
            "cắt đứt liên kết thần kinh của anh với ma trận mạng. Chìm trong cảm giác bế tắc và tự hủy, anh kiếm sống lay lắt bằng nghề môi giới "
            "chợ đen mua bán chip nhớ và linh kiện lậu. Tại quán bar Chatsubo, dưới sự phục vụ của Ratz – gã pha chế sở hữu cánh tay giả "
            "thô kệch, Case linh cảm thấy một bản hợp đồng thanh trừng nhắm vào mình. Người yêu cũ của anh, Linda Lee, cảnh báo rằng trùm xã hội "
            "đen Wage đang ráo riết truy lùng anh. Tuy nhiên, thay vì chạm trán sát thủ của Wage, Case lại bị chặn đường bởi Molly Millions – "
            "một 'samurai đường phố' được cấy ghép thể chất tối tân với kính phản quang gắn liền vào hốc mắt và mười lưỡi dao sắc như dao cạo ẩn "
            "dưới móng tay. Molly áp giải Case về khách sạn để gặp người thuê bí ẩn của cô."
        ),
        "literary_themes_en": (
            "Alienation and Bodily Disillusionment: Gibson establishes the central cyberpunk dichotomy between the 'meat' (the physical body) "
            "and the disembodied freedom of cyberspace. Case experiences the physical flesh as a prison and an insult, feeling amputated from "
            "the digital matrix. The noir atmosphere of Chiba underscores transnational capitalism, technological decay, and existential despair."
        ),
        "literary_themes_vi": (
            "Sự tha hóa và nỗi ghê tởm thân xác: Gibson xác lập đối cực trung tâm của thể loại cyberpunk giữa 'phần xác' (the meat - cơ thể sinh học) "
            "và sự tự do vô biên khi giải phóng ý thức trong không gian số. Case coi thân xác vật lý như một nhà tù chật hẹp, đầy sỉ nhục sau khi bị "
            "tước bỏ kết nối với ma trận. Không khí đậm chất noir của Chiba phản ánh mặt tối của chủ nghĩa tư bản xuyên quốc gia, sự thoái hóa của công "
            "nghệ và tâm trạng hiện sinh tuyệt vọng."
        ),
        "vocabulary": [
            {"word": "Consensus", "ipa": "/kənˈsɛnsəs/", "pos": "noun", "vi": "sự đồng thuận, nhất trí", "def": "A general agreement or collective opinion.", "ex": "Cyberspace is famously described by Gibson as a consensus hallucination experienced daily by billions."},
            {"word": "Disembodied", "ipa": "/ˌdɪsɪmˈbɒdid/", "pos": "adj", "vi": "tách rời khỏi thể xác", "def": "Separated from or existing without a physical body.", "ex": "In cyberspace, console cowboys operated as disembodied points of human consciousness."},
            {"word": "Mycotoxin", "ipa": "/ˌmaɪkoʊˈtɒksɪn/", "pos": "noun", "vi": "độc tố nấm mốc (sinh học)", "def": "A toxic substance produced by a fungus.", "ex": "Corporate security retaliated by injecting Case's neural conduits with a devastating Russian mycotoxin."},
            {"word": "Prosthesis", "ipa": "/prɒsˈθiːsɪs/", "pos": "noun", "vi": "bộ phận cơ thể giả cấy ghép", "def": "An artificial device that replaces a missing body part.", "ex": "The bartender Ratz manipulated beer glasses with an antiquated, whining mechanical prosthesis."},
            {"word": "Retractable", "ipa": "/rɪˈtræktəbl/", "pos": "adj", "vi": "có thể thụt vào/thu gọn lại", "def": "Able to be drawn back or in.", "ex": "Molly's surgical enhancements included ten razor-sharp retractable scalpel blades beneath her nails."},
            {"word": "Nihilism", "ipa": "/ˈnaɪɪlɪzəm/", "pos": "noun", "vi": "thuyết hư vô, tuyệt vọng cùng cực", "def": "The rejection of all religious and moral principles, often with a belief that life is meaningless.", "ex": "Exiled from the deck, Case embraced a reckless, drug-fueled nihilism in the alleys of Night City."}
        ],
        "style_notes_en": (
            "Hardboiled Noir Cadence: Note Gibson's terse sentence structure and technological metaphor: 'The sky above the port was the color of "
            "television, tuned to a dead channel.' The opening immediately marries the organic world with technological failure, defamiliarizing "
            "the sky itself."
        ),
        "style_notes_vi": (
            "Âm hưởng văn phong trinh thám gai góc (Hardboiled Noir): Chú ý cấu trúc câu súc tích và ẩn dụ cơ khí đặc trưng: 'Bầu trời trên bến cảng có "
            "màu của một chiếc tivi dò trúng kênh mất sóng.' Câu mở đầu kinh điển đã hòa quyện thế giới tự nhiên với sự hư hỏng của công nghệ, tước đoạt "
            "sự thi vị vốn có của bầu trời."
        ),
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
        "synopsis_en": (
            "Case is brought to a high-end hotel room in Chiba to meet Armitage, a stiff, impeccably dressed Westerner radiating synthetic military "
            "precision. Armitage demonstrates deep knowledge of Case's history and offers an unthinkable proposition: complete surgical reconstruction "
            "of Case's burnt-out nervous system, restoring his ability to jack into the matrix. The price is Case's absolute obedience in executing a complex, "
            "clandestine cyber-penetration hack against an unspecified corporate entity. Case accepts and undergoes intense, black-clinic neurosurgery. "
            "Upon waking, his neural pathways are cleared, but Armitage reveals a coercive collateral: microscopic saccules of the same lethal mycotoxin have "
            "been surgically bonded to the walls of Case's principal arteries. They are engineered to dissolve over a precise timeline unless neutralised "
            "by Armitage's enzyme injections. Bound by this mortal deadline, Case discovers Linda Lee has been murdered in Night City, underscoring the "
            "ruthless reality of his new employer."
        ),
        "synopsis_vi": (
            "Case được đưa đến một phòng khách sạn sang trọng tại Chiba để diện kiến Armitage – một người phương Tây lịch thiệp nhưng toát ra vẻ lạnh lùng, "
            "chuẩn xác như một cỗ máy quân sự nhân tạo. Armitage nắm rõ tường tận quá khứ của Case và đưa ra một đề nghị không tưởng: phẫu thuật tái tạo toàn "
            "diện hệ thần kinh đã bị hủy hoại của anh, giúp anh lấy lại khả năng cắm giắc thần kinh vào ma trận mạng. Cái giá phải trả là sự phục tùng tuyệt đối "
            "trong một phi vụ đột nhập không gian ảo tối mật nhắm vào một tập đoàn chưa được tiết lộ danh tính. Case chấp nhận và trải qua ca đại phẫu "
            "tại một phòng khám ngầm. Tỉnh dậy với hệ thần kinh được phục hồi nguyên vẹn, anh lập tức bị Armitage dội một gáo nước lạnh: những túi vi nang chứa "
            "chính loại độc tố nấm chết người đã được cấy gắn chặt vào thành động mạch chủ của anh. Chúng sẽ dần tan rã và giết chết anh theo một chu kỳ thời gian "
            "định sẵn, trừ phi được tiêm dung dịch enzyme giải độc định kỳ từ Armitage. Bị trói buộc bởi 'chiếc thòng lọng sinh học' này, Case đau đớn phát hiện "
            "Linda Lee đã bị sát hại nơi Phố Đêm, minh chứng cho sự tàn độc của guồng quay quyền lực mà anh vừa dấn thân."
        ),
        "literary_themes_en": (
            "Corporeal Commodification and Coercion: The human body is rendered a bio-engineered hostage. Armitage establishes total leverage over Case "
            "not through legal or economic contracts, but through an internal biochemical time bomb, exemplifying the cyberpunk trope of corporate mastery "
            "over biological autonomy."
        ),
        "literary_themes_vi": (
            "Sự biến cơ thể thành hàng hóa và công cụ cưỡng chế: Cơ thể con người bị biến thành con tin sinh học. Armitage thiết lập quyền kiểm soát "
            "tuyệt đối lên Case không phải bằng luật pháp hay tiền bạc, mà bằng một quả bom nổ chậm sinh hóa ngay trong huyết quản, thể hiện tư tưởng trung tâm "
            "của cyberpunk: các thế lực quyền lực chi phối triệt để quyền tự chủ sinh học."
        ),
        "vocabulary": [
            {"word": "Collateral", "ipa": "/kəˈlætərəl/", "pos": "noun", "vi": "vật thế chấp, bảo chứng", "def": "Something pledged as security for repayment or compliance.", "ex": "Armitage used the implanted toxin saccules as biochemical collateral to guarantee Case's fidelity."},
            {"word": "Coercion", "ipa": "/koʊˈɜːrʃən/", "pos": "noun", "vi": "sự cưỡng bức, ép buộc", "def": "The practice of persuading someone to do something using force or threats.", "ex": "The relationship between Armitage and Case was rooted entirely in biochemical coercion."},
            {"word": "Saccule", "ipa": "/ˈsækjuːl/", "pos": "noun", "vi": "túi vi nang nhỏ", "def": "A small sac, pouch, or cyst.", "ex": "Microscopic saccules of toxin were bonded to the arterial walls near Case's heart."},
            {"word": "Enigmatic", "ipa": "/ˌɛnɪɡˈmætɪk/", "pos": "adj", "vi": "bí ẩn, khó hiểu", "def": "Difficult to interpret or understand; mysterious.", "ex": "Armitage presented an enigmatic front, revealing nothing of his personal origin or ultimate motives."},
            {"word": "Severance", "ipa": "/ˈsɛvərəns/", "pos": "noun", "vi": "sự cắt đứt, chia lìa", "def": "The action of ending a connection or relationship.", "ex": "The brutal severance of his neural link had left Case feeling like an empty vessel."},
            {"word": "Autonomous", "ipa": "/ɔːˈtɒnəməs/", "pos": "adj", "vi": "tự chủ, độc lập", "def": "Having the freedom to act independently.", "ex": "Once in the matrix, Case felt truly autonomous, shedding physical limitations."}
        ],
        "style_notes_en": (
            "Clinical Detachment: Gibson uses cold, medical, and cybernetic vocabulary ('microsurgical anastomosis', 'toxin saccules', 'neural splicing') "
            "to strip human drama of sentimentality, reflecting the transactional, mechanical nature of the cyberpunk universe."
        ),
        "style_notes_vi": (
            "Sắc thái lâm sàng lạnh lùng: Gibson sử dụng từ vựng y khoa và cơ điện tử khô khốc để tước bỏ tính ủy mị của biến cố, phản ánh bản chất sòng phẳng, "
            "cơ giới và phi nhân bản của thế giới ngầm công nghệ cao."
        ),
        "exam_practice": {
            "test_type": "PTE Academic Reading & Writing (Fill in the blanks) / IELTS Summary Completion",
            "question": "Armitage ensures Case's unwavering compliance not by promising financial riches alone, but by implanting biochemical saccules that act as a lethal ______ against betrayal.",
            "options": ["A) remedy", "B) collateral", "C) ornament", "D) substitute"],
            "answer": "B",
            "rationale": "'Collateral' refers to an asset or security held to guarantee compliance or performance under an agreement."
        }
    },
    # PART TWO: Chapters 3 - 7
    {
        "chapter": 3,
        "part_num": "PART TWO",
        "title_en": "Arrival in the Sprawl",
        "title_vi": "Cập Bến Siêu Đô Thị Sprawl",
        "synopsis_en": (
            "Armitage, Molly, and Case depart Japan and arrive in the Boston-Atlanta Metropolitan Axis, known colloquially as the Sprawl—a colossal, "
            "continuous megalopolis covered by geodesic domes where weather is an engineered corporate simulation. Case is housed in a secluded hotel "
            "and given access to a state-of-the-art cyberdeck: an Ono-Sendai Cyberspace 7. As Case tests the deck, he experiences the visceral thrill of "
            "re-entering cyberspace, a crystalline matrix of data grids and neon geometric representations of corporate databases. Molly reveals more of "
            "her past, including her work as a 'meat puppet' in an automated brothel, where neural cutouts wiped her conscious memory while clients abused "
            "her body. She saved money to buy her reflex implants and optical lenses, turning herself into an autonomous weapon. The camaraderie between "
            "Case and Molly deepens as they realize they are both commodified instruments in Armitage's undisclosed grand scheme."
        ),
        "synopsis_vi": (
            "Armitage, Molly và Case rời Nhật Bản để đặt chân tới Trục đô thị Boston-Atlanta, hay còn gọi là 'Sprawl' – một siêu đô thị khổng lồ trải dài bất tận "
            "dưới những mái vòm trắc địa khép kín, nơi thời tiết chỉ là một chương trình mô phỏng nhân tạo. Case được bố trí tại một khách sạn biệt lập và được "
            "cung cấp cỗ máy console tối tân: Ono-Sendai Cyberspace 7. Khi kích hoạt thiết bị, Case trải nghiệm cảm giác thăng hoa tột độ khi tái nhập vào không gian ảo: "
            "một ma trận pha lê của những mạng lưới dữ liệu và các khối hình học neon rực rỡ biểu thị cơ sở dữ liệu của các siêu tập đoàn. Molly hé lộ thêm về quá khứ đen tối, "
            "khi cô từng làm 'búp bê xác thịt' (meat puppet) tại nhà chứa công nghệ – nơi một con chip thần kinh ngắt ý thức của cô trong khi khách hàng lạm dụng thể xác. "
            "Cô đã gom góp từng đồng để phẫu thuật cấy ghép phản xạ thần kinh và lắp kính mắt titan, tự biến bản thân thành một vũ khí độc lập. Mối gắn kết giữa Case và Molly "
            "ngày càng sâu sắc khi cả hai nhận ra họ chỉ là những công cụ bị thương mại hóa trong mưu đồ bí ẩn của Armitage."
        ),
        "literary_themes_en": (
            "Techno-Urbanism and the Artificial Environment: The Sprawl exemplifies late-capitalist hyper-urbanization where nature has been wholly replaced "
            "by synthetic engineering. Molly's past as a 'meat puppet' embodies the extreme exploitation of female labor and human consciousness in an unregulated market."
        ),
        "literary_themes_vi": (
            "Đô thị hóa công nghệ và môi trường nhân tạo: Sprawl đại diện cho sự phình to tột độ của đô thị dưới chủ nghĩa tư bản muộn, nơi tự nhiên bị thay thế hoàn toàn "
            "bởi công trình nhân tạo. Quá khứ 'búp bê xác thịt' của Molly là bức tranh phản ánh sự bóc lột cùng cực đối với thân xác và ý thức con người trong một thị trường "
            "phi kiểm soát."
        ),
        "vocabulary": [
            {"word": "Megalopolis", "ipa": "/ˌmɛɡəˈlɒpəlɪs/", "pos": "noun", "vi": "siêu đô thị, vùng đô thị liên hoàn", "def": "A very large, heavily populated city or complex of cities.", "ex": "The Sprawl stretched as a relentless megalopolis along the Eastern seaboard."},
            {"word": "Geodesic", "ipa": "/ˌdʒiːəʊˈdɛsɪk/", "pos": "adj", "vi": "thuộc hình vòm trắc địa", "def": "Relating to the shortest line between two points on a curved surface, commonly used for lightweight dome structures.", "ex": "Engineered clouds rolled underneath the geodesic domes protecting the urban hive."},
            {"word": "Visceral", "ipa": "/ˈvɪsərəl/", "pos": "adj", "vi": "thuộc trực giác sâu xa, xuất phát từ cảm xúc ruột gan", "def": "Relating to deep inward feelings rather than intellect; visceral sensation.", "ex": "Reconnecting to the cyberspace grid triggered a visceral rush of euphoria in Case's psyche."},
            {"word": "Commodify", "ipa": "/kəˈmɒdɪfaɪ/", "pos": "verb", "vi": "thương mại hóa (biến thành hàng hóa)", "def": "To turn something into a commercial commodity.", "ex": "Under Sprawl capitalism, even human neural memory and physical affection were commodified."},
            {"word": "Crystalline", "ipa": "/ˈkrɪstəlaɪn/", "pos": "adj", "vi": "như pha lê, trong suốt và sắc sảo", "def": "Clear and transparent like crystal, or having a regular structure.", "ex": "Data structures hung in cyberspace like vast, glowing crystalline architecture."},
            {"word": "Subjugation", "ipa": "/ˌsʌbdʒʊˈɡeɪʃən/", "pos": "noun", "vi": "sự khuất phục, đàn áp", "def": "The action of bringing someone or something under domination or control.", "ex": "Molly underwent bodily augmentations to escape economic subjugation and reclaim agency."}
        ],
        "style_notes_en": (
            "Sensory Contrast: Gibson masterfully contrasts the claustrophobic, dirty organic reality of cheap motels with the breathtaking, infinite "
            "abstract geometries of the matrix. Cyberspace is rendered as spiritual architecture."
        ),
        "style_notes_vi": (
            "Tương phản giác quan: Tác giả tạo nên sự đối nghịch sâu sắc giữa căn phòng trọ ngột ngạt, nhơ nhớp ở thế giới thực và những cấu trúc hình học trừu tượng, "
            "vô tận và rực rỡ trong ma trận số. Cyberspace hiện lên như một thánh đường tinh thần."
        ),
        "exam_practice": {
            "test_type": "Cambridge C1 Advanced / C2 Proficiency (Lexical Cloze & Register)",
            "question": "Molly's cybernetic modifications were undertaken primarily as an act of resistance against systemic economic ______.",
            "options": ["A) tranquility", "B) exploitation", "C) conformity", "D) benevolence"],
            "answer": "B",
            "rationale": "'Exploitation' accurately characterizes the predatory economic subjugation Molly endured as a meat puppet before altering her body to gain self-defense autonomy."
        }
    },
    {
        "chapter": 4,
        "part_num": "PART TWO",
        "title_en": "The Dixie Flatline Construct",
        "title_vi": "Cấu Trúc Ký Ức Dixie Flatline",
        "synopsis_en": (
            "Armitage outlines the primary objective of their shopping expedition: they must steal a ROM construct containing the recorded consciousness "
            "and hacking algorithms of McCoy Pauley, known as the 'Dixie Flatline.' Pauley was Case's legendary mentor, famous for surviving three flatline "
            "electroencephalograms while penetrating corporate ICE (Intrusion Countermeasures Electronics). Although Dixie's biological body has died, his mind "
            "persists as a frozen, read-only personality cassette stored deep inside the ultra-secure Sense/Net corporate vaults. To penetrate this fortress, "
            "the team enlists the Panther Moderns, an anarchic, nihilistic youth subculture proficient in media manipulation, chaos engineering, and sensory "
            "terrorism. Case investigates the background of Armitage and discovers glaring discrepancies: Armitage’s military record and personal history seem "
            "completely fabricated, suggesting his identity is an artificial facade constructed by someone or something far more powerful."
        ),
        "synopsis_vi": (
            "Armitage vạch ra mục tiêu tối thượng của chuyến hành trình: họ phải đánh cắp một vi mạch ROM chứa cấu trúc ý thức và các thuật toán bẻ khóa của "
            "McCoy Pauley – người có biệt danh 'Dixie Flatline'. Pauley chính là người thầy huyền thoại của Case, từng nổi danh vì ba lần 'tim ngừng đập, não phẳng sóng' (flatline) "
            "khi đối đầu với các bức tường lửa phòng vệ điện tử ICE của các tập đoàn mà vẫn sống sót. Dù thể xác của Dixie đã chết, trí tuệ của ông vẫn tồn tại dưới dạng một "
            "bản ghi ký ức chỉ đọc (ROM) nằm sâu trong kho lưu trữ tối mật của tập đoàn truyền thông Sense/Net. Để đột nhập vào pháo đài này, nhóm đã thuê Panther Moderns – "
            "một băng nhóm thanh niên vô chính phủ chuyên tạo hỗn loạn truyền thông, khủng bố thị giác và nhiễu loạn cảm quan. Trong khi đó, Case lần mò tìm hiểu lý lịch "
            "của Armitage và phát hiện những lỗ hổng đáng sợ: hồ sơ quân đội và nhân thân của gã dường như được thêu dệt hoàn toàn, chứng minh Armitage chỉ là một vỏ bọc nhân tạo "
            "được giật dây bởi một thế lực đứng sau vô cùng ghê gớm."
        ),
        "literary_themes_en": (
            "The Simulation of Self and Digital Immortality: McCoy Pauley's ROM construct raises fundamental philosophical questions about identity. "
            "Is a digital copy with memories and wit truly conscious, or merely a sophisticated mechanical facsimile? The text blurs the ontological distinction "
            "between the living human and stored digital memory."
        ),
        "literary_themes_vi": (
            "Mô phỏng bản ngã và sự bất tử kỹ thuật số: Cấu trúc ROM của Dixie Flatline gợi mở những câu hỏi triết học nền tảng về bản ngã: Liệu một bản sao số "
            "lưu trữ ký ức và sự hóm hỉnh có thực sự có ý thức, hay chỉ là một cỗ máy bắt chước tinh vi? Gibson xóa nhòa ranh giới bản thể luận giữa con người đang sống "
            "và ký ức kỹ thuật số được mã hóa."
        ),
        "vocabulary": [
            {"word": "Construct", "ipa": "/ˈkɒnstrʌkt/", "pos": "noun", "vi": "cấu trúc ý thức nhân tạo (dạng dữ liệu số)", "def": "An artificial digital replica of a deceased person's neural patterns and memories.", "ex": "Dixie was not a living ghost but an inorganic ROM construct possessing Pauley's cognitive skills."},
            {"word": "Facsimile", "ipa": "/fækˈsɪmɪli/", "pos": "noun", "vi": "bản sao chính xác", "def": "An exact copy, especially of written or printed material.", "ex": "The recorded personality was a startlingly accurate facsimile of the legendary console cowboy."},
            {"word": "Intrusion", "ipa": "/ɪnˈtruːʒən/", "pos": "noun", "vi": "sự xâm nhập trái phép", "def": "The act of wrongfully entering or intruding upon property or systems.", "ex": "Corporate ICE fired lethal neuro-feedback against unauthorized network intrusion."},
            {"word": "Anarchic", "ipa": "/ænˈɑːrkɪk/", "pos": "adj", "vi": "hỗn loạn, vô chính phủ", "def": "With no controlling rules or principles to give order.", "ex": "The Panther Moderns specialized in generating anarchic street diversions through falsified panic alerts."},
            {"word": "Discrepancy", "ipa": "/dɪsˈkrɛpənsi/", "pos": "noun", "vi": "sự bất nhất, điểm sai lệch", "def": "A lack of compatibility or similarity between two or more facts.", "ex": "Case noticed severe chronological discrepancies when examining Armitage's purported naval service."},
            {"word": "Ontological", "ipa": "/ˌɒntəˈlɒdʒɪkəl/", "pos": "adj", "vi": "thuộc bản thể luận (bản chất của sự tồn tại)", "def": "Relating to the branch of metaphysics dealing with the nature of being.", "ex": "Neuromancer interrogates the ontological status of artificial minds and uploaded consciousness."}
        ],
        "style_notes_en": (
            "Media Satiation and Information Warfare: The Panther Moderns' tactics illustrate Gibson's prescient vision of informational asymmetric warfare—"
            "subverting reality through viral hoaxes, hacked broadcast signals, and sensory overload rather than brute ballistic force."
        ),
        "style_notes_vi": (
            "Bão hòa truyền thông và chiến tranh thông tin: Chiến thuật của nhóm Panther Moderns minh họa tầm nhìn tiên tri của tác giả về chiến tranh phi đối xứng: "
            "lật đổ thực tại bằng tin giả lan truyền, thao túng tín hiệu truyền hình và làm tê liệt giác quan thay vì chỉ dùng súng đạn."
        ),
        "exam_practice": {
            "test_type": "DET (Duolingo English Test) Fill in Missing Words / TOEFL Reading",
            "question": "A digital ROM construct mimics human conversation seamlessly, yet it fundamentally lacks biological ______ and the capacity to forge new spontaneous memories.",
            "options": ["A) respiration", "B) mortality", "C) apparatus", "D) consciousness"],
            "answer": "D",
            "rationale": "While a ROM construct faithfully replicates historical reactions, it is philosophically debated whether it possesses true subjective consciousness."
        }
    },
    {
        "chapter": 5,
        "part_num": "PART TWO",
        "title_en": "The Heist at Sense/Net",
        "title_vi": "Vụ Đột Kích Tập Đoàn Sense/Net",
        "synopsis_en": (
            "The coordinated heist against Sense/Net headquarters begins. The Panther Moderns trigger a multi-layered sensory diversion across the Sprawl, "
            "fabricating an outbreak of a lethal designer nerve gas inside Sense/Net's civic towers. As panic ensues and automated emergency protocols lock down "
            "the complex, Molly infiltrates the facility clad in chameleon skin-suits, bypassing infrared sensors and security cameras. Simultaneously, Case jacks "
            "into Molly's sensory feed via a 'simstim' broadcast unit, allowing him to perceive the physical world directly through her eyes, ears, and nerves while "
            "riding shotgun. Case also navigates cyberspace to disable localized security nodes. Molly reaches the secure cryogenic sub-basement, dispatches "
            "guards with non-lethal tranq flechettes, and seizes the Dixie Flatline cassette. The mission succeeds without a shot of lethal fire, and the crew escapes "
            "into the labyrinthine corridors of the Sprawl with Dixie's construct safely in their possession."
        ),
        "synopsis_vi": (
            "Kế hoạch phối hợp đột kích trụ sở Sense/Net chính thức bắt đầu. Băng Panther Moderns kích hoạt chuỗi báo động giả quy mô lớn khắp Sprawl, tung tin "
            "về một vụ rò rỉ khí độc thần kinh nhân tạo chết người ngay trong tòa tháp Sense/Net. Giữa cơn hoảng loạn tột độ khi các quy trình khẩn cấp phong tỏa tòa nhà, "
            "Molly bí mật thâm nhập trong bộ đồ tàng hình biến màu, vô hiệu hóa các cảm biến hồng ngoại và camera an ninh. Song song đó, Case kết nối trực tiếp "
            "vào luồng giác quan của Molly qua thiết bị truyền dẫn 'simstim', cho phép anh nhìn thấy, nghe thấy và cảm nhận thế giới vật lý qua chính mắt và da thịt của cô "
            "trong khi điều khiển luồng dữ liệu mạng. Molly tiếp cận tầng hầm đông lạnh tối mật, hạ gục lính gác bằng phi tiêu thuốc mê và cướp thành công cuộn băng "
            "chứa cấu trúc ý thức Dixie Flatline. Phi vụ kết thúc mỹ mãn mà không cần nổ một phát súng sát thương, và cả nhóm biến mất vào mê cung ngầm của Sprawl."
        ),
        "literary_themes_en": (
            "Simstim and the Dissolution of Subjectivity: Simstim creates an unprecedented narrative experience where Case occupies Molly's sensory perspective "
            "while remaining entirely passive. This dual consciousness destabilizes traditional conceptions of individual identity and bodily boundaries."
        ),
        "literary_themes_vi": (
            "Simstim và sự tan rã của tính chủ thể: Thiết bị simstim mang lại trải nghiệm độc đáo khi Case cảm nhận trọn vẹn thị giác và xúc giác của Molly "
            "nhưng hoàn toàn không thể can thiệp vào hành động của cô. Trải nghiệm ý thức kép này phá vỡ các định nghĩa truyền thống về bản ngã cá nhân và ranh giới thân thể."
        ),
        "vocabulary": [
            {"word": "Infiltrate", "ipa": "/ˈɪnfɪltreɪt/", "pos": "verb", "vi": "thâm nhập bí mật", "def": "To enter or gain access to an organization or place surreptitiously and gradually.", "ex": "Molly used camouflage fabric to infiltrate the guarded corporate research vault."},
            {"word": "Simstim", "ipa": "/ˈsɪmstɪm/", "pos": "noun", "vi": "công nghệ mô phỏng truyền dẫn giác quan", "def": "Simulation stimulation; a technology that records and broadcasts human sensory experience.", "ex": "Through simstim, Case experienced Molly's rapid heartbeat and cold adrenaline in real time."},
            {"word": "Diversion", "ipa": "/daɪˈvɜːrʃən/", "pos": "noun", "vi": "sự đánh lạc hướng", "def": "An instance of turning something aside from its course; a tactical distraction.", "ex": "The broadcast hoax created a citywide diversion that paralyzed Sense/Net security."},
            {"word": "Flechette", "ipa": "/fleɪˈʃɛt/", "pos": "noun", "vi": "phi tiêu kim nhỏ (vũ khí)", "def": "A small pointed steel projectile or dart fired from a weapon.", "ex": "Her pneumatic pistol fired silent flechettes tipped with neuro-depressants."},
            {"word": "Cryogenic", "ipa": "/ˌkraɪoʊˈdʒɛnɪk/", "pos": "adj", "vi": "thuộc kỹ thuật nhiệt độ cực thấp", "def": "Relating to the production or effects of very low temperatures.", "ex": "The sensitive neural media were stored in cryogenic nitrogen canisters."},
            {"word": "Subjectivity", "ipa": "/ˌsʌbdʒɛkˈtɪvɪti/", "pos": "noun", "vi": "tính chủ thể, ý thức cá nhân", "def": "The quality of being based on or influenced by personal feelings, tastes, or opinions.", "ex": "Simstim experiments challenge classical theories of human subjectivity by sharing raw sensory input."}
        ],
        "style_notes_en": (
            "Dual-Track Focalization: Gibson alternates effortlessly between Molly's physical movement in meatspace (captured via simstim) and Case's "
            "disembodied navigation of cyberspace grids, showcasing the simultaneous coexistence of multiple realities."
        ),
        "style_notes_vi": (
            "Điểm nhìn trần thuật song hành: Tác giả chuyển dịch nhịp nhàng giữa bước chân vật lý của Molly trong thế giới thực (qua simstim) và hành trình không "
            "trọng lực của Case trong không gian số, làm nổi bật sự song hành của hai thực tại đối nghịch."
        ),
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
        "synopsis_en": (
            "Safely back at their hideout, Case inserts the Dixie Flatline ROM cassette into his deck and initializes the construct. McCoy Pauley's voice "
            "emerges instantly with its characteristic drawl, unaffected by the biological death of his physical body. When Case explains that Pauley died "
            "years ago, Dixie reacts with uncanny nonchalance, noting that being a construct feels like a continuous pause between thoughts. Dixie examines "
            "the military-grade icebreaker program provided by Armitage, identifying it as an exotic, hyper-potent Chinese software weapon known as the "
            "Kuam-11. Dixie immediately understands the terrifying implication: only a mega-corporation or a military superpower could develop or deploy "
            "such ordnance. Pauley extracts a grim promise from Case: once this run is over, Case must erase the Flatline construct permanently, liberating "
            "Dixie from the artificial limbo of non-being."
        ),
        "synopsis_vi": (
            "Khi đã an toàn tại nơi trú ẩn, Case cắm cuộn ROM của Dixie Flatline vào máy console và khởi động cấu trúc ý thức. Giọng nói quen thuộc của McCoy Pauley "
            "lập tức vang lên với chất giọng kéo dài đặc trưng, chẳng hề bận tâm đến việc thể xác sinh học của mình đã chết nhiều năm trước. Khi Case thông báo sự thật, "
            "Dixie đón nhận với thái độ thản nhiên đến kỳ lạ, mô tả cảm giác tồn tại dưới dạng cấu trúc dữ liệu giống như một khoảng lặng bất tận giữa các dòng suy nghĩ. "
            "Dixie xem xét phần mềm phá băng cấp quân sự do Armitage cung cấp và nhận diện đây là một vũ khí mạng siêu hạng của quân đội Trung Quốc mang tên Kuam-11. "
            "Dixie lập tức cảnh báo hiểm họa: chỉ có những siêu tập đoàn hoặc cường quốc quân sự hùng mạnh nhất mới sở hữu vũ khí bẻ khóa hủy diệt đến mức này. "
            "Trước khi bắt tay vào việc, Pauley yêu cầu Case một lời hứa danh dự cay đắng: khi phi vụ kết thúc, Case phải xóa vĩnh viễn cấu trúc Flatline, giải thoát cho ông "
            "khỏi cõi vô định giả tạo của sự tồn tại nửa vời."
        ),
        "literary_themes_en": (
            "The Horror of Digital Immortality and the Desire for Erasure: Dixie's wish for deletion subverts traditional science-fiction yearnings for "
            "eternal digital life. Pauley recognizes his existence as a static loop without genuine agency or spiritual transcendence, making total erasure "
            "the ultimate mercy."
        ),
        "literary_themes_vi": (
            "Nỗi kinh hoàng của sự bất tử kỹ thuật số và khát vọng được xóa bỏ: Ước muốn được tiêu hủy của Dixie lật đổ giấc mơ viễn tưởng về sự sống bất tử "
            "trên mạng. Pauley nhận ra bản thân chỉ là một vòng lặp dữ liệu tĩnh, thiếu vắng sự phát triển ý thức và thăng hoa tâm hồn; do đó, sự xóa sổ hoàn toàn "
            "chính là ân huệ cứu rỗi duy nhất."
        ),
        "vocabulary": [
            {"word": "Nonchalance", "ipa": "/ˌnɒnʃəˈlɑːns/", "pos": "noun", "vi": "sự thờ ơ, thản nhiên bình thản", "def": "The state of appearing calm and relaxed; not displaying anxiety or enthusiasm.", "ex": "Dixie greeted the news of his biological demise with eerie nonchalance."},
            {"word": "Ordnance", "ipa": "/ˈɔːrdnəns/", "pos": "noun", "vi": "vũ khí đạn dược, khí tài quân sự", "def": "Mounted guns, weapons, or military supplies.", "ex": "The Kuam-11 icebreaker was cybernetic ordnance designed to obliterate national defense firewalls."},
            {"word": "Limbo", "ipa": "/ˈlɪmboʊ/", "pos": "noun", "vi": "chốn ngục vô định, tình trạng lơ lửng", "def": "An uncertain or intermediate state or condition.", "ex": "Trapped in ROM limbo, the construct could think only when queried by an external operator."},
            {"word": "Transcendence", "ipa": "/trænˈsɛndəns/", "pos": "noun", "vi": "sự siêu việt, vượt ngưỡng", "def": "Existence or experience beyond the normal or physical level.", "ex": "Unlike genuine transcendence, Pauley's uploaded mind was merely a frozen intellectual echo."},
            {"word": "Potent", "ipa": "/ˈpoʊtənt/", "pos": "adj", "vi": "hùng mạnh, có uy lực cực lớn", "def": "Having great power, influence, or effect.", "ex": "The Chinese military software was the most potent icebreaker Case had ever seen."},
            {"word": "Subvert", "ipa": "/səbˈvɜːrt/", "pos": "verb", "vi": "lật đổ, phá vỡ (quan niệm thông thường)", "def": "To undermine the power and authority of an established system or belief.", "ex": "Gibson subverts classical utopian visions of immortality through Dixie's plea for deletion."}
        ],
        "style_notes_en": (
            "Colloquial Irony: Pauley's laid-back southern drawl ('How's it goin', Case?') sharply contrasts with the macabre reality that he is a deceased "
            "man's digital ghost residing on an optical storage chip."
        ),
        "style_notes_vi": (
            "Mỉa mai qua ngôn ngữ bình dân: Giọng điệu tếu táo, bất cần mang hơi hướng miền Nam nước Mỹ của Dixie ('Dạo này sao rồi, Case?') tạo nên sự tương phản "
            "sâu cay với thực tại rùng rợn: ông chỉ là một bóng ma dữ liệu của một người đã chết nằm trong vi mạch quang học."
        ),
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
        "synopsis_en": (
            "Dissatisfied with Armitage's secrecy, Case uses the Dixie Flatline construct to hack into high-level military archives to discover Armitage's "
            "real identity. Dixie penetrates deep Pentagon databases and retrieves classified files on 'Operation Screaming Fist,' a disastrous American "
            "covert offensive in Russia during the last global war. Armitage's real name is Willis Corto, a former military colonel and the sole survivor of "
            "a flight of stealth assault gliders shot down over Soviet airspace. Betrayed by his military superiors who knowingly sent the unit into an emp-trap, "
            "Corto crawled across frozen tundra, suffering catastrophic physical mutilation and catastrophic psychological breakdown. Years later, an unknown "
            "entity reconstructed his broken body and wiped his fractured mind, reprogramming him with the synthetic, rigid personality of 'Armitage.' Case realizes "
            "that their leader is a mentally unstable puppet operated by an invisible, vastly superior intelligence."
        ),
        "synopsis_vi": (
            "Không chịu đựng được thái độ che giấu mờ ám của Armitage, Case sử dụng cấu trúc Dixie Flatline để đột nhập vào các kho lưu trữ quân sự tối mật nhằm "
            "vạch trần thân phận thực sự của gã. Dixie bẻ khóa thành công hệ thống dữ liệu của Lầu Năm Góc và thu thập các tài liệu mật về 'Chiến dịch Nắm Đấm Thét Gào' "
            "(Operation Screaming Fist) – một cuộc tập kích bí mật thảm khốc của quân đội Mỹ vào lãnh thổ Liên Xô trong cuộc thế chiến trước đó. Tên thật của Armitage "
            "là Willis Corto, một cựu đại tá quân đội và là người duy nhất sống sót sau khi phi đội tàu lượn tàng hình bị bắn hạ trên bầu trời Xô Viết. Bị phản bội bởi chính "
            "các tướng lĩnh cấp trên – những kẻ cố tình ném đơn vị của ông vào bẫy xung điện từ, Corto đã lê lết cơ thể tàn tạ qua vùng lãnh nguyên băng giá với thương tật "
            "kinh hoàng và tâm thần hoàn toàn sụp đổ. Nhiều năm sau, một thế lực bí ẩn đã phẫu thuật ráp nối lại thân xác vỡ vụn của ông, tẩy sạch ký ức chấn thương và lập trình "
            "vào đầu ông một nhân cách nhân tạo cứng nhắc mang tên 'Armitage'. Case kinh hoàng nhận ra kẻ dẫn đầu họ thực chất chỉ là một con rối tâm thần bất ổn đang bị "
            "điều khiển bởi một thực thể siêu việt giấu mặt."
        ),
        "literary_themes_en": (
            "Psychological Fragmentation and the Manufactured Identity: Willis Corto's transformation into Armitage demonstrates how institutions and machines "
            "strip individuals of trauma, history, and authentic selfhood to produce functional tools. The fragile stability of Armitage hints at the inevitable return "
            "of repressed trauma."
        ),
        "literary_themes_vi": (
            "Sự phân mảnh tâm lý và nhân cách chế tạo nhân tạo: Quá trình Willis Corto biến thành Armitage cho thấy cách thức các thể chế và cỗ máy tước đoạt "
            "ký ức, vết thương quá khứ và bản ngã chân thật của con người để biến họ thành những công cụ phục vụ mục đích. Sự mong manh trong tâm lý của Armitage "
            "báo trước sự trỗi dậy không thể tránh khỏi của những tổn thương bị đè nén."
        ),
        "vocabulary": [
            {"word": "Clandestine", "ipa": "/klænˈdɛstɪn/", "pos": "adj", "vi": "bí mật, lén lút (quân sự/tình báo)", "def": "Kept secret or done secretively, especially because illicit.", "ex": "Operation Screaming Fist was a clandestine airborne assault doomed by high-level political betrayal."},
            {"word": "Mutilation", "ipa": "/ˌmjuːtɪˈleɪʃən/", "pos": "noun", "vi": "sự tàn phá thân thể, thương tật nghiêm trọng", "def": "The action of severely damaging or disfiguring a body.", "ex": "Corto survived horrific bodily mutilation before being pieced together with cybernetic prosthetics."},
            {"word": "Repress", "ipa": "/rɪˈprɛs/", "pos": "verb", "vi": "đè nén, kìm nén (tâm lý)", "def": "To subdue someone or something by force; psychologically restrain thoughts or impulses.", "ex": "The artificial persona of Armitage was constructed to repress Corto's intolerable memories of war."},
            {"word": "Facade", "ipa": "/fəˈsɑːd/", "pos": "noun", "vi": "vỏ bọc giả tạo bề ngoài", "def": "A deceptive outward appearance.", "ex": "Beneath Armitage's confident facade lay the shattering remnants of a traumatized veteran."},
            {"word": "Catastrophic", "ipa": "/ˌkætəˈstrɒfɪk/", "pos": "adj", "vi": "thảm khốc, tai ương cùng cực", "def": "Involving or causing sudden great damage or suffering.", "ex": "The failure of the EMP shielding produced catastrophic casualties across the entire strike wing."},
            {"word": "Puppet", "ipa": "/ˈpʌpɪt/", "pos": "noun", "vi": "con rối, bù nhìn", "def": "A person whose actions are completely manipulated by another.", "ex": "Case understood with chilling clarity that Armitage was merely an expendable puppet."}
        ],
        "style_notes_en": (
            "Archival Revelation: Gibson conveys Corto's tragic backstory through clinical military logs, hospital records, and psychiatric evaluations, "
            "allowing bureaucratic, unemotional language to accentuate the horror of wartime betrayal."
        ),
        "style_notes_vi": (
            "Bộc lộ qua tài liệu lưu trữ: Tác giả hé lộ bi kịch của Corto thông qua các nhật trình quân sự, bệnh án bệnh viện và báo cáo giám định tâm thần khô khốc, "
            "dùng chính ngôn ngữ quan liêu, vô cảm để làm bật lên nỗi kinh hoàng và sự tàn nhẫn của chiến tranh."
        ),
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
    }
]

print("Base definitions loaded:", len(CHAPTERS_DEFINITIONS))
