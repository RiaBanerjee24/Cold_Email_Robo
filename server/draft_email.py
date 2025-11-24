from openai import OpenAI
import os

client = OpenAI()

def load_template(template_path):
    """Load email template from a .txt file"""
    with open(template_path, "r") as f:
        return f.read()


# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(SCRIPT_DIR, "email_template.txt")

SYSTEM_MESSAGE = load_template(TEMPLATE_PATH)

conversation = [
    {"role": "system", "content": SYSTEM_MESSAGE}
]

def draft_email_nano(name, company, job_description=None, skills_summary=None):
    """
    Draft a new email using the same system message across multiple calls.
    
    Arguments:
    - name: recipient's first name
    - company: recipient's company
    - job_description: text of the job description
    - skills_summary: optional string of your skills to include
    """
    # Compose user prompt
    user_prompt = f"Draft a concise, warm outreach email to {name} at {company}, "
    if job_description:
        user_prompt += f"tailored to this job description:\n{job_description}"

    if skills_summary:
        user_prompt += f"\nInclude these skills: {skills_summary}"

    user_prompt += f"\nKeep it under 150 words, professional and friendly. Do not include a Subject line. Also make my email sound human."

    # Append user message to conversation
    conversation.append({"role": "user", "content": user_prompt})

    # Call GPT with the current conversation
    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=conversation
    )

    # Get GPT response
    draft = response.choices[0].message.content

    # Append GPT response to conversation for continuity
    conversation.append({"role": "assistant", "content": draft})

    return draft