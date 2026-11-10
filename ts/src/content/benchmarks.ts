import type { BenchmarkRow, ConcordanceRow, ProseSection } from "../model.js";

/**
 * The five target credentials, exactly as commissioned, with researched
 * concordance context (ETS / IELTS partners / Pearson / Duolingo / Cambridge
 * published mappings; see bibliography entries [b-test-*]).
 */
export const benchmarks: BenchmarkRow[] = [
  {
    test: "TOEFL iBT",
    target: "90 / 120 (legacy, before 21 Jan 2026) · Band 5.0 (from 21 Jan 2026)",
    cefr: "C1",
    whatItProves: {
      en: "Comfort with dense academic passages, inference and rhetorical purpose, plus integrated listening-to-writing stamina.",
      vi: "Khả năng đọc hiểu văn bản học thuật dày đặc, suy luận và nắm mục đích tu từ, kèm sức bền tích hợp nghe-viết.",
    },
    editionUse: {
      en: "Chapter synopses train passage-level inference; the Grammar Masterclass models the rhetorical moves ETS asks you to recognise.",
      vi: "Tóm lược chương luyện suy luận cấp đoạn; Chuyên đề Ngữ pháp mô phỏng các thủ pháp tu từ mà ETS yêu cầu nhận diện.",
    },
  },
  {
    test: "IELTS Academic",
    target: "7.0 (band)",
    cefr: "C1 (lowest C1 band)",
    whatItProves: {
      en: "Flexible, precise language across four skills; ability to handle long, demanding texts and produce structured arguments.",
      vi: "Ngôn ngữ linh hoạt, chính xác ở cả bốn kỹ năng; xử lý được văn bản dài, phức tạp và lập luận có cấu trúc.",
    },
    editionUse: {
      en: "The Academic Glossary feeds Lexical Resource; every writing prompt is an IELTS-style discursive task you can outline in ten minutes.",
      vi: "Từ điển học thuật cung cấp Lexical Resource; mọi đề viết đều là dạng bài nghị luận kiểu IELTS có thể dàn ý trong mười phút.",
    },
  },
  {
    test: "PTE Academic",
    target: "65 (overall)",
    cefr: "C1 (65 ≈ IELTS 7.0 on Pearson's concordance)",
    whatItProves: {
      en: "Fast, accurate processing of extended English: re-telling, summarising written text, and reading aloud under time pressure.",
      vi: "Xử lý tiếng Anh dài nhanh và chính xác: kể lại, tóm tắt văn bản viết, và đọc thành thạo dưới áp lực thời gian.",
    },
    editionUse: {
      en: "Use unit synopses for oral re-tell drills; the vocabulary tables drill the 'Read and Select' recognition reflex PTE rewards.",
      vi: "Dùng tóm tắt chương để luyện kể lại miệng; bảng từ vựng rèn phản xạ nhận diện 'Read and Select' mà PTE trọng.",
    },
  },
  {
    test: "Cambridge C1 Advanced / C2 Proficiency",
    target: "185 (Cambridge English Scale)",
    cefr: "C1 (180-192 = C1 Advanced Grade C; 185-190 ≈ IELTS 7.0)",
    whatItProves: {
      en: "Mastery of advanced grammar in use: inversion, clefts, absolute constructions, and the fine control of register.",
      vi: "Làm chủ ngữ pháp nâng cao trong thực hành: đảo ngữ, câu chẻ, cấu trúc tuyệt đối, và kiểm soát tinh tế sắc thái trang trọng.",
    },
    editionUse: {
      en: "The Grammar Masterclass is built for Use of English: transformations, open cloze and word formation all map onto its sixteen units.",
      vi: "Chuyên đề Ngữ pháp được thiết kế cho Use of English: bài chuyển đổi, điền khuyết và tạo từ đều quy chiếu mười sáu đơn vị.",
    },
  },
  {
    test: "Duolingo English Test",
    target: "120 (scale 10-160)",
    cefr: "B2+/C1 borderline (120 ≈ IELTS 6.5 on Duolingo's 2025 concordance; 130+ is solid C1)",
    whatItProves: {
      en: "Adaptive vocabulary recognition (Read and Select), interactive reading, and quick sentence-level production.",
      vi: "Nhận diện từ vựng thích ứng (Read and Select), đọc tương tác, và sản xuất câu nhanh.",
    },
    editionUse: {
      en: "Every glossary entry is a Read and Select candidate; the mini-quizzes mimic the test's short, sharp item style.",
      vi: "Mỗi mục từ điển là một câu hỏi Read and Select tiềm năng; câu hỏi nhỏ mô phỏng phong cách ngắn, gọn của bài thi.",
    },
  },
];

