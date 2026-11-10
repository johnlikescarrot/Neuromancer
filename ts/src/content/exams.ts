import type { BibEntry, ExamPlaybook, PlanSection, RubricRow } from "../model.js";

export const exams: ExamPlaybook[] = [
  {
    id: "ex-toefl",
    test: "TOEFL iBT",
    target: "90/120 (legacy) · Band 5.0 (from 21 Jan 2026)",
    scaleNote: {
      en: "On 21 January 2026 ETS replaced the 0-120 scale with 1-6 bands in half-point steps, CEFR-aligned, with the overall band the average of four section bands. Band 5.0 indicates C1 for a skill. During the two-year transition, reports carry both the band and a comparable legacy total.",
      vi: "Ngày 21 tháng 1 năm 2026, ETS thay thang 0-120 bằng thang băng điểm 1-6 theo nấc nửa điểm, gắn với CEFR, trong đó tổng điểm là trung bình bốn băng kỹ năng. Băng 5.0 chỉ ra mức C1 cho một kỹ năng. Trong hai năm chuyển tiếp, phiếu điểm mang cả băng mới và tổng điểm quy đổi thang cũ.",
    },
    formatBullets: [
      {
        en: "Reading and Listening are two-stage adaptive; Speaking and Writing are linear, with the test under 90 minutes total.",
        vi: "Đọc và Nghe là thích ứng hai giai đoạn; Nói và Viết tuyến tính, tổng thời gian bài thi dưới 90 phút.",
      },
      {
        en: "Reading now blends word-level items (Complete the Words) with comprehension sets; Writing includes sentence reconstruction plus academic responses.",
        vi: "Đọc giờ trộn câu hỏi cấp từ (Complete the Words) với bộ câu hỏi hiểu; Viết gồm tái tạo câu và phản hồi học thuật.",
      },
      {
        en: "The legacy 90 target sits at the C1 threshold; on the new scale, aim for band 5.0 or better overall.",
        vi: "Mục tiêu 90 thang cũ nằm ở ngưỡng C1; trên thang mới, hãy nhắm băng 5.0 trở lên cho tổng điểm.",
      },
    ],
    c1Profile: [
      {
        en: "Inference: you read past the sentence to the claim behind it.",
        vi: "Suy luận: bạn đọc xuyên qua câu tới khẳng định phía sau nó.",
      },
      {
        en: "Rhetorical purpose: you can say why a paragraph exists, not just what it says.",
        vi: "Mục đích tu từ: bạn nói được vì sao một đoạn tồn tại, chứ không chỉ nó nói gì.",
      },
      {
        en: "Vocabulary in context: you decode a word from its neighbours, not from the dictionary first.",
        vi: "Từ vựng trong ngữ cảnh: bạn giải mã từ qua các từ xung quanh, không tra từ điển trước.",
      },
    ],
    trainingMap: [
      {
        skill: "Reading inference",
        use: {
          en: "Read a chapter unit's synopsis, then the chapter; write one inference per page and check it against the unit's themes.",
          vi: "Đọc tóm tắt trong đơn vị chương, rồi đọc chương; viết một suy luận mỗi trang và đối chiếu với các chủ đề của đơn vị.",
        },
      },
      {
        skill: "Rhetorical purpose",
        use: {
          en: "Take the craft note and name the purpose of the technique in one sentence.",
          vi: "Lấy ghi chú kỹ thuật và gọi tên mục đích của thủ pháp trong một câu.",
        },
      },
      {
        skill: "Sentence reconstruction",
        use: {
          en: "Cover the Grammar Masterclass examples and rebuild them from the notes alone.",
          vi: "Che các ví dụ trong Chuyên đề Ngữ pháp và dựng lại chúng chỉ từ phần ghi chú.",
        },
      },
    ],
    strategies: [
      {
        title: { en: "Read the question stem first", vi: "Đọc hướng dẫn câu hỏi trước" },
        body: {
          en: "Know whether you are hunting inference, detail or purpose before the passage; the hunt changes the reading speed.",
          vi: "Biết trước bạn đang săn suy luận, chi tiết hay mục đích trước khi đọc; kiểu săn quyết định tốc độ đọc.",
        },
      },
      {
        title: { en: "Kill the extreme options", vi: "Loại phương án cực đoan" },
        body: {
          en: "Words like 'always', 'never', 'proves' are distractor perfume in academic items.",
          vi: "Các từ như 'luôn luôn', 'không bao giờ', 'chứng minh' là hương liệu của phương án nhiễu trong câu hỏi học thuật.",
        },
      },
      {
        title: { en: "Budget the last five minutes", vi: "Dành năm phút cuối" },
        body: {
          en: "Unanswered items score zero; a wrong guess scores the same and takes courage. Fill every bubble.",
          vi: "Câu bỏ trống được 0 điểm; đoán sai cũng 0 điểm và cần dũng cảm. Hãy tô kín mọi ô.",
        },
      },
    ],
    practice: [
      {
        id: "q-ex-toefl-1",
        stem: {
          en: "The word 'burned' in 'his nerves were burned' most nearly means:",
          vi: "Từ 'burned' trong 'thần kinh của anh bị thiêu cháy' gần nghĩa nhất với:",
        },
        options: ["Illuminated", "Destroyed deliberately", "Warmed", "Photographed"],
        answer: 1,
        explain: {
          en: "Context of punishment by a former employer gives 'burned' the sense of deliberate destruction, not heat or light.",
          vi: "Ngữ cảnh trừng phạt bởi chủ cũ cho 'burned' nghĩa là phá hủy có chủ đích, không phải nhiệt hay ánh sáng.",
        },
      },
      {
        id: "q-ex-toefl-2",
        stem: {
          en: "Why does the author describe the future through brand names and worn objects rather than explanation?",
          vi: "Vì sao tác giả mô tả tương lai qua tên thương hiệu và đồ vật cũ kỹ thay vì giải thích?",
        },
        options: [
          "To advertise the products he liked",
          "To let readers infer a world where the new is instantly obsolete",
          "To prove the future will be Japanese",
          "To slow the pacing of the first chapter",
        ],
        answer: 1,
        explain: {
          en: "The rhetorical purpose of catalogue imagery is inference-building: obsolescence and commerce are shown, not argued.",
          vi: "Mục đích tu từ của hình ảnh liệt kê là xây dựng suy luận: sự lỗi thời và thương mại được cho thấy, không được tranh luận.",
        },
      },
    ],
  },
  {
    id: "ex-ielts",
    test: "IELTS Academic",
    target: "Band 7.0",
    scaleNote: {
      en: "IELTS 7.0 is the lowest band the IELTS partners map to CEFR C1 (7.0-8.0). It demands precise, flexible language with occasional lapses rather than flawless monotony.",
      vi: "IELTS 7.0 là băng thấp nhất mà các đối tác IELTS ánh xạ sang CEFR C1 (7.0-8.0). Nó đòi hỏi ngôn ngữ chính xác, linh hoạt với đôi chút sai sót thay vì sự hoàn hảo đơn điệu.",
    },
    formatBullets: [
      {
        en: "Academic Reading: three long passages, tasks include matching headings, summary completion and Yes/No/Not Given.",
        vi: "Đọc Học thuật: ba bài đọc dài, các dạng bài gồm nối tiêu đề, hoàn thành tóm tắt và Có/Không/Không nêu.",
      },
      {
        en: "Writing Task 1 (report on visual data) and Task 2 (discursive essay) both count; Task 2 weighs double.",
        vi: "Viết Task 1 (báo cáo dữ liệu trực quan) và Task 2 (bài luận nghị luận) đều được tính; Task 2 trọng số gấp đôi.",
      },
      {
        en: "Speaking is a live interview: long turn in Part 2, abstract discussion in Part 3.",
        vi: "Nói là phỏng vấn trực tiếp: lượt nói dài ở Phần 2, thảo luận trừu tượng ở Phần 3.",
      },
    ],
    c1Profile: [
      {
        en: "Lexical resource: rare and collocational words used with occasional inaccuracy.",
        vi: "Vốn từ vựng: dùng từ hiếm và cụm từ đi kèm, đôi khi chưa chính xác.",
      },
      {
        en: "Grammatical range: complex structures attempted confidently.",
        vi: "Phạm vi ngữ pháp: tự tin thử các cấu trúc phức tạp.",
      },
      {
        en: "Coherence: clear progression with appropriate cohesive devices, not mechanical linking.",
        vi: "Sự mạch lạc: diễn biến rõ ràng với phương tiện gắn kết phù hợp, không phải nối máy móc.",
      },
    ],
    trainingMap: [
      {
        skill: "Matching headings",
        use: {
          en: "Write your own one-line heading for each unit section, then compare with the unit's titles.",
          vi: "Tự viết tiêu đề một dòng cho mỗi phần của đơn vị, rồi so sánh với tiêu đề của đơn vị.",
        },
      },
      {
        skill: "Task 2 essays",
        use: {
          en: "Answer every writing prompt in this book twice: once timed, once polished. Keep the polished version.",
          vi: "Làm mọi đề viết trong sách hai lần: một lần bấm giờ, một lần trau chuốt. Giữ bản trau chuốt.",
        },
      },
      {
        skill: "Speaking Part 2 long turn",
        use: {
          en: "Speak about a chapter's theme for two minutes from the synopsis alone; record and transcribe your errors.",
          vi: "Nói về chủ đề của một chương trong hai phút chỉ dựa vào tóm tắt; ghi âm và chép lại lỗi của bạn.",
        },
      },
    ],
    strategies: [
      {
        title: { en: "Yes/No/Not Given is a logic game", vi: "Có/Không/Không nêu là trò chơi logic" },
        body: {
          en: "'Not Given' means the text is silent, not that you disagree. Absence is an answer.",
          vi: "'Không nêu' nghĩa là văn bản im lặng, không phải bạn không đồng ý. Sự vắng mặt cũng là một đáp án.",
        },
      },
      {
        title: { en: "One idea, one paragraph", vi: "Một ý, một đoạn" },
        body: {
          en: "Topic sentence first, then evidence from the passage or your reading; the examiner skims for structure.",
          vi: "Câu chủ đề trước, rồi bằng chứng từ bài đọc hoặc vốn đọc của bạn; giám khảo lướt tìm cấu trúc.",
        },
      },
      {
        title: { en: "Collocations over adjectives", vi: "Cụm từ đi kèm thay vì tính từ" },
        body: {
          en: "'Utterly convincing' beats 'very very good': the band descriptors pay for combinations, not intensifiers.",
          vi: "'Cực kỳ thuyết phục' thắng 'rất rất tốt': thang band trả tiền cho sự kết hợp, không phải cho từ nhấn.",
        },
      },
    ],
    practice: [
      {
        id: "q-ex-ielts-1",
        stem: {
          en: "In IELTS Reading, a statement that the passage neither supports nor contradicts is:",
          vi: "Trong Đọc IELTS, một phát biểu mà bài đọc không ủng hộ cũng không phản bác là:",
        },
        options: ["False", "Not Given", "Yes", "Contradicted"],
        answer: 1,
        explain: {
          en: "Silence in the text is Not Given; False requires an explicit contradiction.",
          vi: "Sự im lặng trong văn bản là Không nêu; Sai đòi hỏi một sự phản bác tường minh.",
        },
      },
      {
        id: "q-ex-ielts-2",
        stem: {
          en: "Which sentence best demonstrates C1 lexical resource?",
          vi: "Câu nào thể hiện tốt nhất vốn từ vựng C1?",
        },
        options: [
          "The technology is very very bad for people.",
          "Technology is bad and also good in many ways.",
          "The technology exacts a quiet tax on attention.",
          "Technology: it depends, in my opinion, on some things.",
        ],
        answer: 2,
        explain: {
          en: "C shows precise, collocational language ('exacts a tax on attention') with figurative control; the others rely on intensifiers or vagueness.",
          vi: "C cho thấy ngôn ngữ chính xác, có cụm từ đi kèm ('exacts a tax on attention') với kiểm soát hình tượng; các câu khác dựa vào từ nhấn hoặc sự mơ hồ.",
        },
      },
    ],
  },
  {
    id: "ex-pte",
    test: "PTE Academic",
    target: "65 overall",
    scaleNote: {
      en: "Pearson's concordance places 65 near IELTS 7.0 (the 2025 table gives 63-70 for band 7.0). The test is entirely computer-scored, so performance is timing and clarity as much as language.",
      vi: "Bảng quy đổi của Pearson đặt 65 gần IELTS 7.0 (bảng 2025 cho 63-70 tương ứng băng 7.0). Bài thi chấm hoàn toàn bằng máy, nên hiệu suất phụ thuộc vào thời gian và độ rõ ràng nhiều như ngôn ngữ.",
    },
    formatBullets: [
      {
        en: "Speaking & Writing in one block: read aloud, repeat sentences, re-tell lecture, summarize written text, essay.",
        vi: "Nói & Viết trong một khối: đọc thành thạo, nhắc lại câu, kể lại bài giảng, tóm tắt văn bản viết, viết luận.",
      },
      {
        en: "Reading includes multiple choice, re-order paragraphs and fill-in-the-blanks; Listening includes highlight-incorrect-words and write-from-dictation.",
        vi: "Đọc gồm trắc nghiệm, sắp xếp đoạn và điền khuyết; Nghe gồm đánh dấu từ sai và viết chính tả.",
      },
      {
        en: "The integrated tasks reward oral fluency built from reading habits: what you can say, you can hear.",
        vi: "Các bài tích hợp thưởng cho sự trôi chảy miệng được xây từ thói quen đọc: điều bạn nói được, bạn sẽ nghe được.",
        },
    ],
    c1Profile: [
      {
        en: "Oral fluency without long hesitations; pronunciation is about clarity, not accent.",
        vi: "Trôi chảy miệng không ngập ngừng dài; phát âm là về độ rõ, không phải giọng.",
      },
      {
        en: "Written discourse: essays with clear structure and linking that serves logic.",
        vi: "Diễn ngôn viết: bài luận có cấu trúc rõ và sự nối phục vụ logic.",
      },
      {
        en: "Vocabulary range visible in summarising tasks where compression is forced.",
        vi: "Vốn từ vựng hiện rõ trong các bài tóm tắt khi sự nén bị ép buộc.",
      },
    ],
    trainingMap: [
      {
        skill: "Re-tell lecture",
        use: {
          en: "After each unit, re-tell its synopsis aloud in 40 seconds; the structure trains the exam's memory load.",
          vi: "Sau mỗi đơn vị, kể lại tóm tắt của nó thành tiếng trong 40 giây; cấu trúc này rèn tải trí nhớ của bài thi.",
        },
      },
      {
        skill: "Summarize written text",
        use: {
          en: "Compress a chapter unit into one sentence of 30-70 words containing its main claim and one qualifier.",
          vi: "Nén một đơn vị chương thành một câu 30-70 từ chứa khẳng định chính và một yếu tố hạn định.",
        },
      },
      {
        skill: "Read aloud",
        use: {
          en: "Read the glossary examples aloud daily; the asyndetic ones teach breath control.",
          vi: "Đọc to các ví dụ trong từ điển hằng ngày; những câu asyndeton dạy kiểm soát hơi thở.",
        },
      },
    ],
    strategies: [
      {
        title: { en: "Fluency beats perfection", vi: "Trôi chảy thắng hoàn hảo" },
        body: {
          en: "A minor grammatical error spoken smoothly outscores a perfect sentence buried in hesitation.",
          vi: "Một lỗi ngữ pháp nhỏ nói trôi chảy được điểm cao hơn câu hoàn hảo chìm trong ngập ngừng.",
        },
      },
      {
        title: { en: "Write-from-dictation is a typing exam", vi: "Viết chính tả là bài thi gõ phím" },
        body: {
          en: "Train your ears and fingers together: dictation drills pay double in Listening and Writing.",
          vi: "Rèn tai và ngón tay cùng lúc: bài luyện chính tả trả gấp đôi ở Nghe và Viết.",
        },
      },
      {
        title: { en: "Templates are scaffolding, not answers", vi: "Mẫu là giàn giáo, không phải đáp án" },
        body: {
          en: "Learn essay frames for structure, then replace the content with your own claims or the score caps.",
          vi: "Học khung bài luận để lấy cấu trúc, rồi thay nội dung bằng khẳng định của riêng bạn, nếu không điểm sẽ bị chặn trần.",
        },
      },
    ],
    practice: [
      {
        id: "q-ex-pte-1",
        stem: {
          en: "In 'summarize written text', the safest strategy is to:",
          vi: "Trong 'tóm tắt văn bản viết', chiến lược an toàn nhất là:",
        },
        options: [
          "List every detail mentioned in the passage",
          "Capture the main claim and its key qualifier in one grammatical sentence",
          "Copy two full sentences from the text verbatim",
          "Write three short sentences instead of one long one",
        ],
        answer: 1,
        explain: {
          en: "The task demands one sentence and semantic coverage; detail lists and verbatim copying lose points on form.",
          vi: "Bài đòi hỏi một câu và độ bao phủ ngữ nghĩa; liệt kê chi tiết và chép nguyên văn mất điểm về hình thức.",
        },
      },
      {
        id: "q-ex-pte-2",
        stem: {
          en: "'Read aloud' scores depend MOST on:",
          vi: "Điểm 'đọc thành thạo' phụ thuộc NHIỀU NHẤT vào:",
        },
        options: ["Vocabulary rarity", "Fluency, pacing and clear pronunciation", "Grammar complexity", "Opinion quality"],
        answer: 1,
        explain: {
          en: "It is an oral delivery task: smooth pacing and clarity dominate the machine's scoring features.",
          vi: "Đây là bài thể hiện miệng: nhịp mượt và độ rõ ràng chiếm ưu thế trong các đặc trưng chấm của máy.",
        },
      },
    ],
  },
  {
    id: "ex-cambridge",
    test: "Cambridge C1 Advanced / C2 Proficiency",
    target: "185 (Cambridge English Scale)",
    scaleNote: {
      en: "On the Cambridge English Scale, C1 Advanced results of 180-192 count as Grade C (level C1); 185-190 is the IELTS-7.0 equivalence band. C2 Proficiency starts higher on the same scale. Use of English is where the scale is truly won.",
      vi: "Trên Thang Cambridge English, kết quả C1 Advanced từ 180-192 được coi là Hạng C (trình độ C1); 185-190 là dải tương đương IELTS 7.0. C2 Proficiency bắt đầu cao hơn trên cùng thang. Use of English là nơi thang điểm thực sự được giành.",
    },
    formatBullets: [
      {
        en: "Reading & Use of English: multiple choice, open cloze, word formation, key word transformation, gapped text.",
        vi: "Đọc & Use of English: trắc nghiệm, điền khuyết mở, tạo từ, chuyển đổi từ khóa, văn bản có khoảng trống.",
      },
      {
        en: "Writing: essay plus a task with a text input (review, report, proposal, letter/email).",
        vi: "Viết: bài luận cộng một bài có đầu vào văn bản (bình luận, báo cáo, đề xuất, thư/email).",
      },
      {
        en: "Listening and Speaking test collaborative discussion, not just recall.",
        vi: "Nghe và Nói kiểm tra thảo luận hợp tác, không chỉ ghi nhớ.",
      },
    ],
    c1Profile: [
      {
        en: "Command of structure: inversion, clefts and conditionals used for effect, not display.",
        vi: "Làm chủ cấu trúc: đảo ngữ, câu chẻ và câu điều kiện dùng để đạt hiệu quả, không phải phô trương.",
      },
      {
        en: "Register control: the writing fits its genre (proposal vs essay) without strain.",
        vi: "Kiểm soát sắc thái: bài viết phù hợp thể loại (đề xuất vs luận) mà không gượng ép.",
      },
      {
        en: "Discourse management: a clear argumentative line across paragraphs.",
        vi: "Quản lý diễn ngôn: một mạch lập luận rõ ràng xuyên suốt các đoạn.",
      },
    ],
    trainingMap: [
      {
        skill: "Key word transformation",
        use: {
          en: "Drill the sixteen Grammar Masterclass units: each is a transformation family (inversion, cleft, absolute...).",
          vi: "Luyện mười sáu đơn vị Chuyên đề Ngữ pháp: mỗi đơn vị là một họ bài chuyển đổi (đảo ngữ, câu chẻ, tuyệt đối...).",
        },
      },
      {
        skill: "Word formation",
        use: {
          en: "Turn each glossary headword into its family: noun, verb, adjective, adverb, and one negative form.",
          vi: "Biến mỗi từ mục trong từ điển thành họ từ: danh từ, động từ, tính từ, trạng từ, và một dạng phủ định.",
        },
      },
      {
        skill: "Essay register",
        use: {
          en: "Rewrite one writing prompt as a proposal to a board: same ideas, different register.",
          vi: "Viết lại một đề viết dưới dạng đề xuất gửi hội đồng: cùng ý tưởng, khác sắc thái.",
        },
      },
    ],
    strategies: [
      {
        title: { en: "Open cloze is grammar, not meaning", vi: "Điền khuyết là ngữ pháp, không phải ý nghĩa" },
        body: {
          en: "The missing word is usually a preposition, auxiliary, article or pronoun. Parse the sentence skeleton first.",
          vi: "Từ thiếu thường là giới từ, trợ động từ, mạo từ hoặc đại từ. Hãy phân tích khung câu trước.",
        },
      },
      {
        title: { en: "Transformation: match the pattern", vi: "Chuyển đổi: khớp khuôn mẫu" },
        body: {
          en: "Identify the structure the key word forces ('not until' forces inversion) before writing anything.",
          vi: "Nhận diện cấu trúc mà từ khóa buộc ('not until' buộc đảo ngữ) trước khi viết bất cứ điều gì.",
        },
      },
      {
        title: { en: "Gapped text: glue is logical", vi: "Văn bản có khoảng trống: keo là logic" },
        body: {
          en: "Cohesion devices (these, however, such) travel with the right paragraph; match the glue, then the content.",
          vi: "Phương tiện gắn kết (these, however, such) đi kèm đoạn đúng; khớp phần keo trước, rồi nội dung.",
        },
      },
    ],
    practice: [
      {
        id: "q-ex-cambridge-1",
        stem: {
          en: "Key word transformation: 'Never had the team felt so exposed.' The structure tested is:",
          vi: "Chuyển đổi từ khóa: 'Never had the team felt so exposed.' Cấu trúc được kiểm tra là:",
        },
        options: ["Cleft sentence", "Inversion after a fronted negative", "Passive causative", "Third conditional"],
        answer: 1,
        explain: {
          en: "Fronted 'Never' triggers subject-auxiliary inversion: the classic C1 transformation target.",
          vi: "'Never' đặt trước kích hoạt đảo chủ ngữ-trợ động từ: mục tiêu chuyển đổi kinh điển của C1.",
        },
      },
      {
        id: "q-ex-cambridge-2",
        stem: {
          en: "In open cloze, the missing word in 'The decision rested ___ the evidence' is most likely:",
          vi: "Trong điền khuyết, từ thiếu trong 'The decision rested ___ the evidence' nhiều khả năng là:",
        },
        options: ["to", "on", "for", "with"],
        answer: 1,
        explain: {
          en: "'Rest on' is the collocation; open cloze rewards collocation knowledge over translation.",
          vi: "'Rest on' là cụm từ đi kèm; điền khuyết thưởng cho kiến thức cụm từ hơn dịch thuật.",
        },
      },
    ],
  },
  {
    id: "ex-det",
    test: "Duolingo English Test",
    target: "120 (scale 10-160)",
    scaleNote: {
      en: "Duolingo's own concordance (revised around 2025) is stricter at the boundary: DET 120-125 corresponds to IELTS 6.5 (B2+/C1 border), while 130-135 matches IELTS 7.0. Treat 120 as the floor of C1 and push to 130+ to be safe.",
      vi: "Bảng quy đổi của Duolingo (điều chỉnh khoảng 2025) khắt khe hơn ở biên: DET 120-125 tương ứng IELTS 6.5 (biên B2+/C1), trong khi 130-135 khớp IELTS 7.0. Hãy coi 120 là sàn của C1 và đẩy lên 130+ cho an toàn.",
    },
    formatBullets: [
      {
        en: "Adaptive items: Read and Select (word recognition), Read and Complete (passage cloze), interactive reading.",
        vi: "Câu hỏi thích ứng: Read and Select (nhận diện từ), Read and Complete (điền khuyết đoạn), đọc tương tác.",
      },
      {
        en: "Production: write about a photo, interactive writing, speak about a topic, read aloud.",
        vi: "Sản xuất: viết về ảnh, viết tương tác, nói về chủ đề, đọc thành thạo.",
      },
      {
        en: "The test is short, adaptive and taken at home with heavy proctoring; speed matters from the first item.",
        vi: "Bài thi ngắn, thích ứng và làm tại nhà với giám sát chặt; tốc độ quan trọng ngay từ câu đầu.",
      },
    ],
    c1Profile: [
      {
        en: "Instant word recognition: thousands of words known well enough to judge in under a second.",
        vi: "Nhận diện từ tức thì: hàng nghìn từ được biết đủ kỹ để phán đoán trong dưới một giây.",
      },
      {
        en: "Sentence-level control: cloze items punish vagueness about prepositions and articles.",
        vi: "Kiểm soát cấp câu: câu hỏi điền khuyết phạt sự mơ hồ về giới từ và mạo từ.",
      },
      {
        en: "Quick, coherent production under a visible timer.",
        vi: "Sản xuất nhanh, mạch lạc dưới đồng hồ đếm ngược hiện thị.",
      },
    ],
    trainingMap: [
      {
        skill: "Read and Select",
        use: {
          en: "Use the glossary as a recognition deck: cover the definition, decide word-not-word in one second per entry.",
          vi: "Dùng từ điển như bộ thẻ nhận diện: che định nghĩa, quyết định từ-không-phải-từ trong một giây mỗi mục.",
        },
      },
      {
        skill: "Read and Complete",
        use: {
          en: "The unit vocabulary tables double as cloze banks: hide the headword column and fill from context.",
          vi: "Bảng từ vựng của đơn vị kiêm luôn kho câu hỏi điền khuyết: che cột từ mục và điền từ ngữ cảnh.",
        },
      },
      {
        skill: "Write about a photo",
        use: {
          en: "Use the location guide entries as photo prompts: describe a scene in 60 words, then extend to 120.",
          vi: "Dùng các mục hướng dẫn địa điểm làm đề ảnh: mô tả cảnh trong 60 từ, rồi mở rộng lên 120.",
        },
      },
    ],
    strategies: [
      {
        title: { en: "Trust your first second", vi: "Tin vào giây đầu tiên" },
        body: {
          en: "Adaptive tests punish dithering; a 70% instinct answered fast beats a slow coin flip.",
          vi: "Bài thi thích ứng phạt sự do dự; bản năng 70% trả lời nhanh thắng việc tung đồng xu chậm.",
        },
      },
      {
        title: { en: "Word families beat word lists", vi: "Họ từ thắng danh sách từ" },
        body: {
          en: "Recognise 'obsolescent, obsolesce, obsolete' as one item; the test samples families, not glossary headwords.",
          vi: "Nhận diện 'obsolescent, obsolesce, obsolete' như một mục; bài thi lấy mẫu theo họ từ, không phải theo từ mục.",
        },
      },
      {
        title: { en: "Speak in clean sentences", vi: "Nói bằng câu gọn" },
        body: {
          en: "The speaking sample rewards clarity and range: three clean sentences outscore one tangled paragraph.",
          vi: "Bài nói mẫu thưởng cho độ rõ và phạm vi: ba câu gọn thắng một đoạn rối.",
        },
      },
    ],
    practice: [
      {
        id: "q-ex-det-1",
        stem: {
          en: "DET 120 is best described, on Duolingo's current concordance, as:",
          vi: "DET 120 được mô tả tốt nhất, theo bảng quy đổi hiện hành của Duolingo, là:",
        },
        options: [
          "Solid C1, equivalent to IELTS 7.5",
          "B2+/C1 borderline, close to IELTS 6.5",
          "C2, equivalent to IELTS 8.5",
          "B1, equivalent to IELTS 5.5",
        ],
        answer: 1,
        explain: {
          en: "The revised concordance places 120-125 at IELTS 6.5; 130-135 is the IELTS-7.0 zone. Aim accordingly.",
          vi: "Bảng quy đổi điều chỉnh đặt 120-125 ở mức IELTS 6.5; 130-135 mới là vùng IELTS 7.0. Hãy đặt mục tiêu phù hợp.",
        },
      },
      {
        id: "q-ex-det-2",
        stem: {
          en: "Which study habit maps BEST onto 'Read and Select' items?",
          vi: "Thói quen học nào khớp NHẤT với dạng 'Read and Select'?",
        },
        options: [
          "Writing long essays weekly",
          "Timed word-recognition drills on glossary headwords",
          "Memorising full dictionary pages alphabetically",
          "Listening to lectures without taking notes",
        ],
        answer: 1,
        explain: {
          en: "The item type is rapid lexical recognition; timed recognition drills replicate the cognitive demand.",
          vi: "Dạng câu hỏi là nhận diện từ vựng nhanh; các bài luyện nhận diện có bấm giờ tái hiện đúng nhu cầu nhận thức.",
        },
      },
    ],
  },
];

