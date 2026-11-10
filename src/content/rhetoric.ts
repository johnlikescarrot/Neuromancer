/**
 * Rhetoric & grammar compendium — twelve features of the novel's prose, each
 * tied to the exam skill it trains. Original analysis and constructed examples.
 */
import type { Block } from "../types.js";
import { h1, h2, pair, bullets, callout, table } from "./kit.js";

interface Feature {
  no: number;
  title: string;
  titleVi: string;
  what: string;
  whatVi: string;
  why: string;
  whyVi: string;
  exam: string;
  examVi?: string;
  example: string;
}

const features: Feature[] = [
  {
    no: 1,
    title: "Parataxis: clauses in a row",
    titleVi: "Parataxis: mệnh đề đặt cạnh nhau",
    what: "Coordination without subordination. Short independent clauses follow one another with *and*, or with nothing at all, instead of being nested inside a main clause.",
    whatVi: "Liên kết đẳng lập không có bậc phụ thuộc. Những mệnh đề độc lập ngắn nối tiếp nhau bằng *and*, hoặc không bằng gì cả, thay vì lồng vào một mệnh đề chính.",
    why: "It produces speed and moral flatness. Events do not cause each other; they merely follow, which is how violence feels to the person inside it.",
    whyVi: "Nó tạo tốc độ và sự phẳng lặng đạo đức. Biến cố không gây ra nhau; chúng chỉ nối tiếp, đúng như cảm giác của người ở bên trong bạo lực.",
    exam: "IELTS Writing: use parataxis deliberately for narrative, hypotaxis for argument. Mixed control of the two is a Band 7 marker.",
    example: "Constructed: *He paid. The door opened. The street was the same street.*",
  },
  {
    no: 2,
    title: "Asyndeton and the deleted conjunction",
    titleVi: "Asyndeton và sự vắng mặt của liên từ",
    what: "A list whose joints have been removed: three nouns, three verbs, no *and* before the last item.",
    whatVi: "Một danh sách bị cắt bỏ các khớp nối: ba danh từ, ba động từ, không có *and* trước mục cuối.",
    why: "Readers fill the gap themselves, and what they supply is always faster and uglier than what the writer would have written.",
    whyVi: "Người đọc tự lấp khoảng trống, và thứ họ bổ sung luôn nhanh hơn, xấu hơn thứ người viết có thể viết ra.",
    exam: "PTE summarising and Cambridge Use of English: recognising the missing connector is often the whole item.",
    example: "Constructed: *Rain, neon, a locked door.*",
  },
  {
    no: 3,
    title: "Noun stacking",
    titleVi: "Chồng danh từ",
    what: "Premodification with long strings of nouns and adjectives, where a clause would normally be used.",
    whatVi: "Tiền biến đổi bằng những chuỗi danh từ và tính từ dài, ở chỗ lẽ ra phải dùng một mệnh đề.",
    why: "The world arrives pre-categorised. Things have already been sorted into types before the sentence gets a chance to judge them.",
    whyVi: "Thế giới đến trong tình trạng đã được phân loại sẵn. Sự vật đã được xếp vào loại trước khi câu văn kịp phán xét.",
    exam: "Academic writing rewards precision, not density. Learn to *unstack* noun phrases in your own prose and to *read* them in others'.",
    example: "Constructed: *coffin-hotel corridor light*",
  },
  {
    no: 4,
    title: "Present tense as permanent present",
    titleVi: "Hiện tại như một hiện tại vĩnh viễn",
    what: "The whole novel is narrated in the present, including memory and backstory.",
    whatVi: "Toàn bộ tiểu thuyết được kể ở thì hiện tại, kể cả ký ức và quá khứ.",
    why: "It removes the safety of retrospection. Nothing has been survived, because nothing is over.",
    whyVi: "Nó lấy đi sự an toàn của việc nhìn lại. Không gì đã được sống qua, vì không gì đã kết thúc.",
    exam: "TOEFL rhetorical-purpose items frequently ask why an author chooses a tense. The answer is always about certainty and distance.",
    example: "Constructed: *Eleven years ago he is standing in the same rain, and the rain is now.*",
  },
  {
    no: 5,
    title: "Free indirect discourse",
    titleVi: "Diễn ngôn tự do gián tiếp",
    what: "A character's thought or idiom appears in the narrator's third person, without quotation marks or *he thought*.",
    whatVi: "Suy nghĩ hoặc cách nói của nhân vật xuất hiện trong ngôi thứ ba của người kể, không có ngoặc kép hay *he thought*.",
    why: "It blurs the boundary between Case's mind and the machine's voice — a formal equivalent of the novel's central anxiety about who is speaking.",
    whyVi: "Nó làm nhòe ranh giới giữa tâm trí Case và giọng của cỗ máy — tương đương hình thức của nỗi lo trung tâm trong tiểu thuyết: ai đang nói.",
    exam: "C2 reading: identifying whose opinion a sentence carries. In writing, it is a way to vary narrative distance without quotation.",
    example: "Constructed: *Fine, he thought, or the voice thought, or nobody did.*",
  },
  {
    no: 6,
    title: "Neologism by compounding",
    titleVi: "Từ mới bằng ghép hình vị",
    what: "New words built from existing English pieces — *deck*, *simstim*, *ICE* — so that meaning is inferable from morphology and context together.",
    whatVi: "Từ mới được dựng từ những mảnh tiếng Anh có sẵn — *deck*, *simstim*, *ICE* — để nghĩa suy ra được từ hình thái và ngữ cảnh cùng lúc.",
    why: "It lets Gibson be technical without being didactic: the reader learns the vocabulary the way a newcomer learns a trade's slang, by exposure.",
    whyVi: "Nó cho phép Gibson vừa kỹ thuật vừa không lên lớp: người đọc học từ vựng theo cách người mới học tiếng lóng của một nghề — bằng phơi nhiễm.",
    exam: "DET read-and-select and Cambridge word formation both test morphological reasoning. Practise guessing from roots before checking the gloss.",
    example: "Constructed: *a sleep-deck, a wet-ware courier, a dead-channel sky*",
  },
  {
    no: 7,
    title: "Nominalisation as institutional voice",
    titleVi: "Danh từ hóa như giọng thể chế",
    what: "Verbs become abstract nouns — *verification*, *disposition*, *extraction* — and the agent disappears.",
    whatVi: "Động từ biến thành danh từ trừu tượng — *verification*, *disposition*, *extraction* — và chủ thể biến mất.",
    why: "The corporations in this novel do not act; processes occur. Grammar is where their impunity lives.",
    whyVi: "Các tập đoàn trong tiểu thuyết này không hành động; các quy trình diễn ra. Ngữ pháp chính là nơi trú ngụ của sự vô trách nhiệm của chúng.",
    exam: "The single most useful feature for academic writing — and the most dangerous. Nominalise to compress; keep the agent when accountability matters.",
    example: "Constructed: *Retrieval was authorised before the ownership question had been resolved.*",
  },
  {
    no: 8,
    title: "Absolute constructions",
    titleVi: "Cấu trúc tuyệt đối",
    what: "A noun plus a participle, attached to a sentence without a conjunction: *hands shaking, he reached for the deck*.",
    whatVi: "Một danh từ cộng phân từ, gắn vào câu không cần liên từ: *tay run, anh với lấy chiếc deck*.",
    why: "Two events, one sentence, no stated causality. The compression is exactly what the novel's action scenes need.",
    whyVi: "Hai biến cố, một câu, không nêu quan hệ nhân quả. Sự nén ấy đúng là thứ các cảnh hành động của tiểu thuyết cần.",
    exam: "A signature C1/C2 structure. Cambridge Part 1–4 transformation items love it; examiners reward one or two per essay, not six.",
    example: "Constructed: *Her eyes still on the door, she answered the question he had not asked.*",
  },
  {
    no: 9,
    title: "Inversion after fronted adverbials",
    titleVi: "Đảo ngữ sau trạng ngữ đầu câu",
    what: "A fronted negative or restrictive adverbial triggers subject–auxiliary inversion: *not once did he ask*.",
    whatVi: "Một trạng ngữ phủ định hoặc giới hạn đứng đầu câu kéo theo đảo ngữ trợ động từ: *not once did he ask*.",
    why: "It gives emphasis without adjectives, and it makes a sentence sound like a verdict.",
    whyVi: "Nó tạo nhấn mạnh mà không cần tính từ, và khiến câu văn nghe như một phán quyết.",
    exam: "High-value Cambridge structure; overuse reads as a party trick. One well-placed inversion per piece of writing is worth more than five.",
    example: "Constructed: *Only later would he understand what the suite had cost, and who had paid.*",
  },
  {
    no: 10,
    title: "Deixis and the missing compass",
    titleVi: "Chỉ định và chiếc la bàn thiếu",
    what: "Directions and times given relative to an unstated position: *in*, *up*, *further along*, *tonight*.",
    whatVi: "Phương hướng và thời gian được nêu tương đối so với một vị trí không được nói ra: *in*, *up*, *further along*, *tonight*.",
    why: "The reader is placed inside a body and a city without being told where either one is. Disorientation is a technique, not an accident.",
    whyVi: "Người đọc được đặt vào trong một thân thể và một thành phố mà không được cho biết mình đang ở đâu. Mất phương hướng là kỹ thuật, không phải sự cố.",
    exam: "Cohesion and reference questions (IELTS matching, TOEFL reference items) are deixis tests in disguise.",
    example: "Constructed: *Two junctions in, the corridor began to feel like the inside of a throat.*",
  },
  {
    no: 11,
    title: "Synaesthesia and sensory substitution",
    titleVi: "Cảm giác chéo và thay thế giác quan",
    what: "One sense described in the vocabulary of another: data has texture, cold has a colour, sound has weight.",
    whatVi: "Một giác quan được miêu tả bằng từ vựng của giác quan khác: dữ liệu có kết cấu, lạnh có màu, âm thanh có trọng lượng.",
    why: "Cyberspace has no native senses. To make it perceptible, Gibson has to borrow from the body — which is also the novel's way of insisting that the body is not optional.",
    whyVi: "Không gian mạng không có giác quan bản địa. Để khiến nó cảm nhận được, Gibson phải vay mượn từ thân thể — và đó cũng là cách tiểu thuyết khẳng định thân thể không phải thứ tùy chọn.",
    exam: "Descriptive writing at C1/C2 lives on this: replace the abstract adjective with a sensory one from another channel.",
    example: "Constructed: *The ice was the temperature of a doorknob in winter, and it tasted of batteries.*",
  },
  {
    no: 12,
    title: "Understatement and the flat close",
    titleVi: "Nói giảm và cái kết phẳng",
    what: "The most extreme event is given the least emphatic sentence, often ending on a concrete noun.",
    whatVi: "Biến cố cực đoan nhất được trao câu văn ít nhấn mạnh nhất, thường kết bằng một danh từ cụ thể.",
    why: "Restraint transfers the work to the reader and makes the moment unarguable. It is the opposite of melodrama, and it is much harder.",
    whyVi: "Sự tiết chế chuyển công việc sang người đọc và khiến khoảnh khắc ấy không thể tranh cãi. Đó là phản đề của kịch tính hóa, và khó hơn nhiều.",
    exam: "Tone questions in every exam. If a passage is about something terrible and the prose is calm, the answer is never 'the author does not care'.",
    example: "Constructed: *They buried the deck with him. It seemed like the polite thing to do.*",
  },
];

