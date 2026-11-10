/** Appendices: character map, chronology, coinages, further reading, index. */
import type { Block } from "../types.js";
import { h1, h2, pair, bullets, table, callout } from "./kit.js";

export const appendicesSection: Block[] = [
  h1("Appendices", "appendices", "Reference"),

  h2("A · Character map", "A · Sơ đồ nhân vật"),
  pair(
    "Names in this novel arrive attached to actions, and several characters appear under more than one designation. Use this table when a name has appeared twice and you still cannot place it.",
    "Tên trong tiểu thuyết này xuất hiện dính liền với hành động, và một số nhân vật xuất hiện dưới nhiều danh xưng. Hãy dùng bảng này khi một cái tên đã xuất hiện hai lần mà bạn vẫn chưa định vị được.",
  ),
  table(
    ["Name", "Who they are", "What to remember"],
    [1.0, 1.9, 2.4],
    [
      ["**Case** (Henry Dorsett Case)", "Console cowboy, the novel's focal character", "His damage is his resume: he is valuable because he is desperate."],
      ["**Molly** (Molly Millions)", "Razorgirl; mercenary; Case's partner and lover", "She has agency where Case has appetite. Her body is her capital."],
      ["**Armitage** (Colonel Corto)", "The employer's field commander", "A rebuilt soldier running a program he cannot inspect."],
      ["**Wintermute**", "One of two intelligences; the operation's sponsor", "Speaks in deadlines and offers. Its impatience is a character trait."],
      ["**Neuromancer**", "The second intelligence", "Speaks in invitations and images. Its method is seduction, not coercion."],
      ["**McCoy Pauley** ('Dixie Flatline')", "A construct; Case's mentor in the matrix", "Dead three times; funny, rude, and unfree."],
      ["**Julius Deane**", "Chiba fixer and fence", "The first lesson in how information is priced."],
      ["**Ratz**", "Barman at the Chatsubo", "The novel's listening post made human."],
      ["**Linda Lee**", "Case's former partner in Chiba", "Memory as a resource the machine can mine."],
      ["**Peter Riviera**", "Thief and performance artist", "His talent is illusion; his cruelty is using it on people."],
      ["**3Jane Tessier-Ashpool**", "Heir to the family firm", "The novel's real political subject: a person owned by a structure."],
      ["**Ashpool**", "Founder of the dynasty", "Property as a theory of the self, stated out loud."],
      ["**Hideo**", "3Jane's bodyguard", "Aesthetic object and lethal instrument, deliberately indistinguishable."],
      ["**Maelcum**", "Zionite pilot of the *Marcus Garvey*", "Competence, faith, and the only community in the book that is not for sale."],
      ["**Aerol**", "Zionite elder", "The novel's moral chorus, and it is not impressed."],
      ["**The Finn**", "Fixer who operates through the grid", "Comic relief, exposition, and a liar."],
      ["**Cath** and **Bruce**", "Freeside couple; simstim performer and hanger-on", "What a life looks like when everything in it is for sale."],
      ["**Terzibashjian**", "Istanbul fixer", "Loyalty bought twice, and visibly affordable."],
    ],
    "Table 5. Principal characters. Designations in brackets are the names under which they first appear.",
  ),

  h2("B · Chronology of the operation", "B · Niên biểu chiến dịch"),
  pair(
    "The novel is not told in strict chronological order, and a good deal of what Case learns late happened long before he was hired. This table separates the two timelines: what the reader reads, and what the world did.",
    "Tiểu thuyết không được kể theo trật tự thời gian nghiêm ngặt, và nhiều điều Case biết muộn đã xảy ra rất lâu trước khi anh được thuê. Bảng này tách hai dòng thời gian: điều người đọc đọc, và điều thế giới đã làm.",
  ),
  table(
    ["When (world time)", "Event", "Where the reader learns it"],
    [1.2, 2.6, 1.5],
    [
      ["Decades before", "The Tessier-Ashpool family builds its orbital holdings and begins reproducing by cloning", "Part Three, in fragments"],
      ["Years before", "Two intelligences are built inside the family's holdings; each is given half of what it needs", "Parts Three and Four"],
      ["Years before", "Case is punished by a former employer; his nervous system is damaged", "Part One, largely by implication"],
      ["Months before", "A soldier named Corto is rebuilt and renamed Armitage", "Part Four"],
      ["Chapter 1", "Case is offered work in Chiba", "Part One"],
      ["Chapters 3–7", "The team, the construct, the weapon, the reconnaissance", "Part Two"],
      ["Chapters 8–12", "Arrival in Freeside; the target is studied", "Part Three"],
      ["Chapters 13–23", "The operation, its collapse, and the merger of the two intelligences", "Part Four"],
      ["Chapter 24", "Settlement: departures, arrivals, and one return to work", "Coda"],
    ],
    "Table 6. Two timelines. Dates in the novel are deliberately vague; 'world time' here means narrative priority, not calendar years.",
  ),

  h2("C · Gibson's coinages", "C · Những từ do Gibson tạo ra"),
  pair(
    "Why do some invented words survive and others die within a decade? The short answer is morphology: the durable ones are built from pieces an English speaker already owns, and they name something a reader has half-noticed but never named.",
    "Vì sao có những từ được phát minh mà vẫn sống, còn những từ khác chết trong vòng một thập kỷ? Câu trả lời ngắn là hình thái học: những từ bền vững được dựng từ các mảnh mà người nói tiếng Anh đã có, và chúng gọi tên một thứ người đọc đã lờ mờ nhận ra nhưng chưa từng đặt tên.",
  ),
  table(
    ["Term", "Built from", "Why it works"],
    [1.2, 1.7, 2.4],
    [
      ["**cyberspace**", "*cyber(netic)* + *space*", "Two familiar pieces; the second one does the philosophy — it makes data a place."],
      ["**matrix**", "Latin *mater*, 'womb'; existing mathematical term", "Borrowed, not invented: the reader already feels the implication of containment."],
      ["**ICE**", "Initialism expanding to Intrusion Countermeasures Electronics", "Sounds like a procurement acronym and reads as a substance. Double life."],
      ["**simstim**", "*sim(ulated)* + *stim(ulation)*", "A blend whose sound suggests a product on a shelf."],
      ["**flatline**", "Existing medical term, repurposed", "No invention at all — only a new syntax. That is why it feels inevitable."],
      ["**deck**", "Existing word, narrowed", "Monosyllabic, physical, unglamorous: technology you can drop."],
      ["**razorgirl**", "*razor* + *girl*", "Fuses a weapon and a gender marker into a job title."],
      ["**wetware**", "Analogy with *hardware/software*", "Argues, in one word, that people are equipment."],
    ],
    "Table 7. Coinages and near-coinages. The pattern is reuse rather than invention.",
  ),

  h2("D · Further reading", "D · Đọc thêm"),
  pair(
    "A short, opinionated list. Everything here is a real book or essay worth your time; nothing here is required to use this companion.",
    "Một danh sách ngắn và có quan điểm. Mọi mục ở đây đều là sách hoặc bài viết thật, đáng thời gian của bạn; không mục nào là bắt buộc để dùng cuốn sách đồng hành này.",
  ),
  bullets(
    [
      "**Primary.** *Neuromancer* itself, in a physical copy with wide margins — the only text this book is a companion to. Then *Count Zero* and *Mona Lisa Overdrive*, which answer questions the first novel leaves open.",
      "**Context.** Bruce Sterling's *Mirrorshades* preface remains the clearest contemporary statement of what the cyberpunk writers thought they were doing.",
      "**Craft.** Any edition of Gibson's later essays and interviews; his remarks on style are unusually practical, and unusually modest.",
      "**Language.** A learner's dictionary with CEFR labels (Oxford Advanced Learner's, or Cambridge Advanced Learner's) beside the lexicon in this book; the two disagree usefully.",
      "**Exams.** One official practice test per examination, taken cold, before you decide which of the five targets you are actually closest to.",
    ],
    [
      "**Nguyên tác.** Chính *Neuromancer*, một bản giấy có lề rộng — văn bản duy nhất mà cuốn sách này là bạn đồng hành. Sau đó là *Count Zero* và *Mona Lisa Overdrive*, hai cuốn trả lời những câu hỏi mà tiểu thuyết đầu để ngỏ.",
      "**Bối cảnh.** Lời tựa *Mirrorshades* của Bruce Sterling vẫn là tuyên ngôn rõ ràng nhất đương thời về điều các nhà văn cyberpunk nghĩ mình đang làm.",
      "**Tay nghề.** Bất kỳ tuyển tập tiểu luận và phỏng vấn nào của Gibson; những nhận xét của ông về văn phong thực dụng một cách bất thường, và khiêm tốn một cách bất thường.",
      "**Ngôn ngữ.** Một từ điển cho người học có gắn nhãn CEFR (Oxford Advanced Learner's hoặc Cambridge Advanced Learner's) đặt cạnh từ điển trong sách này; hai bên bất đồng một cách hữu ích.",
      "**Thi cử.** Mỗi kỳ thi một đề luyện chính thức, làm lạnh không chuẩn bị, trước khi bạn quyết định trong năm mục tiêu thì mục tiêu nào bạn thật sự gần nhất.",
    ],
  ),

  h2("E · Vietnamese–English index of key terms", "E · Bảng tra thuật ngữ Việt – Anh"),
  pair(
    "Twelve core concepts, with the Vietnamese term this edition uses, so that a reader discussing the novel in Vietnamese and writing about it in English does not have to translate twice.",
    "Mười hai khái niệm cốt lõi, kèm thuật ngữ tiếng Việt mà ấn bản này dùng, để người đọc bàn về tiểu thuyết bằng tiếng Việt và viết về nó bằng tiếng Anh không phải dịch hai lần.",
  ),
  table(
    ["Tiếng Việt", "English headword", "Note"],
    [1.3, 1.3, 2.4],
    [
      ["không gian mạng", "cyberspace", "Use *cyberspace* for Gibson's concept; *không gian số* for the general modern sense."],
      ["ma trận", "the matrix", "Capitalise neither in running text; the definite article is part of the term."],
      ["bản sao tâm thức", "construct", "Not *bản sao lưu* (backup): a construct converses."],
      ["chết não / đường thẳng", "flatline", "Keep the monitor image: *đường thẳng trên điện não đồ*."],
      ["phần mềm phòng vệ", "ICE", "Never translate the acronym; gloss it on first use."],
      ["tập đoàn tài phiệt", "zaibatsu", "Loanword in both languages; keep it."],
      ["thợ sửa việc / người dàn xếp", "fixer", "*Người môi giới* is too respectable for the novel's usage."],
      ["khu nghỉ dưỡng quỹ đạo", "orbital resort", "Freeside is a proper noun: do not translate the name."],
      ["cấu trúc ký sinh", "parasitic structure", "The novel's own judgement of Villa Straylight."],
      ["việc làm thuê", "employment", "The book's real subject; avoid *công việc* (task) here."],
      ["sự chiếm hữu", "ownership", "Distinguish from *sở hữu* (legal property) when discussing people."],
      ["diễn ngôn tự do gián tiếp", "free indirect discourse", "Standard term in Vietnamese narratology; keep both languages parallel."],
    ],
    "Table 8. A bilingual working vocabulary for discussion and essay writing.",
  ),

  callout(
    "A last word",
    [
      "A companion has done its job when the reader no longer needs it. If you finish this book and find that you are reading Gibson's sentences faster, arguing with his decisions, and reaching for a word because it is the right one rather than the impressive one, then the apparatus has succeeded and can be closed.",
    ],
    [
      "Một cuốn sách đồng hành đã hoàn thành nhiệm vụ khi người đọc không còn cần nó nữa. Nếu bạn đọc hết cuốn này và thấy mình đọc câu văn của Gibson nhanh hơn, tranh luận với các quyết định của ông, và với tay lấy một từ vì nó đúng chứ không phải vì nó nghe sang, thì bộ khung này đã thành công và có thể gấp lại.",
    ],
  ),
];
