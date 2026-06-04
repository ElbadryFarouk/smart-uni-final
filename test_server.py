import sys
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyD64xUsN_XnhPXBDU-ZWyf3c623AUrfWtI"
os.chdir(r'C:\Users\hp\Downloads\__pycache__')
sys.path.insert(0, r'C:\Users\hp\Downloads\__pycache__')

print("=== Testing imports ===")
try:
    from langchain_google_genai import GoogleGenerativeAIEmbeddings
    print("GoogleGenerativeAIEmbeddings OK")
except Exception as e:
    print(f"FAIL: {e}")

try:
    from pypdf import PdfReader
    print("pypdf OK")
except Exception as e:
    print(f"FAIL pypdf: {e}")

print("\n=== Testing PDF load ===")
f = r'C:\Users\hp\Downloads\مراجعة شاملة إستراتيجية.pdf'
reader = PdfReader(f)
print(f"Pages: {len(reader.pages)}")
for i, page in enumerate(reader.pages[:2]):
    text = page.extract_text()
    print(f"Page {i+1}: {len(text) if text else 0} chars")

print("\n=== Testing embeddings init ===")
try:
    emb = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    print("Embeddings initialized")
    vec = emb.embed_query("test")
    print(f"Embedding dim: {len(vec)}")
except Exception as e:
    print(f"FAIL: {e}")
    import traceback
    traceback.print_exc()
