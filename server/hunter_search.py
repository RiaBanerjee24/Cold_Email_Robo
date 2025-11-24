import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file (in parent directory)
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env'))

HUNTER_API_KEY = os.getenv("HUNTER_API_KEY")
HUNTER_URL = "https://api.hunter.io/v2/email-finder"

def hunter_search(full_name, domain):
    """
    Find email address using Hunter.io API
    
    Args:
        full_name: Full name of the person (e.g., "John Doe")
        domain: Domain name of the company (e.g., "example.com")
    
    Returns:
        Email address if found, None otherwise
    """
    first, last = full_name.split(" ", 1)
    params = {
        "domain": domain,
        "first_name": first,
        "last_name": last,
        "api_key": HUNTER_API_KEY
    }

    results = requests.get(HUNTER_URL, params=params)
    data = results.json()
    return data.get("data", {}).get("email")

