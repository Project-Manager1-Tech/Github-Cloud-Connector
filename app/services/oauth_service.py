import requests
from app.config import GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET, GITHUB_REDIRECT_URI

def exchange_code_for_token(code: str):
    url = "https://github.com/login/oauth/access_token"

    payload = {
        "client_id": GITHUB_CLIENT_ID,
        "client_secret": GITHUB_CLIENT_SECRET,
        "code": code,
        "redirect_uri": GITHUB_REDIRECT_URI
    }

    headers = {"Accept": "application/json"}

    res = requests.post(url, data=payload, headers=headers)

    if res.status_code != 200:
        raise Exception(res.json())

    return res.json()