export const concordance: ConcordanceRow[] = [
  {
    cefr: "C2",
    ielts: "8.5-9.0",
    toeflLegacy: "114-120",
    toeflBand: "6.0",
    pte: "84+",
    det: "155-160",
    cambridge: "200-210 (C2 Proficiency)",
  },
  {
    cefr: "C1 (high)",
    ielts: "7.5-8.0",
    toeflLegacy: "102-113",
    toeflBand: "5.5",
    pte: "76-83",
    det: "140-154",
    cambridge: "193-199",
  },
  {
    cefr: "C1 (target band of this edition)",
    ielts: "7.0",
    toeflLegacy: "90-101",
    toeflBand: "5.0",
    pte: "65-72",
    det: "120-135",
    cambridge: "185-190",
  },
  {
    cefr: "B2 (upper)",
    ielts: "6.5",
    toeflLegacy: "79-89",
    toeflBand: "4.5",
    pte: "55-62",
    det: "110-119",
    cambridge: "176-184",
  },
];

export const legal: ProseSection[] = [
  {
    id: "legal-copyright",
    title: { en: "Copyright and editorial independence", vi: "Bản quyền và độc lập biên tập" },
    paragraphs: [
      {
        en: "Neuromancer is a novel by William Gibson, first published in 1984, and remains the property of its author and publishers. This volume is an independent, unofficial academic companion. It is not affiliated with, sponsored by, or endorsed by William Gibson, Ace Books, Gollancz, or any rights holder. The full text of the novel is not reproduced here, and no translation of the novel is included: translation and adaptation rights belong exclusively to the rights holders.",
        vi: "Neuromancer là tiểu thuyết của William Gibson, xuất bản lần đầu năm 1984, và thuộc về tác giả cùng các nhà xuất bản của nó. Tập tài liệu này là một cẩm nang học thuật độc lập, không chính thức. Tài liệu không liên kết, không được tài trợ và không được bảo trợ bởi William Gibson, Ace Books, Gollancz hay bất kỳ bên nắm giữ bản quyền nào. Toàn văn tiểu thuyết không được tái bản trong tài liệu này, và không kèm bản dịch tác phẩm: quyền dịch và chuyển thể thuộc độc quyền của bên nắm giữ bản quyền.",
      },
      {
        en: "Short quotations appear only where a single sentence is needed for stylistic commentary, clearly attributed, in the spirit of fair use and fair dealing for criticism and study. All summaries, analyses, glosses, translations of commentary, and exercises are original to this companion and may be reused for personal study with attribution.",
        vi: "Các trích dẫn ngắn chỉ xuất hiện khi một câu đơn lẻ là cần thiết cho bình luận văn phong, luôn ghi rõ nguồn, theo tinh thần sử dụng hợp lý (fair use / fair dealing) cho mục đích phê bình và học tập. Mọi tóm tắt, phân tích, chú giải, bản dịch phần bình luận và bài tập trong cẩm nang là nguyên bản và có thể tái sử dụng cho mục đích học tập cá nhân kèm ghi nguồn.",
      },
    ],
  },
  {
    id: "legal-trademarks",
    title: { en: "Trademarks and credits", vi: "Thương hiệu và ghi công" },
    paragraphs: [
      {
        en: "TOEFL is a registered trademark of ETS. IELTS is a registered trademark of IELTS Partners. PTE Academic is a trademark of Pearson. Cambridge English Qualifications are trademarks of Cambridge University Press & Assessment. Duolingo English Test is a trademark of Duolingo, Inc. This companion is not endorsed by any of these organisations; score mappings are indicative and learners should always check the official concordance of each test owner.",
        vi: "TOEFL là thương hiệu đã đăng ký của ETS. IELTS là thương hiệu đã đăng ký của IELTS Partners. PTE Academic là thương hiệu của Pearson. Cambridge English Qualifications là thương hiệu của Cambridge University Press & Assessment. Duolingo English Test là thương hiệu của Duolingo, Inc. Cẩm nang này không được bất kỳ tổ chức nào trong số trên bảo trợ; các quy đổi điểm chỉ mang tính tham khảo và người học luôn cần kiểm tra bảng quy đổi chính thức của từng đơn vị tổ chức thi.",
      },
      {
        en: "The visual system of this edition is built with the Astryx design system (Meta Platforms, open source) using the theme-gothic token set, and with the Open Font License families distributed by Fontsource: Manufacturing Consent and UnifrakturMaguntia (the gothic display and flourish roles), Playfair Display, Fustat, Source Serif 4, Inter, and JetBrains Mono.",
        vi: "Hệ thống thị giác của ấn bản được xây dựng bằng hệ thống thiết kế Astryx (Meta Platforms, mã nguồn mở) sử dụng bộ token theme-gothic, cùng các họ phông chữ theo Giấy phép Phông chữ Mở (OFL) do Fontsource phân phối: Manufacturing Consent và UnifrakturMaguntia (vai trò trang trí gothic), Playfair Display, Fustat, Source Serif 4, Inter và JetBrains Mono.",
      },
    ],
  },
];

