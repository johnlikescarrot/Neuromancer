/** The whole book, assembled in reading order. */
import type { Block } from "../types.js";
import { divider, h1, pair, glossaryList } from "./kit.js";
import { frontMatter } from "./front.js";
import { novelSection } from "./parts.js";
import { rhetoricSection } from "./rhetoric.js";
import { lexiconA } from "./lexicon-a.js";
import { lexiconB } from "./lexicon-b.js";
import { workbookSection } from "./workbook.js";
import { appendicesSection } from "./appendices.js";

export { collectToc } from "./assemble.js";

export const lexicon = [...lexiconA, ...lexiconB];

const lexiconSection: Block[] = [
  h1("The lexicon", "lexicon", "The apparatus"),
  pair(
    `${lexicon.length} headwords in eight fields, each with IPA, part of speech, a CEFR band, an English gloss, a Vietnamese gloss, and — where it earns one — a note on why the word matters in this novel. The bands are honest: many entries are B2 or C1, and only a minority are C2. A glossary in which everything is advanced teaches nothing.`,
    `${lexicon.length} mục từ trong tám nhóm, mỗi mục có phiên âm IPA, từ loại, mức CEFR, nghĩa tiếng Anh, nghĩa tiếng Việt, và — khi đáng — một ghi chú về vai trò của từ ấy trong tiểu thuyết. Các mức được ghi trung thực: nhiều mục là B2 hoặc C1, chỉ một phần nhỏ là C2. Một cuốn từ điển mà mọi mục đều "cao cấp" thì không dạy được gì.`,
    true,
  ),
  pair(
    "Entries are grouped by field rather than alphabetised, because a reader meeting *ICE* for the first time needs *black ice*, *deck* and *construct* next to it. The index at the back gives quick lookup for the twelve core terms.",
    "Các mục được xếp theo trường nghĩa chứ không theo bảng chữ cái, vì người đọc lần đầu gặp *ICE* cần thấy *black ice*, *deck* và *construct* ngay bên cạnh. Bảng tra ở cuối sách giúp tra nhanh mười hai thuật ngữ cốt lõi.",
  ),
  glossaryList(lexicon, true),
];

export function buildDocument(): Block[] {
  return [
    { t: "cover" },
    { t: "titlepage" },
    { t: "colophon" },
    { t: "toc" },
    ...frontMatter,
    divider(
      "novel",
      "Part I of this volume",
      "The Novel",
      "Twenty-four chapter guides · Tóm lược, phân tích và ngữ pháp theo từng chương",
      "Each guide opens with a synopsis, pairs the English and Vietnamese columns so the two languages can be read against each other, then names what to watch and what the language is doing. Read the chapter first. The guides assume you have just finished the pages they describe, and they spoil freely.",
      "Mỗi bài dẫn mở đầu bằng phần tóm lược, đặt cột tiếng Anh và cột tiếng Việt song song để đọc đối chiếu, rồi nêu những điểm cần chú ý và những gì ngôn ngữ đang làm. Hãy đọc chương trước. Các bài dẫn giả định bạn vừa đọc xong đúng những trang nó nói tới, và chúng tiết lộ nội dung không hề e dè.",
    ),
    ...novelSection,
    divider(
      "apparatus",
      "Part II of this volume",
      "The Apparatus",
      "Tu từ học · Từ điển CEFR · Sách bài tập luyện thi · Phụ lục",
      "Twelve rhetorical features, a levelled lexicon, an exam workbook with keys, and four appendices. This is the part that turns reading into measurable competence — and the part you can return to long after the novel has been finished.",
      "Mười hai đặc điểm tu từ, một từ điển phân tầng CEFR, một sách bài tập có đáp án, và bốn phụ lục. Đây là phần biến việc đọc thành năng lực đo được — và là phần bạn có thể quay lại rất lâu sau khi đã đọc xong tiểu thuyết.",
    ),
    ...rhetoricSection,
    ...lexiconSection,
    ...workbookSection,
    ...appendicesSection,
  ];
}
