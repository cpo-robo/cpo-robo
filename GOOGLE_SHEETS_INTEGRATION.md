# CPO Robo - Google Sheets Integration Setup

## Files Included
- `google-sheets-logger.js` - Apps Script code (goes in Google Sheet)
- This setup guide

## Quick Setup (9 Steps)

### 1. Create Google Sheet
- Go to [Google Sheets](https://sheets.google.com)
- Create new sheet: "CPO Robo Questions"
- Copy the Spreadsheet ID from URL: `https://docs.google.com/spreadsheets/d/`**ID_HERE**/edit

### 2. Set Up Apps Script
- In Google Sheet: Extensions → Apps Script
- Delete default code
- Copy-paste ALL code from `google-sheets-logger.js`
- Replace line 5: `const SPREADSHEET_ID = "YOUR_ID_HERE";` with your Sheet ID

### 3. Deploy as Web App
- Click Deploy → New deployment
- Type: Web app
- Execute as: Your email
- Who has access: Anyone
- Click Deploy
- Copy the deployment URL (looks like: https://script.google.com/macros/d/DEPLOYMENT_ID/usercontent)

### 4. Initialize Sheets
- In Apps Script, click Run → setup
- Authorize when prompted
- Your "Standard" and "Custom" sheets are now created

### 5. Update Your Frontend
In `docs/index.html`, find the `<script>` section and add:

```javascript
// Google Sheets Logger
const GOOGLE_APPS_SCRIPT_URL = "https://script.google.com/macros/d/YOUR_DEPLOYMENT_ID/usercontent";

function logQuestionToSheets(question, isStandard = false) {
  fetch(GOOGLE_APPS_SCRIPT_URL, {
    method: "POST",
    body: JSON.stringify({ question: question, isStandard: isStandard })
  })
  .then(r => r.json())
  .then(result => console.log("Logged:", question))
  .catch(e => console.error("Error:", e));
}
```

### 6. Log Standard Questions
In the `useSuggestion()` function, add:
```javascript
logQuestionToSheets(text, true); // Logs to Standard sheet
```

### 7. Log Custom Questions
When user sends a message, add:
```javascript
logQuestionToSheets(message, false); // Logs to Custom sheet
```

### 8. Test It
- Send a message or click a suggestion button
- Check your Google Sheet - question should appear with timestamp

### 9. Done!
Two tabs automatically created:
- **Standard**: Predefined button questions
- **Custom**: User typed questions

Both auto-timestamp!

## What You Get
- ✅ Zero API costs (Google Sheets free tier)
- ✅ Auto-timestamped questions
- ✅ Two organized tabs
- ✅ Formatted headers
- ✅ Auto-sized columns

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Script not working | Check SPREADSHEET_ID matches your Sheet |
| No questions appearing | Check deployment URL is correct in HTML |
| Auth error | Make sure "Who has access" = "Anyone" |

## Questions?
Refer to the code comments in `google-sheets-logger.js`
