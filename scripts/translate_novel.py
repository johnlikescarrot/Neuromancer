import json, urllib.request, urllib.parse, time, os, re

CACHE_FILE = "data/translation_cache.json"

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False)

def translate_item(text):
    enc = urllib.parse.quote(text)
    url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=en&tl=vi&q={enc}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as r:
        data = json.loads(r.read().decode("utf-8"))
        if isinstance(data, list) and len(data) > 0:
            return data[0]
    return text

def main():
    with open("data/neuromancer_structured.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    cache = load_cache()
    untranslated = []
    for c in data["chapters"]:
        for p in c["paragraphs"]:
            en = p["english"]
            t = cache.get(en, "")
            if not t or (t == en and len(en) > 30):
                untranslated.append(en)
    untranslated = list(dict.fromkeys(untranslated))
    print("Total untranslated:", len(untranslated))
    for i, t in enumerate(untranslated):
        try:
            cache[t] = translate_item(t)
        except Exception as e:
            print(f"Err {i}: {e}")
        if (i + 1) % 50 == 0 or i == len(untranslated) - 1:
            save_cache(cache)
            print(f"Processed {i+1}/{len(untranslated)}")
        time.sleep(0.08)
    save_cache(cache)
    for c in data["chapters"]:
        for p in c["paragraphs"]:
            en = p["english"]
            p["vietnamese"] = cache.get(en, en)
    with open("data/neuromancer_bilingual.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Done updating data/neuromancer_bilingual.json")

if __name__ == "__main__":
    main()