# run_main.py
from run_agent import run_agent_simple
import csv
import os

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE_PATH = os.path.join(SCRIPT_DIR, "Contacts.csv")

company = "Company_Name"
job_description = "We are hiring a software engineer to build scalable backend services."
domain = "company_name.com"

with open(CSV_FILE_PATH, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        person_name = row['name']
        response = run_agent_simple(company, person_name, job_description, domain)
        print(response)