export const plans: PlanSection[] = [
  {
    id: "plan-8",
    title: { en: "The eight-week arc", vi: "Lộ trình tám tuần" },
    intro: {
      en: "One part of the novel per week, with the coda and the exam playbooks folded into week eight. Each week leaves a measurable artifact: vocabulary cards, one essay, one recorded re-tell.",
      vi: "Một phần tiểu thuyết mỗi tuần, phần kết và các cẩm nang đề thi gộp vào tuần tám. Mỗi tuần để lại một sản phẩm đo được: thẻ từ vựng, một bài luận, một bản ghi âm kể lại.",
    },
    weeks: [
      {
        week: "Week 1",
        focus: { en: "Part One + method setup", vi: "Phần Một + thiết lập phương pháp" },
        tasks: [
          { en: "Read units 1-2 and the chapters they cover.", vi: "Đọc đơn vị 1-2 và các chương tương ứng." },
          { en: "Build 20 glossary cards (ids from the units).", vi: "Làm 20 thẻ từ vựng (các id từ đơn vị)." },
          { en: "Write the unit 1 prompt, timed 20 minutes.", vi: "Làm đề viết đơn vị 1, bấm giờ 20 phút." },
        ],
        output: { en: "A one-page reading contract with your error log started.", vi: "Một trang cam kết đọc với sổ lỗi đã bắt đầu." },
      },
      {
        week: "Week 2",
        focus: { en: "Part Two: the heist as language", vi: "Phần Hai: phi vụ như ngôn ngữ" },
        tasks: [
          { en: "Units 3-7; mark one register shift per chapter.", vi: "Đơn vị 3-7; đánh dấu một lần chuyển sắc thái mỗi chương." },
          { en: "Grammar units 1-4 with the practice items.", vi: "Ngữ pháp đơn vị 1-4 kèm bài tập." },
          { en: "Record one 40-second re-tell per unit.", vi: "Ghi âm một lần kể lại 40 giây mỗi đơn vị." },
        ],
        output: { en: "Four re-tell recordings and four grammar fixes in your log.", vi: "Bốn bản ghi âm kể lại và bốn lỗi ngữ pháp trong sổ." },
      },
      {
        week: "Week 3",
        focus: { en: "Part Three: surfaces and registers", vi: "Phần Ba: bề mặt và sắc thái" },
        tasks: [
          { en: "Units 8-12; write one inference per chapter.", vi: "Đơn vị 8-12; viết một suy luận mỗi chương." },
          { en: "Grammar units 5-8.", vi: "Ngữ pháp đơn vị 5-8." },
          { en: "Take TOEFL playbook practice 1 under time.", vi: "Làm bài tập Cẩm nang TOEFL 1 dưới áp lực giờ." },
        ],
        output: { en: "A marked-up chapter with ten inferences, half verified.", vi: "Một chương được đánh dấu với mười suy luận, một nửa được kiểm chứng." },
      },
      {
        week: "Week 4",
        focus: { en: "Mid-course calibration", vi: "Hiệu chỉnh giữa lộ trình" },
        tasks: [
          { en: "Re-do week 1-3 vocabulary as recognition drills.", vi: "Ôn từ vựng tuần 1-3 dưới dạng bài nhận diện." },
          { en: "Sit one full practice set from any playbook.", vi: "Làm trọn một bộ đề từ bất kỳ cẩm nang nào." },
          { en: "Rewrite your worst essay from the log.", vi: "Viết lại bài luận tệ nhất trong sổ." },
        ],
        output: { en: "A calibration report: what improved, what decays, what to change.", vi: "Báo cáo hiệu chỉnh: gì đã cải thiện, gì đang phân rã, gì cần đổi." },
      },
      {
        week: "Week 5",
        focus: { en: "Part Four I: the run begins", vi: "Phần Bốn I: phi vụ bắt đầu" },
        tasks: [
          { en: "Units 13-17; track the braid structure in unit 17.", vi: "Đơn vị 13-17; theo dõi cấu trúc bện trong đơn vị 17." },
          { en: "Grammar units 9-12.", vi: "Ngữ pháp đơn vị 9-12." },
          { en: "IELTS Task 2 essay from unit 16's prompt.", vi: "Bài luận IELTS Task 2 từ đề đơn vị 16." },
        ],
        output: { en: "One essay scored against the C1 rubric in this book.", vi: "Một bài luận được chấm theo thang C1 trong sách." },
      },
      {
        week: "Week 6",
        focus: { en: "Part Four II: labyrinth and duel", vi: "Phần Bốn II: mê cung và trận đấu" },
        tasks: [
          { en: "Units 18-22; analyse one craft note per unit in writing.", vi: "Đơn vị 18-22; phân tích một ghi chú kỹ thuật mỗi đơn vị bằng văn viết." },
          { en: "Grammar units 13-16.", vi: "Ngữ pháp đơn vị 13-16." },
          { en: "PTE re-tell drills from the units' synopses.", vi: "Luyện kể lại PTE từ tóm tắt các đơn vị." },
        ],
        output: { en: "Six craft analyses in your own words, no quotations.", vi: "Sáu bài phân tích kỹ thuật bằng lời bạn, không trích dẫn." },
      },
      {
        week: "Week 7",
        focus: { en: "The merge + exam integration", vi: "Sự hợp nhất + tích hợp đề thi" },
        tasks: [
          { en: "Units 23-24 plus the close-reading page.", vi: "Đơn vị 23-24 kèm trang đọc kỹ." },
          { en: "Full practice sets: one reading, one writing, one speaking.", vi: "Bộ đề trọn: một đọc, một viết, một nói." },
          { en: "Audit your glossary: keep, fix or drop each card.", vi: "Kiểm toán từ điển: giữ, sửa hoặc bỏ mỗi thẻ." },
        ],
        output: { en: "A pruned deck of 200 known words you actually own.", vi: "Bộ thẻ 200 từ đã thuộc thật sự, sau khi cắt gọn." },
      },
      {
        week: "Week 8",
        focus: { en: "Simulate, review, decide", vi: "Mô phỏng, ôn tập, quyết định" },
        tasks: [
          { en: "One full mock of your target exam, strictly timed.", vi: "Một đề thi thử trọn của kỳ thi mục tiêu, bấm giờ nghiêm ngặt." },
          { en: "Review the entire error log; classify every error by skill.", vi: "Ôn toàn bộ sổ lỗi; phân loại mỗi lỗi theo kỹ năng." },
          { en: "Book the exam, or set the date for the next cycle.", vi: "Đăng ký thi, hoặc đặt ngày cho chu kỳ tiếp theo." },
        ],
        output: { en: "A decision with evidence: register now, or run eight more weeks.", vi: "Một quyết định có bằng chứng: đăng ký ngay, hoặc chạy thêm tám tuần nữa." },
      },
    ],
  },
  {
    id: "plan-4",
    title: { en: "The four-week intensive", vi: "Lộ trình bốn tuần tăng cường" },
    intro: {
      en: "For learners already at a strong B2 with an exam date close. Compressed, ruthless about vocabulary, generous with output practice.",
      vi: "Dành cho người học đã ở B2 vững với ngày thi gần. Lộ trình cô đọng, khắt khe với từ vựng, hào phóng với luyện sản xuất.",
    },
    weeks: [
      {
        week: "Week 1",
        focus: { en: "Units 1-7 + grammar 1-8", vi: "Đơn vị 1-7 + ngữ pháp 1-8" },
        tasks: [
          { en: "Two units per day; glossary cards at night.", vi: "Hai đơn vị mỗi ngày; làm thẻ từ vựng buổi tối." },
          { en: "One timed paragraph per unit prompt (paragraph, not essay).", vi: "Một đoạn văn bấm giờ theo đề mỗi đơn vị (đoạn, không phải bài luận)." },
        ],
        output: { en: "7 paragraphs, 70 cards.", vi: "7 đoạn văn, 70 thẻ." },
      },
      {
        week: "Week 2",
        focus: { en: "Units 8-17 + grammar 9-16", vi: "Đơn vị 8-17 + ngữ pháp 9-16" },
        tasks: [
          { en: "Two units per day; one recorded re-tell daily.", vi: "Hai đơn vị mỗi ngày; một bản ghi âm kể lại mỗi ngày." },
          { en: "Grammar practice items, all sixteen.", vi: "Bài tập ngữ pháp, cả mười sáu đơn vị." },
        ],
        output: { en: "7 recordings, grammar practice complete.", vi: "7 bản ghi, hoàn thành bài tập ngữ pháp." },
      },
      {
        week: "Week 3",
        focus: { en: "Units 18-24 + full practice sets", vi: "Đơn vị 18-24 + bộ đề trọn" },
        tasks: [
          { en: "Finish the units; run one playbook practice set per day.", vi: "Hoàn tất các đơn vị; làm một bộ đề cẩm nang mỗi ngày." },
          { en: "Daily: 20-minute essay, then 10-minute edit.", vi: "Hằng ngày: luận 20 phút, rồi sửa 10 phút." },
        ],
        output: { en: "6 essays, the whole book covered.", vi: "6 bài luận, phủ kín toàn bộ cuốn sách." },
      },
      {
        week: "Week 4",
        focus: { en: "Mocks and margin hunting", vi: "Thi thử và săn điểm lề" },
        tasks: [
          { en: "Three full mocks, two days apart, same time of day.", vi: "Ba đề thi thử, cách nhau hai ngày, cùng giờ trong ngày." },
          { en: "Between mocks: error log only. No new material.", vi: "Giữa các đề: chỉ sổ lỗi. Không học tài liệu mới." },
        ],
        output: { en: "A stable score band and a one-page exam-day plan.", vi: "Một dải điểm ổn định và kế hoạch một trang cho ngày thi." },
      },
    ],
  },
];

