/**
 * Part essays — short orienting pieces that open each of the novel's five parts.
 */
import type { Block } from "../types.js";
import { h1, pair, bullets, table, callout } from "./kit.js";
import { chapters } from "./chapters.js";
import { chapterBlock } from "./assemble.js";

const partEssays: Record<string, { en: string[]; vi: string[] }> = {
  "Part One": {
    en: [
      "The first part does an unusual amount of work in very little space. In two chapters it establishes a city, a class system, an economy, a technology, a protagonist, a wound and a contract — and it does so without a single paragraph of explanation. Everything you need is present; nothing is presented to you.",
      "Watch how the novel handles Case's disability. It is not a metaphor for anything; it is a fact with a price, and the price is the engine of the plot. He does not want to be healed. He wants to be *plugged in*, which is a different and much more interesting desire — and the novel knows the difference.",
    ],
    vi: [
      "Phần đầu làm một khối lượng việc bất thường trong rất ít không gian. Chỉ hai chương mà nó dựng lên một thành phố, một hệ thống giai cấp, một nền kinh tế, một công nghệ, một nhân vật chính, một vết thương và một hợp đồng — và làm tất cả mà không có một đoạn giảng giải nào. Mọi thứ bạn cần đều có mặt; không thứ nào được trình bày sẵn cho bạn.",
      "Hãy để ý cách tiểu thuyết xử lý tàn tật của Case. Nó không phải ẩn dụ cho bất cứ thứ gì; nó là một sự thật có giá, và cái giá ấy là động cơ của cốt truyện. Anh không muốn được chữa lành. Anh muốn được *cắm vào*, một khao khát khác và thú vị hơn nhiều — và tiểu thuyết biết rõ sự khác biệt ấy.",
    ],
  },
  "Part Two": {
    en: [
      "The second part is a recruitment montage with a body count. A team is assembled out of parts: a guide who is a recording, a doctor who is a criminal, a gang who are artists, a city that is a market. Each acquisition teaches you one thing about the world and one thing about the employer.",
      "This is also where the novel's comic register opens up. The dead man's voice, the Panther Moderns' theatre, the pleasure Case takes in a difficult run — the humour is not relief from the grimness. It is the sound of professionals enjoying their work, which is exactly what makes the ending hurt.",
    ],
    vi: [
      "Phần hai là một màn chiêu mộ liên tục có kèm số người chết. Một đội được lắp từ các bộ phận: một người dẫn đường là bản ghi, một bác sĩ là tội phạm, một băng nhóm là nghệ sĩ, một thành phố là chợ. Mỗi lần thu nạp dạy bạn một điều về thế giới và một điều về ông chủ.",
      "Đây cũng là chỗ phong cách hài của tiểu thuyết mở ra. Giọng của người đã chết, màn trình diễn của bọn Panther Modern, niềm vui của Case trước một cú chạy khó — tiếng cười ở đây không phải chỗ trút nhẹ sau căng thẳng. Đó là âm thanh của những người chuyên nghiệp thích công việc của mình, và chính điều ấy khiến cái kết đau.",
    ],
  },
  "Part Three": {
    en: [
      "Freeside changes the novel's scale and its morality. Down below, money was a fact of life; up here it is the whole environment. The orbital city is a resort built inside a mountain that somebody owns, and the novel treats its beauty as evidence in a case it is quietly building.",
      "This is the part that slows down on purpose. Reconnaissance chapters, dinner chapters, a geography chapter: the machinery of a heist, given room to breathe. Enjoy the architecture. Everything the book will later break is standing in these pages.",
    ],
    vi: [
      "Freeside đổi quy mô và cả đạo đức của tiểu thuyết. Ở dưới kia, tiền là một phần của cuộc sống; ở trên này, nó là toàn bộ môi trường. Thành phố quỹ đạo là một khu nghỉ dưỡng xây trong một ngọn núi mà có người sở hữu, và tiểu thuyết coi vẻ đẹp của nó như chứng cứ trong một vụ án nó đang lặng lẽ dựng lên.",
      "Đây là phần cố tình chậm lại. Chương trinh sát, chương ăn tối, chương địa lý: guồng máy của một vụ trộm, được cho không gian để thở. Hãy tận hưởng kiến trúc. Mọi thứ cuốn sách sẽ phá về sau đều đang đứng trong những trang này.",
    ],
  },
  "Part Four": {
    en: [
      "Eleven chapters, one continuous operation, and a steady loss of control. The heist becomes a confrontation between two intelligences that have been using people as hands for decades, and the humans discover — late, and one at a time — that they were never the subject of the sentence.",
      "Structurally this is the novel's most adventurous part: a stoned hallucination sequence, a gothic crypt, a locked-room conversation with a machine, an escape that is really a job offer. If the first three parts teach you to read *Neuromancer*, this one asks you to read *with* it.",
    ],
    vi: [
      "Mười một chương, một chiến dịch liên tục, và sự mất kiểm soát đều đặn. Vụ trộm trở thành cuộc đối đầu giữa hai trí tuệ đã dùng con người làm bàn tay suốt nhiều thập kỷ, và loài người phát hiện — muộn, và từng người một — rằng họ chưa bao giờ là chủ ngữ của câu.",
      "Về cấu trúc, đây là phần táo bạo nhất của tiểu thuyết: một đoạn ảo giác do thuốc, một hầm mộ gothic, một cuộc trò chuyện trong phòng kín với một cỗ máy, một cuộc trốn thoát thực chất là một lời mời làm việc. Nếu ba phần đầu dạy bạn cách đọc *Neuromancer*, phần này yêu cầu bạn đọc *cùng* nó.",
    ],
  },
  Coda: {
    en: [
      "One chapter, and it is mostly silence. The coda pays out every promise the plot made and finds that the currency has changed: what the survivors get is not what they wanted, and the novel is honest enough not to call this unfair.",
      "Read the coda twice — once for plot, once for temperature. Notice how few sentences are needed to end a book that spent two hundred and fifty pages refusing to slow down.",
    ],
    vi: [
      "Một chương, và phần lớn là im lặng. Coda thanh toán mọi lời hứa mà cốt truyện đã đưa ra và phát hiện ra rằng đơn vị tiền tệ đã đổi: thứ những người sống sót nhận được không phải thứ họ muốn, và tiểu thuyết đủ trung thực để không gọi đó là bất công.",
      "Hãy đọc coda hai lần — một lần vì cốt truyện, một lần vì nhiệt độ. Hãy để ý chỉ cần bao nhiêu câu để kết thúc một cuốn sách đã dành hai trăm năm mươi trang từ chối chậm lại.",
    ],
  },
};

