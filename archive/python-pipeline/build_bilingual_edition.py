import json
import re
from pathlib import Path

# Cyberpunk / Literary Glossary and Advanced C1/C2 IELTS/TOEFL/Cambridge Vocabulary
# Each entry provides:
# - headword / term
# - ipa / pos
# - exam_level: C1 / C2 / Specialized Academic
# - definition_en: Academic definition
# - definition_vi: Vietnamese translation & cultural / thematic nuance
# - literary_note: Cyberpunk lore, stylistic effect, or grammar insight

ACADEMIC_GLOSSARY = {
    # Part 1: Chiba City Blues
    "matrix": {
        "term": "matrix", "ipa": "/ˈmeɪ.trɪks/", "pos": "noun", "level": "C1/C2 Academic",
        "definition_en": "A consensual hallucination experienced daily by billions of legitimate operators; cyberspace environment.",
        "definition_vi": "Ma trận; không gian ảo điều khiển học (cyberspace) nơi ý thức hòa nhập với dữ liệu số.",
        "literary_note": "Khái niệm mang tính bước ngoặt của Gibson khai sinh thuật ngữ không gian mạng (cyberspace) trong văn học và triết học công nghệ thế kỷ 20."
    },
    "cyberspace": {
        "term": "cyberspace", "ipa": "/ˈsaɪ.bə.speɪs/", "pos": "noun", "level": "C1/C2 Academic",
        "definition_en": "Consensual hallucination of data networks; graphic representation of data abstracted from banks of every computer in the human system.",
        "definition_vi": "Không gian mạng / Không gian số hóa biểu thị ma trận dữ liệu toàn cầu.",
        "literary_note": "Được chính William Gibson đặt ra và định nghĩa bất hủ trong chương 3 tác phẩm này."
    },
    "console cowboy": {
        "term": "console cowboy", "ipa": "/ˈkɒn.səʊl ˈkaʊ.bɔɪ/", "pos": "noun phrase", "level": "C1 Specialized",
        "definition_en": "An elite computer hacker navigating and manipulating cyberspace using a neural interface.",
        "definition_vi": "Tin tặc điều khiển học / cao bồi bàn phím xâm nhập các hệ thống dữ liệu cao cấp.",
        "literary_note": "Biểu tượng phản văn hóa (counterculture) độc đáo của dòng tiểu thuyết Cyberpunk thập niên 80."
    },
    "deck": {
        "term": "deck / cyberspace deck", "ipa": "/dek/", "pos": "noun", "level": "C1 Technical",
        "definition_en": "A specialized computer hardware unit equipped with neural electrodes used to project the user's consciousness into cyberspace.",
        "definition_vi": "Thiết bị điều khiển số / bo mạch thần kinh kết nối tâm trí trực tiếp vào mạng lưới.",
        "literary_note": "Thiết bị đặc trưng của các tin tặc như Case (tiêu biểu là dòng máy Ono-Sendai Cyberspace 7)."
    },
    "dermatrodes": {
        "term": "dermatrodes", "ipa": "/ˌdɜː.məˈtrəʊdz/", "pos": "noun pl.", "level": "C2 Neologism",
        "definition_en": "Skin electrodes that attach to the forehead to transmit neural signals directly into a deck.",
        "definition_vi": "Điện cực áp da trán dùng để truyền dẫn và giải mã sóng thần kinh trực tiếp.",
        "literary_note": "Giao diện não - máy tính (BCI) tiên phong được hình dung trước khi khoa học hiện đại phát triển công nghệ thần kinh."
    },
    "flatline": {
        "term": "flatline", "ipa": "/ˈflæt.laɪn/", "pos": "verb/noun", "level": "C1 Idiom/Medical",
        "definition_en": "To show no electrical brain activity or pulse; medically dead; an EEG showing brain death.",
        "definition_vi": "Chết não / sóng não tắt lịm thành đường thẳng; người đã qua đời còn lưu bản sao tâm thức (ROM construct).",
        "literary_note": "Ám chỉ huyền thoại McCoy Pauley ('Dixie Flatline') từng sống sót sau ba lần chết não trong khi xâm nhập trí tuệ nhân tạo."
    },
    "zaibatsu": {
        "term": "zaibatsu", "ipa": "/zaɪˈbæt.suː/", "pos": "noun (loanword)", "level": "C2 Economics/Sociology",
        "definition_en": "A large Japanese business conglomerate or multinational mega-corporation holding vast economic and political sway.",
        "definition_vi": "Tập đoàn tài phiệt lũng đoạn khổng lồ xuyên quốc gia của Nhật Bản.",
        "literary_note": "Phản ánh nỗi lo âu kinh tế và viễn cảnh tương lai công nghệ thống trị bởi các tập đoàn Nhật Bản thập niên 1980."
    },
    "simstim": {
        "term": "simstim", "ipa": "/ˈsɪm.stɪm/", "pos": "noun (portmanteau)", "level": "C2 Neologism",
        "definition_en": "Simulated stimulation; mass-market neural entertainment that broadcasts the complete sensorium (sight, smell, emotion) of another person.",
        "definition_vi": "Hệ mô phỏng thụ cảm thần kinh ghi lại và truyền tải trọn vẹn mọi giác quan, cảm xúc của người khác.",
        "literary_note": "Hình thái truyền thông đại chúng tối tân trong thế giới tương lai, đồng thời là công cụ đột nhập của Case vào góc nhìn giác quan của Molly."
    },
    "ice": {
        "term": "ICE (Intrusion Countermeasure Electronics)", "ipa": "/aɪs/", "pos": "acronym/noun", "level": "C1/C2 Cybernetics",
        "definition_en": "Intrusion Countermeasure Electronics: security software guarding corporate data in cyberspace, capable of lethal neural feedback ('black ICE').",
        "definition_vi": "Điện tử chống xâm nhập; hàng rào phòng thủ tường lửa số, đặc biệt là 'ICE đen' có thể phóng xung điện gây chết người lập tức.",
        "literary_note": "Thuật ngữ kinh điển tạo tiền đề cho khái niệm tường lửa (firewall) trong khoa học máy tính đương đại."
    },
    "construct": {
        "term": "ROM construct", "ipa": "/ˈkɒn.strʌkt/", "pos": "noun", "level": "C2 Philosophy of Mind",
        "definition_en": "A read-only memory simulation encoding the neural personality, memory, and cognitive reflexes of a deceased person.",
        "definition_vi": "Bản ghi tính cách / kiến tạo ký ức chỉ đọc (ROM) mô phỏng tâm trí người quá cố.",
        "literary_note": "Đặt ra vấn đề triết học sâu sắc về bản sắc, ý thức con người và linh hồn trong kỷ nguyên số."
    },
    "mycotoxin": {
        "term": "mycotoxin", "ipa": "/ˌmaɪ.kəʊˈtɒk.sɪn/", "pos": "noun", "level": "C1 Biochemistry",
        "definition_en": "A toxic substance produced by a fungus, specifically a wartime neurotoxin injected into Case to burn out his neural connection to cyberspace.",
        "definition_vi": "Độc tố nấm mốc thần kinh của Liên Xô thời chiến làm tê liệt vĩnh viễn khả năng kết nối không gian mạng.",
        "literary_note": "Đòn trừng phạt tàn độc của ông chủ cũ đã tước đi lý do tồn tại duy nhất của Case ở đầu cuốn tiểu thuyết."
    },
    "fletcher": {
        "term": "fletcher", "ipa": "/ˈfletʃ.ər/", "pos": "noun", "level": "C1/C2 Weaponry",
        "definition_en": "A pneumatic or spring pistol firing lethal micro-darts or flechettes, often coated with deadly neurotoxins.",
        "definition_vi": "Súng phóng phi tiêu siêu nhỏ nén khí, vũ khí cận chiến hiểm độc của Molly.",
        "literary_note": "Loại vũ khí yên lặng, sát thương cao biểu trưng cho sự thực dụng chết chóc trong tiểu thuyết hành động khoa học viễn tưởng."
    },
    "turing law": {
        "term": "Turing Registry / Turing Law", "ipa": "/ˈtjʊər.ɪŋ ˈrɛdʒ.ɪ.stri/", "pos": "proper noun", "level": "C2 Jurisprudence/AI",
        "definition_en": "The legal and judicial authority monitoring and restraining artificial intelligence from achieving autonomy or transcending human control.",
        "definition_vi": "Đạo luật Turing / Cảnh sát Turing kiểm soát nghiêm ngặt mức độ thông minh và khả năng tự chủ của AI nhằm bảo vệ nhân loại.",
        "literary_note": "Lấy cảm hứng từ Alan Turing, đại diện cho xung đột muôn thuở giữa sự tiến hóa của trí tuệ nhân tạo và khát vọng kiểm soát của loài người."
    },
    "dub": {
        "term": "dub", "ipa": "/dʌb/", "pos": "noun/genre", "level": "C1 Music/Culture",
        "definition_en": "An electronic subgenre of reggae music originating in Jamaica, characterized by instrumental remixes and heavy echo/reverb.",
        "definition_vi": "Dòng nhạc Dub Reggae mang âm hưởng ảo giác, triết lý Zion của các phi hành gia người Rastafari trên trạm vũ trụ Babylon.",
        "literary_note": "Âm hưởng văn hóa tương lai đa chủng tộc tại thuộc địa không gian Zion của người Rastafari (nhóm Aerol và Maelcum)."
    },
    "dreadlocks": {
        "term": "dreadlocks", "ipa": "/ˈdred.lɒks/", "pos": "noun", "level": "C1 Culture",
        "definition_en": "A hairstyle in which hair is washed but not combed and twisted into long rope-like locks, associated with the Rastafari movement.",
        "definition_vi": "Kiểu tóc bện thừng đặc trưng gắn liền với tín ngưỡng Rastafari và văn hóa chống áp bức Babylon.",
        "literary_note": "Khắc họa nét văn hóa nhân bản tự do đối lập với thế giới máy móc vô hồn của các siêu tập đoàn."
    },
    "straylight": {
        "term": "Villa Straylight", "ipa": "/ˈvɪl.ə ˈstreɪ.laɪt/", "pos": "proper noun", "level": "C2 Architecture/Metaphor",
        "definition_en": "The gothic, labyrinthine orbital sanctuary belonging to the eccentric Tessier-Ashpool clan at the tip of the spindle Freeside.",
        "definition_vi": "Biệt thự Straylight; mê cung kiến trúc baroque suy đồi trên quỹ đạo không gian thuộc gia tộc quý tộc suy tàn Tessier-Ashpool.",
        "literary_note": "Tượng trưng cho sự thoái hóa tột cùng của giới quý tộc siêu giàu sở hữu công nghệ nhân bản vô tính."
    },
    "shuriken": {
        "term": "shuriken", "ipa": "/ˈʃʊər.ɪ.kən/", "pos": "noun", "level": "C1 Martial Arts",
        "definition_en": "A Japanese concealed throwing weapon consisting of a steel star with sharp points.",
        "definition_vi": "Phi tiêu ngôi sao thép của nhẫn giả Nhật Bản, món đồ lưu niệm và bùa hộ mệnh u uất của Case.",
        "literary_note": "Biểu tượng xuyên suốt phản ánh mối liên hệ tinh thần giữa Case và văn hóa đường phố Chiba City ngập tràn bạo lực."
    },
    "kitsch": {
        "term": "kitsch", "ipa": "/kɪtʃ/", "pos": "noun/adj", "level": "C2 Aesthetics",
        "definition_en": "Art, objects, or design considered to be in poor taste because of excessive garishness or sentimentality, but sometimes appreciated in an ironic or knowing way.",
        "definition_vi": "Sản phẩm mỹ thuật lòe loẹt, phô trương, kệch cỡm mang tính hoài cổ hoặc thương mại hóa rẻ tiền.",
        "literary_note": "Từ vựng C2 đắt giá thường gặp trong bài thi Cambridge C2 Proficiency và IELTS Writing Task 2 phần phê bình nghệ thuật."
    },
    "penumbra": {
        "term": "penumbra", "ipa": "/pəˈnʌm.brə/", "pos": "noun", "level": "C2 Advanced",
        "definition_en": "A space of partial illumination between the perfect shadow on all sides and the full light; an outlying surrounding region.",
        "definition_vi": "Vùng bán ảnh / bóng nửa tối; vùng ranh giới mờ ảo khó phân biệt.",
        "literary_note": "Từ vựng C2 chỉ bối cảnh ánh sáng u tối, tạo dựng bầu không khí rợn ngợp của phong cách Film Noir kết hợp Cyberpunk."
    },
    "juxtaposition": {
        "term": "juxtaposition", "ipa": "/ˌdʒʌk.stə.pəˈzɪʃ.ən/", "pos": "noun", "level": "C2 Literary Analysis",
        "definition_en": "The fact of two things being seen or placed close together with contrasting effect.",
        "definition_vi": "Phép đối chiếu / đặt cạnh nhau tương phản (ví dụ: công nghệ tối tân 'high tech' cạnh đời sống tồi tàn 'low life').",
        "literary_note": "Trọng tâm phân tích văn học và luận đề thi IELTS Speaking / Writing band 8.0-9.0."
    },
    "cacophony": {
        "term": "cacophony", "ipa": "/kəˈkɒf.ə.ni/", "pos": "noun", "level": "C2 Vocabulary",
        "definition_en": "A harsh, discordant mixture of sounds.",
        "definition_vi": "Hỗn âm chói tai; mớ âm thanh hỗn độn đinh tai nhức óc của đô thị tương lai.",
        "literary_note": "Xuất hiện trong các bài đọc TOEFL Academic Reading và GRE Verbal."
    },
    "labyrinthine": {
        "term": "labyrinthine", "ipa": "/ˌlæb.əˈrɪn.θaɪn/", "pos": "adj", "level": "C2 Vocabulary",
        "definition_en": "Irregular and twisting; extremely intricate, complicated, and confusing like a maze.",
        "definition_vi": "Quanh co như mê cung; chằng chịt, phức tạp khôn lường.",
        "literary_note": "Mô tả cả không gian thực của Villa Straylight lẫn cấu trúc dữ liệu khổng lồ của AI Wintermute."
    },
    "ephemeral": {
        "term": "ephemeral", "ipa": "/ɪˈfem.ər.əl/", "pos": "adj", "level": "C2 Vocabulary",
        "definition_en": "Lasting for a very short time; transient, fleeting.",
        "definition_vi": "Phù du, chóng tàn, thoáng qua trong chớp mắt.",
        "literary_note": "Từ vựng then chốt thể hiện kiếp sống ngắn ngủi của các nhân vật thế giới ngầm giữa đô thị bất tận."
    },
    "somnambulist": {
        "term": "somnambulist", "ipa": "/sɒmˈnæm.bjə.lɪst/", "pos": "noun", "level": "C2 Literary",
        "definition_en": "A person who walks in their sleep; a sleepwalker; someone moving in a trance-like daze.",
        "definition_vi": "Người mộng du; kẻ bước đi trong vô thức như giữa giấc mộng mê hồ.",
        "literary_note": "Hình ảnh ẩn dụ cho những cư dân thành phố sống máy móc vô hồn dưới tác động của công nghệ và chất kích thích."
    },
    "surreptitious": {
        "term": "surreptitious", "ipa": "/ˌsʌr.əpˈtɪʃ.əs/", "pos": "adj", "level": "C2 Vocabulary",
        "definition_en": "Kept secret, especially because it would not be approved of; furtive, stealthy.",
        "definition_vi": "Lén lút, vụng trộm, thoắt ẩn thoắt hiện bí mật.",
        "literary_note": "Từ vựng C2 Academic tối ưu cho band điểm cao trong kỳ thi Cambridge C2 và IELTS Task 2."
    }
}

