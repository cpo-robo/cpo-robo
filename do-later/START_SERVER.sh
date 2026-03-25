#!/bin/bash

clear
echo "============================================"
echo "ARIA - Permit Intelligence System"
echo "============================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3 from https://www.python.org or via Homebrew:"
    echo "  brew install python3"
    read -p "Press Enter to exit..."
    exit 1
fi

# Check if API key is set
if [ -z "$OPENAI_API_KEY" ]; then
    echo "WARNING: OPENAI_API_KEY environment variable not set!"
    echo ""
    echo "Please run SET_API_KEY.sh first or set it manually:"
    echo "  export OPENAI_API_KEY=your-api-key-here"
    echo ""
    echo "Get your API key from: https://platform.openai.com/account/api-keys"
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

echo "Installing dependencies..."
python3 -m pip install -q -r requirements.txt

if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    read -p "Press Enter to exit..."
    exit 1
fi

echo ""
echo "============================================"
echo "Starting ARIA Server..."
echo "============================================"
echo ""
echo "Opening browser at http://127.0.0.1:5000"
echo "Press CTRL+C to stop the server"
echo ""

# Open the browser (Mac version)
sleep 2
open http://127.0.0.1:5000 2>/dev/null || echo "Please open http://127.0.0.1:5000 in your browser"

# Start Flask server
python3 app.py
