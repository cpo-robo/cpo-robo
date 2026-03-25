@echo off
cls
echo ============================================
echo ARIA - Permit Intelligence System
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

REM Check if API key is set
if "%OPENAI_API_KEY%"=="" (
    echo WARNING: OPENAI_API_KEY environment variable not set!
    echo.
    echo Please run SET_API_KEY.bat first or set it manually:
    echo   set OPENAI_API_KEY=your-api-key-here
    echo.
    echo Get your API key from: https://platform.openai.com/account/api-keys
    echo.
    pause
)

echo Installing dependencies...
python -m pip install -q -r requirements.txt

if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ============================================
echo Starting ARIA Server...
echo ============================================
echo.
echo Opening browser at http://127.0.0.1:5000
echo Press CTRL+C to stop the server
echo.

REM Open the browser
timeout /t 2 /nobreak
start http://127.0.0.1:5000

REM Start Flask server
python app.py
