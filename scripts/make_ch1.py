import json

with open('data/chapters.json') as f:
    chapters = json.load(f)

ch1_paras = [c for c in chapters if c.get('chapter') == '1'][0]['paragraphs']

# Let's map all 221 paragraphs with their Vietnamese translations
# We'll generate content/ch01_bilingual.json with all 221 paragraphs translated faithfully and literary,
# plus academic vocabulary boxes and cyberpunk background notes.
