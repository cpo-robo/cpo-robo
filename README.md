# CPO Robo - Centralized Permitting Bot

A modern, sci-fi themed chatbot for answering questions about Syracuse residential permits. Separates frontend (GitHub Pages) from backend (Flask API).

## 🎯 Features

- **Modern Web Interface** - Dark themed, responsive design with animated gradients
- **AI-Powered** - Uses OpenAI's GPT-4o-mini for fast, cost-effective responses
- **Permit Knowledge** - Trained on Syracuse residential permit guidelines
- **Easy Deployment** - Frontend on GitHub Pages, backend on any server
- **RESTful API** - Simple `/api/chat` endpoint for extensibility

## 📁 Repository Structure

```
cpo-robo/
├── docs/                              # GitHub Pages frontend (deployed at root)
│   └── index.html                     # Web interface (HTML/CSS/JS)
├── app.py                             # Flask backend
├── requirements.txt                   # Python dependencies
├── SET_API_KEY.bat                    # Windows: Set API key
├── SET_API_KEY.sh                     # Mac/Linux: Set API key
├── START_SERVER.bat                   # Windows: Start backend server
├── START_SERVER.sh                    # Mac/Linux: Start backend server
├── Syracuse_Permit_Guide_RAG.json     # Permit data (JSON)
├── Syracuse_Permit_Guide_AI_Optimized.md  # Permit data (Markdown)
└── README.md                          # This file
```

## 🚀 Quick Start

### Option 1: Run Locally (For Development/Testing)

#### Windows
1. Get an OpenAI API key: https://platform.openai.com/account/api-keys
2. Run `SET_API_KEY.bat` and paste your API key
3. Run `START_SERVER.bat`
4. Open http://127.0.0.1:5000

#### Mac/Linux
1. Get an OpenAI API key: https://platform.openai.com/account/api-keys
2. Run `bash SET_API_KEY.sh` and paste your API key
3. Run `bash START_SERVER.sh`
4. Open http://127.0.0.1:5000

### Option 2: Deploy to Production

#### Frontend (GitHub Pages)
- Frontend files are in `/docs` folder
- GitHub Pages is automatically enabled (Settings → Pages → Source: `root`)
- Access at: `https://yourusername.github.io/cpo-robo`

#### Backend (Any Server)
Deploy `app.py` to your preferred platform:
- **Heroku**: `git push heroku main`
- **AWS Lambda**: Use serverless framework
- **Digital Ocean**: Simple Python app hosting
- **Render**: `git push` to deploy
- **PythonAnywhere**: Drag-and-drop upload

Configure your frontend API endpoint in `docs/index.html`:
```javascript
const API_ENDPOINT = 'https://your-backend-api.com/api/chat';
```

## 💻 System Requirements

### Local Development
- Python 3.8+
- OpenAI API key (free account, but API usage is paid)
- Modern web browser

### Backend Server
- Python 3.8+
- Flask and dependencies (see `requirements.txt`)
- Environment variable: `OPENAI_API_KEY`

### Frontend
- Just a web browser! (No server needed for GitHub Pages)

## 🔧 Configuration

### Change the System Prompt
Edit `app.py` line 51-56 to customize bot behavior:
```python
system_prompt = """You are CPO Robo, a Centralized Permitting Bot...
# Add your custom instructions here
"""
```

### Change the Model
Edit `app.py` line 63 to use a different OpenAI model:
```python
model="gpt-4o-mini"  # Change to: gpt-4-turbo, gpt-4o, etc.
```

### Change the Theme Color
Edit `docs/index.html` CSS variables (lines 16-26):
```css
--accent-cyan: #00d9ff;    /* Main neon color */
--accent-blue: #0066ff;    /* Secondary color */
--bg-primary: #0a0e27;     /* Background */
```

### Configure API Endpoint
Edit `docs/index.html` JavaScript (lines 410-415):
```javascript
// Automatically detects localhost vs production
const API_ENDPOINT = window.location.hostname === 'localhost'
    ? 'http://127.0.0.1:5000/api/chat'
    : 'https://your-api-domain.com/api/chat';
```

