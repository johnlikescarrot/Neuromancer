import json
import os
import time
from translate_core import translate_api

def polish_ch1_vietnamese(i, en, raw_vi):
    # Specialized literary polish for key cyberpunk lines
    curated = {
        0: "Bầu trời phía trên bến cảng mang màu của một màn hình tivi bắt trúng kênh tín hiệu chết.",
        1: "“Không phải là tôi đang phê pha,” Case nghe thấy ai đó nói khi anh lách mình qua đám đông quanh cửa quán Chat. “Chỉ là cơ thể tôi vừa phát tác cơn thiếu thuốc trầm trọng thôi.” Đó là một giọng nói vùng Sprawl và một câu đùa kiểu Sprawl. Quán Chatsubo vốn là quán bar dành cho dân tha hương chuyên nghiệp; bạn có thể ngồi uống ở đó suốt cả tuần mà chẳng bao giờ nghe thấy lấy hai từ tiếng Nhật.",
        2: "Ratz đang đứng quầy, cánh tay cơ khí giả của gã giật giật đều đặn khi gã rót đầy một khay bia Kirin tươi. Gã nhìn thấy Case và mỉm cười, hàm răng gã là một mạng lưới thép Đông Âu đan xen với những mảng mục nát ố nâu. Case tìm được một chỗ ở quầy bar, chen giữa làn da rám nắng kỳ quặc của một trong những ả đào nhà Lonny Zone và bộ quân phục hải quân chỉnh tề của một gã châu Phi cao lớn có gò má hằn những vệt sẹo bộ tộc ngay ngắn. “Wage ghé qua đây lúc sớm, cùng hai gã du côn joeboy,” Ratz nói, đẩy một vại bia qua mặt quầy bằng bàn tay lành lặn. “Có mối làm ăn gì với cậu à, Case?”",
        3: "Case nhún vai. Cô ả bên phải anh khúc khích cười rồi huých nhẹ vào người anh.",
        4: "Nụ cười của gã pha chế càng nở rộng. Vẻ xấu xí của gã đã đi vào huyền thoại. Trong một thời đại mà vẻ đẹp có thể mua được dễ dàng, sự thiếu thốn nhan sắc của gã lại mang một nét gì đó đường bệ, huy hoàng. Cánh tay cổ lỗ rít lên ken két khi gã với lấy một vại bia khác. Đó là một cánh tay giả quân sự của Nga, một bộ thao tác phản hồi lực bảy chức năng, bọc trong lớp nhựa màu hồng bẩn thỉu. “Cậu đúng là một nghệ sĩ quá đỗi, Herr Case.” Ratz khịt mũi gầm gừ; âm thanh ấy thay cho tiếng cười. Gã gãi gãi cái bụng phệ lộ ra dưới lớp áo sơ mi trắng bằng cái vuốt màu hồng. “Cậu là nghệ sĩ của những phi vụ có đôi chút nực cười.”",
        5: "“Chắc rồi,” Case nói, nhấp một ngụm bia. “Phải có ai đó vui nhộn ở cái chốn này chứ. Mà kẻ đó dứt khoát đếch phải lão rồi.”",
        15: "Người Nhật đã quên nhiều kiến thức phẫu thuật thần kinh hơn cả những gì người Trung Quốc từng biết. Những phòng khám chợ đen ở Chiba là đỉnh cao công nghệ, các hệ thống kỹ thuật hoàn toàn mới được thay thế hàng tháng, vậy mà họ vẫn không thể hàn gắn được tổn thương mà anh đã phải gánh chịu tại khách sạn Memphis đó.",
        16: "Một năm ở đây và anh vẫn mơ về không gian ảo (cyberspace), niềm hy vọng cứ lụi tàn dần qua từng đêm. Mọi liều thuốc kích thích speed anh từng nạp, mọi khúc cua anh từng rẽ và mọi lối tắt anh từng lách qua ở Night City, anh vẫn thấy ma trận hiện về trong giấc ngủ, những mạng tinh thể logic rực rỡ mở ra trên khoảng hư không vô sắc... Giờ đây Sprawl là một chặng đường về kỳ lạ và thăm thẳm bên kia bờ Thái Bình Dương, và anh không còn là một tay điều khiển bàn điều khiển, không còn là chàng cao bồi không gian ảo. Chỉ là một kẻ xoay xở kiếm sống tầm thường khác, gắng gượng qua ngày. Nhưng những giấc mơ ập đến trong đêm xứ Nhật tựa thứ tà thuật voodoo dây điện sống, và anh sẽ khóc vì nó, bật khóc trong cơn mê, rồi thức giấc đơn độc trong bóng tối, co ro trong khoang con nhộng tại một khách sạn quan tài nào đó, đôi bàn tay cào cấu vào phiến đệm, lớp mút xốp temperfoam vón cục giữa các ngón tay, tuyệt vọng với tìm bàn điều khiển vốn đã chẳng còn ở đó nữa.",
        23: "Case hai mươi tư tuổi. Năm hai mươi hai tuổi, anh từng là một cao bồi, một tay trộm dữ liệu siêu đẳng, một trong những tay cừ khôi nhất ở Sprawl. Anh từng được đào tạo bởi những huyền thoại xuất sắc nhất, bởi McCoy Pauley và Bobby Quine, những tượng đài trong giới. Anh từng hoạt động trong cơn hưng phấn adrenaline gần như triền miên, hệ quả của tuổi trẻ và kỹ năng siêu việt, cắm giắc cắm thần kinh vào cỗ máy cyberspace được tinh chỉnh riêng nhằm phóng chiếu ý thức phi thể xác của mình vào ảo giác đồng thuận mang tên ma trận (the matrix). Một kẻ trộm, anh từng làm việc cho những tên trộm khác giàu có hơn, những kẻ thuê mướn cung cấp các phần mềm ngoại lai tinh vi cần thiết để chọc thủng những bức tường kiên cố của hệ thống các tập đoàn, mở toang những ô cửa dẫn vào các mỏ dữ liệu màu mỡ.",
        24: "Anh đã phạm phải sai lầm kinh điển, sai lầm mà anh từng thề sẽ không bao giờ mắc phải. Anh đã ăn trộm của chính những kẻ thuê mình. Anh giữ lại một phần cho riêng mình và cố tuồn nó qua một tay tiêu thụ đồ gian ở Amsterdam. Anh vẫn không hiểu làm sao họ phát hiện ra, dẫu giờ đây điều đó chẳng còn quan trọng nữa. Lúc ấy anh đã chuẩn bị tinh thần đón nhận cái chết, nhưng họ chỉ mỉm cười. Họ bảo anh rằng dĩ nhiên anh cứ tự nhiên, cứ cầm lấy số tiền đó đi. Và anh sẽ cần đến nó đấy. Bởi vì — vẫn với nụ cười ấy — họ sẽ bảo đảm rằng anh sẽ không bao giờ còn có thể hành nghề được nữa.",
        25: "Họ hủy hoại hệ thần kinh của anh bằng một loại độc tố nấm mycotoxin quân dụng thời chiến của Nga.",
        26: "Bị trói chặt trên giường trong một khách sạn ở Memphis, tài năng của anh bị thiêu rụi từng micron một, anh đã rơi vào ảo giác suốt ba mươi giờ đồng hồ.",
        27: "Tổn thương cực kỳ vi tế, tinh vi, và hiệu quả một cách tàn nhẫn.",
        28: "Đối với Case, người từng sống vì sự thăng hoa phi thể xác của không gian ảo, đó chính là Sự Sa Ngã (the Fall). Trong những quán bar mà anh từng lui tới thời còn là một cao bồi cự phách, phong thái của giới thượng đẳng luôn gắn liền với một sự khinh miệt thản nhiên đối với xác thịt. Thể xác chỉ là miếng thịt tầm thường. Giờ đây, Case đã rơi vào chốn ngục tù của chính thể xác mình.",
        220: "Cô xòe hai bàn tay ra, lòng bàn tay hướng lên trên, những ngón tay trắng ngần hơi xòe nhẹ, và với một tiếng lách cách êm ru, mười lưỡi dao mổ hai lưỡi dài bốn phân trượt ra khỏi ổ chứa bên dưới những móng tay màu đỏ rượu vang rực rỡ."
    }
    if i in curated:
        return curated[i]
    return raw_vi

