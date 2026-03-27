// CPO ROBO - Google Apps Script
// Copy and paste this entire code into your Google Sheet's Apps Script editor
// (Extensions → Apps Script in your Google Sheet)

const SPREADSHEET_ID = "YOUR_SPREADSHEET_ID_HERE"; // Replace with your Sheet ID
const CUSTOM_SHEET_NAME = "Custom";
const STANDARD_SHEET_NAME = "Standard";

function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const { question, isStandard } = data;

    if (!question) {
      return ContentService.createTextOutput(
        JSON.stringify({ success: false, error: "No question" })
      ).setMimeType(ContentService.MimeType.JSON);
    }

    if (isStandard) {
      logToStandardSheet(question);
    } else {
      logToCustomSheet(question);
    }

    return ContentService.createTextOutput(
      JSON.stringify({ success: true, message: "Logged" })
    ).setMimeType(ContentService.MimeType.JSON);
  } catch (error) {
    return ContentService.createTextOutput(
      JSON.stringify({ success: false, error: error.toString() })
    ).setMimeType(ContentService.MimeType.JSON);
  }
}

function logToStandardSheet(question) {
  const ss = SpreadsheetApp.openById(SPREADSHEET_ID);
  let sheet = ss.getSheetByName(STANDARD_SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(STANDARD_SHEET_NAME);
    initializeSheet(sheet);
  }
  const nextRow = sheet.getLastRow() + 1;
  sheet.getRange(nextRow, 1).setValue(question);
  sheet.getRange(nextRow, 2).setValue(new Date());
}

function logToCustomSheet(question) {
  const ss = SpreadsheetApp.openById(SPREADSHEET_ID);
  let sheet = ss.getSheetByName(CUSTOM_SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(CUSTOM_SHEET_NAME);
    initializeSheet(sheet);
  }
  const nextRow = sheet.getLastRow() + 1;
  sheet.getRange(nextRow, 1).setValue(question);
  sheet.getRange(nextRow, 2).setValue(new Date());
}

function initializeSheet(sheet) {
  sheet.getRange(1, 1).setValue("User Question");
  sheet.getRange(1, 2).setValue("Date");
  const headerRange = sheet.getRange(1, 1, 1, 2);
  headerRange.setFontWeight("bold");
  headerRange.setBackground("#00d9ff");
  headerRange.setFontColor("#0a0e27");
  sheet.autoResizeColumns(1, 2);
}

function setup() {
  const ss = SpreadsheetApp.openById(SPREADSHEET_ID);
  let standardSheet = ss.getSheetByName(STANDARD_SHEET_NAME);
  if (!standardSheet) {
    standardSheet = ss.insertSheet(STANDARD_SHEET_NAME);
    initializeSheet(standardSheet);
  }
  let customSheet = ss.getSheetByName(CUSTOM_SHEET_NAME);
  if (!customSheet) {
    customSheet = ss.insertSheet(CUSTOM_SHEET_NAME);
    initializeSheet(customSheet);
  }
}

function doGet() {
  return HtmlService.createHtmlOutput("CPO Robo Apps Script running!");
}