export const rhetoricSection: Block[] = [
  h1("Rhetoric & grammar: how the sentences work", "rhetoric", "The apparatus"),
  pair(
    "Twelve features, ordered roughly from the smallest unit (two clauses in a row) to the largest effect (the tone of an ending). Each entry gives what the feature is, why Gibson uses it, what it trains you for in an exam, and a constructed example — modelled on the novel's habits but written for this book, so that nothing here is a substitute for reading Gibson himself.",
    "Mười hai đặc điểm, sắp xếp đại khái từ đơn vị nhỏ nhất (hai mệnh đề đặt cạnh nhau) tới hiệu quả lớn nhất (giọng điệu của một cái kết). Mỗi mục nêu: đặc điểm ấy là gì, vì sao Gibson dùng nó, nó rèn cho bạn kỹ năng gì trong thi cử, và một ví dụ tự soạn — mô phỏng thói quen của tiểu thuyết nhưng viết cho cuốn sách này, để không có gì ở đây thay thế được việc đọc chính Gibson.",
    true,
  ),
  table(
    ["#", "Feature", "Exam home", "Band value"],
    [0.3, 1.5, 2.1, 1.1],
    [
      ["1", "Parataxis", "IELTS Writing Task 1/2; TOEFL sentence simplification", "7.0+"],
      ["2", "Asyndeton", "PTE summary; Cambridge Use of English", "7.0+"],
      ["3", "Noun stacking", "Academic reading; TOEFL vocabulary in context", "C1"],
      ["4", "Present-tense narration", "TOEFL rhetorical purpose", "C1"],
      ["5", "Free indirect discourse", "C2 reading; narrative writing", "C2"],
      ["6", "Neologism / compounding", "DET read-and-select; Cambridge word formation", "C1"],
      ["7", "Nominalisation", "Academic writing; Cambridge register transfer", "7.0+"],
      ["8", "Absolute constructions", "Cambridge Key Word Transformation", "C1/C2"],
      ["9", "Inversion", "Cambridge Use of English; IELTS GT letters", "C1/C2"],
      ["10", "Deixis", "IELTS matching; TOEFL reference items", "C1"],
      ["11", "Synaesthesia", "Descriptive writing; DET interactive writing", "C2"],
      ["12", "Understatement", "Tone and attitude questions in all five exams", "C1/C2"],
    ],
    "Table 3. The twelve features and the items they predict.",
  ),
  ...features.flatMap((f): Block[] => [
    h2(`${f.no}. ${f.title}`, f.titleVi),
    pair(`**What it is.** ${f.what}`, `**Đó là gì.** ${f.whatVi}`),
    pair(`**Why Gibson uses it.** ${f.why}`, `**Vì sao Gibson dùng nó.** ${f.whyVi}`),
    pair(`**What it trains.** ${f.exam}`, `**Nó rèn gì.** ${f.examVi ?? f.exam}`),
    pair(`*${f.example}*`, ""),
  ]),
  callout(
    "How to practise a feature",
    [
      "Take one feature a week. On Monday, find three instances in the novel and copy only the sentence structure — not the content. On Wednesday, write four sentences of your own in the same shape about your own subject. On Friday, use exactly one of them in a timed essay. One feature, three touches, is how a structure becomes available under pressure.",
    ],
    [
      "Mỗi tuần lấy một đặc điểm. Thứ Hai, tìm ba chỗ trong tiểu thuyết và chỉ chép lại cấu trúc câu — không chép nội dung. Thứ Tư, viết bốn câu của bạn theo đúng hình dạng ấy về chủ đề của bạn. Thứ Sáu, dùng đúng một trong số đó trong một bài luận có bấm giờ. Một đặc điểm, ba lần chạm, là cách một cấu trúc trở nên sẵn dùng khi bị sức ép.",
    ],
  ),
];
