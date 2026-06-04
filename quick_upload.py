import glob
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

files = sorted(glob.glob(r"C:\Users\hp\Downloads\*.pdf"))
print(f"Found PDFs: {len(files)}")
f = files[0]
print(f"Uploading: {f}")
try:
    with open(f, "rb") as fp:
        r = requests.post("http://127.0.0.1:8000/upload", files={"file": ("upload.pdf", fp, "application/pdf")}, timeout=200)
    print("Status:", r.status_code)
    print("Body:", r.text)
except Exception as e:
    print("ERROR:", e)