export const howToUse: ProseSection[] = [
  {
    id: "use-orientation",
    title: { en: "How this companion works", vi: "Cẩm nang này hoạt động ra sao" },
    paragraphs: [
      {
        en: "This is a study layer, not the novel. Read the chapter itself first with the unit pages beside you: each unit hands you a bilingual synopsis, a craft note on how the prose does its work, a ten-word vocabulary set drawn from the master glossary, and two grammar pointers into the Grammar Masterclass. The unit ends with one exam-style question and one writing prompt, so every chapter leaves measurable evidence of learning behind.",
        vi: "Đây là một lớp học liệu đi kèm, không phải bản thân tiểu thuyết. Hãy đọc chương trước với các trang đơn vị học tập đặt cạnh: mỗi đơn vị cung cấp tóm tắt song ngữ, ghi chú kỹ thuật về cách văn chương vận hành, bộ mười từ vựng trích từ từ điển chính, và hai chỉ dẫn ngữ pháp dẫn tới Chuyên đề Ngữ pháp. Mỗi đơn vị khép lại bằng một câu hỏi kiểu đề thi và một đề viết, để mỗi chương đều để lại bằng chứng học tập đo lường được.",
      },
      {
        en: "The book runs on one engine: the 220-entry Academic Glossary. Chapter units point into it, the exam playbooks drill it, and the study plans schedule it. Learn an entry by saying its definition aloud in English, then its Vietnamese gloss, then one collocation in a sentence of your own.",
        vi: "Cuốn sách vận hành trên một động cơ duy nhất: Từ điển Học thuật 220 mục. Các đơn vị chương trỏ vào nó, các cẩm nang đề thi luyện trên nó, và kế hoạch học tập lên lịch cho nó. Hãy học một mục bằng cách đọc to định nghĩa tiếng Anh, rồi chú nghĩa tiếng Việt, rồi một cụm từ đi kèm trong một câu do bạn tự đặt.",
      },
    ],
  },
  {
    id: "use-method",
    title: { en: "The three-pass reading method", vi: "Phương pháp đọc ba lượt" },
    paragraphs: [
      {
        en: "Pass one is reconnaissance: read the unit synopsis, then the chapter at speed. Pass two is excavation: re-read with the vocabulary table and grammar pointers active, marking one sentence per page that surprised you. Pass three is production: answer the unit question in writing, then the prompt, then swap into the next unit. The three passes convert recognition into recall, which is the only currency exams accept.",
        vi: "Lượt một là trinh sát: đọc tóm tắt trong đơn vị, rồi đọc chương với tốc độ nhanh. Lượt hai là khai quật: đọc lại với bảng từ vựng và chỉ dẫn ngữ pháp được kích hoạt, đánh dấu mỗi trang một câu khiến bạn bất ngờ. Lượt ba là sản xuất: trả lời câu hỏi của đơn vị bằng văn viết, rồi làm đề viết, sau đó chuyển sang đơn vị tiếp theo. Ba lượt chuyển hóa nhận diện thành ghi nhớ, đồng tiền duy nhất mà các kỳ thi chấp nhận.",
      },
    ],
    bullets: [
      {
        en: "Ten minutes a day beats two hours on Sunday: vocabulary decays on a curve, and spacing flattens it.",
        vi: "Mười phút mỗi ngày thắng hai giờ vào Chủ nhật: từ vựng phân rã theo đường cong, và giãn cách làm phẳng đường cong đó.",
      },
      {
        en: "Keep an error log. The question you got wrong is worth ten you got right.",
        vi: "Hãy giữ sổ lỗi. Câu bạn làm sai đáng giá hơn mười câu bạn làm đúng.",
      },
      {
        en: "Say things out loud. Reading silently is the slowest road to speaking and writing gains.",
        vi: "Hãy nói thành tiếng. Đọc im lặng là con đường chậm nhất tới tiến bộ ở nói và viết.",
      },
    ],
  },
];
