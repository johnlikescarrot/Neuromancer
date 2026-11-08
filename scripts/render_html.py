import sys
import subprocess
from pathlib import Path

def generate_html():
    print("Calling TypeScript Astryx HTML renderer via npm run render:html...")
    res = subprocess.run(["npm", "run", "render:html"], check=True)
    out_file = Path("data/novel_bilingual.html")
    if out_file.exists():
        size_mb = out_file.stat().st_size / (1024 * 1024)
        print(f"HTML generated successfully at {out_file} ({size_mb:.2f} MB)")
    else:
        print("Error: data/novel_bilingual.html was not generated.")
        sys.exit(1)

if __name__ == "__main__":
    generate_html()
