import gspread
from oauth2client.service_account import ServiceAccountCredentials
from form_app.models import FormResponse
from django.utils.timezone import now

def run():
    # Google Sheets setup
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("form_app\credentials.json", scope)
    client = gspread.authorize(creds)

    # Open your spreadsheet by ID
    sheet = client.open_by_key("1ih8MbDmMaJ8aWm_BkvYa66wNpGLLMoXEvRFKkwcOCVo").sheet1
    records = sheet.get_all_records()

    for row in records:
        FormResponse.objects.get_or_create(
            full_name=row.get("Full Name"),
            email_address=row.get("Email"),
            submitted_at=now()
        )
