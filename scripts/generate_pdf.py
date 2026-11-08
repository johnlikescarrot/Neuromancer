import sys
import subprocess
from pathlib import Path

def compile_pdf():
    print("Compiling bilingual PDF via TypeScript engine (npm run build:pdf)...")
    subprocess.run(["npm", "run", "build:pdf"], check=True)
    pdf_out = Path("output/neuromancer_bilingual_edition.pdf")
    if pdf_out.exists():
        size_mb = pdf_out.stat().st_size / (1024 * 1024)
        print(f"PDF verified at {pdf_out} ({size_mb:.2f} MB)")
    else:
        print("Error: output/neuromancer_bilingual_edition.pdf was not generated.")
        sys.exit(1)

if __name__ == "__main__":
    compile_pdf()
