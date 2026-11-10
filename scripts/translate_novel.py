import json
import time
import urllib.request
import urllib.parse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

def translate_batch(batch):
    # Join paragraphs with a distinct delimiter that won't get lost
    delimiter = "\n<<<PARAGRAPH_SEP>>>\n"
    combined = delimiter.join(batch)

    url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=vi&dt=t&q=' + urllib.parse.quote(combined)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                res_text = ''.join([seg[0] for seg in data[0] if seg and seg[0]])
                parts = [p.strip() for p in res_text.split("<<<PARAGRAPH_SEP>>>")]
                if len(parts) == len(batch) and all(parts):
                    return parts
                # If separator split length doesn't match perfectly, fallback to individual translation
                break
        except Exception as e:
            time.sleep(1 + attempt)

    # Fallback individual translate
    results = []
    for text in batch:
        for attempt in range(5):
            try:
                single_url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=vi&dt=t&q=' + urllib.parse.quote(text)
                single_req = urllib.request.Request(single_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(single_req, timeout=10) as r:
                    d = json.loads(r.read().decode('utf-8'))
                    translated = ''.join([s[0] for s in d[0] if s and s[0]])
                    if not translated.strip():
                        raise ValueError("Empty translation")
                    results.append(translated.strip())
                    break
            except Exception:
                time.sleep(0.5 * (attempt + 1))
        else:
            raise RuntimeError("Translation failed after retries; no source text was saved as a translation")
    return results

def main():
    input_file = Path("data/extracted_novel.json")
    cache_file = Path("data/translated_cache.json")

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    cache = {}
    if cache_file.exists():
        with open(cache_file, "r", encoding="utf-8") as f:
            cache = json.load(f)

    # Collect all paragraphs that need translation
    to_translate = []
    for p_idx, part in enumerate(data["parts"]):
        for c_idx, chap in enumerate(part["chapters"]):
            for para_idx, para in enumerate(chap["paragraphs"]):
                key = f"{p_idx}_{c_idx}_{para_idx}"
                if key not in cache:
                    to_translate.append((key, para))

    print(f"Total paragraphs to translate: {len(to_translate)} (already cached: {len(cache)})")

    # Process in chunks of 5
    chunk_size = 5
    chunks = [to_translate[i:i + chunk_size] for i in range(0, len(to_translate), chunk_size)]

    def process_chunk(chunk):
        keys = [item[0] for item in chunk]
        texts = [item[1] for item in chunk]
        translations = translate_batch(texts)
        return list(zip(keys, translations))

    completed = 0
    # Use 10 workers for speed and stability
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(process_chunk, c): c for c in chunks}
        for future in as_completed(futures):
            res = future.result()
            for key, trans in res:
                cache[key] = trans
            completed += len(res)
            if completed % 100 == 0 or completed == len(to_translate):
                print(f"Progress: {completed} / {len(to_translate)} paragraphs translated...")
                # Periodic save
                with open(cache_file, "w", encoding="utf-8") as f:
                    json.dump(cache, f, ensure_ascii=False)

    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False)

    print(f"Translation complete! Total cached paragraphs: {len(cache)}")

if __name__ == "__main__":
    main()