export const rubric: RubricRow[] = [
  {
    skill: "Reading inference",
    c1Evidence: {
      en: "You state what a passage implies in one sentence, without quoting it.",
      vi: "Bạn phát biểu điều một đoạn ngụ ý trong một câu, không cần trích dẫn.",
    },
    selfTest: {
      en: "Take unit 7's phones scene: explain the threat in 25 words. Time yourself.",
      vi: "Lấy cảnh điện thoại ở đơn vị 7: giải thích mối đe dọa trong 25 từ. Bấm giờ.",
    },
  },
  {
    skill: "Vocabulary range",
    c1Evidence: {
      en: "You use glossary items in your own sentences that could not be swapped for basic words.",
      vi: "Bạn dùng mục từ điển trong câu của mình mà không thể thay bằng từ cơ bản.",
    },
    selfTest: {
      en: "Write 80 words on surveillance using five glossary items, none of them repeated.",
      vi: "Viết 80 từ về giám sát dùng năm mục từ điển, không lặp lại.",
    },
  },
  {
    skill: "Grammar control",
    c1Evidence: {
      en: "One inversion, one absolute and one participle clause per essay, all correct.",
      vi: "Một đảo ngữ, một cấu trúc tuyệt đối và một mệnh đề phân từ mỗi bài luận, tất cả đúng.",
    },
    selfTest: {
      en: "Transform five sentences using this week's grammar units; check against the key.",
      vi: "Chuyển đổi năm câu dùng các đơn vị ngữ pháp tuần này; đối chiếu đáp án.",
    },
  },
  {
    skill: "Writing coherence",
    c1Evidence: {
      en: "A reader can outline your essay from your topic sentences alone.",
      vi: "Người đọc có thể dàn ý bài luận của bạn chỉ từ các câu chủ đề.",
    },
    selfTest: {
      en: "Give a friend only your first sentences; ask them for the argument back.",
      vi: "Đưa bạn chỉ các câu mở đầu; hỏi họ kể lại lập luận.",
    },
  },
  {
    skill: "Speaking fluency",
    c1Evidence: {
      en: "Two minutes on a unit theme with no long silence and one self-correction maximum.",
      vi: "Hai phút về chủ đề đơn vị không im lặng dài và tối đa một lần tự sửa.",
    },
    selfTest: {
      en: "Record unit 11's theme; count your pauses over two seconds.",
      vi: "Ghi âm chủ đề đơn vị 11; đếm các lần ngập ngừng quá hai giây.",
    },
  },
];

