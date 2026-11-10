import type { GrammarUnit } from "../model.js";

export const grammar: GrammarUnit[] = [
  {
    id: "g-asyndeton",
    title: { en: "Asyndeton and parataxis", vi: "Asyndeton và parataxis" },
    whatItIs: {
      en: "Asyndeton is the deliberate omission of conjunctions between clauses or list items; parataxis is the stacking of short independent clauses without subordination. Both create speed, momentum and a flat, documentary glare.",
      vi: "Asyndeton là sự lược bỏ có chủ đích liên từ giữa các mệnh đề hoặc các mục trong danh sách; parataxis là việc xếp chồng các mệnh đề độc lập ngắn mà không có sự phụ thuộc. Cả hai tạo tốc độ, đà và ánh sáng phẳng, kiểu tài liệu.",
    },
    mechanics: [
      {
        en: "Cut 'and/but/so' between clauses; let the reader's breath do the joining.",
        vi: "Cắt chữ 'và/nhưng/vậy' giữa các mệnh đề; để hơi thở người đọc tự nối chúng.",
      },
      {
        en: "Keep clauses short and parallel; long parataxis without rhythm becomes a list, not prose.",
        vi: "Giữ mệnh đề ngắn và song song; parataxis dài mà không có nhịp sẽ thành danh sách, không phải văn xuôi.",
      },
      {
        en: "Use for action, inventory and shock; reserve subordination for reflection.",
        vi: "Dùng cho hành động, liệt kê và cú sốc; dành sự phụ thuộc cho suy ngẫm.",
      },
    ],
    examples: [
      {
        good: "She ran the corridor, checked the lock, killed the light, listened.",
        note: {
          en: "Four verbs, no conjunctions: the sentence performs the checklist it describes.",
          vi: "Bốn động từ, không liên từ: câu văn trình diễn đúng danh sách kiểm tra mà nó mô tả.",
        },
      },
      {
        good: "The market sold kidneys, visas, radios, luck.",
        note: {
          en: "The list escalates by category until 'luck', which lands as commentary without a single opinion word.",
          vi: "Danh sách leo thang theo hạng mục cho tới 'may mắn', một mục đổ xuống như lời bình luận mà không cần một từ nào thể hiện quan điểm.",
        },
      },
    ],
    practice: {
      id: "q-g-asyndeton",
      stem: {
        en: "Which sentence uses asyndeton?",
        vi: "Câu nào sử dụng asyndeton?",
      },
      options: [
        "She ran the corridor, checked the lock, killed the light, and listened.",
        "She ran the corridor, checked the lock, killed the light, listened.",
        "Although she was tired, she checked the lock before listening.",
        "Running the corridor, she checked the lock, which she then killed.",
      ],
      answer: 1,
      explain: {
        en: "Option B drops the final conjunction: pure asyndeton. A keeps the 'and' (polysyndeton's cousin, ordinary listing), C subordinates, D mixes participial subordination.",
        vi: "Phương án B lược bỏ liên từ cuối: asyndeton thuần. A giữ chữ 'và' (liệt kê thông thường), C dùng mệnh đề phụ, D trộn phân từ phụ thuộc.",
      },
    },
    examValue: {
      en: "Cambridge Use of English rewards recognising it in transformation tasks; PTE's 'read aloud' punishes reading an asyndetic list with sing-song conjunctions you add yourself.",
      vi: "Use of English của Cambridge thưởng cho việc nhận diện nó trong bài chuyển đổi; 'đọc thành thạo' của PTE phạt việc bạn tự thêm liên từ và đọc danh sách asyndeton như hát.",
    },
  },
  {
    id: "g-polysyndeton",
    title: { en: "Polysyndeton", vi: "Polysyndeton" },
    whatItIs: {
      en: "The deliberate repetition of conjunctions between every item in a series, the mirror image of asyndeton. Where asyndeton accelerates, polysyndeton swells: each 'and' adds weight, creating a sense of accumulation, ritual or excess.",
      vi: "Sự lặp lại có chủ đích liên từ giữa mọi mục trong một chuỗi, hình ảnh gương của asyndeton. Asyndeton tăng tốc, polysyndeton phình to: mỗi chữ 'và' cộng thêm trọng lượng, tạo cảm giác tích tụ, nghi lễ hoặc thừa mứa.",
    },
    mechanics: [
      {
        en: "Repeat 'and' or 'or' before every item, including where grammar would allow none.",
        vi: "Lặp lại 'và' hoặc 'hoặc' trước mọi mục, kể cả nơi ngữ pháp cho phép lược bỏ.",
      },
      {
        en: "Slow the reader deliberately; the pace itself becomes the meaning.",
        vi: "Cố ý làm chậm người đọc; chính nhịp độ trở thành ý nghĩa.",
      },
      {
        en: "Good for litany, grief, abundance and the overwhelming; bad for routine lists.",
        vi: "Hợp với lời cầu nguyện, tang tóc, sung túc và sự choáng ngợp; không hợp với danh sách thường nhật.",
      },
    ],
    examples: [
      {
        good: "There were debts and regrets and promises and one unfinished cup of tea.",
        note: {
          en: "The repeated 'and' makes each item heavier; the last one turns the list into a portrait.",
          vi: "Chữ 'và' lặp lại khiến mỗi mục nặng hơn; mục cuối biến danh sách thành một chân dung.",
        },
      },
    ],
    practice: {
      id: "q-g-polysyndeton",
      stem: {
        en: "The main effect of polysyndeton in 'debt and rain and another delay' is:",
        vi: "Hiệu ứng chính của polysyndeton trong 'nợ và mưa và thêm một lần trễ nữa' là:",
      },
      options: [
        "Speeding the reader through the list",
        "Making each item accumulate weight and feel inescapable",
        "Removing the need for parallel structure",
        "Converting the list into a question",
      ],
      answer: 1,
      explain: {
        en: "Repeated conjunctions slow and weigh; the series becomes a pile pressing on the reader. Speed is asyndeton's job.",
        vi: "Liên từ lặp lại làm chậm và làm nặng; chuỗi thành đống chất lên người đọc. Tốc độ là công việc của asyndeton.",
      },
    },
    examValue: {
      en: "A guaranteed IELTS 'writer's craft' talking point: name the device, then its pacing effect, then its emotional meaning.",
      vi: "Một điểm bàn luận 'nghệ thuật viết' đảm bảo của IELTS: gọi tên thủ pháp, rồi hiệu ứng nhịp điệu, rồi ý nghĩa cảm xúc.",
    },
  },
  {
    id: "g-absolute",
    title: { en: "The absolute construction", vi: "Cấu trúc tuyệt đối" },
    whatItIs: {
      en: "A noun (or pronoun) plus a participle or participle phrase, grammatically detached from the main clause, adding circumstance in one compressed stroke: 'The key in her hand, she opened the vault.' It is the grammar of stage directions smuggled into narrative.",
      vi: "Một danh từ (hoặc đại từ) cộng với phân từ hoặc cụm phân từ, tách khỏi mệnh đề chính về mặt ngữ pháp, bổ sung hoàn cảnh trong một nét nén: 'Chìa khóa trong tay, cô mở hầm.' Đó là ngữ pháp của chỉ dẫn sân khấu tuồn vào lời kể.",
    },
    mechanics: [
      {
        en: "The absolute noun must not be the subject of the main clause; if it is, you have a dangling modifier or a plain participle clause.",
        vi: "Danh từ trong cấu trúc tuyệt đối không được là chủ ngữ của mệnh đề chính; nếu là vậy, bạn đang có một bổ ngữ treo hoặc một mệnh đề phân từ thông thường.",
      },
      {
        en: "It replaces 'with + noun + participle' or a subordinate clause; use it to save words and slow the eye.",
        vi: "Nó thay thế 'with + danh từ + phân từ' hoặc một mệnh đề phụ; dùng nó để tiết kiệm chữ và làm chậm mắt.",
      },
      {
        en: "Common in literary prose and in Cambridge C1/C2 transformations.",
        vi: "Phổ biến trong văn xuôi văn chương và bài chuyển đổi Cambridge C1/C2.",
      },
    ],
    examples: [
      {
        good: "Her nerves rebuilt, Case had nothing left to sell but nerve.",
        note: {
          en: "The absolute sets the condition in four words; the main clause lands the irony.",
          vi: "Cấu trúc tuyệt đối nêu điều kiện trong bốn từ; mệnh đề chính đáp xuống sự trào phúng.",
        },
      },
      {
        good: "The city humming below them, nobody on the balcony spoke.",
        note: {
          en: "Circumstance first, silence second: the sentence is a camera move.",
          vi: "Hoàn cảnh trước, sự im lặng sau: câu văn là một cú máy quay.",
        },
      },
    ],
    practice: {
      id: "q-g-absolute",
      stem: {
        en: "Which sentence contains an absolute construction?",
        vi: "Câu nào chứa cấu trúc tuyệt đối?",
      },
      options: [
        "With her nerves rebuilt, she could work again.",
        "Her nerves rebuilt, she could work again.",
        "Because her nerves were rebuilt, she could work again.",
        "She rebuilt her nerves and could work again.",
      ],
      answer: 1,
      explain: {
        en: "B pairs the noun 'nerves' with the participle 'rebuilt' outside the main clause: the classic absolute. A is a prepositional with-phrase, C a subordinate clause, D coordination.",
        vi: "B ghép danh từ 'nerves' với phân từ 'rebuilt' bên ngoài mệnh đề chính: dạng tuyệt đối kinh điển. A là cụm giới từ with, C là mệnh đề phụ, D là sự phối hợp.",
      },
    },
    examValue: {
      en: "Cambridge C1 Advanced transformations repeatedly target the absolute; it is also the fastest way to raise the register of an IELTS Task 2 introduction.",
      vi: "Bài chuyển đổi Cambridge C1 Advanced liên tục nhắm vào cấu trúc tuyệt đối; đây cũng là cách nhanh nhất nâng sắc thái mở bài IELTS Task 2.",
    },
  },
  {
    id: "g-inversion",
    title: { en: "Inversion and fronted negatives", vi: "Đảo ngữ và phủ định đặt trước" },
    whatItIs: {
      en: "Placing a negative or restrictive adverbial at the front of a clause forces the subject-auxiliary order to invert: 'Never had he felt so owned.' It is emphasis by ritual displacement, formal and theatrical at once.",
      vi: "Đặt trạng từ phủ định hoặc hạn chế lên đầu mệnh đề buộc thứ tự chủ ngữ-trợ động từ phải đảo: 'Chưa bao giờ anh cảm thấy bị sở hữu đến thế.' Đó là sự nhấn mạnh bằng nghi thức dịch chuyển, trang trọng và kịch tính cùng lúc.",
    },
    mechanics: [
      {
        en: "Fronted negatives (never, rarely, seldom, no sooner, not only, under no circumstances) trigger full inversion in the main clause.",
        vi: "Phủ định đặt trước (never, rarely, seldom, no sooner, not only, under no circumstances) kích hoạt đảo ngữ hoàn toàn trong mệnh đề chính.",
      },
      {
        en: "The auxiliary comes before the subject; if no auxiliary exists, add do/does/did.",
        vi: "Trợ động từ đứng trước chủ ngữ; nếu không có trợ động từ, thêm do/does/did.",
      },
      {
        en: "Use sparingly: one inversion per page is a flourish; three is a speech.",
        vi: "Dùng tiết kiệm: một lần đảo ngữ mỗi trang là nét hoa mỹ; ba lần là một bài diễn văn.",
      },
    ],
    examples: [
      {
        good: "Not once did the phones ring without purpose.",
        note: {
          en: "The fronted 'not once' forces 'did the phones ring': menace dressed as formality.",
          vi: "'Not once' đặt trước buộc 'did the phones ring': mối đe dọa mặc lễ phục trang trọng.",
        },
      },
    ],
    practice: {
      id: "q-g-inversion",
      stem: {
        en: "Rewrite with inversion: 'He had never seen the matrix so calm.'",
        vi: "Viết lại với đảo ngữ: 'He had never seen the matrix so calm.'",
      },
      options: [
        "Never he had seen the matrix so calm.",
        "Never had he seen the matrix so calm.",
        "Never did he saw the matrix so calm.",
        "Never had he see the matrix so calm.",
      ],
      answer: 1,
      explain: {
        en: "Fronted 'Never' requires auxiliary-subject inversion with the past perfect intact: 'Never had he seen'. C mixes did with a past form; D corrupts the participle.",
        vi: "'Never' đặt trước đòi hỏi đảo trợ động từ-chủ ngữ với thì quá khứ hoàn thành nguyên vẹn: 'Never had he seen'. C trộn did với dạng quá khứ; D làm hỏng phân từ.",
      },
    },
    examValue: {
      en: "The single most tested structure in Cambridge key-word transformation; one mastered inversion pattern lifts an entire essay's register.",
      vi: "Cấu trúc bị kiểm tra nhiều nhất trong bài chuyển đổi từ khóa của Cambridge; một mẫu đảo ngữ thành thạo nâng sắc thái của cả bài luận.",
    },
  },
  {
    id: "g-freeindirect",
    title: { en: "Free indirect style", vi: "Kiểu tự do gián tiếp" },
    whatItIs: {
      en: "Third-person narration that borrows the character's inner vocabulary and tense without quotation or reporting clause. The narrator and the mind share one voice, so the reader lives inside the character while still reading prose.",
      vi: "Lời kể ngôi thứ ba mượn vốn từ vựng nội tâm và thì của nhân vật mà không có dấu ngoặc kép hay mệnh đề tường thuật. Người kể và tâm trí chia sẻ một giọng, nên người đọc sống bên trong nhân vật trong khi vẫn đang đọc văn xuôi.",
    },
    mechanics: [
      {
        en: "Delete 'he thought/he felt'; keep the thought's own words ('idiots, all of them').",
        vi: "Xóa 'anh nghĩ/anh cảm thấy'; giữ nguyên lời nghĩ ('đồ ngu, lũ chúng nó').",
      },
      {
        en: "Watch tense: narration past, mind present; the friction is the effect.",
        vi: "Chú ý thì: lời kể quá khứ, tâm trí hiện tại; ma sát chính là hiệu ứng.",
      },
      {
        en: "It is the default style of literary close third person, and of noir especially.",
        vi: "Đây là phong cách mặc định của văn học ngôi thứ ba gần, và của noir đặc biệt.",
      },
    ],
    examples: [
      {
        good: "The suit was lying, obviously; the money would have to do the talking.",
        note: {
          en: "No 'Case thought': the judgment and the plan arrive in his diction, the narration holding the past tense.",
          vi: "Không có 'Case nghĩ': phán quyết và kế hoạch đến theo cách dùng từ của anh, lời kể giữ nguyên thì quá khứ.",
        },
      },
    ],
    practice: {
      id: "q-g-freeindirect",
      stem: {
        en: "Which sentence is free indirect style?",
        vi: "Câu nào là kiểu tự do gián tiếp?",
      },
      options: [
        "Case thought: the suit is lying.",
        "Case thought that the suit was lying.",
        "The suit was lying, obviously; only a fool would pay first.",
        "He said, 'The suit is lying.'",
      ],
      answer: 2,
      explain: {
        en: "C carries the character's judgment ('obviously', 'only a fool') inside third-person narration with no reporting clause. A is direct thought, B reported thought, D direct speech.",
        vi: "C mang phán quyết của nhân vật ('obviously', 'only a fool') bên trong lời kể ngôi thứ ba không có mệnh đề tường thuật. A là suy nghĩ trực tiếp, B là suy nghĩ tường thuật, D là lời nói trực tiếp.",
      },
    },
    examValue: {
      en: "IELTS reading's 'writer's views' questions are often free indirect passages: the opinion is unlabelled, and you must attribute it by diction.",
      vi: "Câu hỏi 'quan điểm tác giả' của đọc IELTS thường là các đoạn tự do gián tiếp: quan điểm không được gán nhãn, và bạn phải quy nó về bằng cách dùng từ.",
    },
  },
  {
    id: "g-nonce",
    title: { en: "Nonce compounds and word-building", vi: "Từ ghép tạm và cách tạo từ" },
    whatItIs: {
      en: "A nonce word is coined for one occasion and understood from its parts: 'meat puppet', 'dead channel', 'console cowboy'. English prose gains speed and strangeness by compounding, and science fiction lives on it.",
      vi: "Từ tạm (nonce) được đặt cho một dịp và được hiểu từ các bộ phận của nó: 'meat puppet', 'dead channel', 'console cowboy'. Văn xuôi tiếng Anh đạt tốc độ và sự lạ lùng nhờ ghép từ, và khoa học viễn tưởng sống nhờ đó.",
    },
    mechanics: [
      {
        en: "Noun + noun ('broadcast rig') and adjective + noun ('dead channel') are the productive patterns.",
        vi: "Danh từ + danh từ ('broadcast rig') và tính từ + danh từ ('dead channel') là các mẫu hiệu quả.",
      },
      {
        en: "A good compound makes a definition unnecessary; a bad one needs a footnote.",
        vi: "Một từ ghép tốt khiến định nghĩa trở nên thừa; một từ ghép dở cần chú thích.",
      },
      {
        en: "Verbing (to flatline, to interface) is the sister process: nouns become actions.",
        vi: "Động từ hóa (to flatline, to interface) là quá trình chị em: danh từ trở thành hành động.",
      },
    ],
    examples: [
      {
        good: "The street sold him a new life in a coffin-sized box: memory, metabolism, mood.",
        note: {
          en: "'Coffin-sized' needs no definition; the compound does world-building in one hyphen.",
          vi: "'Coffin-sized' không cần định nghĩa; từ ghép làm công việc xây dựng thế giới trong một dấu gạch nối.",
        },
      },
    ],
    practice: {
      id: "q-g-nonce",
      stem: {
        en: "In 'console cowboy', the compound's force comes mainly from:",
        vi: "Trong 'console cowboy', sức mạnh của từ ghép chủ yếu đến từ:",
      },
      options: [
        "Its Latinate etymology",
        "The ironic collision of old frontier myth with new technology",
        "Its grammatical ambiguity as a verb phrase",
        "Its status as an established dictionary term before the novel",
      ],
      answer: 1,
      explain: {
        en: "The cowboy rides data ranges, not horses; the compound yokes two centuries. It entered wider usage through this world, not before it.",
        vi: "Cowboy cưỡi các vùng dữ liệu, không phải ngựa; từ ghép buộc hai thế kỷ lại với nhau. Nó đi vào sử dụng rộng rãi qua thế giới này, không phải trước đó.",
      },
    },
    examValue: {
      en: "DET and TOEFL word-formation items love productive patterns; knowing compound logic beats memorising single words.",
      vi: "Bài tạo từ của DET và TOEFL chuộng các mẫu hiệu quả; hiểu logic ghép từ thắng việc học vẹt từng từ đơn.",
    },
  },
  {
    id: "g-zeugma",
    title: { en: "Zeugma and syllepsis", vi: "Zeugma và syllepsis" },
    whatItIs: {
      en: "One word grammatically governing two others that fit it differently: 'She lowered her standards and her neckline.' The joke or the shock lives in the gap between the two senses of the shared word.",
      vi: "Một từ ngữ pháp chi phối hai từ khác mà nó hợp theo hai cách khác nhau: 'Cô hạ tiêu chuẩn và cổ áo.' Tiếng cười hoặc cú sốc nằm ở khoảng cách giữa hai nghĩa của từ chung.",
    },
    mechanics: [
      {
        en: "Place the shared verb or preposition first; the second object must pull it into a different sense.",
        vi: "Đặt động từ hoặc giới từ chung lên trước; tân ngữ thứ hai phải kéo nó sang một nghĩa khác.",
      },
      {
        en: "Syllepsis is the semantic version (one word, two senses); zeugma is often used for both.",
        vi: "Syllepsis là bản ngữ nghĩa (một từ, hai nghĩa); zeugma thường được dùng để chỉ cả hai.",
      },
    ],
    examples: [
      {
        good: "The clinic repaired his nerves and his credit rating.",
        note: {
          en: "'Repaired' works for tissue and finance at once: the sentence prices the body in one verb.",
          vi: "'Repaired' hợp cho cả mô cơ và tài chính: câu văn định giá cơ thể trong một động từ.",
        },
      },
    ],
    practice: {
      id: "q-g-zeugma",
      stem: {
        en: "'The storm took our roof and our patience' is an example of:",
        vi: "'Cơn bão cuốn mất mái nhà và sự kiên nhẫn của chúng tôi' là ví dụ về:",
      },
      options: [
        "Litotes",
        "Zeugma/syllepsis",
        "Polysyndeton",
        "An absolute construction",
      ],
      answer: 1,
      explain: {
        en: "'Took' governs a physical object and an abstract quality, shifting sense mid-list: syllepsis.",
        vi: "'Took' chi phối một vật thể vật lý và một phẩm chất trừu tượng, đổi nghĩa giữa danh sách: syllepsis.",
      },
    },
    examValue: {
      en: "Cambridge C2 sentence-completion and tone questions often hinge on a zeugma you must not read flatly.",
      vi: "Bài hoàn thành câu và câu hỏi tông của Cambridge C2 thường xoay quanh một zeugma mà bạn không được đọc phẳng lì.",
    },
  },
  {
    id: "g-litotes",
    title: { en: "Litotes and understatement", vi: "Litotes và cách nói giảm" },
    whatItIs: {
      en: "Affirming by negating the opposite: 'not unkind', 'no small favour', 'he was not a young man.' Understatement is the broader family; litotes is its double-negative form. The effect is dryness, irony or quiet emphasis.",
      vi: "Khẳng định bằng cách phủ định cái đối lập: 'không phải không tử tế', 'không nhỏ tí nào', 'ông không còn trẻ'. Cách nói giảm là họ rộng hơn; litotes là dạng phủ định kép của nó. Hiệu ứng là sự khô khan, trào phúng hoặc nhấn mạnh thầm lặng.",
    },
    mechanics: [
      {
        en: "Negate the opposite adjective rather than assert the real one.",
        vi: "Phủ định tính từ đối lập thay vì khẳng định tính từ thật.",
      },
      {
        en: "Tone risk: understatement can read as evasion; it suits noir, dry comedy and academic hedging alike.",
        vi: "Rủi ro tông: cách nói giảm có thể đọc như lảng tránh; nó hợp với noir, hài khô khan và cả cách nói thận trọng học thuật.",
      },
    ],
    examples: [
      {
        good: "The run would not be without complications.",
        note: {
          en: "Classic litotes: the crew is walking into disaster with a straight face.",
          vi: "Litotes kinh điển: thủy thủ đoàn bước vào thảm họa với vẻ mặt tỉnh bơ.",
        },
      },
    ],
    practice: {
      id: "q-g-litotes",
      stem: {
        en: "'Her record was not without failures' implies that she:",
        vi: "'Hồ sơ của cô không phải là không có thất bại' ngụ ý rằng cô ấy:",
      },
      options: [
        "Had no failures at all",
        "Had quite a few failures",
        "Failed only once",
        "Refused to keep records",
      ],
      answer: 1,
      explain: {
        en: "Double negation politely affirms the presence of failures, often with an ironic lean toward 'many'.",
        vi: "Phủ định kép lịch sự khẳng định sự hiện diện của các thất bại, thường với sắc thái trào phúng nghiêng về 'không ít'.",
      },
    },
    examValue: {
      en: "TOEFL inference questions love litotes: the surface says 'not bad', the answer is 'very good'.",
      vi: "Câu hỏi suy luận của TOEFL rất thích litotes: bề mặt nói 'không tệ', đáp án là 'rất tốt'.",
    },
  },
  {
    id: "g-anaphora",
    title: { en: "Anaphora and epistrophe", vi: "Anaphora và epistrophe" },
    whatItIs: {
      en: "Anaphora repeats an opening element across clauses or sentences; epistrophe repeats a closing one. Both build rhythm and insistence, turning prose toward speech, prayer or verdict.",
      vi: "Anaphora lặp lại một yếu tố mở đầu qua các mệnh đề hoặc câu; epistrophe lặp lại yếu tố kết. Cả hai xây nhịp điệu và sự khăng khăng, đưa văn xuôi về phía lời nói, lời cầu nguyện hoặc phán quyết.",
    },
    mechanics: [
      {
        en: "Three repetitions minimum for the pattern to register; more than five starts to chant.",
        vi: "Tối thiểu ba lần lặp để khuôn mẫu hiện hình; hơn năm lần bắt đầu thành tụng niệm.",
      },
      {
        en: "Vary the clause tail after the repeated head, or the rhythm dies.",
        vi: "Đổi phần cuối mệnh đề sau đầu lặp lại, nếu không nhịp điệu sẽ chết.",
      },
    ],
    examples: [
      {
        good: "They owned his nerves. They owned his schedule. They did not own the way he remembered the sea.",
        note: {
          en: "The third turn breaks the pattern: resistance defined by where the repetition stops.",
          vi: "Lần thứ ba phá khuôn: sự kháng cự được định nghĩa bởi nơi sự lặp lại dừng lại.",
        },
      },
    ],
    practice: {
      id: "q-g-anaphora",
      stem: {
        en: "In the example, the third sentence is effective mainly because:",
        vi: "Trong ví dụ, câu thứ ba hiệu quả chủ yếu vì:",
      },
      options: [
        "It repeats 'They owned' a third time",
        "It breaks the established pattern at the exact point of resistance",
        "It is the longest of the three",
        "It switches to direct speech",
      ],
      answer: 1,
      explain: {
        en: "Anaphora sets the drumbeat; the break is the meaning. Pattern plus rupture is the rhetoric of defiance.",
        vi: "Anaphora đặt nhịp trống; sự đứt gãy chính là ý nghĩa. Khuôn mẫu cộng với đổ vỡ là tu từ của sự thách thức.",
      },
    },
    examValue: {
      en: "PTE's 'read aloud' and IELTS Speaking Part 2 both reward deliberate repetition you can ride without stumbling.",
      vi: "'Đọc thành thạo' của PTE và IELTS Speaking Part 2 đều thưởng cho sự lặp lại có chủ đích mà bạn cưỡi được mà không vấp.",
    },
  },
  {
    id: "g-ellipsis",
    title: { en: "Ellipsis and verbless sentences", vi: "Câu lược và câu không có động từ" },
    whatItIs: {
      en: "Leaving out words recoverable from context, up to and including the verb: 'Home.' 'Rain.' 'Ten kilometres from the airport.' The fragment is not an error in literary prose; it is compression with attitude.",
      vi: "Bỏ qua các từ có thể suy ra từ ngữ cảnh, kể cả động từ: 'Nhà.' 'Mưa.' 'Mười ki-lô-mét từ sân bay.' Mảnh vỡ không phải lỗi trong văn xuôi văn chương; đó là sự nén có thái độ.",
    },
    mechanics: [
      {
        en: "A verbless sentence needs a context that completes it; in isolation it is noise.",
        vi: "Một câu không động từ cần ngữ cảnh hoàn tất nó; đứng riêng nó là tiếng ồn.",
      },
      {
        en: "One per page creates snap; a paragraph of them becomes a telegram.",
        vi: "Một câu mỗi trang tạo tiếng nổ; một đoạn toàn chúng thành bức điện tín.",
      },
    ],
    examples: [
      {
        good: "Home. The kind you spend a life running from and a fortune running toward.",
        note: {
          en: "The fragment lands, then the relative clause refunds the missing syntax.",
          vi: "Mảnh vỡ đáp xuống, rồi mệnh đề quan hệ hoàn trả cú pháp còn thiếu.",
        },
      },
    ],
    practice: {
      id: "q-g-ellipsis",
      stem: {
        en: "A one-word sentence like 'Rain.' in narrative prose chiefly serves to:",
        vi: "Một câu một từ như 'Mưa.' trong văn xuôi tường thuật chủ yếu phục vụ:",
      },
      options: [
        "Signal a grammatical error in the draft",
        "Compress setting and mood into a single percussive beat",
        "Replace the need for any further description",
        "Mark the change of narrator",
      ],
      answer: 1,
      explain: {
        en: "The fragment is percussive scene-setting; its power depends on the sentences around it supplying grammar.",
        vi: "Mảnh vỡ là tiếng gõ dựng cảnh; sức mạnh của nó phụ thuộc vào các câu quanh nó cung cấp ngữ pháp.",
      },
    },
    examValue: {
      en: "Reading-aloud tasks must not 'repair' fragments; writers-use-of-English items test whether you can restore what was elided.",
      vi: "Bài đọc thành thạo không được 'sửa' các mảnh vỡ; bài dùng từ của người viết kiểm tra bạn có khôi phục được phần bị lược không.",
    },
  },
  {
    id: "g-metaphor",
    title: { en: "Metaphor, dead metaphor and conceit", vi: "Ẩn dụ, ẩn dụ chết và ẩn dụ kéo dài" },
    whatItIs: {
      en: "Metaphor asserts a transfer of meaning ('the sky was dead-channel grey'); a dead metaphor has worn smooth ('the leg of a table'); a conceit sustains the transfer across a passage, building a whole argument from one comparison.",
      vi: "Ẩn dụ khẳng định sự chuyển nghĩa ('bầu trời xám màu kênh chết'); ẩn dụ chết đã mòn nhẵn ('chân bàn'); ẩn dụ kéo dài (conceit) duy trì sự chuyển nghĩa qua một đoạn, xây cả lập luận từ một phép so sánh.",
    },
    mechanics: [
      {
        en: "Name the tenor (what is described) and the vehicle (what does the describing); the distance between them is the energy.",
        vi: "Gọi tên ẩn dụ gốc (thứ được mô tả) và phương tiện (thứ làm mô tả); khoảng cách giữa chúng là năng lượng.",
      },
      {
        en: "Revive dead metaphors only on purpose; 'leg of a table' surprises nobody.",
        vi: "Chỉ hồi sinh ẩn dụ chết khi có chủ đích; 'chân bàn' không làm ai ngạc nhiên.",
      },
      {
        en: "A conceit must pay rent: every further line must extend the comparison, not repeat it.",
        vi: "Ẩn dụ kéo dài phải trả tiền thuê: mọi dòng tiếp theo phải mở rộng phép so sánh, không lặp lại nó.",
      },
    ],
    examples: [
      {
        good: "The matrix was real estate nobody walked: light, logic, and lethal lobbies.",
        note: {
          en: "Property vocabulary colonises cyberspace; the conceit makes capitalism the geography.",
          vi: "Vốn từ bất động sản xâm chiếm không gian mạng; ẩn dụ kéo dài biến chủ nghĩa tư bản thành địa lý.",
        },
      },
    ],
    practice: {
      id: "q-g-metaphor",
      stem: {
        en: "Which is a dead metaphor?",
        vi: "Cái nào là ẩn dụ chết?",
      },
      options: [
        "The sky was the colour of a dead channel",
        "The leg of the table",
        "Data wants to be free",
        "The city was a circuit board someone had stepped on",
      ],
      answer: 1,
      explain: {
        en: "'Leg of a table' is so worn that it no longer reads as comparison. The others still transfer energy between unlike things.",
        vi: "'Chân bàn' đã mòn đến mức không còn đọc ra phép so sánh. Các ví dụ khác vẫn còn chuyển năng lượng giữa các thứ khác loại.",
      },
    },
    examValue: {
      en: "Every exam's reading section asks you to interpret figurative language; naming tenor and vehicle is the analysis they pay for.",
      vi: "Phần đọc của mọi kỳ thi đều yêu cầu diễn giải ngôn ngữ hình tượng; gọi tên ẩn dụ gốc và phương tiện chính là phần phân tích được trả điểm.",
    },
  },
  {
    id: "g-synaesthesia",
    title: { en: "Synaesthesia and sensory crossing", vi: "Thông cảm giác và sự bắt chéo cảm giác" },
    whatItIs: {
      en: "Fusing one sense with another: 'a loud colour', 'a warm silence', 'cold light'. It renders the overstimulated body of the future and, done well, makes description feel like experience rather than report.",
      vi: "Hòa trộn một giác quan với giác quan khác: 'một màu sắc ồn ào', 'sự im lặng ấm áp', 'ánh sáng lạnh'. Nó khắc họa cơ thể bị kích thích quá mức của tương lai và, nếu làm tốt, khiến mô tả có cảm giác như trải nghiệm chứ không phải bản báo cáo.",
    },
    mechanics: [
      {
        en: "Pair adjective and noun from different sensory domains; the swap must be felt, not puzzled over.",
        vi: "Ghép tính từ và danh từ từ các miền giác quan khác nhau; sự hoán đổi phải được cảm nhận, không phải phải băn khoăn.",
      },
      {
        en: "Best for altered states: drugs, simstim, cyberspace, fever.",
        vi: "Hợp nhất với các trạng thái thay đổi: ma túy, simstim, không gian mạng, sốt.",
      },
    ],
    examples: [
      {
        good: "The dub came up warm through the floor, and the sunrise tasted of static.",
        note: {
          en: "Sound has temperature, light has flavour: the body's sensors are cross-wired by the night.",
          vi: "Âm thanh có nhiệt độ, ánh sáng có vị: các cảm biến của cơ thể bị đấu chéo bởi đêm.",
        },
      },
    ],
    practice: {
      id: "q-g-synaesthesia",
      stem: {
        en: "'The sunrise tasted of static' works because it:",
        vi: "'Ánh bình minh có vị của nhiễu' hiệu quả vì nó:",
      },
      options: [
        "Describes the literal flavour of pollution",
        "Crosses taste and vision to render an altered, media-shaped perception",
        "Uses a dead metaphor of weather",
        "Is an example of litotes",
      ],
      answer: 1,
      explain: {
        en: "Taste and vision swap to show a consciousness rewired by technology and fatigue; the image is the character's perception, not a fact about the air.",
        vi: "Vị giác và thị giác hoán đổi để cho thấy một ý thức bị đấu lại bởi công nghệ và mệt mỏi; hình ảnh là cảm nhận của nhân vật, không phải sự thật về không khí.",
      },
    },
    examValue: {
      en: "IELTS 'vocabulary range' criteria reward accurate figurative language in writing; one well-placed synaesthesia beats three ornate adjectives.",
      vi: "Tiêu chí 'vốn từ vựng' của IELTS thưởng cho ngôn ngữ hình tượng chính xác trong viết; một hình ảnh thông cảm giác đặt đúng chỗ thắng ba tính từ hoa mỹ.",
    },
  },
  {
    id: "g-participle",
    title: { en: "Participle clauses and the dangling modifier", vi: "Mệnh đề phân từ và bổ ngữ treo" },
    whatItIs: {
      en: "A clause reduced to a participle phrase ('Crossing the room, he noticed the key'), attaching circumstance to the main clause in one stroke. When its implied subject mismatches the main subject, the modifier dangles and the sentence blames the wrong person.",
      vi: "Một mệnh đề được thu thành cụm phân từ ('Băng qua phòng, anh để ý chiếc chìa khóa'), gắn hoàn cảnh vào mệnh đề chính trong một nét. Khi chủ ngữ ngụ ý không khớp với chủ ngữ chính, bổ ngữ treo và câu văn đổ lỗi nhầm người.",
    },
    mechanics: [
      {
        en: "The participle's understood subject must be the main clause's subject.",
        vi: "Chủ ngữ ngụ ý của phân từ phải là chủ ngữ của mệnh đề chính.",
      },
      {
        en: "Perfect participles ('having stolen the key') mark prior action; passives ('being repaired') mark circumstance endured.",
        vi: "Phân từ hoàn thành ('having stolen the key') đánh dấu hành động trước; bị động ('being repaired') đánh dấu hoàn cảnh phải chịu.",
      },
    ],
    examples: [
      {
        good: "Repaired and repossessed, the body was never quite his.",
        note: {
          en: "The participles front-load the whole economic history; the main clause lands the theme.",
          vi: "Các phân từ nạp trước toàn bộ lịch sử kinh tế; mệnh đề chính đáp xuống chủ đề.",
        },
      },
      {
        good: "Walking through the crypt, the cold seemed to follow them.",
        note: {
          en: "Dangling: the cold is not walking. Fix: 'Walking through the crypt, they felt the cold follow.'",
          vi: "Bổ ngữ treo: cái lạnh không phải đang đi. Sửa: 'Băng qua hầm mộ, họ cảm thấy cái lạnh bám theo.'",
        },
      },
    ],
    practice: {
      id: "q-g-participle",
      stem: {
        en: "Which sentence is correctly formed?",
        vi: "Câu nào được hình thành đúng?",
      },
      options: [
        "Opening the vault, the key was missing.",
        "Opening the vault, she found the key missing.",
        "Opening the vault, the cold rushed out.",
        "The vault being open, the key was found by her.",
      ],
      answer: 1,
      explain: {
        en: "Only B gives the participle the same subject as the main clause ('she'). A and C dangle; D is grammatical but passive-heavy and stylistically weak.",
        vi: "Chỉ B cho phân từ cùng chủ ngữ với mệnh đề chính ('she'). A và C bị treo; D đúng ngữ pháp nhưng quá nặng bị động và yếu về phong cách.",
      },
    },
    examValue: {
      en: "The most frequent advanced-grammar correction item in Cambridge exams, and the fastest credibility leak in IELTS Writing.",
      vi: "Bài sửa ngữ pháp nâng cao thường gặp nhất trong đề Cambridge, và là chỗ rò uy tín nhanh nhất trong IELTS Writing.",
    },
  },
  {
    id: "g-cleft",
    title: { en: "Cleft and pseudo-cleft sentences", vi: "Câu chẻ và câu chẻ giả" },
    whatItIs: {
      en: "Clefts split one idea into two clauses to focus part of it: 'It was Wintermute who called.' Pseudo-clefts use a wh-clause: 'What he wanted was the key.' Focus is the resource; word order is the tool.",
      vi: "Câu chẻ tách một ý thành hai mệnh đề để tập trung vào một phần: 'Chính Wintermute đã gọi.' Câu chẻ giả dùng mệnh đề wh: 'Điều anh ta muốn là chiếc chìa khóa.' Sự tập trung là tài nguyên; thứ tự từ là công cụ.",
    },
    mechanics: [
      {
        en: "It-cleft: 'It + be + focus + relative clause.' Pseudo-cleft: 'What/All + clause + be + focus.'",
        vi: "Câu chẻ It: 'It + be + trọng tâm + mệnh đề quan hệ.' Câu chẻ giả: 'What/All + mệnh đề + be + trọng tâm.'",
      },
      {
        en: "Choose the focus deliberately; clefting the wrong element sounds evasive.",
        vi: "Chọn trọng tâm một cách chủ đích; chẻ sai yếu tố sẽ nghe như lảng tránh.",
      },
    ],
    examples: [
      {
        good: "What the villa kept was not treasure but time.",
        note: {
          en: "Pseudo-cleft turning an inventory into a thesis; the 'but' supplies the correction.",
          vi: "Câu chẻ giả biến một bảng kê thành luận điểm; chữ 'but' cung cấp sự đính chính.",
        },
      },
    ],
    practice: {
      id: "q-g-cleft",
      stem: {
        en: "The focus of 'It was the key that she lifted' is:",
        vi: "Trọng tâm của 'It was the key that she lifted' là:",
      },
      options: [
        "The act of lifting",
        "The key",
        "The person named she",
        "The villa",
      ],
      answer: 1,
      explain: {
        en: "The cleft slot between 'was' and the relative clause holds the focus: the key, contrasted against whatever else was on the table.",
        vi: "Ô chẻ giữa 'was' và mệnh đề quan hệ giữ trọng tâm: chiếc chìa khóa, tương phản với bất cứ thứ gì khác trên bàn.",
      },
    },
    examValue: {
      en: "Cambridge key-word transformation: 'The key is what matters' and friends appear constantly; mastering one cleft pattern handles a whole question family.",
      vi: "Chuyển đổi từ khóa Cambridge: 'The key is what matters' và họ hàng của nó xuất hiện liên tục; thành thạo một mẫu câu chẻ xử lý cả họ câu hỏi.",
    },
  },
  {
    id: "g-tense",
    title: { en: "Tense drift and the historical present", vi: "Sự trôi thì và hiện tại lịch sử" },
    whatItIs: {
      en: "Narrative that shifts tense for effect: past for narration, present for vivid replay ('So he walks into the bar...'), past perfect for backstory. Conscious drift is control; accidental drift is a defect.",
      vi: "Lời kể đổi thì để đạt hiệu ứng: quá khứ cho tường thuật, hiện tại cho cảnh sống động ('Thế là anh ta bước vào quán...'), quá khứ hoàn thành cho phần quá khứ. Sự trôi có ý thức là kiểm soát; trôi vô thức là khuyết tật.",
    },
    mechanics: [
      {
        en: "Set a baseline tense and signal every deliberate shift; oral storytelling licences the present.",
        vi: "Đặt một thì nền tảng và báo hiệu mọi lần chuyển có chủ đích; kể chuyện miệng cho phép dùng hiện tại.",
      },
      {
        en: "Past perfect opens the flashback; return to baseline in the same paragraph.",
        vi: "Quá khứ hoàn thành mở hồi tưởng; quay về thì nền tảng ngay trong đoạn đó.",
      },
    ],
    examples: [
      {
        good: "The run was going badly. He thinks: one more minute. Then the ice opens.",
        note: {
          en: "The present crackles the memory live; the return to past re-tenses the timeline.",
          vi: "Thì hiện tại làm ký ức sống dậy; sự quay về quá khứ tái chỉnh mốc thời gian.",
        },
      },
    ],
    practice: {
      id: "q-g-tense",
      stem: {
        en: "Deliberate tense drift in narrative is primarily used to:",
        vi: "Sự trôi thì có chủ đích trong lời kể chủ yếu được dùng để:",
      },
      options: [
        "Correct earlier errors in the draft",
        "Control vividness and time depth without extra words",
        "Satisfy a formal grammar requirement",
        "Change the point-of-view character",
      ],
      answer: 1,
      explain: {
        en: "Tense is a camera lens: present tightens, past steadies, past perfect opens depth. The shifts are stylistic resource, not repair.",
        vi: "Thì là ống kính máy quay: hiện tại siết chặt, quá khứ ổn định, quá khứ hoàn thành mở chiều sâu. Các lần chuyển là tài nguyên phong cách, không phải sửa chữa.",
      },
    },
    examValue: {
      en: "IELTS narrative tasks and PTE 'respond to a situation' punish accidental drift; noticing the baseline is half the fix.",
      vi: "Bài kể chuyện IELTS và 'phản hồi tình huống' PTE phạt sự trôi vô ý; nhận ra thì nền tảng là một nửa giải pháp.",
    },
  },
  {
    id: "g-apposition",
    title: { en: "Extended apposition and noun piles", vi: "Đồng vị mở rộng và các đống danh từ" },
    whatItIs: {
      en: "Apposition places a noun phrase beside another to rename or classify it: 'Straylight, the family's privacy machine, bled the resort dry.' Extended apposition stacks several such glosses, producing the dense catalogue texture of encyclopaedic prose.",
      vi: "Đồng vị đặt một cụm danh từ cạnh một cụm khác để đổi tên hoặc phân loại nó: 'Straylight, cỗ máy riêng tư của gia tộc, hút cạn khu nghỉ dưỡng.' Đồng vị mở rộng xếp chồng nhiều chú giải như vậy, tạo kết cấu catalogue dày đặc của văn xuôi bách khoa.",
    },
    mechanics: [
      {
        en: "Set off non-restrictive apposition with commas; restrictive apposition takes none.",
        vi: "Tách đồng vị không hạn định bằng dấu phẩy; đồng vị hạn định không cần dấu.",
      },
      {
        en: "Noun piles ('guns, ships, credit, names') work as appositional catalogues: rhythm replaces verbs.",
        vi: "Các đống danh từ ('súng, tàu, tín dụng, tên tuổi') hoạt động như catalogue đồng vị: nhịp điệu thay thế động từ.",
      },
    ],
    examples: [
      {
        good: "The deck, a battered Hosaka with one good socket, was the only honest thing he owned.",
        note: {
          en: "The appositive carries two facts and one judgment in six words before the clause even starts.",
          vi: "Cụm đồng vị mang hai sự thật và một phán quyết trong sáu từ trước khi mệnh đề kịp bắt đầu.",
        },
      },
    ],
    practice: {
      id: "q-g-apposition",
      stem: {
        en: "In 'The deck, a battered Hosaka, was his only friend', the underlined phrase functions as:",
        vi: "Trong 'The deck, a battered Hosaka, was his only friend', cụm được coi là:",
      },
      options: [
        "A relative clause",
        "An appositive renaming the subject",
        "An adverbial of time",
        "A vocative address",
      ],
      answer: 1,
      explain: {
        en: "'A battered Hosaka' renames 'the deck' beside it: apposition. The commas mark it as non-restrictive gloss.",
        vi: "'A battered Hosaka' đổi tên 'the deck' ngay cạnh nó: đồng vị. Các dấu phẩy đánh dấu nó là chú giải không hạn định.",
      },
    },
    examValue: {
      en: "Apposition is the fastest register-raiser in academic writing; examiners read comma-rich noun piles as control, if the rhythm holds.",
      vi: "Đồng vị là công cụ nâng sắc thái nhanh nhất trong viết học thuật; giám khảo đọc các đống danh từ đầy dấu phẩy như sự kiểm soát, nếu nhịp điệu được giữ.",
    },
  },
];
