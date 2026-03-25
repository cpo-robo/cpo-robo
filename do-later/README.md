# Flask Backend (For Future Deployment)

This folder contains the Flask backend for CPO Robo. Currently, the bot runs serverless using direct OpenAI API calls from the frontend.

## When to Use This

Switch to Flask backend for production when you need:
- Better security (API key hidden on server)
- Server-side logging and monitoring
- Database integration for conversation history
- Rate limiting and usage controls
- Multiple cities/configurations

## Files

- `app.py` - Flask server with OpenAI integration
- `requirements.txt` - Python dependencies (Flask, OpenAI, CORS)
- `SET_API_KEY.bat` / `SET_API_KEY.sh` - Scripts to set API key
- `START_SERVER.bat` / `START_SERVER.sh` - Scripts to start server
- `DEPLOYMENT_GUIDE.md` - Complete deployment instructions for Heroku, Render, AWS, etc.

## Quick Start (Future)

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set your API key:
   ```bash
   # Windows
   SET_API_KEY.bat

   # Mac/Linux
   bash SET_API_KEY.sh
   ```

3. Start server:
   ```bash
   # Windows
   START_SERVER.bat

   # Mac/Linux
   bash START_SERVER.sh
   ```

4. Update frontend to call `http://127.0.0.1:5000/api/chat`

## See Also

- **DEPLOYMENT_GUIDE.md** - Detailed deployment instructions for production platforms
- Parent directory README.md - Current serverless setup
