/**
 * Front matter: preface, the exam map, and the structural orientation.
 * All prose here is original editorial writing for this companion.
 */
import type { Block } from "../types.js";
import { h1, h2, h3, pair, bullets, table, callout, quote, only } from "./kit.js";

export const frontMatter: Block[] = [
  h1("Preface: a companion for a difficult book", "preface", "Front matter"),

  pair(
    "There is a particular kind of reading problem that *Neuromancer* creates. The sentences are short — sometimes only three or four words long — and yet the page in front of you feels dense, because every second noun is a thing that does not exist, and Gibson never stops to explain any of it. You are forty pages in before you realise that nobody is going to tell you what a deck is, or why Case cannot enter the matrix, or what the Tessier-Ashpool family actually does for money. The novel treats exposition as a failure of nerve.",
    "Có một kiểu khó đọc rất riêng mà *Neuromancer* tạo ra. Câu văn ngắn — có khi chỉ ba bốn chữ — nhưng trang sách trước mắt lại đặc quánh, bởi cứ hai danh từ thì một cái là thứ không hề tồn tại, và Gibson không bao giờ dừng lại giải thích. Bạn đọc tới trang bốn mươi mới nhận ra rằng sẽ không ai nói cho bạn biết *deck* là gì, vì sao Case không thể vào ma trận, hay gia tộc Tessier-Ashpool thực sự kiếm tiền bằng cách nào. Tiểu thuyết này coi việc giảng giải là một sự hèn nhát.",
    true,
  ),

  pair(
    "That difficulty is not a defect, and it is not only a matter of invented vocabulary. It is a difficulty of **grammar** and of **information design**: who is speaking, where a scene is taking place, whether a paragraph is happening now or eleven years ago. This companion exists to make that difficulty legible — to name the machinery, level the lexicon, and give you a way to talk about what Gibson is doing with a sentence.",
    "Cái khó ấy không phải khuyết điểm, và cũng không chỉ là chuyện từ vựng được phát minh. Đó còn là cái khó của **ngữ pháp** và của **thiết kế thông tin**: ai đang nói, cảnh này diễn ra ở đâu, đoạn văn này đang xảy ra lúc này hay mười một năm trước. Cuốn sách này tồn tại để làm cho cái khó ấy trở nên rõ ràng: gọi tên guồng máy, phân tầng vốn từ, và cho bạn cách nói về những gì Gibson đang làm với một câu văn.",
  ),

  h2("What is in this book", "Cuốn sách này có gì"),

  bullets(
    [
      "**Twenty-four chapter guides.** For each chapter: a synopsis, a short list of what to watch, a language-focus note on the grammar or rhetoric doing the work, and the chapter's key terms.",
      "**A rhetoric and grammar compendium.** Twelve recurring features of Gibson's prose, each explained in plain terms and tied to the exam skill it trains.",
      "**A levelled lexicon.** Every headword carries IPA, part of speech, a CEFR band, an English gloss, a Vietnamese gloss and a note on why it matters in this novel.",
      "**An exam workbook.** Lexical precision, grammar transformation, paraphrase and style, inference reading, writing tasks and speaking prompts — with an answer key and model answers.",
      "**Appendices.** A character map, a structural timeline, Gibson's coinages, and a Vietnamese–English index.",
    ],
    [
      "**Hai mươi tư bài dẫn chương.** Mỗi chương gồm: tóm lược cốt truyện, danh sách ngắn những điểm cần chú ý, ghi chú về ngữ pháp – tu từ học đang gánh cảnh đó, và các thuật ngữ then chốt.",
      "**Tuyển tập tu từ học và ngữ pháp.** Mười hai đặc trưng lặp lại trong văn phong Gibson, giải thích bằng ngôn ngữ giản dị và gắn với kỹ năng thi mà nó rèn luyện.",
      "**Từ điển phân tầng CEFR.** Mỗi mục từ có phiên âm IPA, từ loại, mức CEFR, nghĩa tiếng Anh, nghĩa tiếng Việt và ghi chú về vai trò của nó trong tiểu thuyết.",
      "**Sách bài tập luyện thi.** Chính xác từ vựng, biến đổi ngữ pháp, diễn đạt lại và phong cách, đọc suy luận, bài viết và bài nói — kèm đáp án và bài mẫu.",
      "**Phụ lục.** Sơ đồ nhân vật, dòng thời gian cấu trúc, những từ do Gibson tạo ra, và bảng tra Việt – Anh.",
    ],
  ),

  h2("How to use it", "Cách sử dụng"),

  pair(
    "Read the chapter first, then the guide. The guides assume you have just finished the pages they describe; they summarise instead of retelling, and they spoil freely. If you are reading the novel for a class, use the guide as a debrief: what happened, what it was for, what the language was doing.",
    "Hãy đọc chương trước, rồi mới đọc bài dẫn. Các bài dẫn giả định rằng bạn vừa đọc xong đúng những trang nó nói tới; chúng tóm lược chứ không kể lại, và tiết lộ nội dung không hề e dè. Nếu bạn đọc tiểu thuyết cho một lớp học, hãy dùng bài dẫn như một buổi tổng kết: chuyện gì đã xảy ra, để làm gì, và ngôn ngữ đang làm gì.",
  ),

  pair(
    "If you are reading for English, work in three passes. Pass one: read the chapter with the glossary open in a second window and mark only the headwords marked **C1** or **C2**. Pass two: read the guide's language focus and find the feature in the chapter yourself before you read the explanation. Pass three: do one exercise set from the workbook. Three passes over a chapter is worth more than one pass over the whole novel.",
    "Nếu bạn đọc vì tiếng Anh, hãy đọc theo ba lượt. Lượt một: đọc chương với từ điển mở ở cửa sổ thứ hai, chỉ đánh dấu những mục từ được ghi **C1** hoặc **C2**. Lượt hai: đọc phần trọng tâm ngôn ngữ, rồi tự tìm đặc điểm đó trong chương trước khi đọc lời giải thích. Lượt ba: làm một bộ bài tập trong sách bài tập. Ba lượt trên một chương có giá trị hơn một lượt trên cả cuốn tiểu thuyết.",
  ),

  callout(
    "A note on quotation",
    [
      "This is a critical companion, not an edition of the novel. No chapter, scene or passage of *Neuromancer* is reproduced here; where the analysis needs to point at Gibson's wording, it quotes no more than a few words, in the way any close-reading essay must. Keep your own copy of the novel open beside this one.",
    ],
    [
      "Đây là sách đồng hành phê bình, không phải một ấn bản của tiểu thuyết. Không có chương, cảnh hay đoạn văn nào của *Neuromancer* được in lại ở đây; khi phần phân tích cần chỉ đúng vào cách dùng từ của Gibson, sách chỉ trích vài chữ, đúng như mọi bài bình giảng văn bản vẫn phải làm. Hãy để bản *Neuromancer* của bạn mở bên cạnh cuốn này.",
    ],
  ),

  h2("A note on the levels", "Ghi chú về các mức độ"),

  pair(
    "Bands in the lexicon follow the Common European Framework. **B2** is confident upper-intermediate: the word is useful but not yet the mark of an advanced reader. **C1** is the vocabulary that separates a 6.5 from a 7.5 in IELTS, or a 95 from a 110 in TOEFL. **C2** marks either rare literary usage or a term whose precision matters more than its frequency. A small number of entries are labelled *specialist* — words from computing, medicine, finance or navigation that an academic reader is expected to be able to handle even if they never produce them.",
    "Các mức trong từ điển theo Khung tham chiếu châu Âu (CEFR). **B2** là trình độ trung cao vững vàng: từ hữu ích nhưng chưa phải dấu hiệu của người đọc cao cấp. **C1** là nhóm từ phân định 6.5 với 7.5 IELTS, hay 95 với 110 TOEFL. **C2** đánh dấu cách dùng văn chương hiếm gặp, hoặc một thuật ngữ mà độ chính xác quan trọng hơn tần suất. Một số ít mục được ghi *chuyên ngành* — từ của tin học, y học, tài chính hay hàng hải mà người đọc học thuật cần xử lý được, kể cả khi không bao giờ dùng để viết.",
  ),

  // ---------------------------------------------------------------- exam map
  h1("The exam map: what this book is calibrated to", "exam-map", "Front matter"),

  pair(
    "Five different examinations, five different dialects of the same underlying construct. All of them, at the level this edition targets, ask for the same three things: a reader who can process long and syntactically dense text without losing the thread; a writer who controls a wide lexical range with precision rather than decoration; and a user of English who can hear register — who knows when a word is too formal, too clinical, too slangy for the sentence around it. *Neuromancer* is an unusually good gym for all three.",
    "Năm kỳ thi khác nhau, năm phương ngữ của cùng một cấu trúc năng lực. Ở mức mà ấn bản này nhắm tới, cả năm đều đòi ba thứ như nhau: một người đọc xử lý được văn bản dài và dày đặc cú pháp mà không mất mạch; một người viết điều khiển được vốn từ rộng với độ chính xác thay vì trang trí; và một người dùng tiếng Anh nghe được *register* — biết khi nào một từ quá trang trọng, quá lâm sàng, hay quá đường phố so với câu xung quanh. *Neuromancer* là một phòng tập hiếm có cho cả ba.",
  ),

  table(
    ["Examination", "Target band", "What it actually measures at this level", "Where this book trains it"],
    [1.05, 0.95, 2.5, 2.2],
    [
      [
        "**IELTS Academic**",
        "**7.0** overall, with 7.0 in Reading",
        "Lexical resource used *precisely*; grammatical range with only occasional error; matching headings and True/False/Not Given items that punish paraphrase blindness.",
        "Language focus notes (paraphrase pairs in each chapter); Workbook A and C; every glossary note gives a synonym field, not a single gloss.",
      ],
      [
        "**TOEFL iBT**",
        "**90+** on the pre-21 January 2026 scale; **5.0** on the new 1–6 band scale",
        "Inference, rhetorical purpose, vocabulary in context, and the ability to hold a 700-word academic passage in working memory.",
        "Chapter guides train inference on a text with no exposition; Workbook D uses TOEFL-style rhetorical-purpose and negative-fact items.",
      ],
      [
        "**PTE Academic**",
        "**65** overall",
        "Speed of processing, collocation recognition, and summarising a dense text in one sentence.",
        "Workbook C (paraphrase and summary); the structural tables make one-sentence summarising a habit.",
      ],
      [
        "**Cambridge English**",
        "**185** — C1 Advanced, with C2 Proficiency as the stretch target",
        "Use of English: word formation, fixed expressions, inversion, subjunctive, absolute constructions, register transformation.",
        "Workbook B (transformation); the rhetoric compendium names the constructions and shows them in Gibson's own syntax.",
      ],
      [
        "**Duolingo English Test**",
        "**120**",
        "Rapid real-word/non-word discrimination, c-test-style gap filling, and interactive reading of short academic extracts.",
        "Glossary IPA plus the full levelled lexicon for read-and-select speed; Workbook A's odd-one-out sets mimic the discrimination task.",
      ],
    ],
    "Table 1. Examination targets and where the companion trains each one. Scores are the floors this edition is built to serve, not ceilings.",
  ),

  pair(
    "One warning about score equivalence. A band is not a property of a book; it is a claim about what a reader can do afterwards. Nothing here will raise a score by itself. What a book can do is make the *input* hard enough, and the *feedback* precise enough, that the work you put in lands where it counts. That is the design brief for everything that follows: hard text, named features, and no vocabulary left unglossed.",
    "Một lời cảnh báo về việc quy đổi điểm. Band điểm không phải thuộc tính của một cuốn sách; nó là một tuyên bố về việc người đọc có thể làm gì sau đó. Không cuốn sách nào tự nâng điểm của bạn. Điều một cuốn sách có thể làm là khiến *đầu vào* đủ khó, và *phản hồi* đủ chính xác, để công sức bạn bỏ ra rơi đúng chỗ. Đó là bản thiết kế cho toàn bộ phần còn lại: văn bản khó, đặc điểm được gọi tên, và không một từ nào bị bỏ mặc.",
  ),

  // ------------------------------------------------------------ orientation
  h1("How the novel is built", "structure", "Front matter"),

  pair(
    "*Neuromancer* is a heist novel wearing a detective novel's coat, and it is assembled with a screenwriter's sense of scene. Five parts, twenty-four chapters, no chapter titles — only numbers, because a number is all the orientation you get. The narrative runs in the present tense throughout, in the third person, locked to Case's skull. When it leaves him, it leaves for only a few pages at a time, and usually to show you something he is about to walk into.",
    "*Neuromancer* là một tiểu thuyết trộm cắp khoác áo tiểu thuyết trinh thám, và nó được lắp ghép bằng cảm giác về cảnh của một nhà biên kịch. Năm phần, hai mươi tư chương, không có tên chương — chỉ có số, vì con số là tất cả những gì bạn được cung cấp để định hướng. Trần thuật chạy ở thì hiện tại xuyên suốt, ngôi thứ ba, gắn chặt vào hộp sọ của Case. Khi rời khỏi anh ta, nó chỉ rời vài trang mỗi lần, và thường là để cho bạn thấy thứ mà anh ta sắp bước vào.",
  ),

  pair(
    "The engineering underneath is worth stating plainly, because the structure *is* the argument. A broken console cowboy is repaired by an employer he cannot identify, given back the only thing he loves, and sent to steal something he is not allowed to understand. Everything else — the orbital city, the ninja, the artificial intelligences, the family that owns itself — is the machinery of that one sentence. The novel's subject is not technology. It is employment.",
    "Cỗ máy bên dưới đáng được nói thẳng, vì cấu trúc *chính là* luận điểm. Một cao bồi bàn phím tàn phế được sửa chữa bởi một ông chủ không rõ danh tính, được trao lại thứ duy nhất anh ta yêu, rồi bị sai đi lấy cắp một thứ mà anh ta không được phép hiểu. Mọi thứ còn lại — thành phố quỹ đạo, nữ ninja, các trí tuệ nhân tạo, gia tộc sở hữu chính mình — đều là guồng máy của đúng một câu đó. Chủ đề của tiểu thuyết không phải công nghệ. Mà là việc làm thuê.",
  ),

  table(
    ["Part", "Chapters", "Where it happens", "What the part is for"],
    [1.75, 0.6, 1.15, 1.9],
    [
      ["**One — Chiba City Blues**", "1–2", "Chiba City, Japan", "The offer. Establishes Case's damage, the body as a rented object, and the fact that Molly is the one with agency."],
      ["**Two — The Shopping Expedition**", "3–7", "The Sprawl; Baltimore; Istanbul", "Assembly. The team, the dead man's construct, the hardware, the first runs — and the first proof that the employer is not a person."],
      ["**Three — Midnight in the Rue Jules Verne**", "8–12", "Freeside, the orbital archipelago", "Arrival and reconnaissance. Luxury as architecture; the target family; the widening gap between the contract and the truth."],
      ["**Four — The Straylight Run**", "13–23", "Villa Straylight, Freeside", "The operation itself, then the collapse of the operation into something else: a contest between two intelligences, fought with people."],
      ["**Coda — Departure and Arrival**", "24", "Freeside; the Sprawl; Vancouver", "Settlement. What each survivor bought, what it cost, and the novel's refusal to call any of it a victory."],
    ],
    "Table 2. Structure of the novel. The five part titles are Gibson's; the descriptions are this edition's.",
  ),

  h3("Reading the present tense"),
  pair(
    "Because the narration never uses the past tense, it has almost no way to mark memory as memory. Flashbacks arrive without signposts: a paragraph in the middle of a scene will simply *be* eleven years earlier, and the reader is expected to catch the switch from the change of nouns. This is the single largest source of confusion for first-time readers, and it is also the single largest source of the novel's characteristic speed. Learn to watch for the moment when the furniture changes.",
    "Vì trần thuật không bao giờ dùng thì quá khứ, nó gần như không có cách nào đánh dấu ký ức là ký ức. Hồi tưởng xuất hiện không có biển chỉ đường: một đoạn giữa cảnh bỗng *chính là* mười một năm trước, và người đọc phải tự bắt lấy cú chuyển bằng sự thay đổi của đồ vật. Đây là nguồn gây bối rối lớn nhất cho người đọc lần đầu, và cũng là nguồn tạo nên tốc độ đặc trưng của tiểu thuyết. Hãy học cách để ý khoảnh khắc đồ đạc trong phòng thay đổi.",
  ),

  h3("Reading the names"),
  pair(
    "Gibson almost never introduces a character. Names arrive attached to actions, and often the same character returns under a different designation — a street name, a corporate name, a construct's name, a false name. The appendices contain a character map for exactly this reason; consult it when a name has appeared twice and you still cannot place it.",
    "Gibson gần như không bao giờ giới thiệu nhân vật. Tên xuất hiện dính liền với hành động, và thường cùng một nhân vật quay lại dưới một danh xưng khác — tên đường phố, tên tập đoàn, tên bản sao tâm thức, tên giả. Phụ lục có sơ đồ nhân vật chính vì lý do này; hãy tra khi một cái tên đã xuất hiện hai lần mà bạn vẫn chưa định vị được.",
  ),

  quote(
    "The novel's famous opening sentence is a lesson in the whole method: a natural image (the sky), a domestic technology (television), and a comparison that quietly deletes the difference between them. Nothing is explained. Everything is placed.",
    "This edition's reading of the first sentence of *Neuromancer* — description as analysis, not quotation.",
  ),

  only(
    "From here the book turns to the chapters themselves. Each guide opens with the part it belongs to, then the synopsis, the things worth watching, the language under the hood, and the terms to carry forward.",
  ),
];
