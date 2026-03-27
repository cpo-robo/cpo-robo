# HTML Integration Code for Google Sheets Logger

## Copy this code into your `docs/index.html` in the `<script>` section

---

## ADD THIS AT THE TOP OF YOUR SCRIPT SECTION (after existing variables):

```javascript
// ===== GOOGLE SHEETS LOGGER =====
const GOOGLE_APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwgxtUy9QY_uC94z9oUlipVmwUQ1OuxjYRP7m25XnDGI3OkW-YwxR8agtDNYWxPa1H6/exec";

function logQuestionToSheets(question, isStandard = false) {
  fetch(GOOGLE_APPS_SCRIPT_URL, {
    method: "POST",
    body: JSON.stringify({ question: question, isStandard: isStandard })
  })
  .then(r => r.json())
  .then(result => {
    if (result.success) {
      console.log("✓ Logged to Google Sheets:", question);
    }
  })
  .catch(e => console.error("Sheet logging error:", e));
}
// ===== END GOOGLE SHEETS LOGGER =====
```

---

## MODIFY EXISTING useSuggestion() FUNCTION:

Find this function in your code:
```javascript
function useSuggestion(text) {
  inputField.value = text;
  inputField.style.height = 'auto';
  inputField.style.height = Math.min(inputField.scrollHeight, 120) + 'px';
  inputField.focus();
  // Auto-send after a short delay
  setTimeout(() => {
```

Add this line after `inputField.focus();`:
```javascript
  logQuestionToSheets(text, true); // Log standard question to Google Sheets
```

Full modified function should look like:
```javascript
function useSuggestion(text) {
  inputField.value = text;
  inputField.style.height = 'auto';
  inputField.style.height = Math.min(inputField.scrollHeight, 120) + 'px';
  inputField.focus();
  logQuestionToSheets(text, true); // Log standard question to Google Sheets
  // Auto-send after a short delay
  setTimeout(() => {
    const sendButton = document.querySelector('.send-button');
    if (sendButton) sendButton.click();
  }, 100);
}
```

---

## MODIFY THE CHAT FETCH REQUEST:

Find where you send messages to the API:
```javascript
const response = await fetch(`${BACKEND_URL}/api/chat`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ message: user_message })
});
```

Add this line RIGHT BEFORE the fetch:
```javascript
logQuestionToSheets(user_message, false); // Log custom question to Google Sheets
```

Full modified section should look like:
```javascript
const user_message = data.get('message', '').strip();

if (!user_message) {
  return jsonify({'error': 'Empty message'}), 400

logQuestionToSheets(user_message, false); // Log custom question to Google Sheets

const response = await fetch(`${BACKEND_URL}/api/chat`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ message: user_message })
});
```

---

## THAT'S IT!

Now when users:
- **Click a suggestion button** → Logged to "Standard" sheet
- **Type a custom message** → Logged to "Custom" sheet

Both with auto-timestamps!

Check your Google Sheet to see questions appearing:
https://docs.google.com/spreadsheets/d/1ifmw3iDe3Usj7OeDQojnsgQaNw7PDMkThXGeTJhkCAsRdaOLWDU992VU/

---

## VERIFY IT WORKS:

1. Go to your chatbot
2. Click "Required Documents" button
3. Go to your Google Sheet
4. Should see "Required Documents" in Standard tab with timestamp
5. Done! ✅
