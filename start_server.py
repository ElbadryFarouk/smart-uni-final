#!/usr/bin/env python
import os
import sys

os.environ["GOOGLE_API_KEY"] = "AIzaSyD64xUsN_XnhPXBDU-ZWyf3c623AUrfWtI"
os.chdir(r'C:\Users\hp\Downloads\__pycache__')

print("Starting server...")

import uvicorn
try:
    uvicorn.run("Elbadry:app", host="0.0.0.0", port=8001, log_level="info")
except Exception as e:
    print(f"SERVER ERROR: {e}")
    import traceback
    traceback.print_exc()
