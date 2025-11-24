from googleapiclient.discovery import build
from email.message import EmailMessage
import base64

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os

SCOPES = ['https://www.googleapis.com/auth/gmail.send',
        "https://www.googleapis.com/auth/gmail.compose"]

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_PATH = os.path.join(SCRIPT_DIR, 'credentials.json')
TOKEN_PATH = os.path.join(SCRIPT_DIR, 'token.json')

def get_gmail_creds():
    creds = None
    # Check if token.json exists (stored after first auth)
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    
    # If no valid creds, run OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the token for next time
        with open(TOKEN_PATH, 'w') as token_file:
            token_file.write(creds.to_json())
    
    return creds



def save_email_as_draft(to_email, subject, body, creds):
    service = build("gmail", "v1", credentials=creds)

    msg = EmailMessage()
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    # Encode the message
    encoded_message = base64.urlsafe_b64encode(msg.as_bytes()).decode()

    # Create draft
    draft = service.users().drafts().create(
        userId="me",
        body={
            "message": {
                "raw": encoded_message
            }
        }
    ).execute()

    return {"status": "draft saved", "draftId": draft["id"]}

