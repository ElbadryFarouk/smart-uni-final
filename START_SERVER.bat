@echo off
chcp 65001 >nul
echo.
echo ========================================
echo   RAG Server Launcher - CORS Fixed
echo ========================================
echo.
cd /d "C:\Users\hp\Downloads\__pycache__"

echo [1/3] Stopping old servers...
taskkill /FI "IMAGENAME eq python.exe" /F >nul 2>&1
timeout /t 3 /nobreak >nul

echo [2/3] Starting server with CORS enabled...
echo.

REM Delete old DB to avoid dimension mismatch
rmdir /s /q chroma_db 2>nul

python -m uvicorn Elbadry:app --host 0.0.0.0 --port 8000 --app-dir "C:\Users\hp\Downloads\__pycache__"

echo.
echo Server stopped.
pause
