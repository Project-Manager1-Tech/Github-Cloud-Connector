import requests
from app.config import GITHUB_TOKEN, GITHUB_API_BASE

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def fetch_my_repos():
    url = f"{GITHUB_API_BASE}/user/repos"
    res = requests.get(url, headers=HEADERS)

    if res.status_code != 200:
        raise Exception(res.json())

    return res.json()

def fetch_repos(username: str):
    url = f"{GITHUB_API_BASE}/users/{username}/repos"
    res = requests.get(url, headers=HEADERS)

    if res.status_code != 200:
        raise Exception(res.json())

    return res.json()

def list_issues(owner: str, repo: str):
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/issues"
    res = requests.get(url, headers=HEADERS)

    if res.status_code != 200:
        raise Exception(res.json())

    return res.json()

def create_issue(owner: str, repo: str, title: str, body: str = None):
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/issues"
    payload = {"title": title, "body": body}

    res = requests.post(url, json=payload, headers=HEADERS)

    if res.status_code not in [200, 201]:
        raise Exception(res.json())

    return res.json()