def main():
    with open('data/chapters.json', 'r', encoding='utf-8') as f:
        chapters = json.load(f)

    ch1 = [c for c in chapters if c.get('chapter') == '1'][0]
    paras = ch1['paragraphs']

    cache_file = 'data/ch1_vi_cache.json'
    if os.path.exists(cache_file):
        with open(cache_file, 'r', encoding='utf-8') as f:
            vi_paras = json.load(f)
    else:
        vi_paras = []
        print(f"Translating {len(paras)} paragraphs for Chapter 1...")
        for idx, p in enumerate(paras):
            t = translate_api(p)
            vi_paras.append(t)
            if idx % 20 == 0:
                print(f"  Translated {idx+1}/{len(paras)}")
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(vi_paras, f, ensure_ascii=False, indent=2)

    sections = []

    # Study notes & vocab mapping at pedagogical checkpoints
    vocab_checkpoints = {
        5: {
            "title": "CHIBA CITY & THE UNDERWORLD: HIGH-LEVEL ACADEMIC VOCABULARY",
            "items": [
                {"word": "prosthetic", "ipa": "/prɒsˈθet.ɪk/", "level": "C1 / IELTS 7.5", "en_def": "relating to an artificial body part, such as a limb, tooth, or eye", "vi_def": "thuộc về chi giả, bộ phận cơ thể giả"},
                {"word": "monotonously", "ipa": "/məˈnɒt.ən.əs.li/", "level": "C1 / TOEFL 95", "en_def": "in a dull, unvarying, and repetitive tone or manner", "vi_def": "đều đều, đơn điệu, không đổi nhịp"},
                {"word": "heraldic", "ipa": "/hɪˈræl.dɪk/", "level": "C2 / Cambridge CPE 190+", "en_def": "bearing distinctive, prestigious historic or symbolic significance", "vi_def": "mang tính huy hiệu, đường bệ, có dấu ấn biểu trưng"},
                {"word": "force-feedback", "ipa": "/fɔːs ˈfiːd.bæk/", "level": "Technical C1", "en_def": "the simulation of physical sensations such as resistance or vibration in a human-machine interface", "vi_def": "cơ chế phản hồi lực trong giao diện máy móc - thần kinh"}
            ]
        },
        17: {
            "title": "CYBERSPACE & LOSS: ACADEMIC & CEFR C1/C2 VOCABULARY",
            "items": [
                {"word": "supplant", "ipa": "/səˈplɑːnt/", "level": "C2 / GRE / IELTS 8.0", "en_def": "to supersede and replace something through superior force, innovation, or efficiency", "vi_def": "thay thế, soán chỗ, vượt mặt"},
                {"word": "lattices", "ipa": "/ˈlæt.ɪ.sɪz/", "level": "C1 / PTE 70+", "en_def": "interlaced structures or regular periodic geometrical frameworks", "vi_def": "mạng tinh thể, mạng lưới cấu trúc không gian"},
                {"word": "consensual", "ipa": "/kənˈsen.sju.əl/", "level": "C1 / TOEFL 92", "en_def": "existing by mutual agreement or shared perception among a community", "vi_def": "đồng thuận, được sự nhất trí chung"},
                {"word": "disembodied", "ipa": "/ˌdɪs.ɪmˈbɒd.id/", "level": "C1 / DET 125", "en_def": "separated from or existing without a biological physical body", "vi_def": "phi thể xác, tách rời khỏi thân xác"}
            ]
        },
        33: {
            "title": "THE FALL & BLACK MARKET PHENOMENOLOGY",
            "items": [
                {"word": "exultation", "ipa": "/ˌeɡ.zʌlˈteɪ.ʃən/", "level": "C2 / Cambridge 190+", "en_def": "a feeling of triumphant elation, supreme ecstasy, or boundless joy", "vi_def": "sự hoan hỉ tột độ, niềm thăng hoa đắc thắng"},
                {"word": "atavism", "ipa": "/ˈæt.ə.vɪ.zəm/", "level": "C2 / GRE Academic", "en_def": "a recurrence of or reversion to an earlier ancestral type, trait, or behavior", "vi_def": "sự lại giống, trạng thái hồi tố về thời nguyên thủy"},
                {"word": "mycotoxin", "ipa": "/ˌmaɪ.kəʊˈtɒk.sɪn/", "level": "Advanced Bio-tech", "en_def": "a toxic secondary metabolite produced by organisms of the fungus kingdom", "vi_def": "độc tố nấm mốc (đặc biệt trong chiến tranh sinh học thần kinh)"},
                {"word": "subcutaneous", "ipa": "/ˌsʌb.kjuːˈteɪ.ni.əs/", "level": "C1 Medical English", "en_def": "applied, located, or existing under the skin", "vi_def": "dưới da (chíp cấy ghép, vi mạch sinh học)"}
            ]
        }
    }

    cultural_notes = {
        0: {
            "title": "KÍNH VẠN HOA CỦA ĐẦU SÁCH: CÂU MỞ ĐẦU KINH ĐIỂN CỦA VĂN HỌC THẾ KỶ 20",
            "content": "Câu mở đầu kinh điển: 'The sky above the port was the color of television, tuned to a dead channel' (Bầu trời phía trên bến cảng mang màu của một màn hình tivi bắt trúng kênh tín hiệu chết). Vào năm 1984 khi cuốn sách ra đời, 'dead channel' trên tivi CRT analog phát ra nhiễu tĩnh điện xám xịt nhấp nháy ('snow/static'). Chi tiết này lập tức thiết lập thế giới quan cyberpunk nơi tự nhiên đã bị đồng hóa và mô tả hoàn toàn bằng ẩn dụ công nghệ và màn hình điện tử."
        },
        23: {
            "title": "THUẬT NGỮ CYBERSPACE VÀ COWBOY KHÔNG GIAN ẢO",
            "content": "William Gibson chính là người đã phổ biến và định hình từ 'Cyberspace' vào văn hóa đại chúng qua Neuromancer. 'Console cowboy' (cao bồi bàn điều khiển) là hình tượng người dịch chuyển ý thức vào mạng lưới dữ liệu toàn cầu bằng 'deck' (thiết bị điều khiển giao diện thần kinh), mang tinh thần độc lập, liều lĩnh và nổi loạn của những chàng cao bồi viễn Tây nước Mỹ thế kỷ 19."
        }
    }

    for idx, (en_p, raw_vi) in enumerate(zip(paras, vi_paras)):
        vi_p = polish_ch1_vietnamese(idx, en_p, raw_vi)

        if idx in cultural_notes:
            sections.append({
                "type": "note",
                "title": cultural_notes[idx]["title"],
                "content": cultural_notes[idx]["content"]
            })

        sections.append({
            "type": "parallel",
            "en": en_p,
            "vi": vi_p
        })

        if idx in vocab_checkpoints:
            sections.append({
                "type": "vocab",
                "title": vocab_checkpoints[idx]["title"],
                "items": vocab_checkpoints[idx]["items"]
            })

    output_data = {
        "part": "PART ONE - CHIBA CITY BLUES",
        "part_vi": "PHẦN MỘT - NỖI SẦU THÀNH PHỐ CHIBA",
        "is_first_of_part": True,
        "chapter": "CHAPTER 1",
        "chapter_vi": "CHƯƠNG 1",
        "sections": sections
    }

    os.makedirs('content', exist_ok=True)
    with open('content/ch01_bilingual.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print("Successfully built content/ch01_bilingual.json with all paragraphs and annotations!")

if __name__ == '__main__':
    main()