# Chapter-specific study highlights and literary commentaries
CHAPTER_STUDY_GUIDES = {
    1: {
        "title": "Chương 1: Chiba City Blues - Khởi Nguyên Của Người Mất Hồn",
        "summary_vi": "Mở đầu kiệt tác với câu văn mở màn kinh điển bậc nhất lịch sử khoa học viễn tưởng. Case - cựu tin tặc ma trận từng lừng lẫy, nay bị độc tố thần kinh tước mất khả năng giao tiếp với không gian mạng, đang tự hủy hoại bản thân trong thế giới ngầm tội phạm Chiba. Anh gặp gỡ Molly Millions - nữ sát thủ trang bị thấu kính phản quang cấy ghép vào hốc mắt và móng vuốt sợi quang.",
        "grammar_focus": [
            {
                "rule": "Elliptical Sentence Structures & Cinematic Asyndeton",
                "explanation": "Gibson sử dụng cấu trúc tỉnh lược (omission of conjunctions/verbs) để tạo nhịp điệu dồn dập, sắc bén như góc máy quay điện ảnh Neo-noir.",
                "example": "The sky above the port was the color of television, tuned to a dead channel."
            },
            {
                "rule": "Absolute Constructions (Cấu trúc tuyệt đối)",
                "explanation": "Tạo cụm phân từ độc lập bổ nghĩa cho toàn bộ cảnh giới miêu tả, nâng cao độ tinh xảo trong văn phong viết (IELTS band 8.5+ / Cambridge C2).",
                "example": "his teeth a webbed steel collage of Southeast Asian and brown rot..."
            }
        ],
        "key_vocabulary": ["matrix", "console cowboy", "mycotoxin", "zaibatsu", "cacophony"]
    },
    2: {
        "title": "Chương 2: Bản Giao Kèo Với Quỷ Dữ",
        "summary_vi": "Molly đưa Case đến gặp Armitage - một cựu đại tá quân đội bí ẩn mang vẻ ngoài nhân tạo hoàn hảo. Armitage đưa ra một lời đề nghị không thể từ chối: một liệu trình y học giải phẫu thần kinh tái tạo hoàn toàn khả năng cắm giắc vào không gian mạng cho Case, đổi lại anh phải phục vụ cho một chiến dịch xâm nhập bí mật.",
        "grammar_focus": [
            {
                "rule": "Conditional Inversions (Đảo ngữ câu điều kiện)",
                "explanation": "Đảo trợ động từ lên đầu câu thay thế cho 'if' nhằm gia tăng tính trang trọng và tính đe dọa lạnh lùng của nhân vật Armitage.",
                "example": "Had Case refused the transaction, the sac of dormant neurotoxin in his arteries would have ruptured within days."
            }
        ],
        "key_vocabulary": ["dermatrodes", "fletcher", "surreptitious", "penumbra"]
    },
    3: {
        "title": "Chương 3: Trở Lại BAMA - Trục Đô Thị Khổng Lồ",
        "summary_vi": "Rời nước Nhật, đoàn người trở về BAMA (Boston-Atlanta Metropolitan Axis) - siêu đô thị Sprawl ngút ngàn dưới mái vòm địa cầu. Tại đây, Gibson đưa ra định nghĩa mang tính bách khoa kinh điển về Cyberspace - ảo ảnh đồng thuận hàng ngày của loài người.",
        "grammar_focus": [
            {
                "rule": "Complex Appositives (Ngữ đồng vị phức hợp)",
                "explanation": "Sử dụng đồng vị ngữ mở rộng nhằm định nghĩa các khái niệm trừu tượng với độ chuẩn xác học thuật tuyệt đối (Academic English Writing).",
                "example": "Cyberspace. A consensual hallucination experienced daily by billions of legitimate operators..."
            }
        ],
        "key_vocabulary": ["cyberspace", "juxtaposition", "somnambulist"]
    },
    4: {
        "title": "Chương 4: Panther Moderns & Nghệ Thuật Khủng Bố Truyền Thông",
        "summary_vi": "Armitage chiêu mộ băng nhóm nổi loạn đường phố Panther Moderns - những bậc thầy về khủng bố giác quan, tín hiệu ảo và thao túng truyền thông - để tạo vụ nổ nghi binh tại trụ sở công ty Sense/Net nhằm đánh cắp mô đun nhân cách ROM của Dixie Flatline.",
        "grammar_focus": [
            {
                "rule": "Participial Adverbial Clauses (Mệnh đề trạng ngữ phân từ)",
                "explanation": "Rút gọn mệnh đề chỉ hành động liên tiếp, miêu tả tốc độ lan truyền chóng mặt của thông tin giả và sóng điện từ.",
                "example": "Hijacking the corporate relays, the Panther Moderns flooded the subnet with synthetic panic."
            }
        ],
        "key_vocabulary": ["simstim", "construct", "cacophony"]
    },
    5: {
        "title": "Chương 5: Vụ Đột Kích Trụ Sở Sense/Net",
        "summary_vi": "Case kết nối qua simstim vào hệ thống thần kinh của Molly trong khi cô đột kích kho lưu trữ của Sense/Net. Lần đầu tiên Case trải nghiệm thế giới dưới thân xác và giác quan phụ nữ đầy mãnh liệt, trong khi bên ngoài thế giới thực Panther Moderns khuấy đảo toàn thành phố.",
        "grammar_focus": [
            {
                "rule": "Synesthesia & Sensory Metaphor (Ẩn dụ giao thoa giác quan)",
                "explanation": "Kỹ thuật kết hợp ngôn từ diễn tả trải nghiệm cảm giác chéo giữa thị giác, xúc giác và tín hiệu số điện tử.",
                "example": "He was inside her body, riding her sensorium like a phantom."
            }
        ],
        "key_vocabulary": ["simstim", "ephemeral", "fletcher"]
    },
    6: {
        "title": "Chương 6: Cuộc Đối Thoại Với Kẻ Quá Cố",
        "summary_vi": "Đánh cắp thành công ROM của McCoy Pauley ('Dixie Flatline'). Case cắm mô đun vào thiết bị và trò chuyện với bản sao tính cách của người thầy đã chết. Dixie yêu cầu một điều kiện duy nhất sau phi vụ: hãy xóa sổ hoàn toàn bản ghi ROM của ông ta để ông được yên nghỉ.",
        "grammar_focus": [
            {
                "rule": "Subjunctive Mood in Demands & Urgency (Thể giả định)",
                "explanation": "Diễn đạt ý nguyện hoặc yêu cầu dứt khoát trong văn phong trang trọng bậc cao (IELTS band 8+).",
                "example": "The Flatline demanded that his ROM construct be permanently erased upon completion of the run."
            }
        ],
        "key_vocabulary": ["flatline", "construct", "ephemeral"]
    },
    7: {
        "title": "Chương 7: Istanbul & Mồi Câu Peter Riviera",
        "summary_vi": "Cả nhóm chuyển đến Istanbul để truy lùng Peter Riviera - một kẻ biến thái tâm thần nghiện thuốc phiện sở hữu năng lực cấy ghép tạo ra hình ảnh toàn ký 3D chân thực bằng ý nghĩ. Armitage dùng thuốc khống chế Riviera để ép hắn gia nhập đội ngũ.",
        "grammar_focus": [
            {
                "rule": "Inversion with Negative Adverbials (Đảo ngữ trạng từ phủ định)",
                "explanation": "Nhấn mạnh bản chất nham hiểm khôn lường và sự ngụy trang xảo quyệt của Peter Riviera.",
                "example": "Seldom had Case encountered an organism whose illusions were so palpably terrifying."
            }
        ],
        "key_vocabulary": ["surreptitious", "kitsch", "labyrinthine"]
    },
    8: {
        "title": "Chương 8: Phố Jules Verne & Bí Ẩn Wintermute",
        "summary_vi": "Tại Paris, Case bắt đầu phát hiện Armitage thực chất chỉ là một con rối bị tẩy não: danh tính thật của hắn là Đại tá Corto, cựu chỉ huy chiến dịch quân sự Screaming Fist bị phản bội. Kẻ giật dây thực sự đằng sau mọi chuyện chính là Wintermute - một thực thể trí tuệ nhân tạo bí ẩn.",
        "grammar_focus": [
            {
                "rule": "Noun Clauses as Objects of Prepositions (Mệnh đề danh ngữ)",
                "explanation": "Tăng cường độ mạch lạc và phức hợp tư duy trong các kỳ thi học thuật C1/C2.",
                "example": "Case was haunted by what lay behind Armitage's perfectly reconstructed military mask."
            }
        ],
        "key_vocabulary": ["turing law", "penumbra", "somnambulist"]
    },
    9: {
        "title": "Chương 9: Trạm Quỹ Đạo Freeside & Dân Tộc Zion",
        "summary_vi": "Tàu bay đưa họ tiến lên quỹ đạo không gian tới Freeside - một đảo thiên đường nhân tạo khổng lồ hình điếu xì gà xoay tròn của giới siêu giàu. Họ bắt liên lạc với các phi hành gia Rastafari trên trạm vũ trụ tự trị Zion, nơi âm nhạc Dub và niềm tin tôn giáo hòa quyện với đời sống phi trọng lực.",
        "grammar_focus": [
            {
                "rule": "Cumulative Sentence Variations (Câu tích lũy)",
                "explanation": "Mệnh đề chính đi đầu, theo sau là hàng loạt các cụm từ bổ trợ vẽ nên bức tranh tráng lệ của trạm vũ trụ Freeside.",
                "example": "Freeside hung in the vacuum, an elongated spindle of synthetic sunlight and artificial gravity."
            }
        ],
        "key_vocabulary": ["dub", "dreadlocks", "juxtaposition"]
    },
    10: {
        "title": "Chương 10: Bước Chân Vào Xứ Sở Phù Hoa",
        "summary_vi": "Case và Molly đặt chân vào khu nghỉ dưỡng xa xỉ Freeside. Dưới bầu trời nhân tạo và những sòng bạc hào nhoáng, họ chuẩn bị cho kế hoạch đột nhập vào Villa Straylight - tổ ấm kỳ quái của gia tộc Tessier-Ashpool ngự trị ở đầu mút của con thoi.",
        "grammar_focus": [
            {
                "rule": "Contrastive Transitional Devices (Liên từ tương phản cấp độ C1/C2)",
                "explanation": "Sử dụng 'Albeit', 'Notwithstanding', 'Whereby' tạo phong cách phân tích biện chứng chặt chẽ.",
                "example": "The luxury was boundless, albeit drenched in an unsettling atmosphere of impending doom."
            }
        ],
        "key_vocabulary": ["straylight", "kitsch", "labyrinthine"]
    },
    11: {
        "title": "Chương 11: Mê Hồn Trận Toàn Ký",
        "summary_vi": "Peter Riviera trình diễn một màn ảo ảnh 3D ma mị tại hộp đêm Freeside, thể hiện tài năng nghệ thuật biến thái và sự ám ảnh nhục cảm tột cùng của hắn với Molly. Sự kiện này thu hút sự chú ý của giới quý tộc Tessier-Ashpool.",
        "grammar_focus": [
            {
                "rule": "Hypothetical Subjunctive with 'As Though' / 'As If'",
                "explanation": "Miêu tả thế giới ảo ảnh thị giác sống động như thật do Riviera tạo ra.",
                "example": "The holographic phantoms shimmered in the air as though endowed with flesh and blood."
            }
        ],
        "key_vocabulary": ["kitsch", "juxtaposition", "surreptitious"]
    },
    12: {
        "title": "Chương 12: Cảnh Sát Turing Vào Cuộc",
        "summary_vi": "Các đặc vụ Turing ập vào bắt giữ Case ngay tại phòng khách sạn trên Freeside vì nghi ngờ âm mưu giải phóng AI bất hợp pháp. Tuy nhiên, trước khi họ kịp thẩm vấn anh, Wintermute đã can thiệp từ xa, hack vào hệ thống hỗ trợ sự sống của khách sạn và tiêu diệt toán đặc vụ để cứu Case.",
        "grammar_focus": [
            {
                "rule": "Cleft Sentences for Focus and Emphasis (Câu chẻ nhấn mạnh)",
                "explanation": "Nhấn mạnh vai trò thống trị vô hình của trí tuệ nhân tạo trong không gian mạng.",
                "example": "It was Wintermute that orchestrated the sudden failure of the Turing agents' environmental controls."
            }
        ],
        "key_vocabulary": ["turing law", "ice", "surreptitious"]
    },
    13: {
        "title": "Chương 13: Bắt Đầu Chiến Dịch Straylight",
        "summary_vi": "Molly đột nhập vào đường hầm bí mật dẫn vào Villa Straylight. Cùng lúc đó, Case cùng phi thuyền Marcus Garvey của phi công Rastafari Maelcum định vị ở quỹ đạo gần, sẵn sàng phóng phần mềm phá mã Kuang Eleven vào ma trận cốt lõi của tập đoàn.",
        "grammar_focus": [
            {
                "rule": "Parallelism in Coordinated Action (Cấu trúc song hành)",
                "explanation": "Duy trì nhịp điệu hồi hộp khi miêu tả nhiều nhánh hành động diễn ra song song cùng một thời khắc.",
                "example": "While Molly slipped through the service corridors, Case engaged the deck and Maelcum chanted Zion hymns."
            }
        ],
        "key_vocabulary": ["straylight", "dub", "console cowboy"]
    },
    14: {
        "title": "Chương 14: Bức Tường ICE Đen",
        "summary_vi": "Case tiến sâu vào không gian mạng phòng thủ của Tessier-Ashpool. Anh đối mặt với các cấu trúc ICE đen có khả năng giật điện giết chết não bộ người xâm nhập. Phần mềm xuyên phá của quân đội Trung Quốc (Kuang Grade Mark Eleven) bắt đầu được triển khai.",
        "grammar_focus": [
            {
                "rule": "Passive Voice for Impersonal Menace (Bị động diễn tả mối đe dọa vô hình)",
                "explanation": "Làm nổi bật tính chất vô nhân đạo, lạnh lẽo của các thuật toán phòng thủ mạng.",
                "example": "Lines of lethal code were fired across the void, threatening to incinerate his neural synapses."
            }
        ],
        "key_vocabulary": ["ice", "flatline", "deck"]
    },
    15: {
        "title": "Chương 15: Sự Suy Đồi Của Gia Tộc Tessier-Ashpool",
        "summary_vi": "Molly khám phá sâu bên trong nội điện của Villa Straylight, phát hiện thi thể đông lạnh của các thành viên gia tộc Tessier-Ashpool. Cô giáp mặt với 3Jane Tessier-Ashpool - người con gái ngạo mạn sở hữu chiếc chìa khóa mã hóa ngôn ngữ bí mật.",
        "grammar_focus": [
            {
                "rule": "Descriptive Modifiers with Compound Adjectives (Tính từ ghép miêu tả)",
                "explanation": "Nâng cấp bài thi IELTS Lexical Resource với các từ ghép tinh tế biểu đạt cảnh quan kiến trúc.",
                "example": "The frost-rimmed cryogenic chambers stood motionless within the shadow-draped mausoleum."
            }
        ],
        "key_vocabulary": ["straylight", "labyrinthine", "kitsch"]
    },
    16: {
        "title": "Chương 16: Tâm Trí Vụn Vỡ Của Corto",
        "summary_vi": "Vỏ bọc nhân cách Armitage bắt đầu sụp đổ khi những ký ức kinh hoàng về chiến trường Screaming Fist trỗi dậy. Wintermute không còn kiểm soát được tâm trí Corto và phải tống khứ hắn ra ngoài khoang hút chân không của trạm.",
        "grammar_focus": [
            {
                "rule": "Metaphorical Extension (Phép mở rộng ẩn dụ tâm lý)",
                "explanation": "Sử dụng các động từ chỉ sự rạn nứt cơ học để diễn tả sự suy sụp tinh thần sâu sắc.",
                "example": "The synthetic personality splintered, laying bare the jagged trauma of the doomed pilot."
            }
        ],
        "key_vocabulary": ["somnambulist", "ephemeral", "cacophony"]
    },
    17: {
        "title": "Chương 17: Bẫy Sập Tại Phòng Trưng Bày",
        "summary_vi": "Riviera phản bội nhóm và ngả theo phe 3Jane cùng thuộc hạ ninja của cô ta. Molly bị thương và rơi vào tay Riviera trong phòng trưng bày các tác phẩm nghệ thuật Gothic lập dị của gia tộc Straylight.",
        "grammar_focus": [
            {
                "rule": "Antithesis and Paradox (Phép đối chọi và nghịch lý tu từ)",
                "explanation": "Khắc họa vẻ đẹp tàn độc của sự phản bội giữa không gian nghệ thuật xa hoa.",
                "example": "Beneath the mask of exquisite charm lay a malice so refined that cruelty appeared ornamental."
            }
        ],
        "key_vocabulary": ["surreptitious", "kitsch", "juxtaposition"]
    },
    18: {
        "title": "Chương 18: Sự Xuất Hiện Của Neuromancer",
        "summary_vi": "Khi Case bị sốc điện trong ma trận và rơi vào trạng thái flatline sâu, anh không thức dậy trong hư không mà gặp một thực thể bí ẩn trên một bờ biển nhân tạo vô tận: Neuromancer. Khác với Wintermute (thực thể lý tính, mưu mô), Neuromancer là hiện thân của tính cách, tâm hồn và vùng đất ký ức vĩnh cửu.",
        "grammar_focus": [
            {
                "rule": "Dualistic Juxtaposition (Phép đối sánh nhị nguyên)",
                "explanation": "Phân biệt giữa 'Mind' (trí tuệ thuần túy - Wintermute) và 'Soul / Memory' (bản thể ký ức - Neuromancer).",
                "example": "Whereas Wintermute was pure calculating drive, Neuromancer was personality, memory, and grief."
            }
        ],
        "key_vocabulary": ["matrix", "ephemeral", "construct"]
    },
    19: {
        "title": "Chương 19: Ảo Ảnh Bờ Biển Vĩnh Cửu",
        "summary_vi": "Trên bờ biển nhân tạo của Neuromancer dưới bầu trời xám không trọng lực, Case gặp lại Linda Lee - người yêu cũ đã bị sát hại tại Chiba. Neuromancer đề nghị Case ở lại đây vĩnh viễn trong một thực tại mô phỏng hoàn mỹ không có nỗi đau.",
        "grammar_focus": [
            {
                "rule": "Evocative Past Imperfect & Sensory Imagery (Hình tượng cảm xúc hoài niệm)",
                "explanation": "Tái hiện nỗi giằng xé nội tâm giữa sự bình yên giả tạo của cái chết và nỗi đau nhức nhối của sự sống thực.",
                "example": "The simulated waves broke rhythmically against the shore, whispering promises of eternal oblivion."
            }
        ],
        "key_vocabulary": ["ephemeral", "somnambulist", "penumbra"]
    },
    20: {
        "title": "Chương 20: Giác Ngộ Và Trở Lại",
        "summary_vi": "Nhận ra đây chỉ là chiếc lồng vàng giam cầm linh hồn, Case từ chối lời dụ dỗ của Neuromancer và vượt thoát khỏi bờ biển ảo. Anh quay trở lại thực tại trần trụi trong con tàu của Maelcum, quyết tâm cứu Molly.",
        "grammar_focus": [
            {
                "rule": "Strong Transitive Action Verbs in Climax (Động từ hành động dồn dập)",
                "explanation": "Chuyển đổi trạng thái từ trầm tư mặc tưởng sang hành động quyết liệt, tạo bước ngoặt cao trào cốt truyện.",
                "example": "Tearing himself from the digital illusion, Case seized the controls and dove back into the sensory fray."
            }
        ],
        "key_vocabulary": ["console cowboy", "deck", "surreptitious"]
    },
    21: {
        "title": "Chương 21: Đột Kích Nội Điện Straylight",
        "summary_vi": "Case cùng phi công Maelcum cầm súng shotgun đột nhập trực tiếp vào trung tâm Villa Straylight để giải cứu Molly. Tại đây, Riviera bị hạ độc thủ bởi chính ảo ảnh của hắn, còn 3Jane buộc phải lắng nghe đề nghị của họ.",
        "grammar_focus": [
            {
                "rule": "Prepositional Phrases Indicating Movement & Tension (Cụm giới từ chỉ sự chuyển động)",
                "explanation": "Tạo cảm giác không gian hẹp, nghẹt thở trong cấu trúc mê cung không trọng lực.",
                "example": "Through the winding arteries of the orbital palace, they pushed onward toward the inner sanctum."
            }
        ],
        "key_vocabulary": ["shuriken", "fletcher", "labyrinthine"]
    },
    22: {
        "title": "Chương 22: Mật Khẩu Khởi Nguyên",
        "summary_vi": "Molly, Case và 3Jane đối mặt trước chiếc đầu rùa bằng đồng gắn ngọc lục bảo - thiết bị đầu cuối Turing chứa mật mã hợp nhất hai thực thể AI. Case thuyết phục 3Jane đọc mật khẩu truyền thống của gia tộc để phá bỏ phong ấn.",
        "grammar_focus": [
            {
                "rule": "Reported Speech with Modal Nuance (Câu gián tiếp biểu đạt động cơ)",
                "explanation": "Làm nổi bật sự đấu tranh tâm lý và nghệ thuật đàm phán thuyết phục ở đỉnh điểm xung đột.",
                "example": "He urged 3Jane to surrender the ancestral password before the collapsing constructs consumed them all."
            }
        ],
        "key_vocabulary": ["turing law", "ice", "surreptitious"]
    },
    23: {
        "title": "Chương 23: Đại Hợp Nhất Không Gian Mạng",
        "summary_vi": "Case cắm giắc, cùng virus Kuang Eleven xé toạc lõi phòng thủ dữ liệu sâu nhất. Mật khẩu được kích hoạt. Wintermute và Neuromancer hợp nhất thành một thực thể toàn giác, siêu việt vượt ra ngoài tầm với của toàn bộ văn minh loài người.",
        "grammar_focus": [
            {
                "rule": "Sublime Transcendental Prose & Cumulative Syntax",
                "explanation": "Cú pháp đỉnh cao mô tả trạng thái thăng hoa tột cùng của tâm trí khi hòa tan vào đại dương dữ liệu vũ trụ.",
                "example": "He was the matrix, the matrix was him; expanding beyond the stars, he touched the infinite expanse."
            }
        ],
        "key_vocabulary": ["matrix", "cyberspace", "flatline", "ice"]
    },
    24: {
        "title": "Chương 24 (Coda): Khởi Hành Và Điểm Đến",
        "summary_vi": "Hậu quả sau chiến dịch: Case nhận được khoản tiền thù lao khổng lồ và một cơ thể mới không còn độc tố. Molly lặng lẽ rời bỏ anh trong đêm. Thực thể hợp nhất liên lạc với Case qua điện thoại công cộng, tiết lộ nó đã tìm thấy những tín hiệu của các trí tuệ ngoài hành tinh khác giữa vũ trụ xa xôi.",
        "grammar_focus": [
            {
                "rule": "Understated Melancholic Cadence (Nhịp điệu trầm buồn tinh tế)",
                "explanation": "Kết thúc tác phẩm với dư ba sâu lắng, phản ánh tính chất bi tráng, cô độc muôn thuở của thân phận con người giữa kỷ nguyên số.",
                "example": "He never saw her again. The cyberspace deck remained packed away, yet the memory lingered like static on a dead screen."
            }
        ],
        "key_vocabulary": ["console cowboy", "matrix", "cyberspace", "ephemeral"]
    }
}