## 📚 API Documentation

### POST /api/chat
Send a message to the bot and get a response.

**Request:**
```json
{
    "message": "What documents do I need for a permit?"
}
```

**Response:**
```json
{
    "response": "To apply for a residential permit, you'll need...",
    "usage": {
        "input_tokens": 1024,
        "output_tokens": 512
    }
}
```

### GET /health
Check if the backend is running and configured.

**Response:**
```json
{
    "status": "online",
    "api_configured": true,
    "permit_guide_loaded": true
}
```

## 💰 Cost Estimate

Using OpenAI's gpt-4o-mini:
- **Per conversation**: ~$0.001-0.005
- **Monthly budget**: $10 = ~2,000-5,000 conversations
- **Pro tip**: Set usage limits in OpenAI account settings

## 🐛 Troubleshooting

### "OPENAI_API_KEY not set"
- Make sure you ran `SET_API_KEY.bat` (Windows) or `SET_API_KEY.sh` (Mac)
- Check environment variable: `echo $OPENAI_API_KEY` (Mac/Linux) or `echo %OPENAI_API_KEY%` (Windows)
- Close and reopen terminal after setting the key

### "Cannot connect to API"
- Check backend is running: `curl http://127.0.0.1:5000/health`
- Verify API key is valid at https://platform.openai.com/account/api-keys
- Check internet connection

### "Port 5000 already in use"
- Change port in `app.py` line 110: `app.run(port=8000, ...)`
- Or kill the process using the port: `lsof -i :5000` (Mac/Linux)

### "Templates folder not found"
- Make sure `templates/index.html` exists (for local backend)
- Or use GitHub Pages frontend with remote backend

## 📦 Dependencies

**Backend (Python):**
- Flask 2.3.3
- Flask-CORS 4.0.0
- openai 1.3.0
- Werkzeug 2.3.7

Install with: `pip install -r requirements.txt`

**Frontend:**
- Pure HTML/CSS/JavaScript (no dependencies)

## 🔒 Security Notes

- API key is stored only in environment variables
- Messages are sent to OpenAI servers (review their privacy policy)
- No user data is stored on the server
- Don't commit `.bat` or `.sh` files with API keys to public repos
- Use environment variables in production

## 📝 Customization Examples

### Use Different Permit Guide
1. Replace `Syracuse_Permit_Guide_RAG.json` with your city's data
2. Update `app.py` line 20 to load your file
3. Rebuild system prompt in `app.py` with your content

### Add User Authentication
1. Add login/logout to `docs/index.html`
2. Store tokens in `localStorage`
3. Include auth token in `/api/chat` requests

### Store Conversation History
1. Add database to backend (PostgreSQL, MongoDB, etc.)
2. Save each conversation in `app.py` `/api/chat` endpoint
3. Add conversation history UI in frontend

## 🚀 Deployment Checklist

- [ ] Get OpenAI API key
- [ ] Test locally with `START_SERVER.bat` or `START_SERVER.sh`
- [ ] Create GitHub repo and push code
- [ ] Enable GitHub Pages (Settings → Pages)
- [ ] Test frontend at `https://yourusername.github.io/cpo-robo`
- [ ] Deploy backend to production server
- [ ] Update API endpoint in `docs/index.html`
- [ ] Set `OPENAI_API_KEY` environment variable on production server
- [ ] Test end-to-end with production backend

## 📞 Support

- **API Errors**: Check OpenAI status page
- **Frontend Issues**: Inspect browser console (F12)
- **Backend Issues**: Check server logs
- **Questions**: Read `docs/index.html` comments for code documentation

## 📄 License

MIT License - Feel free to use and modify for your city/organization

## 🎓 Learning Resources

- [OpenAI API Docs](https://platform.openai.com/docs)
- [Flask Documentation](https://flask.palletsprojects.com)
- [GitHub Pages Guide](https://pages.github.com)
- [REST API Best Practices](https://restfulapi.net)

---

**Built with:** Flask • OpenAI • HTML5/CSS3/JavaScript • Love 🚀
