from hunter_search import hunter_search
from draft_email import draft_email_nano
from send_email import save_email_as_draft,get_gmail_creds

def run_agent_simple(company, person_name, job_description, domain):
    recipient_email = hunter_search(person_name, domain)
    
    if not recipient_email:
        print("Email not found!")
        return

    body = draft_email_nano(person_name, company, job_description)

    subject = f"Looking into Software Engineering opportunities at {company}"
    print(body)
    creds = get_gmail_creds()
    result = save_email_as_draft(recipient_email, subject, body, creds)
 
    return result