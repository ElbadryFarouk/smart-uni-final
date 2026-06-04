@echo off
chcp 65001 >nul
setlocal
cd /d "C:\Users\hp\Downloads\__pycache__"

echo Shutting down old uvicorn/python instances...
for /f "skip=1 tokens=1,2 delims=," %%a in ('wmic process where "name='python.exe'" get ProcessId,CommandLine /format:csv ^| findstr /I "uvicorn"') do (
    echo Killing PID %%a
    taskkill /PID %%a /F >nul 2>&1
)

echo.
echo Starting RAG Server...
echo After it says "Uvicorn running on http://0.0.0.0:8000"
echo Open this URL in your browser: http://localhost:8000/docs
echo To STOP the server: press Ctrl+C here, or close this window.
echo.

python -m uvicorn Elbadry:app --host 0.0.0.0 --port 8000

echo.
echo Server stopped.
pause
