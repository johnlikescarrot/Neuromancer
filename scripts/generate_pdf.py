import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

def compile_pdf():
    html_file = Path("data/novel_bilingual.html").resolve()
    pdf_out = Path("output/neuromancer_bilingual_edition.pdf").resolve()
    pdf_out.parent.mkdir(parents=True, exist_ok=True)

    print(f"Opening {html_file}...")
    start_time = time.time()

    with sync_playwright() as p:
        browser = p.chromium.launch(
            args=[
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage',
                '--disable-gpu'
            ]
        )
        page = browser.new_page()
        # Set large viewport
        page.set_viewport_size({"width": 1200, "height": 1600})

        # Navigate to file URL
        page.goto(f"file://{html_file}", wait_until="load")
        print("Page loaded, waiting for render stabilization...")
        page.wait_for_timeout(3000)

        print("Generating PDF (A4 format with page numbers)...")
        page.pdf(
            path=str(pdf_out),
            format="A4",
            print_background=True,
            margin={
                "top": "20mm",
                "bottom": "20mm",
                "left": "15mm",
                "right": "15mm"
            },
            display_header_footer=True,
            header_template='<div style="font-size: 8pt; width: 100%; text-align: right; color: #888; padding-right: 15mm; font-family: sans-serif;">Neuromancer (Bilingual C1/C2 Edition)</div>',
            footer_template='<div style="font-size: 8pt; width: 100%; text-align: center; color: #888; font-family: sans-serif;">Page <span class="pageNumber"></span> of <span class="totalPages"></span></div>'
        )
        browser.close()

    elapsed = time.time() - start_time
    file_size_mb = pdf_out.stat().st_size / (1024 * 1024)
    print(f"PDF generated successfully in {elapsed:.1f}s!")
    print(f"Output: {pdf_out} (Size: {file_size_mb:.2f} MB)")

if __name__ == "__main__":
    compile_pdf()
