# CPO Robo - Deployment Guide

This guide covers deploying CPO Robo with the frontend on GitHub Pages and the backend on a production server.

## 📁 Repository Structure for Deployment

```
cpo-robo/
├── docs/                              # Frontend (GitHub Pages) - Keep here!
│   └── index.html                     # Served at: https://username.github.io/cpo-robo
├── app.py                             # Backend (Deploy separately)
├── requirements.txt                   # Backend dependencies
├── Syracuse_Permit_Guide_RAG.json     # Backend data
├── Syracuse_Permit_Guide_AI_Optimized.md
├── README.md                          # Main documentation
├── DEPLOYMENT_GUIDE.md                # This file
├── .gitignore                         # Git ignore rules
├── SET_API_KEY.bat / .sh              # Local development only
└── START_SERVER.bat / .sh             # Local development only
```

## 🚀 Step 1: Prepare GitHub Repository

### Create the repo:
1. Go to https://github.com/new
2. Name it: `cpo-robo`
3. Add description: "Centralized Permitting Bot for Syracuse"
4. Choose "Public" (for GitHub Pages)
5. Click "Create repository"

### Push your code:
```bash
git init
git add .
git commit -m "Initial commit: CPO Robo chatbot"
git branch -M main
git remote add origin https://github.com/yourusername/cpo-robo.git
git push -u origin main
```

## 📄 Step 2: Configure GitHub Pages

1. Go to your repository: https://github.com/yourusername/cpo-robo
2. Settings → Pages
3. Under "Source":
   - Branch: `main`
   - Folder: `/ (root)`
4. Click "Save"
5. Wait 1-2 minutes for deployment
6. Your site will be available at: **https://yourusername.github.io/cpo-robo/**

## 🔧 Step 3: Deploy Backend

Choose one of these platforms:

### Option A: Heroku (Easiest for beginners)

1. Sign up at https://www.heroku.com/
2. Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
3. Create Procfile in repo root:
   ```
   web: gunicorn app:app
   ```
4. Add gunicorn to requirements.txt:
   ```bash
   echo "gunicorn==21.2.0" >> requirements.txt
   ```
5. Deploy:
   ```bash
   heroku login
   heroku create your-app-name
   heroku config:set OPENAI_API_KEY=sk-...your-key...
   git push heroku main
   ```
6. Your backend will be at: **https://your-app-name.herokuapp.com**

### Option B: Render (Easiest, free tier available)

1. Sign up at https://render.com
2. Create new "Web Service"
3. Connect your GitHub repository
4. Settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment Variables**: Add `OPENAI_API_KEY=sk-...your-key...`
5. Deploy
6. Your backend will be at: **https://your-app-name.onrender.com**

### Option C: AWS (More complex, but scalable)

1. Sign up for AWS and use Lambda + API Gateway
2. Use AWS Chalice framework: https://aws.github.io/chalice/
3. Or use Elastic Beanstalk for traditional Flask deployment

### Option D: PythonAnywhere (Python-specific hosting)

1. Sign up at https://www.pythonanywhere.com
2. Upload your files
3. Configure WSGI file
4. Add `OPENAI_API_KEY` to environment variables
5. Your backend will be at: **https://yourusername.pythonanywhere.com**

## 🔗 Step 4: Connect Frontend to Backend

After deploying backend, update `docs/index.html` with your API endpoint:

**Find this in `docs/index.html` (around line 410):**
```javascript
const API_ENDPOINT = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
    ? 'http://127.0.0.1:5000/api/chat'
    : '/api/chat';
```

**Replace with your backend URL:**
```javascript
const API_ENDPOINT = 'https://your-backend-domain.com/api/chat';
// Examples:
// const API_ENDPOINT = 'https://cpo-robo.herokuapp.com/api/chat';
// const API_ENDPOINT = 'https://cpo-robo.onrender.com/api/chat';
// const API_ENDPOINT = 'https://yourusername.pythonanywhere.com/api/chat';
```

Then push to GitHub:
```bash
git add docs/index.html
git commit -m "Update API endpoint to production backend"
git push origin main
```

## ✅ Step 5: Test Everything

1. **Test Frontend**: Open https://yourusername.github.io/cpo-robo/
2. **Test Backend Health**: Open https://your-backend-domain.com/health
   - Should see: `{"status":"online","api_configured":true,"permit_guide_loaded":true}`
3. **Test Chat**: Type a message in the UI, should get a response

## 🔒 Security Checklist

- [ ] API key is set as environment variable (NOT in code)
- [ ] `.gitignore` includes `SET_API_KEY.bat`, `SET_API_KEY.sh`, and `.env`
- [ ] No API keys in commit history: `git log -p | grep -i "sk-"` (should return nothing)
- [ ] Backend only accepts POST requests from specific origins (optional CORS)
- [ ] API key has spending limits set on OpenAI account

## 🔐 Managing API Keys Securely

### Never do this:
```python
API_KEY = "sk-..."  # ❌ Hardcoded in code
```

### Always do this:
```python
import os
API_KEY = os.getenv('OPENAI_API_KEY')  # ✓ From environment
```

### Setting environment variables on each platform:

**Heroku:**
```bash
heroku config:set OPENAI_API_KEY=sk-...your-key...
```

**Render:**
- Dashboard → Environment → Add `OPENAI_API_KEY`

**AWS Lambda:**
- Lambda function → Configuration → Environment variables

**PythonAnywhere:**
- Web app → WSGI configuration → Add to environment

**Digital Ocean/VPS:**
- SSH into server
- Edit `/etc/environment` or `.env` file
- Restart application

## 📊 Monitoring

### Check backend is running:
```bash
curl https://your-backend-domain.com/health
```

### View backend logs:
- **Heroku**: `heroku logs --tail`
- **Render**: Dashboard → Logs
- **AWS**: CloudWatch Logs
- **PythonAnywhere**: Web → Error log

### Monitor API usage:
- Visit https://platform.openai.com/account/usage
- Set spending limits at: https://platform.openai.com/account/billing/limits

## 🆘 Troubleshooting

### Frontend not loading
- Check GitHub Pages settings
- Verify `docs/index.html` exists
- Check browser console (F12) for errors

### API returns 404
- Verify backend URL in `docs/index.html`
- Check backend is running: `curl https://your-api.com/health`
- Check CORS settings in `app.py`

### "API key not configured" error
- Verify environment variable is set on server
- Check value: Some platforms show "undefined" if not set correctly
- Restart application after setting variable

### Port conflicts
- If running multiple Flask apps, use different ports in `app.py`

## 🚀 Next Steps

1. Test everything locally with `START_SERVER.bat`
2. Push code to GitHub
3. Deploy backend to your chosen platform
4. Update `docs/index.html` with backend URL
5. Share your bot! 🎉

## 📞 Getting Help

- **OpenAI Issues**: https://platform.openai.com/docs/troubleshooting
- **Flask Help**: https://flask.palletsprojects.com
- **GitHub Pages**: https://docs.github.com/en/pages
- **Heroku**: https://devcenter.heroku.com
- **Render**: https://render.com/docs
