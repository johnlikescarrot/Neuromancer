import json
import os
import re

print('=== STARTING COMPREHENSIVE VERIFICATION ===')

# 1. Structured
p_struct = 'data/neuromancer_structured.json'
assert os.path.exists(p_struct), 'Missing struct'
with open(p_struct, 'r', encoding='utf-8') as f:
    s_data = json.load(f)
assert len(s_data['chapters']) == 24
assert len(s_data['parts']) == 5
print('1. Structured JSON: 5 parts, 24 chapters.')

# 2. Bilingual
p_bi = 'data/neuromancer_bilingual.json'
assert os.path.exists(p_bi), 'Missing bi'
with open(p_bi, 'r', encoding='utf-8') as f:
    b_data = json.load(f)
assert len(b_data['chapters']) == 24

total_p = 0
total_en = 0
total_target = 0
for ch in b_data['chapters']:
    for para in ch['paragraphs']:
        total_p += 1
        e = para['english'].strip()
        v = para['vietnamese'].strip()
        assert len(e) > 0
        assert len(v) > 0
        total_en += len(e.split())
        total_target += len(v.split())

print(f'2. Bilingual text: {total_p} parallel paragraphs across all 24 chapters.')
print(f'   Total EN words: {total_en:,}')
print(f'   Total target words: {total_target:,}')

# 3. Academic Guide
p_guide = 'data/academic_guide.json'
assert os.path.exists(p_guide)
with open(p_guide, 'r', encoding='utf-8') as f:
    g_data = json.load(f)
for idx in range(1, 25):
    assert str(idx) in g_data
    assert len(g_data[str(idx)]) > 0
print('3. Academic guide: All 24 chapters have C1-C2 notes.')

# 4. PDF Deliverable
p_pdf = 'Neuromancer_Bilingual_EN_VI.pdf'
assert os.path.exists(p_pdf)
sz = os.path.getsize(p_pdf)
assert sz > 1000000
with open(p_pdf, 'rb') as f:
    content = f.read()
matches = re.findall(rb'/Count\s+(\d+)', content)
pgs = int(matches[0]) if matches else 0
assert pgs >= 250, f'Expected at least 250 pages, found {pgs}'
print(f'4. PDF deliverable: {p_pdf} ({sz:,} bytes, {pgs} pages).')
print('=== ALL VERIFICATION CHECKS PASSED SUCCESSFULLY ===')
