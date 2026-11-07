import json
import re

def main():
    with open('data/chapters.json', 'r', encoding='utf-8') as f:
        chapters = json.load(f)

    # Let's inspect chapter 1 & chapter 2
    ch1 = [c for c in chapters if c.get('chapter') == '1'][0]
    ch2 = [c for c in chapters if c.get('chapter') == '2'][0]

    print(f"Chapter 1 has {len(ch1['paragraphs'])} paragraphs.")
    print(f"Chapter 2 has {len(ch2['paragraphs'])} paragraphs.")

if __name__ == '__main__':
    main()
