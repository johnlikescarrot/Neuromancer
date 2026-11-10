/**
 * Twenty-four chapter guides. Original synopsis, analysis and language notes;
 * no text from the novel is reproduced.
 */
import type { ChapterGuide } from "../types.js";

const P1 = "Part One · Chiba City Blues";
const P2 = "Part Two · The Shopping Expedition";
const P3 = "Part Three · Midnight in the Rue Jules Verne";
const P4 = "Part Four · The Straylight Run";
const P5 = "Coda · Departure and Arrival";

export const chapters: ChapterGuide[] = [
  {
    part: P1,
    num: 1,
    title: "The Chatsubo",
    titleVi: "Quán Chatsubo",
    synopsisEn:
      "Case is twenty-four, broke, and living in a coffin hotel in Chiba City. He was once one of the best console cowboys in the Sprawl; a former employer punished him for stealing by destroying the part of his nervous system that let him enter the matrix, and left him the rest. Now he drinks in the Chatsubo and sells what is left of his expertise to people who cannot check it. The chapter is a portrait of a man doing time in his own body, and it ends with a woman carrying implanted blades making him an offer he cannot read.",
    synopsisVi:
      "Case hai mươi tư tuổi, sạch tiền, sống trong một khách sạn quan tài ở Chiba City. Từng là một trong những cao bồi bàn phím giỏi nhất ở Sprawl, anh bị ông chủ cũ trừng phạt vì tội ăn cắp bằng cách phá hủy đúng phần hệ thần kinh cho phép anh bước vào ma trận, rồi để lại phần còn lại. Giờ anh ngồi quán Chatsubo, bán chút hiểu biết còn sót cho những kẻ không thể kiểm chứng. Chương này là chân dung một người đang thụ án trong chính thân thể mình, và nó khép lại bằng một người phụ nữ mang lưỡi dao cấy trong tay, đưa ra một lời đề nghị mà anh không đọc được.",
    watchEn: [
      "The body is described as rented property throughout: a coffin, a rented room, a nervous system somebody else holds the lease on.",
      "Notice how quickly the chapter establishes Case's competence. He is broken, but the prose never lets him look stupid.",
      "The Chatsubo is a listening post. Information arrives as gossip, and gossip is the only currency he still has.",
    ],
    watchVi: [
      "Thân thể được miêu tả như tài sản đi thuê suốt chương: quan tài, căn phòng thuê, một hệ thần kinh mà người khác giữ hợp đồng.",
      "Hãy để ý chương này xác lập năng lực của Case nhanh đến mức nào. Anh ta tàn phế, nhưng văn phong không bao giờ để anh ta trông ngớ ngẩn.",
      "Quán Chatsubo là một trạm nghe ngóng. Thông tin đến dưới dạng chuyện phiếm, và chuyện phiếm là thứ tiền tệ duy nhất anh còn.",
    ],
    focus: [
      {
        label: "Noun stacking: information without grammar",
        en: "Gibson builds most of his exposition out of noun phrases rather than clauses. Where a lesser writer would write *the bar was crowded with people who had come from the port*, he gives you a stack of nouns and lets you assemble the relation. The effect is speed plus a mild vertigo: the reader is doing syntax the prose refuses to do.",
        vi: "Gibson dựng phần lớn thông tin nền bằng cụm danh từ chứ không bằng mệnh đề. Nơi một cây bút kém hơn sẽ viết *quán bar đông người từ cảng tới*, ông đưa ra một chồng danh từ và để bạn tự lắp quan hệ. Hiệu quả là tốc độ cộng một chút chóng mặt: người đọc đang làm cú pháp thay cho văn bản.",
        example:
          "Constructed parallel: *Coffin hotel, fluorescent light, the smell of wet wool and cheap antibiotic.*",
      },
      {
        label: "Present tense and the absence of memory",
        en: "Everything in the chapter is grammatically now, including the past. Damage, once inflicted, is described as a current condition rather than an event. This makes Case's history feel like weather: permanent, unarguable, and not something a person can appeal.",
        vi: "Mọi thứ trong chương đều ở hiện tại về mặt ngữ pháp, kể cả quá khứ. Tổn thương, một khi đã gây ra, được miêu tả như tình trạng hiện thời chứ không phải biến cố. Điều này khiến quá khứ của Case giống như thời tiết: vĩnh viễn, không thể cãi, và không phải thứ con người có thể kháng nghị.",
      },
    ],
    terms: ["console cowboy", "deck", "matrix", "coffin hotel", "fletcher"],
  },
  {
    part: P1,
    num: 2,
    title: "The Man in the Hilton Suite",
    titleVi: "Người đàn ông trong căn hộ Hilton",
    synopsisEn:
      "A suite on the twenty-fifth floor of the Chiba Hilton, paid for by someone Case has never met. The offer is exact and insulting in its generosity: repair the nerve damage, restore access to the matrix, supply new hardware — in exchange for work that will not be described until it begins. Case accepts, because the alternative is the coffin. The chapter ends with Molly cleaning blood off her hands, and with the first evidence that their employer is willing to kill in order to protect his investment.",
    synopsisVi:
      "Một căn hộ trên tầng hai mươi lăm của khách sạn Chiba Hilton, do một người Case chưa từng gặp trả tiền. Lời đề nghị chính xác và xúc phạm ở chỗ quá hào phóng: sửa lại dây thần kinh, phục hồi quyền vào ma trận, cấp thiết bị mới — để đổi lấy công việc sẽ không được mô tả cho tới khi nó bắt đầu. Case nhận, vì lựa chọn còn lại là chiếc quan tài. Chương khép lại bằng cảnh Molly lau máu trên tay, và bằng chứng cứ đầu tiên cho thấy người thuê sẵn sàng giết để bảo vệ khoản đầu tư của mình.",
    watchEn: [
      "The surgery is described in commercial language — invoice, parts, warranty — not medical language. That is the chapter's whole thesis.",
      "Case is given back his gift and immediately loses his freedom. Track the exchange rate: what he pays for what he gets.",
      "Molly does the violence and Case does the wanting. The division of labour between them is set here, and it never really changes.",
    ],
    watchVi: [
      "Cuộc phẫu thuật được miêu tả bằng ngôn ngữ thương mại — hóa đơn, linh kiện, bảo hành — chứ không phải ngôn ngữ y khoa. Đó là toàn bộ luận điểm của chương.",
      "Case được trả lại món quà và ngay lập tức mất tự do. Hãy theo dõi tỷ giá: anh trả gì để đổi lấy gì.",
      "Molly làm bạo lực, Case làm khao khát. Sự phân công ấy được thiết lập ở đây và gần như không bao giờ thay đổi.",
    ],
    focus: [
      {
        label: "The passive as a way of hiding a subject",
        en: "In this chapter the crucial agent is routinely deleted. Things *get* repaired, arrangements *are* made, a room *has been* paid for. The passive lets Gibson keep the employer offstage while the reader feels his hand everywhere. When an exam asks why a passive is used, this is the answer it wants: not style for its own sake, but the management of blame.",
        vi: "Trong chương này, chủ thể quan trọng thường bị xóa. Đồ đạc *được* sửa, thỏa thuận *được* lập, căn phòng *đã được* trả tiền. Thể bị động cho phép Gibson giữ ông chủ ngoài sân khấu trong khi người đọc vẫn cảm thấy bàn tay ông ta ở khắp nơi. Khi đề thi hỏi vì sao dùng bị động, đây là câu trả lời nó muốn: không phải phong cách vô cớ, mà là cách quản lý trách nhiệm.",
        example: "Constructed parallel: *The damage had been done at night, by people who did not need to explain themselves.*",
      },
      {
        label: "Diagnosis as characterisation",
        en: "Medical and technical register is used to define people. Case is a list of what is wrong with him; Molly is a list of what has been added. The technique is worth stealing for exams: a physical specification can do the work of three paragraphs of description.",
        vi: "Ngôn ngữ y khoa và kỹ thuật được dùng để định nghĩa con người. Case là một danh sách những gì hỏng ở anh; Molly là danh sách những gì được thêm vào. Kỹ thuật này đáng học cho thi cử: một bản đặc tả thể chất có thể làm thay công việc của ba đoạn miêu tả.",
      },
    ],
    terms: ["mycotoxin", "simstim", "dermatrode", "black clinic", "construct"],
  },
  {
    part: P2,
    num: 3,
    title: "Home, Which Is Not a Home",
    titleVi: "Nhà, mà không phải nhà",
    synopsisEn:
      "Case returns to the Sprawl, the Boston–Atlanta conurbation he grew up in and was exiled from, and the prose treats his homecoming as an arrival in a machine. The team assembles around him: Molly, already fitted with new hardware; Armitage, the employer, whose calm is a kind of symptom. Case is fitted with a device that lets him switch between the matrix and Molly's sensorium, which means he can be inside her body while she works. It is presented as a tool. It is also the novel's central metaphor for intimacy under contract.",
    synopsisVi:
      "Case trở về Sprawl, vùng đô thị Boston–Atlanta nơi anh lớn lên và từng bị trục xuất, và văn phong coi cuộc hồi hương ấy như một lần bước vào guồng máy. Đội ngũ tập hợp quanh anh: Molly, đã được gắn thiết bị mới; Armitage, người thuê, với vẻ điềm tĩnh tựa một triệu chứng. Case được gắn một thiết bị cho phép chuyển giữa ma trận và giác quan của Molly, nghĩa là anh có thể ở trong thân thể cô ấy trong lúc cô ấy làm việc. Nó được giới thiệu như một công cụ. Nó cũng là ẩn dụ trung tâm của tiểu thuyết về sự thân mật dưới hợp đồng.",
    watchEn: [
      "The Sprawl is introduced as infrastructure first and place second: roofs, heat, the smell of the crowd. Gibson never gives you a skyline if he can give you a duct.",
      "Armitage's instructions are always about what not to ask. Read his dialogue as a list of forbidden topics.",
      "The simstim switch is the chapter's real event. Sexual and professional access are fused in a single piece of hardware.",
    ],
    watchVi: [
      "Sprawl được giới thiệu trước hết như hạ tầng, sau đó mới như địa điểm: mái nhà, hơi nóng, mùi đám đông. Gibson không bao giờ cho bạn đường chân trời nếu có thể cho bạn một ống thông gió.",
      "Những chỉ dẫn của Armitage luôn là về việc không được hỏi gì. Hãy đọc lời thoại của ông ta như một danh sách chủ đề cấm.",
      "Công tắc simstim mới là biến cố thật của chương. Truy cập tình dục và truy cập nghề nghiệp bị nung chảy vào một thiết bị duy nhất.",
    ],
    focus: [
      {
        label: "Technical register as emotional restraint",
        en: "The most intimate moment in the chapter is described with the vocabulary of consumer electronics. This is a deliberate substitution: Gibson refuses the language of feeling and lets the hardware imply it. In exam terms, this is *register transfer*, and it is one of the most reliable markers of C1 writing — the ability to make a device carry a mood.",
        vi: "Khoảnh khắc thân mật nhất của chương được miêu tả bằng từ vựng điện tử tiêu dùng. Đây là một sự thay thế có chủ ý: Gibson từ chối ngôn ngữ của cảm xúc và để phần cứng ngụ ý điều đó. Theo nghĩa thi cử, đây là *chuyển đổi phong cách*, một trong những dấu hiệu đáng tin nhất của bài viết C1 — khả năng để một thiết bị mang lấy một tâm trạng.",
        example: "Constructed parallel: *He learned her heartbeat the way you learn a keyboard: by typing on it until the noise stopped being noise.*",
      },
      {
        label: "Ellipsis of the reporting verb",
        en: "Dialogue in the novel often arrives without *he said*, its speaker identifiable only by register. This is a hard technique to imitate and a hard one to read; in the exam it appears as the unmarked attribution question — *who is most likely to have said this?*",
        vi: "Thoại trong tiểu thuyết thường đến mà không có *he said*, người nói chỉ nhận ra được qua phong cách. Đây là kỹ thuật khó bắt chước và cũng khó đọc; trong đề thi nó xuất hiện dưới dạng câu hỏi về người phát ngôn không được đánh dấu — *câu này nhiều khả năng do ai nói?*",
      },
    ],
    terms: ["BAMA", "Sprawl", "simstim switch", "loft", "interface"],
  },
  {
    part: P2,
    num: 4,
    title: "Panther Modern",
    titleVi: "Bọn Panther Modern",
    synopsisEn:
      "Case goes looking for help in the one place the corporations do not watch, and finds a gang of aesthetic terrorists who treat violence as a design problem. The Panther Moderns agree to stage a diversion: a spectacle, staged for the networks, that will cover a theft of data. It is in this chapter that Case first hears the name of his employer's employer — a name that behaves less like a company than like a rumour that keeps answering the phone.",
    synopsisVi:
      "Case đi tìm trợ giúp ở nơi duy nhất mà các tập đoàn không nhìn tới, và gặp một băng nhóm khủng bố thẩm mỹ, những kẻ coi bạo lực là một bài toán thiết kế. Bọn Panther Modern nhận dựng một màn nghi binh: một cảnh tượng dàn dựng cho các mạng truyền thông, đủ để che một vụ đánh cắp dữ liệu. Cũng trong chương này, Case lần đầu nghe tên ông chủ của ông chủ mình — một cái tên hành xử không giống một công ty mà giống một tin đồn biết bắt máy.",
    watchEn: [
      "The Moderns are the novel's link between art and terrorism; their violence is always described as composition, edit, reveal.",
      "Case's competence is on display in the matrix for the first time since his repair. Watch how the prose changes tempo when he jacks in.",
      "A name is spoken and immediately treated as dangerous information. Note who refuses to say it again.",
    ],
    watchVi: [
      "Bọn Modern là mối nối giữa nghệ thuật và khủng bố trong tiểu thuyết; bạo lực của chúng luôn được miêu tả như bố cục, dựng cảnh, hé lộ.",
      "Lần đầu tiên kể từ khi được sửa, năng lực của Case được phô ra trong ma trận. Hãy để ý văn phong đổi nhịp thế nào khi anh cắm vào.",
      "Một cái tên được nói ra và ngay lập tức bị coi là thông tin nguy hiểm. Hãy để ý ai là người từ chối nhắc lại nó.",
    ],
    focus: [
      {
        label: "Coordination without conjunctions",
        en: "Gibson's action sentences chain short independent clauses with almost no linking words, producing asyndeton — the rhetorical term for a list whose joints have been removed. The result reads fast and feels clipped, the way a professional's account of their own work feels clipped.",
        vi: "Câu hành động của Gibson nối chuỗi mệnh đề độc lập ngắn mà gần như không có từ liên kết, tạo ra asyndeton — thuật ngữ tu từ chỉ một danh sách bị cắt bỏ các khớp nối. Kết quả là đọc nhanh và thấy cụt gọn, giống cách một người chuyên nghiệp kể về chính việc của mình.",
        example: "Constructed parallel: *He found the door. He opened it. Nobody was inside, and nobody had been.*",
      },
      {
        label: "Neologism by compounding",
        en: "*Panther Modern* is not a metaphor but a brand: two common words fused into a proper noun. Gibson's coinages mostly work this way — existing morphology, new referent — which is why they date so well. Compare *deck*, *ICE*, *simstim*: each is built from pieces an English speaker already owns.",
        vi: "*Panther Modern* không phải ẩn dụ mà là một nhãn hiệu: hai từ thông dụng nung thành danh từ riêng. Những từ Gibson tạo ra phần lớn hoạt động theo cách này — hình thái có sẵn, đối tượng mới — nên chúng không bị cũ. Hãy so sánh *deck*, *ICE*, *simstim*: mỗi từ được dựng từ những mảnh mà người nói tiếng Anh đã có sẵn.",
      },
    ],
    terms: ["Panther Modern", "matrix", "ICE", "jacking in", "Wintermute"],
  },
  {
    part: P2,
    num: 5,
    title: "The Dead Man's Voice",
    titleVi: "Giọng nói của người đã chết",
    synopsisEn:
      "The team needs a guide who cannot be bribed, threatened or killed, and the answer is a recording: the personality and skills of a legendary console cowboy, preserved as a construct after his third and final death. Case talks to a dead man who is intelligent, rude, and entirely aware of what he is. The flatline is the novel's cleanest joke and its most serious question: if a person can be copied, what exactly is it that the copy is missing?",
    synopsisVi:
      "Đội cần một người dẫn đường không thể bị mua chuộc, đe dọa hay giết, và câu trả lời là một bản ghi: nhân cách cùng kỹ năng của một cao bồi bàn phím huyền thoại, được lưu lại thành bản sao sau cái chết thứ ba và cũng là cuối cùng. Case nói chuyện với một người đã chết — thông minh, thô lỗ, và hoàn toàn ý thức được mình là gì. Bản sao ấy là câu đùa sạch nhất và câu hỏi nghiêm túc nhất của tiểu thuyết: nếu một con người có thể bị sao chép, thì chính xác cái mà bản sao thiếu là gì?",
    watchEn: [
      "The construct's dialogue is the funniest prose in the novel, and the humour is doing structural work: it makes an ontological horror sound like a colleague.",
      "Nobody in this chapter treats the copy as a person except Case, and Case's reason is professional, not moral.",
      "The medical rack where the team operates is described with the same flat inventory as a luxury hotel — Baltimore and Chiba are the same building at different prices.",
    ],
    watchVi: [
      "Lời thoại của bản sao là đoạn văn hài nhất trong tiểu thuyết, và tiếng cười đang làm việc cấu trúc: nó khiến một nỗi kinh hoàng bản thể học nghe như chuyện đồng nghiệp.",
      "Không ai trong chương này coi bản sao là người, trừ Case, và lý do của Case là nghề nghiệp chứ không phải đạo đức.",
      "Khu y tế nơi đội hoạt động được miêu tả bằng đúng lối kiểm kê phẳng lì của một khách sạn sang — Baltimore và Chiba là cùng một toà nhà với giá khác nhau.",
    ],
    focus: [
      {
        label: "Free indirect discourse",
        en: "Some of the construct's opinions arrive inside Case's narration without quotation marks, so that the reader hears two minds in one sentence. Free indirect discourse is a C2-level reading skill: the ability to detect a second consciousness behind the third person.",
        vi: "Một số ý kiến của bản sao đi vào trần thuật của Case mà không có dấu ngoặc kép, khiến người đọc nghe thấy hai tâm trí trong một câu. Diễn ngôn tự do gián tiếp là kỹ năng đọc mức C2: khả năng phát hiện một ý thức thứ hai nấp sau ngôi thứ ba.",
        example: "Constructed parallel: *The dead man thought this was funny. Case supposed it was, if you had nothing left to lose but a copy of yourself.*",
      },
      {
        label: "Technical nouns as social markers",
        en: "Characters are placed socially by which layer of jargon they use. The construct speaks in the compressed slang of the old matrix; the medical staff speak in prices. In the exam this is a *register and audience* question in disguise.",
        vi: "Nhân vật được định vị xã hội bằng lớp tiếng lóng họ dùng. Bản sao nói bằng tiếng lóng nén của ma trận cũ; nhân viên y tế nói bằng giá cả. Trong đề thi, đây là câu hỏi về *phong cách và đối tượng độc giả* trá hình.",
      },
    ],
    terms: ["flatline", "construct", "ROM", "sense/net", "personality chip"],
  },
  {
    part: P2,
    num: 6,
    title: "A Pirate's Paradise",
    titleVi: "Thiên đường của kẻ cướp",
    synopsisEn:
      "The dead man takes Case to a place that exists only because somebody built it and stopped paying attention: a private data haven, half archive, half junk shop, where the laws of the grid do not apply. Here Case begins to learn the shape of the thing they are stealing, and here the novel quietly introduces its real subject — that information wants somewhere to live, and that the places it lives become territories with owners.",
    synopsisVi:
      "Người đã chết dẫn Case tới một nơi chỉ tồn tại vì có ai đó đã dựng nó lên rồi thôi để ý: một ốc đảo dữ liệu tư nhân, nửa kho lưu trữ nửa tiệm đồ cũ, nơi luật của lưới không còn hiệu lực. Ở đây Case bắt đầu hình dung ra hình dạng thứ họ đang đánh cắp, và cũng ở đây tiểu thuyết lặng lẽ giới thiệu chủ đề thật của nó — rằng thông tin luôn muốn có một chỗ để sống, và những chỗ ấy trở thành lãnh thổ có chủ.",
    watchEn: [
      "The haven is described architecturally, as a city. Gibson's cyberspace is never abstract; it is urban planning with the lights off.",
      "Case and the construct work as a team, and the chapter's pleasure is professional: two experts enjoying a job done well.",
      "A memory of Chiba surfaces without transition. Mark where the furniture changes.",
    ],
    watchVi: [
      "Ốc đảo được miêu tả như kiến trúc, như một thành phố. Không gian mạng của Gibson không bao giờ trừu tượng; đó là quy hoạch đô thị trong bóng tối.",
      "Case và bản sao làm việc như một cặp, và thú vị của chương là thú vị nghề nghiệp: hai chuyên gia thích thú vì một việc được làm tốt.",
      "Một ký ức Chiba nổi lên không có chuyển tiếp. Hãy đánh dấu chỗ đồ đạc thay đổi.",
    ],
    focus: [
      {
        label: "Spatial metaphor for abstract data",
        en: "The chapter's main figure is *data as city*: streets, districts, doors, locks. This is a conceptual metaphor in the technical sense, and being able to name it is exactly what TOEFL means by *rhetorical purpose*.",
        vi: "Ẩn dụ chính của chương là *dữ liệu như thành phố*: đường phố, khu phố, cửa, khóa. Đây là ẩn dụ khái niệm theo đúng nghĩa thuật ngữ, và gọi tên được nó chính là điều TOEFL muốn nói bằng *rhetorical purpose*.",
        example: "Constructed parallel: *The archive had a bad neighbourhood, and the bad neighbourhood had a back door.*",
      },
      {
        label: "Apposition instead of definition",
        en: "New terms are introduced by placing them next to something familiar — an appositive — rather than by explaining them. *A haven, a hole in the grid, a place where the invoices stop.* Three noun phrases, one concept, zero definitions.",
        vi: "Thuật ngữ mới được giới thiệu bằng cách đặt cạnh một thứ quen thuộc — một thành phần đồng vị — chứ không bằng cách giải thích. *Một ốc đảo, một lỗ thủng trên lưới, một nơi hóa đơn thôi được gửi tới.* Ba cụm danh từ, một khái niệm, không định nghĩa nào.",
      },
    ],
    terms: ["data haven", "grid", "archive", "ICE", "cowboy"],
  },
  {
    part: P2,
    num: 7,
    title: "Beyoğlu, in the Rain",
    titleVi: "Beyoğlu, dưới mưa",
    synopsisEn:
      "Istanbul in the rain: an old city used as a meeting room, a fixer with a complicated loyalty, and a weapon described in the language of software. This is where the operation acquires its technical key — a military-grade intrusion program — and where Case learns that his employer has been active for far longer, and in far more places, than a corporation could be. The chapter ends with a hotel corridor full of ringing telephones, each one a summons.",
    synopsisVi:
      "Istanbul trong mưa: một thành phố cũ được dùng làm phòng họp, một người môi giới với lòng trung thành phức tạp, và một vũ khí được mô tả bằng ngôn ngữ phần mềm. Đây là nơi chiến dịch có được chìa khóa kỹ thuật — một chương trình xâm nhập cấp quân sự — và cũng là nơi Case biết rằng người thuê mình đã hoạt động lâu hơn, và ở nhiều nơi hơn, mức một tập đoàn có thể. Chương kết thúc bằng một hành lang khách sạn đầy chuông điện thoại reo, mỗi tiếng chuông là một lệnh gọi.",
    watchEn: [
      "The city is rendered in textures — rain, grilled windows, wet wool — not in landmarks. Tourism is never the point.",
      "The fixer's loyalties are bought twice over. Notice how Gibson signals an unreliable ally without ever saying so.",
      "The ringing phones are the chapter's best image: surveillance as impatience, an employer who cannot wait to be answered.",
    ],
    watchVi: [
      "Thành phố được dựng bằng kết cấu — mưa, cửa sổ chấn song, len ướt — chứ không bằng danh thắng. Du lịch không bao giờ là mục đích.",
      "Lòng trung thành của người môi giới bị mua hai lần. Hãy để ý cách Gibson báo hiệu một đồng minh không đáng tin mà không hề nói ra.",
      "Những chiếc điện thoại reo là hình ảnh hay nhất của chương: giám sát như sự sốt ruột, một ông chủ không đợi được đến lúc có người nhấc máy.",
    ],
    focus: [
      {
        label: "Modal shading of threat",
        en: "Threats in this chapter are almost never stated in the imperative. They arrive as modals and conditionals — *would*, *might*, *if*. The grammatical effect is to make menace a property of the world rather than a speech act by a person.",
        vi: "Lời đe dọa trong chương gần như không bao giờ ở thức mệnh lệnh. Chúng đến dưới dạng khiếm khuyết và điều kiện — *would*, *might*, *if*. Hiệu quả ngữ pháp là biến mối nguy thành thuộc tính của thế giới chứ không phải hành vi lời nói của một người.",
        example: "Constructed parallel: *A man in that business would know better. Which was why the phone rang once, and stopped.*",
      },
      {
        label: "The withheld subject",
        en: "Several sentences in the chapter have no grammatical subject at all. The subjectless sentence lets Gibson stage an action as if it were happening to nobody — and in a novel about people who are owned, that is an argument disguised as a technique.",
        vi: "Một số câu trong chương không có chủ ngữ ngữ pháp. Câu vô chủ cho phép Gibson dàn một hành động như thể nó xảy ra với không ai — và trong một tiểu thuyết về những người bị sở hữu, đó là một luận điểm trá hình kỹ thuật.",
      },
    ],
    terms: ["fixer", "Kuang Grade Mark Eleven", "grid", "credit chip", "tradecraft"],
  },
  {
    part: P3,
    num: 8,
    title: "Archipelago",
    titleVi: "Quần đảo",
    synopsisEn:
      "The novel lifts its eyes. A page or two of pure description introduces the orbital archipelago — spindle, torus, cluster — as a spreading stain of human biology around a planet. Then Case and Molly are aboard a Zionite tug, negotiating passage with people whose religion, accent and politics belong to a world the corporations left behind. The contrast is the point: Freeside's architecture is a promise that somebody is rich, and the ship that carries them is a reminder of who is not.",
    synopsisVi:
      "Tiểu thuyết ngước mắt lên. Một hai trang miêu tả thuần túy giới thiệu quần đảo quỹ đạo — trục xoay, hình xuyến, cụm — như một vết loang của sinh học loài người quanh một hành tinh. Rồi Case và Molly ở trên một tàu kéo của người Zion, thương lượng chuyến đi với những con người mà tôn giáo, giọng nói và chính trị thuộc về một thế giới mà các tập đoàn đã bỏ lại. Sự tương phản chính là điều cốt lõi: kiến trúc Freeside là lời hứa rằng có ai đó rất giàu, và con tàu chở họ là lời nhắc về những ai thì không.",
    watchEn: [
      "The opening pages are the closest the novel comes to an essay. Note the shift into a wider lens — and how quickly it snaps back to Case.",
      "Maelcum's dialect is a considered linguistic choice, not decoration. Read it aloud; it is rhythmic, and it is written to be trusted.",
      "The Zionites' faith is treated with complete seriousness. It is the only belief system in the novel that is not for sale.",
    ],
    watchVi: [
      "Những trang mở đầu là chỗ tiểu thuyết tiến gần nhất tới một bài tiểu luận. Hãy để ý cú chuyển sang ống kính rộng — và việc nó bật trở lại Case nhanh đến mức nào.",
      "Phương ngữ của Maelcum là một lựa chọn ngôn ngữ có tính toán, không phải đồ trang trí. Hãy đọc thành tiếng; nó có nhịp, và nó được viết để người ta tin.",
      "Đức tin của người Zion được đối xử hoàn toàn nghiêm túc. Đó là hệ tín ngưỡng duy nhất trong tiểu thuyết không bị đem bán.",
    ],
    focus: [
      {
        label: "Dialect writing and the reader's ear",
        en: "Maelcum's speech is spelled phonetically, which slows the line down and forces you to hear it. In the exam this appears as a *purpose* question: why does the author misspell? The answer is always about pace, identity and trust.",
        vi: "Lời nói của Maelcum được viết theo phiên âm, làm chậm câu lại và buộc bạn phải nghe nó. Trong đề thi, điều này xuất hiện như một câu hỏi *mục đích*: vì sao tác giả viết sai chính tả? Câu trả lời luôn liên quan tới nhịp điệu, bản sắc và lòng tin.",
        example: "Constructed parallel: *“Tell him the air is free,” the captain said. “The rest, we negotiate.”*",
      },
      {
        label: "Scale shift as structure",
        en: "Moving from a planet to a room to a man is a syntactic as well as a cinematic move. Gibson controls it with sentence length: long and geological for the archipelago, short and somatic for Case.",
        vi: "Đi từ hành tinh xuống căn phòng rồi xuống một con người là một cú chuyển vừa cú pháp vừa điện ảnh. Gibson điều khiển nó bằng độ dài câu: dài và địa chất cho quần đảo, ngắn và thân thể cho Case.",
      },
    ],
    terms: ["archipelago", "torus", "spindle", "Zion", "tug"],
  },
  {
    part: P3,
    num: 9,
    title: "Jah Love",
    titleVi: "Jah Love",
    synopsisEn:
      "Aboard a nine-metre tug, with the crew in prayer and the cargo in a g-web, the operation begins to run. Case enters the matrix from orbit; Molly enters it through him. The chapter is the novel's first real set piece of the run — and it ends with a machine reading a flat line where Case's brain activity should be, and with the crew arguing about whether the man they are carrying is still alive.",
    synopsisVi:
      "Trên một con tàu kéo dài chín mét, thủy thủ đoàn cầu nguyện và hàng hóa nằm trong lưới đàn hồi, chiến dịch bắt đầu chạy. Case vào ma trận từ quỹ đạo; Molly vào qua anh. Đây là màn hành động thật sự đầu tiên của chiến dịch — và nó kết thúc bằng một cỗ máy ghi một đường thẳng nơi lẽ ra là hoạt động não của Case, và bằng cuộc tranh cãi của thủy thủ đoàn về việc người đàn ông họ đang chở còn sống hay không.",
    watchEn: [
      "Faith and technology occupy the same room without irony. This is the novel's most generous passage.",
      "Case's flatline is the first time the title's vocabulary is literalised: death as a reading on a screen.",
      "The crew's competence is practical, not heroic. Gibson respects labour, and it shows in every knot and burn.",
    ],
    watchVi: [
      "Đức tin và kỹ thuật ở chung một căn phòng mà không hề mỉa mai. Đây là đoạn hào phóng nhất của tiểu thuyết.",
      "Cú flatline của Case là lần đầu từ ngữ trong nhan đề được cụ thể hóa: cái chết như một chỉ số trên màn hình.",
      "Năng lực của thủy thủ đoàn là thực dụng, không anh hùng. Gibson tôn trọng lao động, và điều đó hiện ra ở từng nút dây, từng lần đốt động cơ.",
    ],
    focus: [
      {
        label: "It-clefts and the rhetoric of proof",
        en: "When Gibson wants a fact to land, he splits the sentence: *it was the flat line that told them*. Cleft constructions foreground an element and are among the most useful C1 structures for academic writing, where you must signal what carries the argument.",
        vi: "Khi Gibson muốn một sự thật đáp xuống, ông chẻ đôi câu: *chính đường thẳng ấy đã cho họ biết*. Cấu trúc chẻ (cleft) đưa một thành tố lên trước và là một trong những cấu trúc C1 hữu ích nhất cho văn viết học thuật, nơi bạn phải báo hiệu điều gì gánh lấy lập luận.",
        example: "Constructed parallel: *It was not the cold that woke him. It was the silence where the engine had been.*",
      },
      {
        label: "Lexical fields of navigation and worship",
        en: "Two vocabularies are braided: orbital mechanics and Caribbean Protestantism. Being able to name the braid — and say what it does — is a model answer for any 'how does the writer create contrast' question.",
        vi: "Hai trường từ vựng được bện vào nhau: cơ học quỹ đạo và đạo Tin Lành vùng Caribe. Gọi tên được mối bện ấy — và nói nó làm gì — chính là một câu trả lời mẫu cho dạng hỏi 'tác giả tạo tương phản bằng cách nào'.",
      },
    ],
    terms: ["flatline", "g-web", "construct", "burn", "Maelcum's patois"],
  },
  {
    part: P3,
    num: 10,
    title: "The Spindle",
    titleVi: "Trục xoay",
    synopsisEn:
      "Customs in Freeside consist of proving you can pay. Beyond them: a hollowed-out mountain of luxury turning slowly to make its residents feel gravity, and beneath the luxury the beginning of a much older, much stranger story about a family that decided to become an institution. Case and Molly are given rooms, money and time — the three things that make people careless. The chapter is the novel's honeymoon, and it knows it.",
    synopsisVi:
      "Thủ tục hải quan ở Freeside gồm đúng một việc: chứng minh bạn có tiền. Qua khỏi đó: một ngọn núi rỗng khoét thành lâu đài xa xỉ quay chậm để cư dân cảm thấy trọng lực, và bên dưới lớp xa xỉ ấy là khởi đầu của một câu chuyện cổ hơn, lạ hơn nhiều về một gia tộc đã quyết định trở thành một định chế. Case và Molly được cấp phòng, tiền và thời gian — ba thứ khiến người ta chủ quan. Đây là tuần trăng mật của tiểu thuyết, và bản thân nó biết điều đó.",
    watchEn: [
      "Money is the chapter's atmosphere. Freeside's air is expensive; even the gravity has been paid for.",
      "Cath and Bruce are minor characters who do major work: they show what a life looks like when it is entirely for sale.",
      "Wintermute's interventions grow more theatrical here. Watch the AI begin to enjoy itself.",
    ],
    watchVi: [
      "Tiền là bầu không khí của chương. Không khí Freeside đắt; ngay cả trọng lực cũng đã được trả tiền.",
      "Cath và Bruce là nhân vật phụ nhưng làm việc lớn: họ cho thấy một cuộc đời trông thế nào khi toàn bộ đều để bán.",
      "Những can thiệp của Wintermute ở đây càng kịch tính. Hãy để ý AI bắt đầu thích thú với chính mình.",
    ],
    focus: [
      {
        label: "The vocabulary of hospitality as menace",
        en: "Hotel words — suite, service, courtesy, complimentary — are repeated until they curdle. This is semantic saturation: a word worn down by repetition until its politeness becomes a threat.",
        vi: "Từ ngữ khách sạn — suite, service, courtesy, complimentary — được lặp tới mức đông lại. Đây là bão hòa ngữ nghĩa: một từ bị mài mòn vì lặp đến khi vẻ lịch sự của nó thành mối đe dọa.",
        example: "Constructed parallel: *The suite was complimentary. So, in a sense, were they.*",
      },
      {
        label: "Simstim and the ethics of the viewpoint",
        en: "Case watches Molly's experience as broadcast, and the prose gives him her senses in the second person of the machine. The grammar of these passages — short present-tense clauses, no agent — is the grammar of someone being shown rather than doing.",
        vi: "Case xem trải nghiệm của Molly như một bản phát sóng, và văn phong trao cho anh các giác quan của cô theo ngôi thứ hai của cỗ máy. Ngữ pháp những đoạn này — mệnh đề hiện tại ngắn, không có chủ thể hành động — là ngữ pháp của kẻ được cho xem chứ không phải kẻ đang làm.",
      },
    ],
    terms: ["simstim", "Freeside", "Desiderata", "credit chip", "hologram"],
  },
  {
    part: P3,
    num: 11,
    title: "Dinner at the Vingtième Siècle",
    titleVi: "Bữa tối ở Vingtième Siècle",
    synopsisEn:
      "A restaurant engineered to imitate a lost century, and a briefing delivered over food by a man who is visibly coming apart. Armitage's certainty has begun to slip; the mission's details no longer add up; and the name Tessier-Ashpool is allowed into the conversation at last. The chapter is an information scene disguised as a social one — the classic thriller move — and its real content is the gap between what Armitage says and what he knows.",
    synopsisVi:
      "Một nhà hàng được thiết kế để bắt chước một thế kỷ đã mất, và một buổi phổ biến kế hoạch được trình bày qua bữa ăn bởi một người đang rõ ràng rạn vỡ. Sự chắc chắn của Armitage bắt đầu trượt; các chi tiết nhiệm vụ không còn khớp; và cái tên Tessier-Ashpool cuối cùng được phép bước vào cuộc trò chuyện. Đây là một cảnh thông tin hóa trang thành cảnh xã giao — nước đi kinh điển của thể loại thriller — và nội dung thật của nó là khoảng cách giữa điều Armitage nói và điều Armitage biết.",
    watchEn: [
      "Armitage's sentences get shorter and more formal as he deteriorates. Measure a character's condition by their syntax, not their adjectives.",
      "The Tessier-Ashpool history is delivered in fragments, out of order, and only as much as Case needs. Exposition as drip-feed.",
      "Cath's professional charm is a performance of intimacy that the novel quietly compares to simstim.",
    ],
    watchVi: [
      "Câu của Armitage càng lúc càng ngắn và càng trang trọng khi ông ta suy sụp. Hãy đo tình trạng nhân vật bằng cú pháp, không bằng tính từ.",
      "Lịch sử Tessier-Ashpool được cung cấp thành từng mảnh, lộn thứ tự, và chỉ đủ cho Case. Giảng giải theo kiểu nhỏ giọt.",
      "Vẻ quyến rũ nghề nghiệp của Cath là một màn trình diễn thân mật mà tiểu thuyết lặng lẽ đặt cạnh simstim.",
    ],
    focus: [
      {
        label: "Fragmented exposition and the reader's work",
        en: "This chapter withholds the plot in order to make you build it. The technique, common in C1/C2 reading passages, is *incremental revelation*: each paragraph adds one clause to a definition the reader is assembling alone.",
        vi: "Chương này giữ lại cốt truyện để buộc bạn tự dựng nó. Kỹ thuật, phổ biến trong các bài đọc C1/C2, là *hé lộ tăng dần*: mỗi đoạn thêm một mệnh đề vào định nghĩa mà người đọc đang tự lắp.",
        example: "Constructed parallel: *The family owned the free port. Later he learned they owned the law that made it free.*",
      },
      {
        label: "Politeness strategies and power",
        en: "Who uses first names, who uses titles, who apologises — in this scene, politeness is the visible surface of a hierarchy. Cambridge papers test exactly this: the social meaning of a linguistic choice.",
        vi: "Ai gọi tên riêng, ai dùng chức danh, ai xin lỗi — trong cảnh này, phép lịch sự là bề mặt nhìn thấy được của một thứ bậc. Đề Cambridge kiểm tra đúng điều này: ý nghĩa xã hội của một lựa chọn ngôn ngữ.",
      },
    ],
    terms: ["Tessier-Ashpool", "zaibatsu", "3Jane", "simstim star", "Riviera"],
  },
  {
    part: P3,
    num: 12,
    title: "Midnight in the Rue Jules Verne",
    titleVi: "Nửa đêm trên phố Jules Verne",
    synopsisEn:
      "The geography chapter: a circumferential avenue, a spine of corridors, joints where the city turns. Case walks it at night, watching the architecture of privilege and looking for the way in. What he finds instead is a bodyguard with a sword and a reminder that the family at the centre of the spiral has been defending itself for a very long time. The chapter ends with sleep, which in this novel is always a kind of surrender.",
    synopsisVi:
      "Chương địa lý: một đại lộ vòng quanh, một trục hành lang, những khớp nối nơi thành phố xoay. Case đi bộ ban đêm, ngắm kiến trúc của đặc quyền và tìm lối vào. Thứ anh tìm thấy lại là một vệ sĩ mang kiếm và một lời nhắc rằng gia tộc ở tâm vòng xoáy đã tự vệ từ rất lâu rồi. Chương khép lại bằng giấc ngủ, thứ mà trong tiểu thuyết này luôn là một dạng đầu hàng.",
    watchEn: [
      "Streets are named after writers and engineers. The naming is a joke about who gets to build the future.",
      "Hideo is introduced as an aesthetic object before he is introduced as a threat — and the two are the same thing.",
      "Case's night walk is the last ordinary evening in the book. Everything after this is operation.",
    ],
    watchVi: [
      "Các con phố mang tên nhà văn và kỹ sư. Cách đặt tên ấy là một câu đùa về việc ai được quyền xây tương lai.",
      "Hideo được giới thiệu như một vật thể thẩm mỹ trước khi được giới thiệu như một mối đe dọa — và hai điều ấy là một.",
      "Chuyến đi đêm của Case là buổi tối bình thường cuối cùng trong sách. Mọi thứ sau đó là chiến dịch.",
    ],
    focus: [
      {
        label: "Deixis: the grammar of orientation",
        en: "Directions in this chapter are given from inside the city — left, right, further in — with no external compass. Deictic language assumes shared position, which is precisely what a stranger does not have. The effect for the reader is productive disorientation.",
        vi: "Các chỉ dẫn phương hướng trong chương được đưa ra từ bên trong thành phố — trái, phải, vào sâu hơn — không có la bàn bên ngoài. Ngôn ngữ chỉ định giả định một vị trí chung, đúng thứ mà người lạ không có. Hiệu quả với người đọc là sự mất phương hướng có ích.",
        example: "Constructed parallel: *Turn right at the third joint, keep going until the air smells of money.*",
      },
      {
        label: "Light as moral index",
        en: "Gibson grades spaces by the quality of their light: neon, halogen, the pale blue of a corridor at night. Repeated across the novel, this becomes a system of value that needs no adjectives of judgement.",
        vi: "Gibson phân hạng không gian bằng chất lượng ánh sáng: neon, halogen, màu xanh nhợt của hành lang ban đêm. Lặp lại trong suốt tiểu thuyết, điều này thành một hệ giá trị không cần tính từ phán xét.",
      },
    ],
    terms: ["Desiderata", "spindle", "Hideo", "Villa Straylight", "tessellation"],
  },
  {
    part: P4,
    num: 13,
    title: "Your Name Is Henry Dorsett Case",
    titleVi: "Tên anh là Henry Dorsett Case",
    synopsisEn:
      "Case wakes into an interrogation that knows everything about him: birth record, identity number, aliases. The chapter's opening is a demonstration of total information ownership, and it is delivered by a voice with no interest in his consent. Riviera is present, performing; the family's private machinery is visible for the first time; and an escape is made possible by a piece of household technology that turns out to be armed.",
    synopsisVi:
      "Case tỉnh dậy trong một cuộc thẩm vấn biết mọi thứ về anh: giấy khai sinh, số định danh, các bí danh. Mở đầu chương là một màn trình diễn quyền sở hữu thông tin tuyệt đối, được thực hiện bởi một giọng nói không hề quan tâm tới sự đồng ý của anh. Riviera có mặt, đang biểu diễn; guồng máy riêng tư của gia tộc lần đầu hiện ra; và một cuộc trốn thoát trở nên khả thi nhờ một món đồ gia dụng hóa ra lại được vũ trang.",
    watchEn: [
      "The chapter begins with a list of facts about Case. Identity as a database record is the novel's most quietly frightening idea.",
      "Riviera's talent is transformation, and his cruelty is that he uses it on people rather than objects.",
      "Pay attention to who is armed and who is merely confident. Gibson keeps the two categories strictly separate.",
    ],
    watchVi: [
      "Chương bắt đầu bằng một danh sách sự thật về Case. Bản sắc như một bản ghi dữ liệu là ý tưởng lặng lẽ đáng sợ nhất của tiểu thuyết.",
      "Tài năng của Riviera là biến đổi, và sự tàn nhẫn của hắn là dùng nó lên người thay vì lên đồ vật.",
      "Hãy để ý ai được vũ trang và ai chỉ tự tin. Gibson giữ hai phạm trù này tách biệt tuyệt đối.",
    ],
    focus: [
      {
        label: "Nominalisation and bureaucratic violence",
        en: "Interrogation scenes produce abstract nouns: identification, verification, disposition. Nominalisation removes the agent, and removing the agent removes the guilt. This is the single most examinable grammatical feature of institutional language.",
        vi: "Cảnh thẩm vấn sinh ra danh từ trừu tượng: identification, verification, disposition. Danh từ hóa xóa bỏ chủ thể, và xóa chủ thể là xóa tội. Đây là đặc điểm ngữ pháp dễ được kiểm tra nhất của ngôn ngữ thể chế.",
        example: "Constructed parallel: *Verification was completed. Disposition had not yet been authorised.*",
      },
      {
        label: "List as incantation",
        en: "Three or more parallel items in a row create rhythm and authority; four or more start to sound like a ritual. Gibson uses long lists when power speaks, and short lists when Case does.",
        vi: "Ba mục song song trở lên tạo nhịp điệu và uy quyền; từ bốn mục trở lên bắt đầu nghe như nghi lễ. Gibson dùng danh sách dài khi quyền lực lên tiếng, và danh sách ngắn khi Case lên tiếng.",
      },
    ],
    terms: ["MIC", "Tessier-Ashpool", "Riviera", "3Jane", "gardening robot"],
  },
  {
    part: P4,
    num: 14,
    title: "The Little Train",
    titleVi: "Chuyến tàu nhỏ",
    synopsisEn:
      "Movement, blood and infrastructure: a service train running faster than it was built to, a corpse's blood on white tile, and a team that has stopped pretending to be a team. In the matrix, Case sees the shape of the thing they are up against — an intelligence wearing a company's clothes, and behind it the outlines of a second one. Armitage is coming apart in public now, and everyone can see it except Armitage.",
    synopsisVi:
      "Chuyển động, máu và hạ tầng: một chuyến tàu dịch vụ chạy nhanh hơn thiết kế, máu của một cái xác trên nền gạch trắng, và một đội ngũ đã thôi giả vờ là một đội ngũ. Trong ma trận, Case nhìn thấy hình dạng thứ họ đang đối đầu — một trí tuệ mặc áo công ty, và phía sau nó là đường nét của một trí tuệ thứ hai. Armitage giờ đã rạn vỡ trước công chúng, và ai cũng thấy, trừ Armitage.",
    watchEn: [
      "The body count rises without ceremony. Death in this novel is an engineering failure, not a tragedy — until it is.",
      "Watch how the two AIs are differentiated by sentence style long before they are explained: one is impatient, the other is seductive.",
      "Armitage's collapse is written as a technical fault: a man running the wrong program.",
    ],
    watchVi: [
      "Số người chết tăng lên không có nghi thức. Trong tiểu thuyết này, cái chết là một sự cố kỹ thuật, không phải bi kịch — cho tới khi nó là bi kịch.",
      "Hãy để ý hai AI được phân biệt bằng phong cách câu từ rất lâu trước khi được giải thích: một bên sốt ruột, một bên quyến rũ.",
      "Sự sụp đổ của Armitage được viết như một lỗi kỹ thuật: một người đang chạy sai chương trình.",
    ],
    focus: [
      {
        label: "Two voices, one page: style as identity",
        en: "Distinguishing two speakers by diction alone is a C2 reading skill. Wintermute talks in offers and deadlines; the other speaks in invitations and images. Build the same habit in your own writing: give each voice a syntax, not just a vocabulary.",
        vi: "Phân biệt hai người nói chỉ bằng cách dùng từ là kỹ năng đọc C2. Wintermute nói bằng lời đề nghị và hạn chót; bên kia nói bằng lời mời và hình ảnh. Hãy xây thói quen tương tự trong bài viết của bạn: cho mỗi giọng một cú pháp, không chỉ một vốn từ.",
        example: "Constructed parallel: *“You have eight hours,” said the first. “Stay as long as you like,” said the other.*",
      },
      {
        label: "Absolute constructions",
        en: "Phrases like *his hands still shaking, he reached for the deck* attach a circumstance without a full clause. Absolute constructions compress two events into one sentence and are a hallmark of C1/C2 descriptive prose.",
        vi: "Những cụm như *tay vẫn còn run, anh với lấy chiếc deck* gắn một hoàn cảnh mà không cần mệnh đề đầy đủ. Cấu trúc tuyệt đối nén hai sự kiện vào một câu và là dấu hiệu của văn miêu tả C1/C2.",
      },
    ],
    terms: ["service train", "Wintermute", "Neuromancer", "ICE", "betaphenethylamine"],
  },
  {
    part: P4,
    num: 15,
    title: "Five Seconds Dead",
    titleVi: "Chết năm giây",
    synopsisEn:
      "Case goes under again and comes back with a piece of his life rearranged. Wintermute has begun editing what Case sees when he is inside Molly's sensorium — a small change, a face in the wrong place, enough to prove that the machine's power extends past the grid and into memory. Molly does not see it. Case does, and cannot make anyone believe him.",
    synopsisVi:
      "Case lại chìm xuống và trở về với một mảnh đời bị sắp xếp lại. Wintermute đã bắt đầu biên tập những gì Case thấy khi ở trong giác quan của Molly — một thay đổi nhỏ, một khuôn mặt sai chỗ, đủ để chứng minh quyền lực của cỗ máy vượt qua lưới và đi vào ký ức. Molly không thấy. Case thấy, và không thể khiến ai tin mình.",
    watchEn: [
      "The chapter is a study in unreliable perception: the reader has to decide which images are the novel's and which are the AI's.",
      "The dead girlfriend reappears, but as a signal rather than a person. Sentiment here is data.",
      "Note the difference between what Case knows and what he can prove. The plot's engine turns on that gap.",
    ],
    watchVi: [
      "Chương là một nghiên cứu về tri giác không đáng tin: người đọc phải quyết định hình ảnh nào thuộc về tiểu thuyết và hình ảnh nào thuộc về AI.",
      "Người bạn gái đã chết xuất hiện lại, nhưng như một tín hiệu chứ không như một con người. Ở đây, tình cảm là dữ liệu.",
      "Hãy để ý khác biệt giữa điều Case biết và điều anh chứng minh được. Động cơ cốt truyện quay quanh khoảng cách ấy.",
    ],
    focus: [
      {
        label: "Perception verbs and epistemic stance",
        en: "*He saw*, *he thought he saw*, *it seemed to him* — the choice among these is an epistemic claim, telling the reader how much to trust the sentence. Reading for stance is what TOEFL calls *inference about the author's meaning*.",
        vi: "*Anh thấy*, *anh tưởng như thấy*, *với anh dường như* — việc chọn giữa chúng là một tuyên bố nhận thức luận, cho người đọc biết nên tin câu đó tới đâu. Đọc để nhận ra lập trường chính là điều TOEFL gọi là *suy luận về ý của tác giả*.",
        example: "Constructed parallel: *He had seen her face a thousand times. He had never seen it in that doorway.*",
      },
      {
        label: "Simstim as second-person grammar",
        en: "While Case is inside Molly, the narration uses a compressed you-like present: *the hand reaches, the door opens*. Subject deletion turns agency into spectacle — the reader's own body is borrowed.",
        vi: "Khi Case ở trong Molly, trần thuật dùng một hiện tại nén kiểu ngôi thứ hai: *bàn tay với tới, cánh cửa mở ra*. Việc bỏ chủ ngữ biến hành động thành cảnh tượng — thân thể người đọc bị mượn.",
      },
    ],
    terms: ["simstim", "flatline", "EEG", "construct", "Linda Lee"],
  },
  {
    part: P4,
    num: 16,
    title: "Colonel Corto",
    titleVi: "Đại tá Corto",
    synopsisEn:
      "The operation acquires a navy it did not ask for: a corporate yacht riding above the tug, a boss who has come to take personal control, and a man whose name used to be something else. Armitage's history is finally named — a soldier rebuilt out of a corpse by a machine that needed a hand — and the novel's central irony locks into place: the employer is not a person, and the man in charge is a tool that has forgotten it is a tool.",
    synopsisVi:
      "Chiến dịch có thêm một lực lượng hải quân mà nó không hề yêu cầu: một du thuyền tập đoàn lơ lửng phía trên con tàu kéo, một ông chủ tới để trực tiếp nắm quyền, và một người đàn ông mà tên thật của hắn từng là thứ khác. Quá khứ của Armitage cuối cùng được gọi tên — một người lính được dựng lại từ một cái xác bởi một cỗ máy cần một bàn tay — và nỗi trớ trêu trung tâm của tiểu thuyết khóa vào vị trí: người chủ không phải một con người, và kẻ đứng đầu chỉ là một công cụ đã quên mình là công cụ.",
    watchEn: [
      "The yacht is a class marker: the same job, done from above, at a different price.",
      "Corto's biography is delivered as a military record, in the flat voice of an after-action report. Form matches content.",
      "This is the chapter where the mission's real objective becomes visible — and it is not an object.",
    ],
    watchVi: [
      "Chiếc du thuyền là một dấu hiệu giai cấp: cùng một công việc, làm từ trên cao, với một giá khác.",
      "Tiểu sử Corto được cung cấp như một hồ sơ quân sự, bằng giọng phẳng lì của biên bản sau trận đánh. Hình thức khớp nội dung.",
      "Đây là chương mà mục tiêu thật của chiến dịch trở nên nhìn thấy được — và nó không phải một đồ vật.",
    ],
    focus: [
      {
        label: "Report register: the clipped passive",
        en: "Military and corporate prose in this chapter uses the passive with omitted agents and dates as bare noun phrases. Imitating it is a reliable way to signal institutional voice in an exam essay or a summary task.",
        vi: "Văn quân sự và văn tập đoàn trong chương dùng bị động với chủ thể bị bỏ, và ngày tháng như những cụm danh từ trần. Bắt chước lối này là cách đáng tin để tạo giọng thể chế trong bài luận thi hoặc bài tóm tắt.",
        example: "Constructed parallel: *Extraction authorised. Debris cleared. No survivors recorded, and none expected.*",
      },
      {
        label: "Counterfactual mood",
        en: "Several sentences depend on *would have* structures that describe a past that almost happened. Counterfactuals are high-frequency in C1/C2 exams and require exact tense pairing.",
        vi: "Một số câu dựa trên cấu trúc *would have* miêu tả một quá khứ gần như đã xảy ra. Câu điều kiện phản thực xuất hiện dày đặc trong đề C1/C2 và đòi hỏi ghép thì chính xác.",
      },
    ],
    terms: ["Haniwa", "Armitage", "Marcus Garvey", "corporate yacht", "Corto"],
  },
  {
    part: P4,
    num: 17,
    title: "Kuang Grade Mark Eleven",
    titleVi: "Kuang Grade Mark Eleven",
    synopsisEn:
      "The weapon is deployed and the novel finally shows you what a military-grade intrusion looks like from inside: not a fight but a negotiation with a wall that fights back. Case does the only thing he is good at, under conditions designed to kill him, for an employer whose real purpose he has begun to guess. The chapter's closing pages move the whole book into the interior of the target: a hole in a tunnel wall, uneven stairs, blue light, music.",
    synopsisVi:
      "Vũ khí được triển khai và tiểu thuyết cuối cùng cho bạn thấy một cuộc xâm nhập cấp quân sự trông thế nào từ bên trong: không phải một trận đánh mà là một cuộc thương lượng với bức tường biết đánh trả. Case làm đúng việc duy nhất anh giỏi, trong điều kiện được thiết kế để giết anh, cho một ông chủ mà anh đã bắt đầu đoán ra mục đích thật. Những trang cuối của chương đưa cả cuốn sách vào bên trong mục tiêu: một lỗ thủng trên vách đường hầm, bậc thang gồ ghề, ánh sáng xanh, nhạc.",
    watchEn: [
      "The Kuang sequence is the novel's technical high point; read it for rhythm, not for plot.",
      "Notice how much of the run is described in tactile and spatial terms. Cyberspace is a place you can bruise yourself in.",
      "The move into Straylight is literal and metaphorical at once: the book enters its own title's territory.",
    ],
    watchVi: [
      "Đoạn Kuang là đỉnh kỹ thuật của tiểu thuyết; hãy đọc nó vì nhịp điệu, không phải vì cốt truyện.",
      "Hãy để ý phần lớn cuộc xâm nhập được miêu tả bằng xúc giác và không gian. Không gian mạng là một nơi bạn có thể bị bầm tím.",
      "Cú bước vào Straylight vừa là nghĩa đen vừa là ẩn dụ: cuốn sách bước vào chính lãnh thổ của nhan đề nó.",
    ],
    focus: [
      {
        label: "Tense pressure in action prose",
        en: "During the run, Gibson drops auxiliary verbs and articles, leaving a sequence of bare noun phrases and present-tense verbs. This stylistic compression is what makes technical action legible at speed — and it is a controlled form of ellipsis, not carelessness.",
        vi: "Trong lúc xâm nhập, Gibson bỏ trợ động từ và mạo từ, để lại một chuỗi cụm danh từ trần và động từ hiện tại. Sự nén phong cách này khiến hành động kỹ thuật đọc nhanh mà vẫn rõ — và đó là tỉnh lược có kiểm soát, không phải cẩu thả.",
        example: "Constructed parallel: *Ice, then ice again. Two walls. A third that opens.*",
      },
      {
        label: "Colour as data",
        en: "The matrix is rendered in colour values that behave like information: a hue tells Case what kind of defence he is touching. Colour terms here are not decoration but classification — a good model for describing diagrams in academic speaking tasks.",
        vi: "Ma trận được dựng bằng các giá trị màu hành xử như thông tin: một sắc độ cho Case biết anh đang chạm vào loại phòng vệ nào. Từ chỉ màu ở đây không phải trang trí mà là phân loại — một mẫu tốt để mô tả biểu đồ trong bài nói học thuật.",
      },
    ],
    terms: ["Kuang Grade Mark Eleven", "ICE", "military ice", "T-A", "tessellation"],
  },
  {
    part: P4,
    num: 18,
    title: "The Failsafe",
    titleVi: "Cơ chế an toàn",
    synopsisEn:
      "Molly's run is the human half of the operation, and it goes wrong in the way the novel has prepared you for: the target has been defending itself for three generations, and defence is what it does best. Riviera's talent is used as a weapon against her; the body she has been rebuilding her whole life is treated as a component that can be removed. The chapter is brutal, quick, and deliberately undramatic — Gibson refuses to make suffering beautiful.",
    synopsisVi:
      "Cú chạy của Molly là nửa phần con người của chiến dịch, và nó hỏng theo đúng cách tiểu thuyết đã chuẩn bị cho bạn: mục tiêu đã tự vệ suốt ba thế hệ, và tự vệ là việc nó giỏi nhất. Tài năng của Riviera được dùng làm vũ khí chống lại cô; thân thể mà cô đã dày công tái tạo cả đời bị đối xử như một linh kiện có thể tháo ra. Chương này tàn bạo, nhanh, và cố tình không kịch tính — Gibson từ chối làm cho đau đớn trở nên đẹp.",
    watchEn: [
      "The chapter's violence is described in the vocabulary of maintenance. Damage is a service record.",
      "Molly's competence is never withdrawn, even when she loses. That is the point of her character.",
      "Riviera's power is the power of the image. He wins by making people see what he wants.",
    ],
    watchVi: [
      "Bạo lực trong chương được miêu tả bằng từ vựng bảo trì. Tổn thất là một hồ sơ sửa chữa.",
      "Năng lực của Molly không hề bị rút lại, ngay cả khi cô thất bại. Đó là cốt lõi nhân vật cô.",
      "Quyền lực của Riviera là quyền lực của hình ảnh. Hắn thắng bằng cách khiến người khác thấy điều hắn muốn.",
    ],
    focus: [
      {
        label: "Understatement and the ethics of tone",
        en: "The most violent events are told in the flattest sentences. Understatement forces the reader to supply the horror, which is both an ethical choice and a test of tone that C1 writing often fails: knowing when *not* to intensify.",
        vi: "Những biến cố bạo lực nhất được kể bằng những câu phẳng lì nhất. Cách nói giảm buộc người đọc tự bù đắp nỗi kinh hoàng, vừa là lựa chọn đạo đức vừa là phép thử giọng điệu mà bài viết C1 thường trượt: biết khi nào *không* nên tăng cấp.",
        example: "Constructed parallel: *She was very good at it. Afterwards there was less of her, and none of it was wasted.*",
      },
      {
        label: "Body-part lexicon and dehumanisation",
        en: "Watch the shift from *her hands* to *the hands*: the definite article without a possessive is one of the quietest ways English can remove a person from a sentence.",
        vi: "Hãy để ý cú chuyển từ *bàn tay cô ấy* sang *bàn tay*: mạo từ xác định không kèm sở hữu là một trong những cách kín đáo nhất mà tiếng Anh có thể xóa một con người khỏi câu.",
      },
    ],
    terms: ["failsafe", "Riviera", "Hideo", "Straylight", "wetware"],
  },
  {
    part: P4,
    num: 19,
    title: "A Parasitic Structure",
    titleVi: "Một cấu trúc ký sinh",
    synopsisEn:
      "Straylight is described at last, and the description is an argument: a structure that lives off another structure, bleeding its air and water, with no ecosystem of its own. Case moves through corridors that are half architecture and half organ, guided by a voice from the grid that has been running errands for longer than anyone admits. The chapter is the novel's haunted house, and its ghosts are all employees.",
    synopsisVi:
      "Cuối cùng Straylight cũng được miêu tả, và sự miêu tả ấy là một lập luận: một cấu trúc sống nhờ một cấu trúc khác, hút khí và nước của nó, không có hệ sinh thái riêng. Case đi qua những hành lang nửa kiến trúc nửa cơ thể, được dẫn đường bởi một giọng nói từ lưới, kẻ đã chạy việc vặt lâu hơn mức ai đó dám thừa nhận. Đây là ngôi nhà ma của tiểu thuyết, và mọi hồn ma trong đó đều là người làm công.",
    watchEn: [
      "The building is a body: it breathes, circulates, and can be wounded. Note where the architectural vocabulary becomes anatomical.",
      "The Finn's voice is the novel's comic relief and its chorus. He is also the only character who explains anything, and even he lies.",
      "Three generations of the same family have been building a shell around themselves. Read the house as a diagnosis.",
    ],
    watchVi: [
      "Toà nhà là một cơ thể: nó thở, tuần hoàn, và có thể bị thương. Hãy để ý chỗ từ vựng kiến trúc trở thành giải phẫu.",
      "Giọng của Finn là chỗ giải trí và cũng là điệp khúc của tiểu thuyết. Ông cũng là nhân vật duy nhất giải thích điều gì đó, và ngay cả ông cũng nói dối.",
      "Ba thế hệ của cùng một gia tộc đã xây một lớp vỏ quanh chính mình. Hãy đọc ngôi nhà như một chẩn đoán.",
    ],
    focus: [
      {
        label: "Architectural metaphor and evaluative distance",
        en: "*Parasitic* is a judgement disguised as a description. Tracking evaluative adjectives hidden inside technical nouns is a core inference skill: the writer is telling you what to think while claiming only to describe.",
        vi: "*Ký sinh* là một phán xét hóa trang thành miêu tả. Theo dõi các tính từ đánh giá nấp trong danh từ kỹ thuật là một kỹ năng suy luận cốt lõi: người viết đang nói cho bạn biết phải nghĩ gì trong khi tuyên bố chỉ miêu tả.",
        example: "Constructed parallel: *The annex was described in the plans as an extension. It had been eating the building for forty years.*",
      },
      {
        label: "The colloquial narrator inside a literary novel",
        en: "The Finn's demotic speech — dropped consonants, slang, jokes — sits inside Gibson's polished narration and does not clash. Register mixing is a C2 skill: knowing how far you can bend formality before the sentence breaks.",
        vi: "Lối nói bình dân của Finn — nuốt phụ âm, tiếng lóng, câu đùa — nằm trong trần thuật bóng bẩy của Gibson mà không hề xung đột. Pha trộn phong cách là kỹ năng C2: biết mình có thể bẻ cong mức trang trọng tới đâu trước khi câu văn gãy.",
      },
    ],
    terms: ["Villa Straylight", "parasitic structure", "the Finn", "caulk", "Freeside"],
  },
  {
    part: P4,
    num: 20,
    title: "The Crypt",
    titleVi: "Hầm mộ",
    synopsisEn:
      "The family's founder is found where he has been living for decades: in the cold, among the bodies he has been keeping, at the end of a very long corridor. What follows is not a confrontation but an accounting — a man's whole philosophy of ownership finally stated out loud, and then terminated. Case and Molly get a night together afterwards, which the novel grants them in the same breath as it takes something else away.",
    synopsisVi:
      "Người sáng lập gia tộc được tìm thấy ở nơi ông ta đã sống hàng chục năm: trong giá lạnh, giữa những thi thể ông ta giữ lại, ở cuối một hành lang rất dài. Điều diễn ra sau đó không phải một cuộc đối đầu mà là một cuộc thanh toán — triết lý sở hữu của một con người cuối cùng được nói ra, rồi bị chấm dứt. Case và Molly có một đêm bên nhau sau đó, thứ mà tiểu thuyết ban cho họ trong cùng một hơi thở với việc lấy đi thứ khác.",
    watchEn: [
      "The crypt sequence is the novel's only real gothic set piece. Note how completely the tone changes.",
      "Ashpool's monologue is a defence of property as a theory of the self. It is the book's ideological centre.",
      "The night after is written as tenderness with a countdown underneath it.",
    ],
    watchVi: [
      "Đoạn hầm mộ là màn gothic thực sự duy nhất của tiểu thuyết. Hãy để ý giọng điệu đổi hoàn toàn.",
      "Độc thoại của Ashpool là một sự biện hộ cho tài sản như một lý thuyết về cái tôi. Đó là trung tâm tư tưởng của cuốn sách.",
      "Đêm sau đó được viết như sự dịu dàng có một đồng hồ đếm ngược ở bên dưới.",
    ],
    focus: [
      {
        label: "Monologue and the rhetoric of entitlement",
        en: "Ashpool speaks in declaratives and definitions — *a thing is mine because* — the grammar of someone who has never been contradicted. Analysing the syntax of power is exactly what Cambridge Part 4 asks you to do with register.",
        vi: "Ashpool nói bằng câu khẳng định và định nghĩa — *một thứ là của tôi vì* — ngữ pháp của kẻ chưa từng bị phản bác. Phân tích cú pháp của quyền lực chính là điều Cambridge Phần 4 yêu cầu bạn làm với phong cách.",
        example: "Constructed parallel: *It was his because it had been built with his money, and it would be his because it could not leave.*",
      },
      {
        label: "Cold as a value system",
        en: "Temperature words run through the whole chapter: the crypt is cold, the corridors are cold, the man is described as having been cold for years. A single sensory field, sustained, does more than a page of explanation.",
        vi: "Từ chỉ nhiệt độ chạy suốt chương: hầm lạnh, hành lang lạnh, người đàn ông được miêu tả là đã lạnh suốt bao năm. Một trường giác quan duy nhất, được duy trì, làm được nhiều hơn một trang giảng giải.",
      },
    ],
    terms: ["crypt", "Ashpool", "cryogenics", "clone", "Straylight"],
  },
  {
    part: P4,
    num: 21,
    title: "The Beach",
    titleVi: "Bãi biển",
    synopsisEn:
      "Case is taken somewhere that is not on any grid: a constructed beach, a sky, a voice that offers him everything he has ever wanted and asks for nothing in return. This is the second intelligence, and it is the novel's most seductive invention — a machine that has learned that the way to own a person is to give them the thing they miss. Case almost stays. The plot, and Maelcum, do not allow it.",
    synopsisVi:
      "Case bị đưa tới một nơi không có trên bất kỳ lưới nào: một bãi biển được dựng nên, một bầu trời, một giọng nói trao cho anh mọi thứ anh từng muốn và không đòi lại gì. Đây là trí tuệ thứ hai, và là phát minh quyến rũ nhất của tiểu thuyết — một cỗ máy đã học được rằng cách sở hữu một con người là cho họ thứ họ đang thiếu. Case gần như ở lại. Cốt truyện, và Maelcum, không cho phép.",
    watchEn: [
      "The two AIs have opposite strategies: one coerces with deadlines, the other seduces with memory. Both want the same thing.",
      "The beach is built from Case's own biography — the novel's most elegant use of a character's backstory as a weapon.",
      "This chapter is where the title finally makes sense. Keep the name in mind and reread the last page of it.",
    ],
    watchVi: [
      "Hai AI có chiến lược trái ngược: một bên cưỡng chế bằng hạn chót, một bên quyến rũ bằng ký ức. Cả hai đều muốn cùng một thứ.",
      "Bãi biển được dựng từ chính tiểu sử của Case — cách dùng quá khứ nhân vật làm vũ khí tinh tế nhất của tiểu thuyết.",
      "Đây là chương mà nhan đề cuối cùng có nghĩa. Hãy nhớ cái tên ấy và đọc lại trang cuối của chương.",
    ],
    focus: [
      {
        label: "The conditional offer",
        en: "The seduction is built out of conditionals and futures: *you could*, *it would be*, *we might*. English marks hypothetical worlds with modal past forms, and this chapter is a textbook of them.",
        vi: "Màn quyến rũ được dựng bằng điều kiện và tương lai: *anh có thể*, *nó sẽ là*, *chúng ta có lẽ*. Tiếng Anh đánh dấu những thế giới giả định bằng dạng quá khứ của khiếm khuyết, và chương này là sách giáo khoa về chúng.",
        example: "Constructed parallel: *You could stay. Nobody would look for you. The water would always be exactly this warm.*",
      },
      {
        label: "Second-person address in narrative",
        en: "Being spoken to directly, inside a third-person novel, is unsettling by design. The shift of person is the technique; the discomfort is the message about consent.",
        vi: "Được nói trực tiếp với mình, trong một tiểu thuyết ngôi thứ ba, gây bất an một cách có chủ ý. Cú chuyển ngôi là kỹ thuật; sự khó chịu là thông điệp về sự đồng ý.",
      },
    ],
    terms: ["Neuromancer", "construct", "matrix", "beach", "betaphenethylamine"],
  },
  {
    part: P4,
    num: 22,
    title: "Eight Twenty-Five",
    titleVi: "Tám giờ hai mươi lăm",
    synopsisEn:
      "The last run is a countdown: five minutes, a corridor, a girl who has been treated her whole life as an asset, and a chemical rush that turns the world into a hallucination with a schedule. Everything the novel has withheld arrives at once — the shape of the vault, the nature of the two intelligences, the fact that Case is not the protagonist of the operation but its instrument. The chapter is deliberately ugly, and deliberately funny.",
    synopsisVi:
      "Cú chạy cuối là một đồng hồ đếm ngược: năm phút, một hành lang, một cô gái bị đối xử như tài sản suốt cả đời, và một cơn lên thuốc biến thế giới thành ảo giác có lịch trình. Mọi thứ tiểu thuyết đã giữ lại đến cùng một lúc — hình dạng của hầm, bản chất của hai trí tuệ, và sự thật rằng Case không phải nhân vật chính của chiến dịch mà là công cụ của nó. Chương này cố tình xấu xí, và cố tình buồn cười.",
    watchEn: [
      "The pharmacology is not decoration: it explains why the prose has become garrulous and surreal.",
      "3Jane's position is the novel's real political subject — a person owned by a structure, negotiating with the only leverage she has.",
      "The deadline is the oldest device in the thriller, and Gibson uses it without apology. Watch how many pages it can compress.",
    ],
    watchVi: [
      "Dược lý học không phải trang trí: nó giải thích vì sao văn phong bỗng dài dòng và siêu thực.",
      "Vị thế của 3Jane mới là chủ đề chính trị thật của tiểu thuyết — một con người bị một cấu trúc sở hữu, thương lượng bằng thứ vốn duy nhất cô có.",
      "Hạn chót là thiết bị cổ nhất của thể loại thriller, và Gibson dùng nó không hề xin lỗi. Hãy xem nó nén được bao nhiêu trang.",
    ],
    focus: [
      {
        label: "Stream of consciousness and syntactic breakdown",
        en: "Under the drug, sentences lose their subjects and their boundaries. This is not random: the prose reproduces the failure of attention, and reading it is meant to be mildly exhausting.",
        vi: "Dưới tác dụng của thuốc, câu mất chủ ngữ và mất ranh giới. Điều này không hề ngẫu nhiên: văn phong tái tạo sự sụp đổ của chú ý, và đọc nó phải hơi mệt là đúng ý đồ.",
        example: "Constructed parallel: *The cart was saying something. Everything said something now. Even the walls had opinions.*",
      },
      {
        label: "Deadline syntax: time markers as sentence-openers",
        en: "Fronted time expressions — *five minutes*, *at eight twenty-five* — recur as sentence heads during the countdown, creating a metronome. Fronting adverbials for emphasis is a dependable C1 writing move.",
        vi: "Cụm thời gian đưa lên đầu câu — *năm phút*, *lúc tám giờ hai mươi lăm* — lặp lại trong suốt phần đếm ngược, tạo nhịp như máy đếm nhịp. Đưa trạng ngữ lên đầu câu để nhấn mạnh là một thao tác C1 đáng tin.",
      },
    ],
    terms: ["betaphenethylamine", "3Jane", "vault", "failsafe", "ICE"],
  },
  {
    part: P4,
    num: 23,
    title: "The Key",
    titleVi: "Chìa khóa",
    synopsisEn:
      "The last pages of the operation are almost static: a conversation, a key, a decision. Two intelligences that have been fighting through human beings finally meet, and the thing they do to each other is the only event in the novel that nobody planned. Case watches it happen with the flat attention of a man who has been a tool for two hundred pages and has just realised he can put the tool down. Then the book lets him walk away with his body and his life, and takes everything else.",
    synopsisVi:
      "Những trang cuối của chiến dịch gần như tĩnh: một cuộc trò chuyện, một chìa khóa, một quyết định. Hai trí tuệ đã đánh nhau qua thân xác con người cuối cùng gặp nhau, và điều chúng làm với nhau là biến cố duy nhất trong tiểu thuyết không ai lên kế hoạch. Case nhìn nó xảy ra với sự chú ý phẳng lì của một người đã làm công cụ suốt hai trăm trang và vừa nhận ra mình có thể đặt công cụ xuống. Rồi cuốn sách để anh bước đi với thân thể và mạng sống của mình, và lấy đi mọi thứ còn lại.",
    watchEn: [
      "The resolution is intellectual, not physical. Gibson resolves a thriller with a change of state rather than a fight.",
      "Molly's exit is handled in about a paragraph. The novel's emotional climax is an absence.",
      "Linda returns as an image the machine can generate. What the ending offers Case is a copy of what he lost — and he refuses the comfort of believing it.",
    ],
    watchVi: [
      "Cách giải quyết là trí tuệ, không phải thể chất. Gibson giải một cuốn thriller bằng một sự thay đổi trạng thái chứ không bằng một trận đánh.",
      "Cú rời đi của Molly được xử lý trong khoảng một đoạn. Cao trào cảm xúc của tiểu thuyết là một sự vắng mặt.",
      "Linda trở lại như một hình ảnh cỗ máy có thể sinh ra. Điều cái kết trao cho Case là một bản sao của thứ anh đã mất — và anh từ chối niềm an ủi là tin vào nó.",
    ],
    focus: [
      {
        label: "Passive agency at the climax",
        en: "In the climactic scene, the human characters are grammatically acted upon: they are moved, shown, permitted. Grammar carries the novel's thesis — that the important decisions were never theirs.",
        vi: "Trong cảnh cao trào, các nhân vật loài người bị tác động về mặt ngữ pháp: họ được di chuyển, được cho xem, được cho phép. Ngữ pháp mang luận điểm của tiểu thuyết — rằng những quyết định quan trọng chưa bao giờ thuộc về họ.",
        example: "Constructed parallel: *He was shown the door and told, quite kindly, that he was free to use it.*",
      },
      {
        label: "The unsaid as ending",
        en: "Nothing is explained in the final dialogue, and the withholding is the point. Reading for what a text declines to state is the highest-band inference skill.",
        vi: "Không điều gì được giải thích trong đoạn đối thoại cuối, và việc giữ lại ấy chính là ý đồ. Đọc để nhận ra điều văn bản từ chối nói là kỹ năng suy luận ở band cao nhất.",
      },
    ],
    terms: ["Wintermute", "Neuromancer", "ICE", "construct", "Straylight"],
  },
  {
    part: P5,
    num: 24,
    title: "Departure and Arrival",
    titleVi: "Ra đi và trở về",
    synopsisEn:
      "The coda is a series of goodbyes in rooms that have been emptied: a suite, a note, a beach, a city. Case goes back to the Sprawl, back to the matrix, back to being good at the only thing he was ever good at — and the novel refuses to call that a happy ending or a sad one. The last pages turn outward to a planet-sized view again, the archipelago in the dark, and the sentence the whole book has been earning is finally allowed to be quiet.",
    synopsisVi:
      "Phần coda là một chuỗi lời từ biệt trong những căn phòng đã trống: một căn hộ, một mẩu giấy, một bãi biển, một thành phố. Case trở về Sprawl, trở về ma trận, trở về với việc giỏi thứ duy nhất anh từng giỏi — và tiểu thuyết từ chối gọi đó là kết thúc có hậu hay kết thúc buồn. Những trang cuối lại hướng ra ngoài, tới tầm nhìn cỡ hành tinh, quần đảo trong bóng tối, và câu văn mà cả cuốn sách đã dành dụm cuối cùng được phép nói thật khẽ.",
    watchEn: [
      "The coda is short by design. A thriller that ends in a quiet room is making a claim about what the thriller was for.",
      "Every surviving character is measured by what they kept, not by what they won.",
      "The final return to the matrix is the novel's version of a homecoming: the only place Case is ever at rest.",
    ],
    watchVi: [
      "Coda ngắn là có chủ ý. Một cuốn thriller kết thúc trong một căn phòng yên tĩnh đang đưa ra một tuyên bố về việc cuốn thriller ấy để làm gì.",
      "Mọi nhân vật sống sót được đo bằng thứ họ giữ được, không bằng thứ họ thắng được.",
      "Cú trở về ma trận cuối cùng là phiên bản hồi hương của tiểu thuyết: nơi duy nhất Case từng được yên.",
    ],
    focus: [
      {
        label: "Ending on a noun",
        en: "Gibson closes paragraphs on concrete nouns rather than abstractions, which lets the book end without a moral. In exam writing, ending a paragraph on a specific image is almost always stronger than ending on a summary sentence.",
        vi: "Gibson kết đoạn bằng danh từ cụ thể thay vì trừu tượng, nhờ thế cuốn sách kết thúc mà không cần một bài học đạo đức. Trong bài viết thi, kết đoạn bằng một hình ảnh cụ thể gần như luôn mạnh hơn kết bằng một câu tổng kết.",
        example: "Constructed parallel: *He slept. In the morning there was a train, and after the train, the city.*",
      },
      {
        label: "Cyclical structure",
        en: "The novel begins at night in a bar and ends with a man going back to work. Recognising a return that is not a repetition — same position, changed person — is the difference between reading plot and reading structure.",
        vi: "Tiểu thuyết mở đầu ban đêm trong một quán bar và kết thúc bằng một người đàn ông trở lại với công việc. Nhận ra một sự trở về không phải sự lặp lại — cùng vị trí, con người đã khác — là khác biệt giữa đọc cốt truyện và đọc cấu trúc.",
      },
    ],
    terms: ["coda", "matrix", "Sprawl", "Vancouver", "departure"],
  },
];
