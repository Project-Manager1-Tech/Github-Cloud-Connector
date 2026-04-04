from fastapi import APIRouter, HTTPException, Header
from app.schemas.issue_schema import IssueCreateRequest
from app.services.github_service import (
    fetch_repos,
    fetch_my_repos,
    fetch_my_repos_with_token,
    list_issues,
    create_issue
)

from app.utils.github_exceptions import GitHubAPIError

router = APIRouter(prefix="/github", tags=["GitHub Connector"])


@router.get("/repos/{username}")
def get_repos(username: str):
    try:
        return fetch_repos(username)
    except GitHubAPIError as e:
        raise HTTPException(status_code=e.status_code, detail=e.details)


@router.get("/my-repos")
def get_my_repos():
    try:
        return fetch_my_repos()
    except GitHubAPIError as e:
        raise HTTPException(status_code=e.status_code, detail=e.details)


@router.get("/issues/{owner}/{repo}")
def get_issues(owner: str, repo: str):
    try:
        return list_issues(owner, repo)
    except GitHubAPIError as e:
        raise HTTPException(status_code=e.status_code, detail=e.details)


@router.post("/issues/{owner}/{repo}")
def post_issue(owner: str, repo: str, request: IssueCreateRequest):
    try:
        return create_issue(owner, repo, request.title, request.body)
    except GitHubAPIError as e:
        raise HTTPException(status_code=e.status_code, detail=e.details)


@router.get("/oauth/my-repos")
def get_my_repos_oauth(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]
        return fetch_my_repos_with_token(token)
    except IndexError:
        raise HTTPException(status_code=401, detail="Invalid Authorization header format")
    except GitHubAPIError as e:
        raise HTTPException(status_code=e.status_code, detail=e.details)