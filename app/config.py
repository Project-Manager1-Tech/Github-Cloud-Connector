import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API_BASE = "https://api.github.com"

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
GITHUB_REDIRECT_URI = os.getenv("GITHUB_REDIRECT_URI")

if not GITHUB_CLIENT_ID or not GITHUB_CLIENT_SECRET or not GITHUB_REDIRECT_URI:
    raise ValueError("OAuth config missing in .env (CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)")

if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN is missing. Add it in .env file.")