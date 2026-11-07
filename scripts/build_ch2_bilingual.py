import json
import os
import time
from translate_core import translate_api

def polish_ch2_vietnamese(i, en, raw_vi):
    curated = {
        0: "Sau một năm ròng sống trong những buồng quan tài chật chội, căn phòng trên tầng hai mươi lăm của khách sạn Chiba Hilton này dường như rộng mênh mông. Căn phòng có kích thước mười nhân tám mét, là một nửa của một dãy phòng tổng thống cao cấp. Một chiếc máy pha cà phê Braun màu trắng đang tỏa hơi nghi ngút trên chiếc bàn thấp cạnh những tấm kính trượt dẫn ra một ban công hẹp.",
        1: "“Uống chút cà phê vào đi. Trông anh như thể đang chết mòn vì thiếu nó vậy.” Cô cởi chiếc áo khoác đen; khẩu súng bắn phi tiễu fletcher nằm lủng lẳng dưới cánh tay cô trong bộ đai đeo vai bằng nylon đen. Cô mặc một chiếc áo len sát nách màu xám với những chiếc khóa kéo bằng thép trơn dọc hai bên vai. Chống đạn. Case tự nhủ, rót cà phê vương vãi vào một chiếc cốc màu đỏ rực rỡ. Đôi tay và đôi chân anh có cảm giác nặng trịch và trơ trọi như làm bằng gỗ.",
        2: "“Case.” Anh ngước nhìn lên, lần đầu tiên nhìn thấy người đàn ông đó. “Tên tôi là Armitage.” Chiếc áo choàng tối màu mở phanh ra đến thắt lưng, để lộ vòm ngực rộng vạm vỡ không có lấy một sợi lông, cơ bụng phẳng lì và rắn chắc. Đôi mắt xanh lam nhạt đến mức khiến Case liên tưởng đến dung dịch thuốc tẩy. “Mặt trời đã lên rồi, Case. Hôm nay là ngày may mắn của cậu đấy, chàng trai.”",
        3: "Case vung cánh tay hất ngang và người đàn ông dễ dàng né được vệt cà phê nóng bỏng. Vệt ố màu nâu chảy dài trên bức tường giả giấy bồi dán tường của Nhật. Anh nhìn thấy chiếc nhẫn vàng có cạnh sắc móc qua dái tai trái của gã. Lực lượng Đặc nhiệm. Người đàn ông mỉm cười.",
        5: "“Cậu còn quá trẻ để nhớ về cuộc chiến tranh đó, phải không Case?” Armitage luồn bàn tay to lớn vuốt ngược mái tóc nâu cắt ngắn kiểu nhà binh. Một chiếc lắc tay bằng vàng nặng trịch lóe sáng trên cổ tay gã. “Leningrad, Kiev, Siberia. Chúng tôi đã phát minh ra giống nòi các cậu ở Siberia đấy, Case.”",
        8: "“Nắm Đấm Thét Gào (Screaming Fist), Case. Cậu ắt hẳn từng nghe cái tên đó rồi.”",
        11: "“Cậu là một cao bồi bàn điều khiển. Các phiên bản mẫu đầu tiên của những chương trình mà cậu dùng để bẻ khóa ngân hàng dữ liệu công nghiệp đều được phát triển cho chiến dịch Nắm Đấm Thét Gào. Dành cho cuộc đột kích vào mắt xích máy tính trung tâm Kirensk. Đơn vị cơ bản bao gồm một phi cơ siêu nhẹ Nightwing, một viên phi công, một cỗ máy điều khiển ma trận, và một kỵ sĩ mạng. Chúng tôi từng chạy một loại virus có tên là Chuột Chũi (Mole). Dòng Mole chính là thế hệ đầu tiên của những chương trình xâm nhập thực thụ.”",
        12: "“Chương trình phá băng (Icebreakers),” Case nói, qua miệng chiếc cốc đỏ.",
        13: "“Băng (Ice) xuất phát từ cụm từ I-C-E, Intrusion Countermeasures Electronics — Các thiết bị điện tử chống xâm nhập.”",
        20: "“Cậu sẽ nói sao nếu tôi bảo rằng chúng tôi có thể chữa lành tổn thương thần kinh cho cậu, hả Case?”",
        165: "Sau cuộc kiểm tra hậu phẫu tại phòng khám, Molly đưa anh ra bến cảng. Armitage đã đợi sẵn ở đó. Gã đã thuê bao trọn một chiếc tàu đệm khí. Hình ảnh cuối cùng của Chiba mà Case còn nhìn thấy là những góc cạnh tăm tối của các đại kiến trúc vòm arcology. Rồi màn sương mù khép lại trên mặt nước đen ngòm và những bãi trôi nổi của rác thải xốp phế liệu."
    }
    if i in curated:
        return curated[i]
    return raw_vi

