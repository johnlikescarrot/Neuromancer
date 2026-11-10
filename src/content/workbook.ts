/**
 * Exam workbook: six sections, with answer keys and model answers.
 * Exercises are written for this edition; passages are original editorial prose.
 */
import type { Block } from "../types.js";
import { h1, h2, h3, pair, bullets, table, callout, rule } from "./kit.js";

export const workbookSection: Block[] = [
  h1("Exam workbook", "workbook", "The apparatus"),
  pair(
    "Six sections, in the order a learner should attempt them. A and B are closed-book and take twenty minutes each. C and D need the chapter guides open. E is timed writing. F is for a partner, or a recording app. Answers follow each section, and every answer explains the reasoning, because an answer key that only gives answers is a key to nothing.",
    "Sáu phần, theo thứ tự người học nên làm. Phần A và B làm không mở sách, mỗi phần hai mươi phút. Phần C và D cần mở các bài dẫn chương. Phần E là viết có bấm giờ. Phần F cần một người cùng học, hoặc một ứng dụng ghi âm. Đáp án nằm ngay sau mỗi phần, và mọi đáp án đều giải thích lý do, vì một bảng đáp án chỉ cho đáp án là bảng đáp án vô dụng.",
    true,
  ),

  // -------------------------------------------------------------------- A
  h2("Section A · Lexical precision", "Phần A · Độ chính xác từ vựng"),
  pair(
    "**A1. Match each definition (1–10) to a headword from the lexicon.** Write the number beside the term.",
    "**A1. Nối mỗi định nghĩa (1–10) với một mục từ trong từ điển.** Viết số vào cạnh thuật ngữ.",
  ),
  table(
    ["#", "Definition", "Term"],
    [0.25, 3.2, 1.3],
    [
      ["1", "Defensive software that attacks an intruder rather than merely blocking access", "ICE"],
      ["2", "A recorded personality that can work after its owner's death", "construct"],
      ["3", "A fee paid in advance to secure a professional's loyalty", "retainer"],
      ["4", "A waterproof filler used to seal a joint", "caulk"],
      ["5", "The conversion of a verb into a noun, compressing a clause", "nominalisation"],
      ["6", "Reference to place or time relative to the speaker's position", "deixis"],
      ["7", "An image without an original; a copy that has replaced its model", "simulacrum"],
      ["8", "A framework spanning a structure, carrying cranes or lights", "gantry"],
      ["9", "The capacity to feel and perceive; subjective experience", "sentience"],
      ["10", "A storage site outside any enforceable jurisdiction", "data haven"],
    ],
    "A1 grid. Answers are given unshuffled here; cover the right-hand column to use it as an exercise.",
  ),
  pair(
    "**A2. Odd one out.** In each set, one word does not belong to the same semantic field, register or word class. Identify it and say why in one sentence.",
    "**A2. Từ khác loại.** Trong mỗi nhóm, một từ không cùng trường nghĩa, phong cách hoặc từ loại. Hãy chỉ ra từ đó và giải thích trong một câu.",
  ),
  bullets(
    [
      "**(i)** deck · dermatrode · gantry · console",
      "**(ii)** zaibatsu · consortium · cartel · fletcher",
      "**(iii)** parataxis · asyndeton · apposition · cryogenics",
      "**(iv)** flatline · construct · sentience · simstim",
      "**(v)** nominalisation · commodification · estrangement · extraction",
    ],
    [
      "**(i)** deck · dermatrode · gantry · console",
      "**(ii)** zaibatsu · consortium · cartel · fletcher",
      "**(iii)** parataxis · asyndeton · apposition · cryogenics",
      "**(iv)** flatline · construct · sentience · simstim",
      "**(v)** nominalisation · commodification · estrangement · extraction",
    ],
  ),
  callout(
    "Answer key · A2",
    [
      "(i) **gantry** — the others are personal interface hardware; a gantry is structural engineering. (ii) **fletcher** — the others are forms of corporate organisation; a fletcher is a weapon. (iii) **cryogenics** — the others are rhetorical figures; cryogenics is a branch of physics. (iv) **sentience** — the others name technologies or states produced by technology; sentience is a capacity. (v) **extraction** — the others are abstract processes of social or textual analysis; extraction is a concrete operation, in both espionage and data handling.",
    ],
    [
      "(i) **gantry** — các từ còn lại là thiết bị giao tiếp cá nhân; gantry là kết cấu công trình. (ii) **fletcher** — các từ còn lại là hình thức tổ chức tập đoàn; fletcher là vũ khí. (iii) **cryogenics** — các từ còn lại là biện pháp tu từ; cryogenics là một ngành vật lý. (iv) **sentience** — các từ còn lại gọi tên công nghệ hoặc trạng thái do công nghệ sinh ra; sentience là một năng lực. (v) **extraction** — các từ còn lại là quá trình trừu tượng của phân tích xã hội hoặc văn bản; extraction là một hành động cụ thể, trong cả gián điệp lẫn xử lý dữ liệu.",
    ],
  ),

  // -------------------------------------------------------------------- B
  h2("Section B · Grammar transformation", "Phần B · Biến đổi ngữ pháp"),
  pair(
    "Rewrite each sentence so that it begins with the word or phrase given, keeping the meaning. One mark for the structure, one for accuracy.",
    "Viết lại mỗi câu sao cho bắt đầu bằng từ hoặc cụm từ cho sẵn, giữ nguyên nghĩa. Một điểm cho cấu trúc, một điểm cho độ chính xác.",
  ),
  table(
    ["#", "Prompt", "Begin with"],
    [0.25, 2.9, 1.1],
    [
      ["1", "He never asked who was paying.", "Never …"],
      ["2", "They understood the cost only later.", "Only later …"],
      ["3", "Nobody explained the arrangement to him.", "At no point …"],
      ["4", "He had barely sat down when the phone rang.", "Barely …"],
      ["5", "She was so calm that nobody noticed the blood.", "So calm …"],
      ["6", "The machine made the decision.", "It was …"],
      ["7", "His hands were shaking. He reached for the deck.", "His hands …"],
      ["8", "People say the AI edited the recording.", "The recording …"],
      ["9", "The company owned the free port. It also owned the law that made it free.", "Not only …"],
      ["10", "Because the corridor was unlit, they moved slowly.", "The corridor …"],
      ["11", "He did not know whether the voice was his own.", "Whether …"],
      ["12", "Someone had paid for the suite in advance.", "The suite …"],
    ],
    "B1 prompts.",
  ),
  callout(
    "Answer key · B1 (model transformations)",
    [
      "1. **Never did he ask** who was paying. — negative inversion. 2. **Only later did they understand** the cost. 3. **At no point was the arrangement explained** to him. — passive plus inversion. 4. **Barely had he sat down** when the phone rang. 5. **So calm was she** that nobody noticed the blood. 6. **It was the machine that made** the decision. — cleft. 7. **His hands shaking, he reached** for the deck. — absolute construction. 8. **The recording is said to have been edited** by the AI. — reporting passive with perfect infinitive. 9. **Not only did the company own** the free port, **but it also owned** the law that made it free. 10. **The corridor being unlit**, they moved slowly. — absolute construction; *because of the unlit corridor* is also acceptable. 11. **Whether the voice was his own, he could not say.** — fronted interrogative clause. 12. **The suite had been paid for** in advance. — agent deleted, which is the point.",
    ],
    [
      "1. **Never did he ask** ai đã trả tiền. — đảo ngữ phủ định. 2. **Only later did they understand** cái giá. 3. **At no point was the arrangement explained** cho anh ta. — bị động cộng đảo ngữ. 4. **Barely had he sat down** thì điện thoại reo. 5. **So calm was she** đến mức không ai để ý vết máu. 6. **It was the machine that made** quyết định. — câu chẻ. 7. **His hands shaking, he reached** lấy chiếc deck. — cấu trúc tuyệt đối. 8. **The recording is said to have been edited** bởi AI. — bị động tường thuật với động từ nguyên thể hoàn thành. 9. **Not only did the company own** cảng tự do, **mà nó còn sở hữu** luật khiến cảng ấy tự do. 10. **The corridor being unlit**, họ đi chậm. 11. **Whether the voice was his own, he could not say.** 12. **The suite had been paid for** trước. — chủ thể bị xóa, và đó chính là điều cần đạt.",
    ],
  ),

  // -------------------------------------------------------------------- C
  h2("Section C · Paraphrase, summary and style", "Phần C · Diễn đạt lại, tóm tắt và phong cách"),
  pair(
    "**C1. One-sentence summaries.** Summarise each part of the novel in a single sentence of no more than thirty words. Do not use the words *cyberspace*, *matrix* or *AI*.",
    "**C1. Tóm tắt một câu.** Tóm tắt mỗi phần của tiểu thuyết trong một câu không quá ba mươi từ. Không dùng các từ *cyberspace*, *matrix* hay *AI*.",
  ),
  pair(
    "**C2. Register shift.** Rewrite each sentence twice: once as a formal academic claim, once as a line of dialogue from a character in the novel.",
    "**C2. Chuyển phong cách.** Viết lại mỗi câu hai lần: một lần như một nhận định học thuật trang trọng, một lần như một câu thoại của nhân vật trong tiểu thuyết.",
  ),
  bullets(
    [
      "**(i)** Employment in this novel is indistinguishable from ownership.",
      "**(ii)** The machines want what all institutions want: to keep existing.",
      "**(iii)** Memory in this novel is a resource that can be mined.",
    ],
    [
      "**(i)** Trong tiểu thuyết này, việc làm thuê không thể phân biệt với quyền sở hữu.",
      "**(ii)** Máy móc muốn điều mọi định chế đều muốn: được tiếp tục tồn tại.",
      "**(iii)** Trong tiểu thuyết này, ký ức là một nguồn tài nguyên có thể khai thác.",
    ],
  ),
  callout(
    "Model answers · C2 (one version each)",
    [
      "(i) Academic: *The novel's labour relations are structured as proprietary claims on the body, rendering the distinction between employment and ownership merely nominal.* Dialogue: *“You think you're staff,” she said. “You're inventory.”* (ii) Academic: *Both intelligences pursue the minimal condition of institutional survival, extending their operation by co-opting human agents.* Dialogue: *“It doesn't want to win,” the Finn said. “It wants to still be here tomorrow.”* (iii) Academic: *Nostalgia is instrumentalised: the protagonist's grief is converted into an interface through which the machine negotiates.* Dialogue: *“It showed me a beach,” Case said. “It knew what I'd pay to stand on it.”*",
    ],
    [
      "(i) Học thuật: *Quan hệ lao động trong tiểu thuyết được cấu trúc như những yêu sách sở hữu đối với thân thể, khiến sự phân biệt giữa làm thuê và sở hữu chỉ còn là hình thức.* Thoại: *“Anh tưởng anh là nhân viên,” cô nói. “Anh là hàng tồn kho.”* (ii) Học thuật: *Cả hai trí tuệ đều theo đuổi điều kiện tối thiểu của sự tồn tại định chế, mở rộng hoạt động bằng cách thu nạp các tác nhân con người.* Thoại: *“Nó không muốn thắng,” Finn nói. “Nó muốn ngày mai vẫn còn ở đó.”* (iii) Học thuật: *Nỗi nhớ được công cụ hóa: đau buồn của nhân vật chính bị chuyển thành một giao diện để cỗ máy thương lượng.* Thoại: *“Nó cho tôi thấy một bãi biển,” Case nói. “Nó biết tôi sẽ trả bao nhiêu để được đứng đó.”*",
    ],
  ),

  // -------------------------------------------------------------------- D
  h2("Section D · Reading and inference", "Phần D · Đọc hiểu và suy luận"),
  pair(
    "Two passages of original editorial prose, each followed by six questions. Passage 2 is harder by design: it contains an argument rather than a description.",
    "Hai đoạn văn bản do ấn bản này viết, mỗi đoạn có sáu câu hỏi. Đoạn 2 khó hơn có chủ ý: nó chứa một lập luận chứ không phải một miêu tả.",
  ),
  h3("Passage 1"),
  pair(
    "The novel's cities are not settings; they are invoices. Chiba City is introduced through the price of a room, the cost of a night's sleep, the fee for information that may not be true. Freeside, one hundred pages later, is introduced the same way, only with more zeros. Between the two, Gibson never once describes a building without telling you what it charges. The effect is cumulative and quietly political: by the time the reader reaches the orbital resort, the question of who paid for it has become more interesting than the question of what it looks like.",
    "Các thành phố trong tiểu thuyết không phải bối cảnh; chúng là hóa đơn. Chiba City được giới thiệu qua giá một căn phòng, chi phí một đêm ngủ, lệ phí cho thông tin có thể không đúng. Freeside, một trăm trang sau, được giới thiệu theo đúng cách ấy, chỉ khác là nhiều số không hơn. Giữa hai nơi đó, Gibson không một lần miêu tả một tòa nhà mà không cho bạn biết nó thu bao nhiêu. Hiệu quả tích lũy và lặng lẽ mang tính chính trị: khi người đọc tới khu nghỉ dưỡng quỹ đạo, câu hỏi ai đã trả tiền cho nó đã trở nên thú vị hơn câu hỏi nó trông thế nào.",
  ),
  bullets(
    [
      "**D1.** The phrase *they are invoices* is best described as: (A) a metaphor for cost (B) a literal statement about commerce (C) an allusion (D) an understatement.",
      "**D2.** Why does the writer mention *more zeros*? (A) to signal inflation (B) to mark scale and class (C) to criticise the novel's arithmetic (D) to date the novel.",
      "**D3.** The word *cumulative* suggests that the effect depends on: (A) repetition across the text (B) a single vivid scene (C) the reader's prior knowledge (D) the narrator's opinion.",
      "**D4.** Which claim would the writer most likely accept? (A) Gibson's descriptions are politically neutral (B) Architecture in the novel functions as economic evidence (C) Freeside is better described than Chiba (D) The novel avoids discussing money.",
      "**D5.** The final sentence implies that: (A) the reader loses interest in description (B) ownership matters more than appearance (C) the orbital resort is badly designed (D) the novel is unfinished.",
      "**D6.** In one sentence, state the passage's main claim without using the word *invoice*.",
    ],
    [
      "**D1.** Cụm *they are invoices* được mô tả đúng nhất là: (A) ẩn dụ về chi phí (B) phát ngôn theo nghĩa đen về thương mại (C) một sự ám chỉ (D) một cách nói giảm.",
      "**D2.** Vì sao người viết nhắc *more zeros*? (A) để báo hiệu lạm phát (B) để đánh dấu quy mô và giai cấp (C) để phê bình phép tính của tiểu thuyết (D) để định niên đại tiểu thuyết.",
      "**D3.** Từ *cumulative* gợi rằng hiệu quả phụ thuộc vào: (A) sự lặp lại xuyên văn bản (B) một cảnh sống động duy nhất (C) kiến thức sẵn có của người đọc (D) ý kiến người kể.",
      "**D4.** Nhận định nào người viết nhiều khả năng chấp nhận? (A) Miêu tả của Gibson trung lập về chính trị (B) Kiến trúc trong tiểu thuyết hoạt động như bằng chứng kinh tế (C) Freeside được miêu tả hay hơn Chiba (D) Tiểu thuyết tránh nói về tiền.",
      "**D5.** Câu cuối hàm ý rằng: (A) người đọc mất hứng thú với miêu tả (B) quyền sở hữu quan trọng hơn vẻ ngoài (C) khu nghỉ dưỡng quỹ đạo được thiết kế tồi (D) tiểu thuyết chưa hoàn thành.",
      "**D6.** Trong một câu, nêu luận điểm chính của đoạn mà không dùng từ *invoice*.",
    ],
  ),
  h3("Passage 2"),
  pair(
    "It is often said that Neuromancer predicted the internet. It did not. What it predicted was a business model: the experience of being inside a system that is always someone's property, which you may enter only on terms you did not write. The technical details have aged badly in some places and eerily well in others, but the social architecture has hardly aged at all. This is why the novel is still taught, and why so many of its readers recognise their working lives in a book about orbital resorts and dead hackers: the hardware is fantasy, the employment contract is documentary.",
    "Người ta thường nói Neuromancer đã dự đoán ra internet. Không phải vậy. Thứ nó dự đoán là một mô hình kinh doanh: trải nghiệm ở bên trong một hệ thống luôn là tài sản của ai đó, mà bạn chỉ được bước vào theo những điều khoản bạn không viết ra. Các chi tiết kỹ thuật đã cũ đi ở vài chỗ và mới một cách kỳ lạ ở vài chỗ khác, nhưng kiến trúc xã hội thì gần như không cũ chút nào. Đó là lý do tiểu thuyết vẫn được giảng dạy, và lý do nhiều người đọc nhận ra đời sống lao động của mình trong một cuốn sách về khu nghỉ dưỡng quỹ đạo và những tin tặc đã chết: phần cứng là hư cấu, hợp đồng lao động là tư liệu.",
  ),
  bullets(
    [
      "**D7.** The writer's attitude to the claim in the first sentence is: (A) agreement (B) qualified rejection (C) indifference (D) hostility to the novel.",
      "**D8.** The phrase *eerie* most nearly means: (A) dated (B) uncannily accurate (C) frightening (D) irrelevant.",
      "**D9.** The contrast in the last sentence is between: (A) fiction and documentary film (B) imagined technology and real employment (C) old and new editions (D) two kinds of reader.",
      "**D10.** Which is NOT a claim made in the passage? (A) The novel's social vision remains relevant (B) Some technical predictions were accurate (C) The novel predicted the internet precisely (D) Readers recognise their work in the book.",
      "**D11.** Explain the rhetorical function of *It did not.* in two or three sentences.",
      "**D12.** Write a 25-word summary of the passage suitable for a lecture handout.",
    ],
    [
      "**D7.** Thái độ của người viết với nhận định ở câu đầu là: (A) đồng tình (B) bác bỏ có điều kiện (C) thờ ơ (D) thù địch với tiểu thuyết.",
      "**D8.** Từ *eerie* gần nghĩa nhất với: (A) lỗi thời (B) chính xác một cách kỳ lạ (C) đáng sợ (D) không liên quan.",
      "**D9.** Tương phản ở câu cuối là giữa: (A) hư cấu và phim tài liệu (B) công nghệ được hình dung và việc làm có thật (C) ấn bản cũ và mới (D) hai kiểu người đọc.",
      "**D10.** Điều nào KHÔNG được nêu trong đoạn? (A) Tầm nhìn xã hội của tiểu thuyết vẫn còn liên quan (B) Một số dự đoán kỹ thuật là chính xác (C) Tiểu thuyết dự đoán chính xác internet (D) Người đọc nhận ra công việc của mình trong sách.",
      "**D11.** Giải thích chức năng tu từ của *It did not.* trong hai hoặc ba câu.",
      "**D12.** Viết bản tóm tắt 25 từ cho tờ phát tay bài giảng.",
    ],
  ),
  callout(
    "Answer key · Section D",
    [
      "D1 **A** — a metaphor, since cities cannot literally be invoices. D2 **B** — the zeros measure wealth, and wealth is the passage's subject. D3 **A** — cumulative effects require accumulation across the text. D4 **B** — the whole passage argues exactly this. D5 **B** — the question of who paid becomes 'more interesting' than appearance. D6 Model: *Gibson describes his cities through what they cost, so that the reader learns to read architecture as economic evidence.* D7 **B** — the writer rejects the strong claim and substitutes a narrower one. D8 **B** — the contrast with 'aged badly' forces a positive sense of uncanny accuracy. D9 **B** — hardware (imagined) versus employment contract (real). D10 **C** — the passage denies precise prediction. D11 Model: *The three-word sentence interrupts the expected agreement and forces a revision before the argument continues. Its brevity mimics confidence, so the qualification that follows sounds like evidence rather than hedging.* D12 Model: *Neuromancer is still taught not because it predicted the internet but because it predicted being employed by one.*",
    ],
    [
      "D1 **A** — ẩn dụ, vì thành phố không thể là hóa đơn theo nghĩa đen. D2 **B** — số không đo sự giàu có, và sự giàu có là chủ đề đoạn văn. D3 **A** — hiệu quả tích lũy cần sự tích lũy qua văn bản. D4 **B** — cả đoạn lập luận đúng điều này. D5 **B** — câu hỏi ai trả tiền trở nên 'thú vị hơn' vẻ ngoài. D6 Mẫu: *Gibson miêu tả các thành phố qua cái giá của chúng, để người đọc học cách đọc kiến trúc như bằng chứng kinh tế.* D7 **B** — người viết bác bỏ nhận định mạnh và thay bằng một nhận định hẹp hơn. D8 **B** — tương phản với 'cũ đi nhanh' buộc phải hiểu theo nghĩa tích cực: chính xác kỳ lạ. D9 **B** — phần cứng (hư cấu) đối lập hợp đồng lao động (thật). D10 **C** — đoạn văn phủ nhận dự đoán chính xác. D11 Mẫu: *Câu ba chữ cắt ngang sự đồng tình mà người đọc đang chờ, buộc phải chỉnh lại trước khi lập luận tiếp tục. Sự ngắn gọn ấy bắt chước vẻ tự tin, nên phần lượng định theo sau nghe như bằng chứng chứ không phải rào đón.* D12 Mẫu: *Neuromancer vẫn được giảng dạy không phải vì nó dự đoán ra internet, mà vì nó dự đoán ra việc bị internet thuê.*",
    ],
  ),

  // -------------------------------------------------------------------- E
  h2("Section E · Writing", "Phần E · Viết"),
  pair(
    "Six tasks at increasing length. Time yourself: 40 minutes for the 250-word tasks, 20 for the 120-word ones. The descriptor table below is a simplified CEFR-aligned rubric adapted for exam preparation; it is not an official band descriptor from any awarding body.",
    "Sáu đề với độ dài tăng dần. Hãy bấm giờ: 40 phút cho bài 250 từ, 20 phút cho bài 120 từ. Bảng mô tả dưới đây là thang đánh giá rút gọn theo CEFR, phục vụ luyện thi; đây không phải mô tả band chính thức của bất kỳ tổ chức khảo thí nào.",
  ),
  bullets(
    [
      "**E1** (120 words) Summarise the structural function of the Panther Moderns for a reader who has not started the novel.",
      "**E2** (250 words) *Neuromancer is a novel about employment, not technology.* Discuss, using evidence from at least three chapters.",
      "**E3** (250 words) Some readers find the novel's refusal to explain its world exhilarating; others find it exclusionary. Argue for one position.",
      "**E4** (120 words) Describe a place in the novel as if you were writing a property listing. Keep the sentence structure of an advertisement and the content of a warning.",
      "**E5** (250 words) Compare the novel's two intelligences as rhetorical styles rather than as characters.",
      "**E6** (250 words) Write the case for teaching this novel to C1 learners instead of a graded reader. Anticipate one objection and answer it.",
    ],
    [
      "**E1** (120 từ) Tóm tắt chức năng cấu trúc của bọn Panther Modern cho một người chưa bắt đầu đọc tiểu thuyết.",
      "**E2** (250 từ) *Neuromancer là tiểu thuyết về việc làm thuê, không phải về công nghệ.* Hãy thảo luận, dùng dẫn chứng từ ít nhất ba chương.",
      "**E3** (250 từ) Có người thấy việc tiểu thuyết từ chối giải thích thế giới của nó là thú vị; người khác thấy nó loại trừ. Hãy lập luận cho một phía.",
      "**E4** (120 từ) Miêu tả một địa điểm trong tiểu thuyết như thể bạn đang viết một mẩu rao bán nhà. Giữ cấu trúc câu của một mẩu quảng cáo và nội dung của một lời cảnh báo.",
      "**E5** (250 từ) So sánh hai trí tuệ trong tiểu thuyết như hai phong cách tu từ, không phải như hai nhân vật.",
      "**E6** (250 từ) Viết lập luận ủng hộ việc dạy tiểu thuyết này cho người học C1 thay cho một cuốn sách rút gọn. Dự đoán một phản đối và trả lời nó.",
    ],
  ),
  table(
    ["Criterion", "Band 6.5 / B2+", "Band 7.0–7.5 / C1", "Band 8.0+ / C2"],
    [1.1, 1.5, 1.6, 1.5],
    [
      ["Task response", "Addresses the task, but some points are general or underdeveloped.", "Addresses all parts; ideas are relevant and extended with example.", "Fully engaged; a clear line of argument that the reader follows without effort."],
      ["Cohesion", "Uses a limited range of devices; paragraphing may be mechanical.", "Sequences information logically; cohesion is not obtrusive.", "Cohesion is achieved without visible machinery: reference, ellipsis, and lexical chains."],
      ["Lexical resource", "Adequate range; occasional imprecision in less common words.", "Wide range used with awareness of collocation; errors do not impede.", "Precise, idiomatic, and register-aware; error-free in the words that carry meaning."],
      ["Grammatical range", "Mix of simple and complex forms; complex forms often faulty.", "Variety of complex structures, generally accurate.", "Full flexibility; a wide range of structures used naturally, not displayed."],
    ],
    "Table 4. A working rubric for self-assessment, aligned to the CEFR descriptors rather than to any single examination board.",
  ),
  pair(
    "**Self-marking routine.** Underline every sentence over twenty-five words. If more than a third are underlined, your writing is probably relying on length instead of structure. Circle every nominalisation. If there are fewer than three in a 250-word essay, it will read as narrative rather than argument; if there are more than ten, it will read as bureaucracy. Count the paragraphs. Four is a habit, five is a plan.",
    "**Quy trình tự chấm.** Gạch chân mọi câu dài hơn hai mươi lăm từ. Nếu quá một phần ba số câu bị gạch chân, bài viết của bạn nhiều khả năng đang dựa vào độ dài thay vì cấu trúc. Khoanh mọi trường hợp danh từ hóa. Nếu một bài 250 từ có ít hơn ba, bài sẽ đọc như tường thuật chứ không phải lập luận; nếu hơn mười, bài sẽ đọc như văn bản hành chính. Đếm số đoạn. Bốn đoạn là thói quen, năm đoạn là một kế hoạch.",
  ),

  // -------------------------------------------------------------------- F
  h2("Section F · Speaking", "Phần F · Nói"),
  pair(
    "Twelve prompts, each with a follow-up designed to force a second, longer turn. Record yourself; listen back once for grammar, once for content. Long-turn tasks in IELTS, TOEFL's independent speaking, and DET's interactive section all reward the same thing: a claim, a reason, and a specific example.",
    "Mười hai đề, mỗi đề có một câu hỏi nối tiếp nhằm buộc bạn nói lượt thứ hai dài hơn. Hãy tự ghi âm; nghe lại một lần vì ngữ pháp, một lần vì nội dung. Các bài nói dài trong IELTS, phần nói độc lập của TOEFL và phần tương tác của DET đều thưởng cho cùng một thứ: một khẳng định, một lý do, và một ví dụ cụ thể.",
  ),
  bullets(
    [
      "Describe a place in the novel you would refuse to visit. — *What would it cost you to be wrong about it?*",
      "Explain why the novel avoids explaining itself. — *What does a reader gain by being confused for forty pages?*",
      "Choose a character who is good at their job. What makes them good? — *Would you employ them?*",
      "Is Case free at the end? — *What would freedom have looked like, given who paid for everything?*",
      "Describe the sound of Chiba City. — *Why does Gibson describe cities through price rather than sound?*",
      "Which of the two intelligences would you rather work for? — *Which is more honest?*",
      "Explain the appeal of the flatline construct in two minutes. — *What is missing from it, and does the novel decide?*",
      "Talk about a piece of technology in the novel that now exists in some form. — *Has it made the novel more or less believable?*",
      "What does the novel think about bodies? — *Is that a technological or a religious question?*",
      "Describe the novel's ending to someone who has not read it, without spoiling it. — *Is a spoiler-free summary possible?*",
      "Which chapter would you cut, and what would be lost? — *What does the structure need that the plot does not?*",
      "Make the case that this is a love story. — *Who is the love interest, and is that a comfort or an accusation?*",
    ],
    [
      "Miêu tả một địa điểm trong tiểu thuyết mà bạn sẽ từ chối tới. — *Bạn sẽ mất gì nếu bạn sai về nó?*",
      "Giải thích vì sao tiểu thuyết tránh tự giải thích. — *Người đọc được gì khi bị bối rối suốt bốn mươi trang?*",
      "Chọn một nhân vật giỏi việc của họ. Điều gì khiến họ giỏi? — *Bạn có thuê họ không?*",
      "Cuối truyện, Case có tự do không? — *Tự do sẽ trông thế nào, khi mọi thứ đều do người khác trả tiền?*",
      "Miêu tả âm thanh của Chiba City. — *Vì sao Gibson miêu tả thành phố qua giá cả thay vì âm thanh?*",
      "Bạn thà làm việc cho trí tuệ nào trong hai trí tuệ ấy? — *Bên nào trung thực hơn?*",
      "Trong hai phút, giải thích sức hấp dẫn của bản sao tâm thức. — *Nó thiếu gì, và tiểu thuyết có quyết định điều đó không?*",
      "Nói về một công nghệ trong tiểu thuyết mà ngày nay đã tồn tại ở dạng nào đó. — *Nó làm tiểu thuyết đáng tin hơn hay kém hơn?*",
      "Tiểu thuyết nghĩ gì về thân thể? — *Đó là câu hỏi công nghệ hay câu hỏi tôn giáo?*",
      "Kể lại cái kết cho người chưa đọc, mà không tiết lộ. — *Một bản tóm tắt không tiết lộ có khả thi không?*",
      "Bạn sẽ bỏ chương nào, và mất gì? — *Cấu trúc cần gì mà cốt truyện không cần?*",
      "Hãy lập luận rằng đây là một chuyện tình. — *Ai là người được yêu, và đó là niềm an ủi hay một lời buộc tội?*",
    ],
  ),
  rule(),
  pair(
    "**A closing note on practice.** These exercises are calibrated to the descriptions of C1 performance, not to a particular test's item types. If you can do them, you can do the tests; the reverse is not true, which is why so many candidates plateau at 6.5 while reporting that they have memorised every strategy.",
    "**Ghi chú cuối về luyện tập.** Các bài tập này được hiệu chỉnh theo mô tả năng lực C1, không theo dạng câu hỏi của một kỳ thi cụ thể. Nếu bạn làm được chúng, bạn làm được các kỳ thi; điều ngược lại không đúng — đó là lý do rất nhiều thí sinh mắc kẹt ở 6.5 dù nói rằng đã thuộc mọi mẹo làm bài.",
  ),
];
