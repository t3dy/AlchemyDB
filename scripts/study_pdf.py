import fitz # PyMuPDF
from pathlib import Path

def extract_pdf_info(pdf_path, pages_to_read=10):
    doc = fitz.open(pdf_path)
    text = ""
    for i in range(min(pages_to_read, len(doc))):
        page = doc.load_page(i)
        text += f"\n--- Page {i+1} ---\n"
        text += page.get_text()
    return text

if __name__ == "__main__":
    pdf_path = r"c:\AlchemyDB\pdf\Laboratories of Art_ Alchemy and Art Technology from Antiquity to the 18th Century Springer 20.pdf"
    if Path(pdf_path).exists():
        print(extract_pdf_info(pdf_path))
    else:
        print(f"File not found: {pdf_path}")
