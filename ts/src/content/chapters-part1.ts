import type { ChapterUnit, PartUnit } from "../model.js";

const chapters: ChapterUnit[] = [
  {
    id: "u01",
    partId: "p1",
    number: "1",
    title: {
      en: "Dead Channel: Ninsei and the Man Who Lost the Matrix",
      vi: "Kêng Chết: Ninsei và Người Đánh Mất Ma Trận",
    },
    synopsis: {
      en: "The novel opens on the grey static of a dead television channel hanging over a Japanese port, and narrows fast onto Case, a young data-thief marooned in the Chiba underworld. His nerves were deliberately burned by a former employer as punishment, so the one thing he was brilliant at, riding the matrix from a deck, is now closed to him. He drifts through Ninsei's bars, coffin hotels and black-market clinics, spending what little he has, burning bridges, and quietly courting death. Around him the street does its business: implants, stolen organs, corporate samurai. Two figures notice him: Molly, a street samurai whose mirrored lenses hide her eyes and whose fingernails hide blades, and the shadow of a patron who needs a cowboy with nothing left to lose. The unit closes with Molly's blades at someone's throat and a smile: the future has hired him.",
      vi: "Tiểu thuyết mở đầu bằng lớp nhiễu xám của chiếc tivi dò kênh chết lơ lửng trên một cảng biển Nhật Bản, rồi nhanh chóng thu vào Case, một tên trộm dữ liệu trẻ mắc kẹt trong thế giới ngầm Chiba. Thần kinh của anh bị chủ cũ cố ý thiêu cháy để trừng phạt, nên thứ duy nhất anh xuất sắc, cưỡi ma trận từ bàn điều khiển, giờ đã đóng lại với anh. Anh trôi dạt qua các quán bar, khách sạn quan tài và phòng khám chợ đen ở Ninsei, tiêu nốt chút tiền còn lại, đốt cháy các cây cầu, và âm thầm tìm đến cái chết. Quanh anh, đường phố buôn bán như thường: cấy ghép, nội tạng ăn cắp, samurai doanh nghiệp. Hai bóng người để mắt tới anh: Molly, nữ samurai đường phố với kính gương che mắt và lưỡi dao giấu dưới móng tay, và bóng dáng của một ông chủ cần một cowboy không còn gì để mất. Đơn vị khép lại với lưỡi dao của Molly kề cổ ai đó và một nụ cười: tương lai đã thuê anh.",
    },
    themes: ["disembodiment", "addiction", "the street as marketplace"],
    craftNote: {
      en: "Gibson withholds exposition and trusts imagery: brands, prices and body parts do the world-building. Notice how few verbs of feeling Case is given; his emotion arrives as weather and inventory, which is the free indirect style the Grammar Masterclass unpacks.",
      vi: "Gibson lược bỏ giải thích và tin vào hình ảnh: nhãn hiệu, giá cả và các bộ phận cơ thể đảm nhiệm việc xây dựng thế giới. Hãy để ý Case được cho rất ít động từ cảm xúc; cảm xúc của anh đến như thời tiết và bảng kê, đúng kiểu tự do gián tiếp mà Chuyên đề Ngữ pháp sẽ mổ xẻ.",
    },
    vocab: [
      "matrix",
      "console-cowboy",
      "cyberspace",
      "black-clinic",
      "nerve-splicing",
      "mycotoxin",
      "street-samurai",
      "razors",
      "arcology",
      "meat",
    ],
    grammarRefs: ["g-asyndeton", "g-metaphor"],
    examLens: ["TOEFL: inference from imagery", "IELTS: writer's tone and attitude"],
    practice: {
      id: "q-u01",
      stem: {
        en: "The opening image (a sky the colour of a dead channel) primarily serves to:",
        vi: "Hình ảnh mở đầu (bầu trời màu tivi dò kênh chết) chủ yếu phục vụ mục đích:",
      },
      options: [
        "Explain the pollution technology has caused, in explicit terms",
        "Establish a world where the man-made has replaced the natural, without explaining it",
        "Introduce Case's profession through metaphor",
        "Signal that the novel is set in the distant past",
      ],
      answer: 1,
      explain: {
        en: "The image does world-building by inference: nature is gone, media residue is the default sky, and nothing is explained. It says nothing explicit about pollution policy or Case's job.",
        vi: "Hình ảnh xây dựng thế giới bằng suy luận: thiên nhiên biến mất, dư ảnh truyền thông là bầu trời mặc định, và không có gì được giải thích tường minh. Nó không nói gì tường minh về chính sách ô nhiễm hay nghề của Case.",
      },
    },
    writingPrompt: {
      en: "In 120 words, describe a familiar place (a station, a market) as if its technology were already archaeology. Use one simile and no proper nouns.",
      vi: "Trong 120 từ, hãy mô tả một nơi quen thuộc (nhà ga, khu chợ) như thể công nghệ của nó đã là khảo cổ. Dùng một phép so sánh và không dùng danh từ riêng.",
    },
  },
  {
    id: "u02",
    partId: "p1",
    number: "2",
    title: {
      en: "The Rebuilt Man: Surgery, Contract, Departure",
      vi: "Con Người Được Tái Tạo: Phẫu Thuật, Hợp Đồng, Khởi Hành",
    },
    synopsis: {
      en: "Case wakes in a Chiba Hilton suite that feels enormous after a year of coffin hotels, and the new body is a purchase: repaired nerves, new tissue, a clean bill of metabolism, all paid for by Armitage, the improbably handsome employer who will not explain himself. Molly plays fixer and bodyguard, ferrying Case between clinic checkups and the docks, testing him constantly with the flat affect of a professional. Armitage lays out the offer obliquely: the work involves the matrix, the pay is freedom, and the penalty for cheating is the old damaged body restored. Case accepts because refusing is a kind of death he has already tried. The part ends on a hovercraft leaving Chiba, the arcologies folding into mist: every rebuilt man is also a repossessed one.",
      vi: "Case tỉnh giấc trong một suite khách sạn Chiba Hilton rộng mênh mông sau một năm ngủ quan tài, và cơ thể mới là một món hàng: thần kinh được sửa, mô mới, bảng chuyển hóa sạch, tất cả do Armitage, ông chủ đẹp trai đến mức phi lý và tuyệt đối không giải thích mình, chi trả. Molly làm người môi giới và vệ sĩ, chở Case giữa các lần tái khám và bến cảng, không ngừng thử thách anh bằng vẻ vô cảm của dân chuyên nghiệp. Armitage đưa ra lời đề nghị một cách quanh co: công việc liên quan đến ma trận, phần thưởng là tự do, và hình phạt cho sự lừa dối là cơ thể hư hỏng cũ sẽ được khôi phục. Case chấp nhận vì từ chối là một kiểu cái chết mà anh đã từng thử. Phần kết thúc trên một tàu đệm khí rời Chiba, các arcology tan vào sương mù: mọi con người được tái tạo cũng là một con người bị tịch thu.",
    },
    themes: ["the leased self", "patronage", "bodies as platforms"],
    craftNote: {
      en: "Watch the sentence 'the new body is a purchase' logic play out in imagery rather than argument. Gibson writes economics as anatomy; when you revise your own essays, try converting one abstract claim into three concrete nouns.",
      vi: "Hãy theo dõi logic 'cơ thể mới là một món hàng' được thể hiện qua hình ảnh chứ không qua lập luận. Gibson viết kinh tế học như giải phẫu; khi bạn sửa bài luận, hãy thử chuyển một khẳng định trừu tượng thành ba danh từ cụ thể.",
    },
    vocab: ["black-clinic", "prosthesis", "commodify", "embodiment", "arcology", "socket", "jack-in", "meat", "construct", "agency"],
    grammarRefs: ["g-absolute", "g-participle"],
    examLens: ["PTE: re-tell lecture (re-tell this unit aloud)", "Cambridge: word formation (purchase/possess)"],
    practice: {
      id: "q-u02",
      stem: {
        en: "Armitage's contract is structured so that Case's alternative to compliance is:",
        vi: "Hợp đồng của Armitage được cấu trúc sao cho phương án thay thế việc tuân thủ của Case là:",
      },
      options: [
        "A comfortable retirement in the Sprawl",
        "A restored body that traps him in his old damage",
        "Immediate exposure to the Turing police",
        "A debt paid by working for the zaibatsu",
      ],
      answer: 1,
      explain: {
        en: "The punishment is restoration of the ruined body: freedom is the payment, and its withdrawal is the threat. The other options invent terms the chapter never offers.",
        vi: "Hình phạt là khôi phục cơ thể tan nát: tự do là khoản thanh toán, và việc cắt nó là lời đe dọa. Các phương án khác bịa ra điều kiện mà chương không hề đưa ra.",
      },
    },
    writingPrompt: {
      en: "Write a 100-word contract clause for 'one last job' in a future you invent. Underline every word that prices a human being.",
      vi: "Viết một điều khoản hợp đồng 100 từ cho 'phi vụ cuối cùng' trong một tương lai do bạn tự nghĩ. Gạch dưới mọi từ định giá một con người.",
    },
  },
];

export const part1: PartUnit = {
  id: "p1",
  label: "Part One",
  title: { en: "Chiba City Blues", vi: "Blues Thành Phố Chiba" },
  argument: {
    en: "A man stripped of his only talent is rebuilt as someone else's instrument. The two units establish the novel's economics of the body and its grammar of the street.",
    vi: "Một người bị tước đoạt tài năng duy nhất được tái tạo thành công cụ của kẻ khác. Hai đơn vị thiết lập nền kinh tế về cơ thể và ngữ pháp đường phố của tiểu thuyết.",
  },
  chapters,
};