def main():
    with open('data/chapters.json', 'r', encoding='utf-8') as f:
        chapters = json.load(f)

    ch2 = [c for c in chapters if c.get('chapter') == '2'][0]
    paras = ch2['paragraphs']

    cache_file = 'data/ch2_vi_cache.json'
    if os.path.exists(cache_file):
        with open(cache_file, 'r', encoding='utf-8') as f:
            vi_paras = json.load(f)
    else:
        vi_paras = []
        print(f"Translating {len(paras)} paragraphs for Chapter 2...")
        for idx, p in enumerate(paras):
            t = translate_api(p)
            vi_paras.append(t)
            if idx % 20 == 0:
                print(f"  Translated {idx+1}/{len(paras)}")
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(vi_paras, f, ensure_ascii=False, indent=2)

    sections = []

    vocab_checkpoints = {
        15: {
            "title": "CYBERNETIC ESPIONAGE & ICE PROTOCOLS (ADVANCED C1/C2)",
            "items": [
                {"word": "intrusion", "ipa": "/ɪnˈtruː.ʒən/", "level": "C1 Academic / TOEFL 92", "en_def": "the action of illegally entering, breaking into, or invading a secure domain/system", "vi_def": "sự xâm nhập trái phép vào hệ thống dữ liệu"},
                {"word": "countermeasures", "ipa": "/ˈkaʊn.təˌmeʒ.əz/", "level": "C1 Military / Defence", "en_def": "actions, devices, or systems designed to prevent, neutralize, or counter an adversary's move", "vi_def": "các biện pháp đối phó, hàng rào phản kích"},
                {"word": "biocompatibility", "ipa": "/ˌbaɪ.əʊ.kəmˌpæt.əˈbɪl.ə.ti/", "level": "C2 Bio-tech English", "en_def": "the property of being compatible with living tissue or a living system by not producing a toxic or immunological response", "vi_def": "khả năng tương thích sinh học giữa mô sống và máy móc"},
                {"word": "neuroplasticity", "ipa": "/ˌnjʊə.rəʊ.plæsˈtɪs.ə.ti/", "level": "C2 Neuroscience", "en_def": "the ability of the neural network in the brain to reorganize itself through growth and development", "vi_def": "tính mềm dẻo của hệ thần kinh, khả năng tự tái tạo"}
            ]
        },
        50: {
            "title": "CLINICAL NEUROSURGERY & BIO-ENGINEERING BENCHMARKS",
            "items": [
                {"word": "carapace", "ipa": "/ˈkær.ə.peɪs/", "level": "C2 Biology / IELTS 8.0", "en_def": "the hard upper shell of a turtle, crustacean, or arachnid; armor casing", "vi_def": "mai, giáp bọc cứng cáp (dùng cho vỏ cua/robot bảo vệ)"},
                {"word": "endorphin", "ipa": "/enˈdɔː.fɪn/", "level": "C1 Medical / DET 120", "en_def": "any of a group of hormones secreted within the brain and nervous system having pain-relieving properties", "vi_def": "chất giảm đau tự nhiên của hệ thần kinh"},
                {"word": "inhibitor", "ipa": "/ɪnˈhɪb.ɪ.tər/", "level": "C1 Academic Science", "en_def": "a substance that slows down or prevents a particular chemical reaction or biological process", "vi_def": "chất ức chế phản ứng hoặc dẫn truyền sinh học"},
                {"word": "synaesthesia", "ipa": "/ˌsɪn.əsˈθiː.zi.ə/", "level": "C2 Literary Psychology", "en_def": "a perceptual phenomenon in which stimulation of one sensory pathway leads to involuntary experiences in a second sensory pathway", "vi_def": "hiện tượng cảm giác kèm, sự hòa lẫn giữa các giác quan"}
            ]
        }
    }

    cultural_notes = {
        13: {
            "title": "ICE VÀ ICEBREAKER: THUẬT NGỮ KINH ĐIỂN CỦA AN NINH MẠNG HIỆN ĐẠI",
            "content": "Từ viết tắt ICE (Intrusion Countermeasures Electronics) do Tom Maddox gợi ý và William Gibson hoàn thiện trong Neuromancer để chỉ các hệ thống tường lửa (firewall) chủ động có khả năng phản kích và tiêu diệt não bộ của kẻ xâm nhập. 'Icebreaker' (chương trình phá băng) là tiền thân của các phần mềm khai thác lỗ hổng và thâm nhập mạng bảo mật cao hiện nay."
        },
        30: {
            "title": "STREET SAMURAI: HÌNH TƯỢNG VÕ SĨ ĐƯỜNG PHỐ",
            "content": "Molly Millions là hình tượng kinh điển khởi đầu cho dòng nhân vật 'Street Samurai' (Võ sĩ đường phố) trong văn học và game Cyberpunk (như Shadowrun hay Cyberpunk 2077). Được nâng cấp với thấu kính thị giác cấy ghép phản quang, phản xạ thần kinh nhân tạo và mười lưỡi dao mổ ẩn dưới móng tay, cô đại diện cho đỉnh cao chiến đấu cơ học và sự độc lập tuyệt đối giữa thế giới ngầm."
        }
    }

    for idx, (en_p, raw_vi) in enumerate(zip(paras, vi_paras)):
        vi_p = polish_ch2_vietnamese(idx, en_p, raw_vi)

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
        "is_first_of_part": False,
        "chapter": "CHAPTER 2",
        "chapter_vi": "CHƯƠNG 2",
        "sections": sections
    }

    with open('content/ch02_bilingual.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print("Successfully built content/ch02_bilingual.json with all paragraphs and annotations!")

if __name__ == '__main__':
    main()
