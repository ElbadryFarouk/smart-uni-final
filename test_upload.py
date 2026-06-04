import requests
import glob

url = "http://localhost:8001/upload"
files = glob.glob(r"C:\Users\hp\Downloads\*.pdf")
if not files:
    print("No PDF files found in Downloads")
else:
    f = files[0]
    print(f"Uploading: {f}")
    try:
        with open(f, 'rb') as fp:
            r = requests.post(url, files={"file": fp}, timeout=120)
            print(f"Status: {r.status_code}")
            print(f"Response: {r.text}")
    except Exception as e:
        print(f"Upload error: {e}")