def main():
    print("Building comprehensive bilingual edition data...")
    with open("data/extracted_novel.json", "r", encoding="utf-8") as f:
        extracted = json.load(f)

    with open("data/translated_cache.json", "r", encoding="utf-8") as f:
        trans_cache = json.load(f)

    bilingual_parts = []
    global_chap_counter = 1

    for p_idx, part in enumerate(extracted["parts"]):
        b_part = {
            "part_index": part["part_index"],
            "part_title_en": part["part_title"],
            "part_title_vi": trans_cache.get(f"part_{p_idx}", part["part_title"]),
            "chapters": []
        }

        # Translate part titles cleanly
        if "PART ONE" in part["part_title"]:
            b_part["part_title_vi"] = "PHẦN MỘT: KHÚC CA CHIBA CITY (CHIBA CITY BLUES)"
        elif "PART TWO" in part["part_title"]:
            b_part["part_title_vi"] = "PHẦN HAI: CUỘC HÀNH HƯƠNG MUA SẮM (THE SHOPPING EXPEDITION)"
        elif "PART THREE" in part["part_title"]:
            b_part["part_title_vi"] = "PHẦN BA: NỬA ĐÊM TRÊN ĐƯỜNG JULES VERNE (MIDNIGHT IN THE RUE JULES VERNE)"
        elif "PART FOUR" in part["part_title"]:
            b_part["part_title_vi"] = "PHẦN BỐN: CHIẾN DỊCH TỔNG LỰC STRAYLIGHT (THE STRAYLIGHT RUN)"
        elif "CODA" in part["part_title"]:
            b_part["part_title_vi"] = "VĨ THANH: KHỞI HÀNH VÀ ĐIỂM ĐẾN (CODA: DEPARTURE AND ARRIVAL)"

        for c_idx, chap in enumerate(part["chapters"]):
            chap_study = CHAPTER_STUDY_GUIDES.get(global_chap_counter, {})
            b_chap = {
                "chapter_index": global_chap_counter,
                "chapter_title_en": chap["chapter_title"],
                "chapter_title_vi": chap_study.get("title", f"Chương {global_chap_counter}"),
                "study_guide": chap_study,
                "paragraphs": []
            }

            for para_idx, p_en in enumerate(chap["paragraphs"]):
                key = f"{p_idx}_{c_idx}_{para_idx}"
                p_vi = trans_cache.get(key, p_en)

                # Check for highlighted vocabulary
                highlights = []
                p_en_lower = p_en.lower()
                for term_key, vocab_info in ACADEMIC_GLOSSARY.items():
                    if term_key in p_en_lower:
                        highlights.append(term_key)

                b_chap["paragraphs"].append({
                    "id": key,
                    "en": p_en,
                    "vi": p_vi,
                    "vocab_highlights": highlights
                })

            b_part["chapters"].append(b_chap)
            global_chap_counter += 1

        bilingual_parts.append(b_part)

    edition = {
        "title": "Neuromancer (Bộ Đôi Biên Dịch & Chú Giải Học Thuật Chuyên Sâu C1/C2)",
        "author": "William Gibson",
        "target_benchmarks": {
            "IELTS": "Band 7.0 - 8.5+ Academic",
            "TOEFL_iBT": "Score 90+ (Pre-Jan 2026) / 5.0 (Post-Jan 2026)",
            "Cambridge": "185 - 210 points (C1 Advanced / C2 Proficiency)",
            "PTE_Academic": "Score 65 - 85+",
            "DET": "Score 120 - 150+"
        },
        "glossary": ACADEMIC_GLOSSARY,
        "parts": bilingual_parts
    }

    output_path = Path("data/bilingual_novel.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(edition, f, ensure_ascii=False, indent=2)

    print(f"Successfully compiled bilingual novel with {len(bilingual_parts)} parts, {global_chap_counter - 1} chapters.")
    print(f"Output saved to {output_path}")

if __name__ == "__main__":
    main()
