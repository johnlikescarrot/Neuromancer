import urllib.request
import urllib.parse
import json
import time
import os

def translate_api(text):
    if not text.strip():
        return ""
    url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=vi&dt=t&q=' + urllib.parse.quote(text)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                return ''.join([part[0] for part in data[0] if part and part[0]])
        except Exception as e:
            time.sleep(1)
    return text

print("translate_core ready")
