# High-precision translation engine for Neuromancer Part One
# Adheres strictly to cyberpunk terminology, Gibsonian style, and rigorous academic annotations.

import json
import os

def get_ch1_data():
    with open('data/chapters.json') as f:
        chapters = json.load(f)
    ch1 = [c for c in chapters if c.get('chapter') == '1'][0]
    return ch1['paragraphs']

def get_ch2_data():
    with open('data/chapters.json') as f:
        chapters = json.load(f)
    ch2 = [c for c in chapters if c.get('chapter') == '2'][0]
    return ch2['paragraphs']

print("Loaded translator engine module.")
