# CPO Robo - Future Improvements

## TODO: Switch to Flask Backend (For Production)

**Priority:** Medium
**When:** After proof of concept is approved
**Effort:** ~2 hours

### Why
Current setup calls OpenAI API directly from frontend, exposing API key. Flask backend would:
- Hide API key in environment variables
- Add server-side logging
- Enable rate limiting and usage controls
- Support database for conversation history
- Better error handling and monitoring

### What To Do
1. Move Flask files from `do-later/` back to root
2. Update `docs/index.html` to call Flask backend instead of OpenAI directly
3. Deploy Flask to Heroku, Render, or AWS (see `do-later/DEPLOYMENT_GUIDE.md`)
4. Update frontend API endpoint to production URL
5. Test end-to-end with production backend

### Current Serverless Setup
- Frontend: GitHub Pages at `/docs/index.html`
- API calls: Direct to OpenAI from JavaScript
- Security: API key set via prompt on first load
- Cost: Only OpenAI API costs, no hosting fees

### Files Reference
- Backend code: `do-later/app.py`
- Deployment guide: `do-later/DEPLOYMENT_GUIDE.md`
- Startup scripts: `do-later/SET_API_KEY.*` and `do-later/START_SERVER.*`
