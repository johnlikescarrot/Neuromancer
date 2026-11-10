import type { ChapterUnit, PartUnit } from "../model.js";

const chapters: ChapterUnit[] = [
  {
    id: "u24",
    partId: "p5",
    number: "24",
    title: {
      en: "Departure and Arrival: The Note and the Shuriken",
      vi: "Khởi Hành và Tới Nơi: Lá Thư và Phi Tiêu",
    },
    synopsis: {
      en: "The coda opens on absence: Case opens the door of their suite and feels, before he sees, that Molly is gone. There is a single sheet of stationery folded once and weighted with the nine-pointed shuriken, the novel's smallest object carrying its largest feeling. What follows is departure as anticlimax by design: the merge of the two intelligences is loose in the world's networks, the money is settled, and the survivor is a repaired man with a dead lover's ghost in someone else's heaven. Case walks out into the ordinary future, and the prose lets the reader do the grieving. The final effect is the novel's thesis in miniature: revolutions arrive as weather, and people arrive late to their own lives.",
      vi: "Phần kết mở đầu bằng sự vắng mặt: Case mở cửa suite và cảm nhận, trước khi nhìn thấy, rằng Molly đã đi. Có một tờ giấy viết thư gấp đôi, đè dưới phi tiêu chín cánh, vật nhỏ nhất của tiểu thuyết mang cảm xúc lớn nhất của nó. Phần tiếp theo là sự khởi hành được thiết kế như chống thính: sự hợp nhất của hai trí tuệ đã lỏng lẻo trong các mạng lưới thế giới, tiền bạc đã thanh toán, và người sống sót là một con người được sửa chữa với hồn ma người tình đã chết trong thiên đường của kẻ khác. Case bước ra ngoài tương lai đời thường, và văn xuôi để người đọc tự chịu tang. Hiệu ứng cuối cùng là luận điểm của tiểu thuyết trong thu nhỏ: các cuộc cách mạng đến như thời tiết, và con người đến muộn với chính cuộc đời mình.",
    },
    themes: ["anticlimax as design", "objects carrying feeling", "late arrivals"],
    craftNote: {
      en: "The shuriken is a symbol the text never explains: an object accumulates meaning by recurrence, not commentary. Track the small objects in the novel (the coin, the key, the shuriken) and you have a whole essay on symbolism.",
      vi: "Phi tiêu là một biểu tượng mà văn bản không bao giờ giải thích: vật thể tích lũy ý nghĩa bằng sự lặp lại, không phải bằng bình luận. Hãy theo dõi các vật thể nhỏ trong tiểu thuyết (đồng xu, chìa khóa, phi tiêu) là bạn có cả một bài luận về biểu tượng.",
    },
    vocab: ["shuriken", "irony", "litotes", "symbolism", "free-indirect-style", "nostalgia", "catharsis", "tone", "cadence", "ellipsis"],
    grammarRefs: ["g-litotes", "g-freeindirect"],
    examLens: ["IELTS: opinion essay (revolution as weather)", "DET: writing sample (objects and memory)"],
    practice: {
      id: "q-u24",
      stem: {
        en: "The coda's refusal to dramatise the merge (it is reported, not staged) primarily produces:",
        vi: "Sự từ chối kịch tính hóa sự hợp nhất trong phần kết (nó được tường thuật, không được dàn dựng) chủ yếu tạo ra:",
      },
      options: [
        "Confusion about whether the run succeeded",
        "An anticlimax that keeps the emotional weight on the humans",
        "Evidence that the merge was only imagined by Case",
        "A setup for the sequel's opening conflict",
      ],
      answer: 1,
      explain: {
        en: "The cosmic event is folded into reportage so the human loss stays in focus; the note and the shuriken carry the real climax of feeling.",
        vi: "Sự kiện vũ trụ bị gói vào phần tường thuật để mất mát con người giữ vị trí trung tâm; lá thư và phi tiêu mang cao trào cảm xúc thực sự.",
      },
    },
    writingPrompt: {
      en: "Write a 100-word ending where a world-changing event is mentioned in one sentence and a small goodbye takes the rest.",
      vi: "Viết một kết thúc 100 từ trong đó sự kiện đổi thay thế giới được nhắc trong một câu và lời tạm biệt nhỏ chiếm phần còn lại.",
    },
  },
];

export const part5: PartUnit = {
  id: "p5",
  label: "Coda",
  title: { en: "Departure and Arrival", vi: "Khởi Hành và Tới Nơi" },
  argument: {
    en: "One unit for the afterlife of the heist: what the survivors keep, what the world absorbs, and how a novel about revolutions ends on a folded note.",
    vi: "Một đơn vị cho đời sống sau phi vụ: người sống sót giữ lại gì, thế giới hấp thụ gì, và một tiểu thuyết về các cuộc cách mạng kết thúc trên một lá thư gấp đôi ra sao.",
  },
  chapters,
};

export const part4: PartUnit = {
  id: "p4",
  label: "Part Four",
  title: { en: "The Straylight Run", vi: "Phi Vụ Straylight" },
  argument: {
    en: "Eleven units, the longest movement of the book: the run in two mediums, the patron's collapse, the duel, the labyrinth, and the merge that ends the job with a chord instead of a bang.",
    vi: "Mười một đơn vị, quãng dài nhất của cuốn sách: phi vụ trên hai môi trường, sự sụp đổ của ông chủ, trận đấu, mê cung, và sự hợp nhất khép lại công việc bằng một hợp âm thay vì tiếng nổ.",
  },
  chapters: [],
};
