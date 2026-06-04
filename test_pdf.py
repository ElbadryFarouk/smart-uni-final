import sys
sys.path.insert(0, r'C:\Users\hp\Downloads\__pycache__')
import glob
from pypdf import PdfReader

files = glob.glob(r'C:\Users\hp\Downloads\*.pdf')
print(f'PDF files found: {len(files)}')
if files:
    f = files[0]
    print(f'Testing: {f}')
    try:
        reader = PdfReader(f)
        print(f'Pages: {len(reader.pages)}')
        for i, page in enumerate(reader.pages[:3]):
            text = page.extract_text()
            print(f'Page {i+1} text length: {len(text) if text else 0}')
    except Exception as e:
        print(f'ERROR: {e}')
