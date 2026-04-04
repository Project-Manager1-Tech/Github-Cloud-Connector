import requests
from app.config import GITHUB_TOKEN, GITHUB_API_BASE
from app.utils.github_response_handler import handle_github_response

DEFAULT_HEADERS = {
    "Accept": "application/vnd.github+json"
}

PAT_HEADERS = {
    **DEFAULT_HEADERS,
    "Authorization": f"Bearer {GITHUB_TOKEN}"
}


def fetch_repos(username: str):
    url = f"{GITHUB_API_BASE}/users/{username}/repos"
    res = requests.get(url, headers=PAT_HEADERS)
    return handle_github_response(res)


def fetch_my_repos():
    url = f"{GITHUB_API_BASE}/user/repos"
    res = requests.get(url, headers=PAT_HEADERS)
    return handle_github_response(res)


def fetch_my_repos_with_token(token: str):
    headers = {
        **DEFAULT_HEADERS,
        "Authorization": f"Bearer {token}"
    }

    url = f"{GITHUB_API_BASE}/user/repos"
    res = requests.get(url, headers=headers)
    return handle_github_response(res)


def list_issues(owner: str, repo: str):
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/issues"
    res = requests.get(url, headers=PAT_HEADERS)
    return handle_github_response(res)


def create_issue(owner: str, repo: str, title: str, body: str = None):
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/issues"
    payload = {"title": title, "body": body}

    res = requests.post(url, json=payload, headers=PAT_HEADERS)
    return handle_github_response(res)

def list_branches(owner: str, repo: str):
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/branches"
    res = requests.get(url, headers=PAT_HEADERS)
    return handle_github_response(res)

def branch_exists(owner: str, repo: str, branch: str) -> bool:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/branches/{branch}"
    res = requests.get(url, headers=PAT_HEADERS)

    if res.status_code == 200:
        return True

    if res.status_code == 404:
        return False

    # other GitHub errors
    handle_github_response(res)

def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: str = None):

    if not branch_exists(owner, repo, head):
        raise GitHubAPIError(
            status_code=400,
            message="Invalid head branch",
            details={"message": f"Head branch '{head}' does not exist"}
        )

    if not branch_exists(owner, repo, base):
        raise GitHubAPIError(
            status_code=400,
            message="Invalid base branch",
            details={"message": f"Base branch '{base}' does not exist"}
        )

    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/pulls"

    payload = {
        "title": title,
        "head": head,
        "base": base,
        "body": body
    }

    res = requests.post(url, json=payload, headers=PAT_HEADERS)
    return handle_github_response(res)