export const bibliography: BibEntry[] = [
  {
    id: "b-gibson-1984",
    citation: "Gibson, William. Neuromancer. Ace Books / Gollancz, 1984.",
    note: "The novel itself: read it legally, in a purchased edition. This companion quotes one sentence from it.",
  },
  {
    id: "b-gibson-1982",
    citation: 'Gibson, William. "Burning Chrome." Omni, 1982.',
    note: "The Sprawl short story that incubated the novel's world and vocabulary.",
  },
  {
    id: "b-gibson-1981",
    citation: 'Gibson, William. "Johnny Mnemonic." Omni, 1981.',
    note: "First appearance of Molly Millions, who walks into the novel with her past intact.",
  },
  {
    id: "b-sprawl-trilogy",
    citation: "Gibson, William. Count Zero (1986); Mona Lisa Overdrive (1988).",
    note: "The Sprawl sequels, for readers who finish the novel hungry.",
  },
  {
    id: "b-sterling-1986",
    citation: "Sterling, Bruce (ed.). Mirrorshades: The Cyberpunk Anthology. Arbor House, 1986.",
    note: "The movement's self-portrait; the afterword defines cyberpunk's programme.",
  },
  {
    id: "b-time-2005",
    citation: "Time. 'All-Time 100 Novels' (100 best English-language novels since 1923), 2005.",
    note: "The crossover honour that placed the novel on the mainstream literary map.",
  },
  {
    id: "b-awards",
    citation: "Nebula Award (1984); Hugo Award (1985); Philip K. Dick Award (1985).",
    note: "The 'triple crown' no other novel has won; verified via the award records cited in the research for this edition.",
  },
  {
    id: "b-ets-2026",
    citation: "ETS. TOEFL iBT score scale change, effective 21 January 2026 (1-6 bands, CEFR-aligned).",
    note: "Official scale change; legacy 0-120 scores remain valid and are reported alongside during the transition.",
  },
  {
    id: "b-ielts-concordance",
    citation: "IELTS Partners. IELTS-CEFR concordance (band 7.0-8.0 = C1).",
    note: "Used for the C1 anchor of this edition's benchmark table.",
  },
  {
    id: "b-pearson-2025",
    citation: "Pearson. PTE Academic concordance with IELTS (July 2025 revision: IELTS 7.0 ≈ PTE 63-70).",
    note: "Pearson's own table; institutions quote slightly different cut-offs, so verify per school.",
  },
  {
    id: "b-det-concordance",
    citation: "Duolingo. Duolingo English Test concordance (2023, re-checked 2025: DET 120-125 ≈ IELTS 6.5).",
    note: "Stricter at the B2/C1 boundary than older charts; the reason this book aims DET users at 130+.",
  },
  {
    id: "b-cambridge-scale",
    citation: "Cambridge University Press & Assessment. Cambridge English Scale (C1 Advanced 180-192 = Grade C / C1).",
    note: "The scale behind the 185 target in the commission for this edition.",
  },
  {
    id: "b-astryx",
    citation: "Meta Platforms. Astryx design system (theme-gothic), open source, 2026.",
    note: "The visual language of this edition: palette, type roles and component geometry, consumed as design tokens by the TypeScript build.",
  },
];