const partTitles: { key: string; id: string; title: string; vi: string; range: string }[] = [
  { key: "Part One", id: "part-one", title: "Part One · Chiba City Blues", vi: "Phần Một · Chiba City Blues", range: "Chapters 1–2" },
  { key: "Part Two", id: "part-two", title: "Part Two · The Shopping Expedition", vi: "Phần Hai · The Shopping Expedition", range: "Chapters 3–7" },
  { key: "Part Three", id: "part-three", title: "Part Three · Midnight in the Rue Jules Verne", vi: "Phần Ba · Midnight in the Rue Jules Verne", range: "Chapters 8–12" },
  { key: "Part Four", id: "part-four", title: "Part Four · The Straylight Run", vi: "Phần Bốn · The Straylight Run", range: "Chapters 13–23" },
  { key: "Coda", id: "coda", title: "Coda · Departure and Arrival", vi: "Coda · Ra đi và trở về", range: "Chapter 24" },
];

export const novelSection: Block[] = [
  ...partTitles.flatMap((part, index) => {
    const essay = partEssays[part.key];
    const guides = chapters.filter((c) => c.part.startsWith(part.key));
    const blocks: Block[] = [
      h1(part.title, part.id, `${index + 1} of 5 · ${part.range}`),
      pair(essay.en, essay.vi),
      ...guides.flatMap((g) => [chapterBlock(g)]),
    ];
    return blocks;
  }),
];
