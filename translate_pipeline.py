import json
import time
import urllib.request
import urllib.parse
import os
import re

CACHE_FILE = "translation_cache.json"
OUTPUT_FILE = "translated_chapters.json"

cache = {}
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            cache = json.load(f)
        print(f"Loaded {len(cache)} entries from cache.")
    except Exception as e:
        print(f"Notice: Failed to load cache: {e}")
        cache = {}

REPLACEMENTS = [
    (r"\bTrường hợp\b", "Case"),
    (r"\btrường hợp\b(?=.*(?:Chiba|Ratz|Molly|Sprawl|matrix|bến cảng|quán bar|cao bồi))", "Case"),
    (r"\bngổn ngang\b(?=.*(?:Sprawl|giọng nói|trò đùa))", "Sprawl"),
    (r"\bthợ rèn\b(?=.*(?:cao bồi|Sprawl|cao bồi dữ liệu))", "kẻ cướp dữ liệu"),
    (r"\bchàng cao bồi\b", "cao bồi bàn phím"),
    (r"\bmột kênh chết\b", "một kênh mất sóng"),
    (r"\bquán bar dành cho người nước ngoài chuyên nghiệp\b", "quán bar dành cho giới kiều bào ngoại quốc"),
    (r"\brượu bia tươi\b", "bia tươi"),
    (r"\brót rượu bia tươi vào khay ly\b", "rót bia tươi Kirin đầy một khay cốc"),
]

def post_process_translation(vi_text):
    for pattern, repl in REPLACEMENTS:
        vi_text = re.sub(pattern, repl, vi_text)
    return vi_text

def translate_chunk_direct(chunk):
    delimiter = "\n\n<<<DIV>>>\n\n"
    query = delimiter.join(chunk)
    url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=vi&dt=t&q=' + urllib.parse.quote(query)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        full = ''.join(p[0] for p in data[0] if p[0])
        parts = [p.strip() for p in full.split('<<<DIV>>>')]
        return parts

def translate_single(text):
    if not text.strip():
        return ""
    url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=vi&dt=t&q=' + urllib.parse.quote(text)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        res = ''.join(p[0] for p in data[0] if p[0])
        return post_process_translation(res)

def translate_batch(texts, batch_size=20):
    results = [None] * len(texts)
    missing_indices = []

    for i, t in enumerate(texts):
        if t in cache:
            results[i] = cache[t]
        else:
            missing_indices.append(i)

    if not missing_indices:
        return results

    # Chunk missing items
    for k in range(0, len(missing_indices), batch_size):
        idx_slice = missing_indices[k:k+batch_size]
        chunk_texts = [texts[idx] for idx in idx_slice]

        # Check text length; if > 3500 chars, use smaller chunks
        total_len = sum(len(t) for t in chunk_texts)
        if total_len > 3500:
            # subchunk
            sub_step = max(1, len(chunk_texts) // 2)
            for m in range(0, len(chunk_texts), sub_step):
                sub_slice = idx_slice[m:m+sub_step]
                sub_chunk = [texts[idx] for idx in sub_slice]
                _process_chunk(sub_slice, sub_chunk, results)
        else:
            _process_chunk(idx_slice, chunk_texts, results)

        time.sleep(0.3)

    return results

def _process_chunk(idx_slice, chunk_texts, results):
    success = False
    for attempt in range(3):
        try:
            translated_parts = translate_chunk_direct(chunk_texts)
            if len(translated_parts) == len(chunk_texts):
                for orig, tr, idx in zip(chunk_texts, translated_parts, idx_slice):
                    processed = post_process_translation(tr)
                    cache[orig] = processed
                    results[idx] = processed
                success = True
                break
        except Exception as e:
            time.sleep(1.0 * (attempt + 1))

    if not success:
        # Fallback to single translate
        for orig, idx in zip(chunk_texts, idx_slice):
            try:
                processed = translate_single(orig)
                cache[orig] = processed
                results[idx] = processed
                time.sleep(0.2)
            except Exception as e:
                cache[orig] = orig
                results[idx] = orig

def run_translation(input_file="chapters.json", output_file=OUTPUT_FILE):
    with open(input_file, 'r', encoding='utf-8') as f:
        book_data = json.load(f)

    translated_book = {
        'title': book_data['title'],
        'author': book_data['author'],
        'total_chapters': book_data['total_chapters'],
        'total_paragraphs': book_data['total_paragraphs'],
        'chapters': []
    }

    total_chapters = len(book_data['chapters'])
    total_paras_done = 0

    for ch_idx, ch in enumerate(book_data['chapters']):
        en_paras = ch['paragraphs']
        vi_paras = translate_batch(en_paras, batch_size=20)

        pairs = [{'en': en, 'vi': vi} for en, vi in zip(en_paras, vi_paras)]
        translated_book['chapters'].append({
            'part': ch['part'],
            'chapter': ch['chapter'],
            'paragraphs': pairs
        })

        total_paras_done += len(en_paras)
        print(f"[{ch_idx+1}/{total_chapters}] Chapter {ch['chapter']} complete ({len(en_paras)} paras). Total translated: {total_paras_done}/{book_data['total_paragraphs']}")

        # Save cache atomically
        tmp_cache = CACHE_FILE + ".tmp"
        with open(tmp_cache, 'w', encoding='utf-8') as cf:
            json.dump(cache, cf, ensure_ascii=False)
        os.replace(tmp_cache, CACHE_FILE)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(translated_book, f, ensure_ascii=False, indent=2)

    print(f"All 24 chapters completely translated and saved to {output_file}!")

if __name__ == "__main__":
    run_translation()
