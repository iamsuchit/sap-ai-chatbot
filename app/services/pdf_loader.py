import os
from PyPDF2 import PdfReader

def load_all_pdfs(data_folder="data"):
    text = ""

    if not os.path.exists(data_folder):
        raise ValueError("❌ data folder not found")

    pdf_files = [f for f in os.listdir(data_folder) if f.endswith(".pdf")]

    if not pdf_files:
        raise ValueError("❌ No PDFs found")

    print(f"📂 Found {len(pdf_files)} PDF files")

    for pdf in pdf_files:
        path = os.path.join(data_folder, pdf)
        print(f"📄 Reading: {pdf}")

        try:
            reader = PdfReader(path)
            for page in reader.pages:
                t = page.extract_text()
                if t:
                    text += t
        except Exception as e:
            print(f"⚠️ Skipping {pdf}: {e}")

    if not text.strip():
        raise ValueError("❌ No readable content found")

    return text