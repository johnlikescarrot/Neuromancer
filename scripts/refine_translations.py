import json
from pathlib import Path

# Manual fixes for untranslated or mistranslated cyberpunk lines
MANUAL_TRANSLATION_FIXES = {
    # 36 specific items where vi was identical to en
    "0_0_185": "Linda.",
    "1_1_59": "12:06:26.",
    "2_1_17": "“Dixie?”",
    "2_1_49": "“Dixie...”",
    "2_2_21": "Linda.",
    "2_4_7": "“Dân giang hồ xã hội đen.”",
    "3_1_8": "Armitage.",
    "3_1_23": "“Dixie?”",
    "3_2_64": "“Molly.”",
    "3_3_26": "04:23:04.",
    "3_3_28": "C A S E : 0 0 0 0",
    "3_3_30": "0 0 0 0 0 0 0 0 .",
    "3_3_32": "G E N E R A L G (TỔNG CHỈ HUY)",
    "3_3_34": "T R A I N E D (ĐÃ HUẤN LUYỆN)",
    "3_3_35": "C O R T O F O R (MẬT HIỆU CORTO)",
    "3_3_37": "F I S T A N D (NẮM ĐẤM VÀ)",
    "3_3_39": "A S S T O (HẬU PHƯƠNG TỚI)",
    "3_3_40": "T H E P E N T (LẦU NĂM GÓC)",
    "3_3_41": "A G O N : : : : (NGŨ GIÁC ĐÀI)",
    "3_3_42": "W / M U T E '~ S (LỆNH ĐỒNG MINH)",
    "3_3_44": "G R I P O N (KẸP GIỮ CHẶT)",
    "3_3_45": "A R M I T A G (ARMITAGE)",
    "3_3_46": "E I S A (LÀ MỘT)",
    "3_3_47": "C O N S T R U (BẢN TÁI CẤU TRÚC)",
    "3_3_48": "C T O F G (CỦA TỔNG HÀNH DINH)",
    "3_3_50": "W / M U T E (WINTERMUTE)",
    "3_3_51": "S E Z A '~ S (KHẲNG ĐỊNH)",
    "3_3_53": "O F G (NGUỒN GỐC)",
    "3_3_61": ": : D I X I E",
    "3_3_64": "“Maelcum...”",
    "3_4_29": "“Dixie...”",
    "3_4_55": "07:02:18.",
    "3_5_22": ": : : : : J A C K (CẮM RẮC)",
    "3_5_97": "07:29:40.",
    "3_10_7": "“Đang hừng hực khí thế sẵn sàng xông trận.”",
    "4_0_48": "Vancouver.",
    # High-impact polish for opening and famous lines
    "0_0_0": "Bầu trời trên bến cảng mang màu sắc của màn hình vô tuyến, dò trúng vào một kênh tín hiệu chết.",
    "0_0_1": "“Không phải là tôi đang nghiện ngập đâu,” Case nghe ai đó cất tiếng, trong lúc anh lách mình qua đám đông quanh cửa quán Chat. “Chỉ là cơ thể tôi dường như đang bị thiếu hụt chất kích thích trầm trọng thôi.” Đó là một chất giọng đặc sệt cư dân Sprawl và một câu đùa điển hình vùng Sprawl. Chatsubo là quán bar dành cho dân viễn xứ chuyên nghiệp; bạn có thể ngồi uống ở đó suốt một tuần mà không hề nghe thấy lấy hai từ tiếng Nhật.",
    "0_0_2": "Ratz đang phục vụ sau quầy, cánh tay giả xấu xí của anh ta càu nhàu khi vươn ra rót một vại Kirin khác. Ratz là người biến dị gốc Đức, một gã khổng lồ với hàm răng cá sấu giả bằng thép không gỉ và đôi mắt nhợt nhạt vô cảm.",
    "0_1_0": "Không gian mạng (Cyberspace). Một ảo ảnh đồng thuận được trải nghiệm mỗi ngày bởi hàng tỷ người vận hành hợp pháp, tại mọi quốc gia, bởi những đứa trẻ đang học các khái niệm toán học...",
}

def main():
    path = Path("data/bilingual_novel.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Polish target benchmarks to be fully explicit and comprehensive
    data["target_benchmarks"] = {
        "IELTS": {
            "score": "Band 7.0 - 8.5+ Academic",
            "cefr": "C1 / C2",
            "skills_focus": "Lexical Resource & Grammatical Range through complex clause structures, syntactic inversions, and high-level collocations."
        },
        "TOEFL_iBT": {
            "score": "Score 90+ (Pre-Jan 21, 2026) / 5.0 (Post-Jan 21, 2026)",
            "cefr": "C1 Advanced",
            "skills_focus": "Advanced academic reading comprehension, contextual vocabulary inference, rhetorical purpose, and synthesis of multifaceted narrative arguments."
        },
        "Cambridge": {
            "score": "185 - 210 points (C1 Advanced / C2 Proficiency)",
            "cefr": "C1 - C2 Mastery",
            "skills_focus": "Mastery of advanced inversion, cleft sentences, subjunctive moods, absolute constructions, and idiomatic expressions."
        },
        "PTE_Academic": {
            "score": "Score 65 - 85+",
            "cefr": "C1 / C2",
            "skills_focus": "Rapid comprehension of sophisticated technological/sociological lexicon, abstract discourse, and sentence re-ordering reflex."
        },
        "DET": {
            "score": "Score 120 - 150+",
            "cefr": "C1 Advanced / C2",
            "skills_focus": "Enhanced academic vocabulary recognition (Read & Select), contextual cloze mastery, and complex paragraph stylistics."
        }
    }

    # Apply manual fixes
    fixed_count = 0
    for part in data["parts"]:
        for chap in part["chapters"]:
            for p in chap["paragraphs"]:
                pid = p["id"]
                if pid in MANUAL_TRANSLATION_FIXES:
                    p["vi"] = MANUAL_TRANSLATION_FIXES[pid]
                    fixed_count += 1
                else:
                    # Clean up common mechanical translation artifacts
                    p["vi"] = p["vi"].replace("một giọng nói ngổn ngang", "chất giọng vùng Sprawl")
                    p["vi"] = p["vi"].replace("trò đùa ngổn ngang", "trò đùa đặc trưng Sprawl")
                    p["vi"] = p["vi"].replace("thành phố Chiba", "Thành phố Chiba (Chiba City)")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Applied fixes to {fixed_count} paragraphs in {path}")

if __name__ == "__main__":
    main()
