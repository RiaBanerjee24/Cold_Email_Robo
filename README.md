# Cold Email Bot

An automated cold email outreach tool that finds email addresses using Hunter.io, generates personalized emails using GPT-5 Nano, and saves them as drafts in your Gmail account.

## Overview

This application automates the process of:
1. Finding email addresses for contacts using Hunter.io API
2. Generating personalized cold emails using OpenAI's GPT-5 Nano
3. Saving emails as drafts in your Gmail account for manual review and sending

## Prerequisites

- Python 3.8 or higher
- A Hunter.io account and API key
- An OpenAI API key
- A Google account for Gmail OAuth
- A Gmail account

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ColdEmailBot
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the **root directory** (outside the `server` folder) with the following variables:

```env
HUNTER_API_KEY=your_hunter_io_api_key_here
GMAIL_PASSWORD=your_gmail_password_here
OPENAI_API_KEY=your_openai_api_key_here
```

**How to get your API keys:**
- **Hunter.io API Key**: Sign up at [Hunter.io](https://hunter.io), go to your dashboard, and copy your API key
- **OpenAI API Key**: Sign up at [OpenAI](https://platform.openai.com), go to API keys section, and create a new secret key

### 5. Email Template

Create your own `email_template.txt` file in the `server/` folder. This template will be used as the system message for GPT to generate personalized emails.

Example structure:
```
Hi [Recipient],
I'm [Your Name], a [Your Title] with [X] years of experience, and I saw [relevant opportunity] at your company [Company Name].

[Your background and skills]

I'd love to talk more about [opportunity]. Looking forward to hearing from you.

Thanks,
[Your Name]
```

### 6. Gmail OAuth Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Gmail API:
   - Navigate to "APIs & Services" > "Library"
   - Search for "Gmail API" and enable it
4. Create OAuth 2.0 credentials:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth client ID"
   - Choose "Desktop app" as the application type
   - Download the JSON file
5. Rename the downloaded JSON file to `credentials.json` and place it in the `server/` folder
6. Run the script once to generate `token.json`:
   ```bash
   cd server
   python3 run_me.py
   ```
   - This will open a browser window for OAuth authentication
   - Authorize the application
   - The `token.json` file will be automatically created in the `server/` folder

### 7. Create Your Contacts CSV File

Create a CSV file in the `server/` folder with the following structure:

```csv
name
John Doe
Jane Smith
Bob Johnson
```

**Important**: 
- The CSV file must have a `name` column
- Update the `CSV_FILE_PATH` in `run_me.py` to match your CSV filename
- Each row should contain the name of the person you want to reach out to
- Name your CSV file as `Contacts.csv`. Otherwise, modify the name in run_me.py.

### 8. Configure Your Outreach Details

Edit `server/run_me.py` to set your outreach parameters:

```python
company = "Your Target Company Name"
job_description = "Your job description or opportunity details"
domain = "companydomain.com"  # The domain to search for emails
```

Edit `server/run_agent.py` to set your subject line:
```python
     subject = f"Looking into [Your domain] opportunities at {company}"
```

## Usage

1. Make sure your virtual environment is activated
2. Ensure all setup steps are completed (`.env` file, `credentials.json`, `email_template.txt`, `Contacts.csv`)
3. Run the script:

```bash
cd server
python3 run_me.py
```

The script will:
- Read contacts from your CSV file
- Find their email addresses using Hunter.io
- Generate personalized emails using GPT-5 Nano
- Save each email as a draft in your Gmail account

## Reviewing and Sending Emails

1. Go to your Gmail account
2. Click on "Drafts" in the left sidebar
3. Review each generated email
4. Edit if needed
5. Send manually when ready

## Sending Emails Directly (Instead of Drafts)

If you want emails to be sent directly instead of saved as drafts, modify the `send_email.py` file:

1. Open `server/send_email.py`
2. Find the `save_email_as_draft` function
3. Change the draft creation code to use `send()` instead:

```python
# Change from:
draft = service.users().drafts().create(
    userId="me",
    body={
        "message": {
            "raw": encoded_message
        }
    }
).execute()

# To:
service.users().messages().send(
    userId="me",
    body={"raw": encoded_message}
).execute()
```

**Warning**: Be careful when sending emails directly. Always test with drafts first to ensure the email content is correct.

## Project Structure

```
ColdEmailBot/
├── .env                    # Environment variables (create this)
├── README.md              # This file
├── venv/                  # Virtual environment
└── server/
    ├── AppConfig.py       # Configuration loader
    ├── run_me.py          # Main script to run
    ├── run_agent.py       # Agent logic
    ├── draft_email.py     # Email generation using GPT
    ├── hunter_search.py   # Email finding using Hunter.io
    ├── send_email.py      # Gmail integration
    ├── email_template.txt # Your email template (create this)
    ├── credentials.json   # Gmail OAuth credentials (download from Google Console)
    ├── token.json         # Auto-generated after first OAuth
    └── People_csv - Sheet1.csv  # Your contacts CSV (create this)
```

## Troubleshooting

- **"Module not found" errors**: Make sure your virtual environment is activated and all dependencies are installed
- **"File not found" errors**: Ensure all files (`.env`, `credentials.json`, `email_template.txt`, CSV) are in the correct locations
- **OAuth errors**: Make sure you've enabled Gmail API in Google Cloud Console and downloaded the correct credentials file
- **API key errors**: Verify your API keys in the `.env` file are correct and have proper permissions

## Notes

- The application uses GPT-5 Nano for fast and cost-effective email generation
- Emails are saved as drafts by default for safety and review
- Make sure to comply with email marketing regulations (CAN-SPAM, GDPR, etc.)
- Always personalize and review generated emails before sending
- The company name, job secriptions and company domain are kept manual for now, for human autonomy. Feel free to edit the code on your local env.


