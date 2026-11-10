/** Original study material. No passage of the novel is generated or continued here. */
export interface StudyModule {
  id: string;
  eyebrow: string;
  title: string;
  intro: string;
  blocks: Array<{
    heading: string;
    body: string;
    bullets?: string[];
    example?: { en: string; vi: string; note: string };
  }>;
}

export const STUDY_MODULES: StudyModule[] = [
  {
    id: 'method',
    eyebrow: '01 · Learning architecture',
    title: 'Đọc sâu, không đọc thay',
    intro: 'Mục tiêu là tự đọc văn bản tiếng Anh phức tạp: bản dịch là công cụ kiểm chứng, không phải điểm tựa đầu tiên. Một chu trình 25–35 phút cho mỗi phiên sẽ hiệu quả hơn việc đọc lướt cả chương.',
    blocks: [
      {
        heading: 'Chu trình bốn lượt',
        body: 'Chọn 3–5 cặp đoạn. Ghi lại suy luận bằng từ chính xác, tránh cảm giác “đọc xong là hiểu”.',
        bullets: [
          'Lượt 1 — Chỉ đọc tiếng Anh: xác định ai làm gì, thái độ và chuyển biến trong đoạn.',
          'Lượt 2 — Giải mã: gạch dưới khung câu, từ nối và từ khóa; đoán nghĩa trước khi tra.',
          'Lượt 3 — Đối chiếu tiếng Việt: sửa suy luận sai, chú ý khác biệt trật tự và sắc thái.',
          'Lượt 4 — Tái sử dụng: che văn bản, tóm tắt bằng 2 câu rồi viết một câu mới với cấu trúc vừa học.',
        ],
      },
      {
        heading: 'Ghi chú tối giản có thể ôn lại',
        body: 'Mỗi mục chỉ gồm từ/cụm, ngữ cảnh do bạn tự viết, một collocate và câu ứng dụng. Không sao chép cả định nghĩa dài.',
        example: {
          en: 'The proposal was plausible, albeit difficult to implement at scale.',
          vi: 'Đề xuất có vẻ hợp lý, dù khó triển khai trên quy mô lớn.',
          note: 'albeit + adjective: liên từ nhượng bộ cô đọng, phù hợp văn viết trang trọng; không dùng như “although + clause”.',
        },
      },
      {
        heading: 'Khoảng cách ôn tập',
        body: 'Ôn sau 1 ngày, 3 ngày, 7 ngày và 21 ngày. Mỗi lần phải gọi lại nghĩa từ trí nhớ trước khi xem đáp án. Đánh dấu “biết / chưa chắc / chưa biết”; chỉ tạo thẻ mới khi thẻ cũ đã được ôn.',
      },
    ],
  },
  {
    id: 'reading',
    eyebrow: '02 · Academic reading',
    title: 'Từ câu dài đến lập luận',
    intro: 'Văn chương và bài đọc học thuật cùng đòi hỏi khả năng nhận diện quan hệ giữa các ý. Khác biệt nằm ở mục đích: văn chương tạo trải nghiệm; bài học thuật thường xây dựng và kiểm chứng lập luận.',
    blocks: [
      {
        heading: 'Bóc tách câu theo bốn bước',
        body: 'Tìm động từ chia thì trước, sau đó chủ ngữ tương ứng. Tạm gác cụm chèn, phân từ và đồng vị để đọc khung câu; cuối cùng trả từng lớp bổ nghĩa về vị trí.',
        bullets: [
          'Dấu phẩy không phải ranh giới mệnh đề đáng tin tuyệt đối.',
          'Đại từ phải được nối về đúng danh từ; nếu có hai ứng viên, kiểm tra logic và số ít/số nhiều.',
          'Từ nối nhượng bộ, nguyên nhân hoặc tương phản thường quan trọng hơn một tính từ hiếm.',
        ],
      },
      {
        heading: 'Suy luận có kiểm soát',
        body: 'Câu trả lời suy luận phải được hỗ trợ bởi chi tiết trong văn, nhưng không nhất thiết lặp nguyên câu chữ. Tránh phương án quá rộng, quá tuyệt đối hoặc đúng với kiến thức nền nhưng không nằm trong đoạn.',
        example: {
          en: 'Unlike the earlier system, the revised model consumes less power; nevertheless, its adoption remains limited.',
          vi: 'Khác hệ thống trước, mô hình điều chỉnh tiêu thụ ít điện hơn; tuy vậy, việc áp dụng nó vẫn còn hạn chế.',
          note: 'Có thể suy ra tiết kiệm năng lượng chưa đủ để thúc đẩy áp dụng; không thể kết luận chi phí là nguyên nhân vì văn bản không nêu.',
        },
      },
      {
        heading: 'Rhetorical purpose — mục đích tu từ',
        body: 'Với mỗi chi tiết, hỏi “tác giả đưa chi tiết này vào để làm gì?”: định nghĩa, minh họa, đủ điều kiện cho nhận định, phản bác hay chuyển hướng. Đây là cầu nối hữu ích giữa đọc văn chương và TOEFL/IELTS.',
      },
    ],
  },
  {
    id: 'lexis',
    eyebrow: '03 · Lexical resource',
    title: 'Từ vựng theo hệ thống',
    intro: 'Điểm cao không đến từ việc thay mọi từ quen thuộc bằng từ “khó”. Ưu tiên độ chính xác, kết hợp tự nhiên, register và khả năng paraphrase mà không làm đổi nghĩa.',
    blocks: [
      {
        heading: 'Bốn trục của một mục từ',
        body: 'Học word family, collocation, giới từ và sắc thái. Với thuật ngữ Cyberpunk, tách nghĩa trong thế giới truyện khỏi nghĩa có thể dùng trong bài học thuật.',
        bullets: [
          'ephemeral (adj): ephemeral beauty / an ephemeral trend — ngắn ngủi, phù du.',
          'intricate (adj): an intricate mechanism / an intricate argument — phức tạp do nhiều chi tiết liên kết.',
          'surreptitious (adj): surreptitious monitoring — bí mật, thường hàm ý không được chấp thuận.',
          'juxtapose (verb): juxtapose A with B — đặt cạnh để làm nổi bật sự tương phản.',
        ],
      },
      {
        heading: 'Paraphrase bằng thay đổi cấu trúc',
        body: 'Không chỉ thay từ đồng nghĩa. Có thể chuyển danh từ thành động từ, đổi chủ thể hoặc gộp hai câu; sau đó kiểm tra lại ai chịu trách nhiệm cho hành động và mức độ chắc chắn.',
        example: {
          en: 'The rapid expansion of surveillance has prompted concern among civil-liberties advocates.',
          vi: 'Việc giám sát mở rộng nhanh chóng đã làm dấy lên lo ngại trong số những người ủng hộ quyền tự do dân sự.',
          note: 'Có thể diễn đạt: “Civil-liberties advocates are increasingly concerned because surveillance is expanding rapidly.” Hai câu giữ quan hệ nguyên nhân nhưng thay trọng tâm câu.',
        },
      },
    ],
  },
  {
    id: 'writing',
    eyebrow: '04 · Academic writing',
    title: 'Viết chặt, diễn đạt linh hoạt',
    intro: 'Các cấu trúc C1 chỉ có giá trị khi phục vụ ý. Đảo ngữ sai chủ–vị hay từ nối hoa mỹ sẽ làm giảm độ rõ ràng thay vì nâng band điểm.',
    blocks: [
      {
        heading: 'Đoạn lập luận năm chức năng',
        body: 'Một đoạn có thể gồm: câu chủ đề; giải thích cơ chế; ví dụ cụ thể; giới hạn hoặc phản ý; câu kết nối về luận điểm. Không cần cứng nhắc đủ năm câu, nhưng mỗi chức năng phải dễ nhận ra.',
        example: {
          en: 'Although automation can eliminate repetitive tasks, its benefits depend on whether displaced workers receive credible retraining.',
          vi: 'Mặc dù tự động hóa có thể loại bỏ công việc lặp lại, lợi ích của nó phụ thuộc vào việc người lao động mất việc có được đào tạo lại đáng tin hay không.',
          note: 'Cấu trúc Although + clause, main clause đặt nhượng bộ trước kết luận có điều kiện; depend on whether giữ đúng giới từ.',
        },
      },
      {
        heading: 'Đảo ngữ và câu chẻ: dùng có chọn lọc',
        body: '“Not only does X…” và “It is X that…” tạo trọng tâm. Chỉ dùng khi sự nhấn mạnh cần thiết; không ghép nhiều cấu trúc nhấn vào cùng một câu.',
        bullets: [
          'Not only does the device store data, but it also interprets patterns.',
          'What matters is not the novelty of the technology but its social consequence.',
          'Had the policy been introduced earlier, its impact might have been greater.',
        ],
      },
      {
        heading: 'Tự hiệu đính theo ba lượt',
        body: 'Lượt một kiểm tra task response và logic; lượt hai kiểm tra mạch nối và tham chiếu; lượt ba kiểm tra ngữ pháp, chính tả, dấu câu. Đừng sửa từng chữ ngay khi đang xây dựng ý.',
      },
    ],
  },
  {
    id: 'assessment',
    eyebrow: '05 · Transfer to tests',
    title: 'Chuyển năng lực sang phòng thi',
    intro: 'Đây là học liệu phát triển ngôn ngữ, không phải khóa luyện đề và không bảo đảm một mức điểm. Chiến lược thời gian, dạng bài và rubric hiện hành cần được luyện riêng từ tài liệu chính thức của tổ chức thi.',
    blocks: [
      {
        heading: 'Bản đồ kỹ năng',
        body: 'Cùng một hoạt động đọc có thể phục vụ nhiều bài thi nếu bạn chuyển hóa sản phẩm đầu ra.',
        bullets: [
          'IELTS: phân biệt ý chính/chi tiết; viết tóm tắt 70–100 chữ không sao chép nguyên câu.',
          'TOEFL: ghi mục đích đoạn, quan hệ ý và suy luận; thực hành trên máy với thời gian giới hạn.',
          'Cambridge: nhận diện sắc thái, collocation và biến đổi cấu trúc trong Use of English.',
          'PTE Academic: luyện nói lại nội dung chính xác, mạch lạc; kiểm tra yêu cầu từng dạng bài hiện hành.',
          'DET: mở rộng nhận diện từ trong ngữ cảnh và sản xuất câu ngắn đúng ngữ pháp; không học từ tách rờ i.',
        ],
      },
      {
        heading: 'Bảng tự chấm sau mỗi phiên',
        body: 'Chấm 0–2 cho mỗi tiêu chí: 0 = chưa làm được; 1 = làm được khi có hỗ trợ; 2 = làm độc lập và giải thích được.',
        bullets: [
          'Tôi xác định đúng khung câu và quan hệ giữa các mệnh đề.',
          'Tôi nêu được bằng chứng cho suy luận thay vì dựa vào cảm giác.',
          'Tôi dùng lại một cấu trúc/collocation trong ngữ cảnh mới.',
          'Tôi tóm tắt được mà không nhìn bản dịch hoặc sao chép câu gốc.',
        ],
      },
    ],
  },
  {
    id: 'plan',
    eyebrow: '06 · Four-week cycle',
    title: 'Kế hoạch bốn tuần',
    intro: 'Năm buổi mỗi tuần, 30–45 phút/buổi. Lượng nhỏ nhưng đều giúp duy trì truy hồi và sản xuất ngôn ngữ. Điều chỉnh theo năng lực thực tế; không cần đọc theo thứ tự nếu mục tiêu là luyện một kỹ năng cụ thể.',
    blocks: [
      {
        heading: 'Tuần 1 — Chẩn đoán và nền tảng',
        body: 'Đọc một đoạn không bản dịch, ghi thời gian và lỗi. Các buổi tiếp theo tập bóc tách câu, tạo tối đa 10 mục từ và viết một tóm tắt cuối tuần. Giữ bản đầu làm mốc so sánh.',
      },
      {
        heading: 'Tuần 2 — Suy luận và sắc thái',
        body: 'Mỗi buổi chọn một chi tiết để giải thích mục đích tu từ. Phân biệt dữ kiện, suy luận và phỏng đoán. Viết lại hai câu theo register trang trọng mà không thay đổi mức độ chắc chắn.',
      },
      {
        heading: 'Tuần 3 — Sản xuất',
        body: 'Viết hai đoạn phân tích và thu âm hai bài nói 90 giây. Dùng checklist để sửa lập luận trước ngôn ngữ. Chọn lại các lỗi lặp lại thành bài tập nhỏ cho ngày hôm sau.',
      },
      {
        heading: 'Tuần 4 — Tổng hợp và đánh giá',
        body: 'Làm lại nhiệm vụ tuần 1 với văn bản mới, giới hạn thời gian. So sánh độ chính xác, tốc độ và chất lượng giải thích. Sau đó dùng đề/rubric chính thức của kỳ thi mục tiêu để đo mức chuyển giao kỹ năng.',
      },
    ],
  },
];
