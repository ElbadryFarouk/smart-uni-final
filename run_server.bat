@echo off
chcp 65001 >nul
setlocal
cd /d "C:\Users\hp\Downloads\__pycache__"
echo Killing old uvicorn servers...
for /f "tokens=2" %%p in ('netstat -ano ^| findstr ":8000.*LISTENING"') do taskkill /PID %%p /F >nul 2>&1
timeout /t 2 /nobreak >nul
echo.
echo Starting RAG Server...
echo.
python -m uvicorn Elbadry:app --host 0.0.0.0 --port 8000 --app-dir "C:\Users\hp\Downloads\__pycache__"
echo.
echo Server stopped.
pause
