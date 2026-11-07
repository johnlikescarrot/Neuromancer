import json

with open('data/chapters.json') as f:
    chapters = json.load(f)

ch1_paras = [c for c in chapters if c.get('chapter') == '1'][0]['paragraphs']

# We define high quality translations for Chapter 1
# And pedagogical notes interspersed at key narrative beats
