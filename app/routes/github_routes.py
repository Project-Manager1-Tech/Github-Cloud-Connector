from fastapi import APIRouter, HTTPException
from app.schemas.issue_schema import IssueCreateRequest
from app.services.github_service import fetch_repos, fetch_my_repos, list_issues, create_issue

router = APIRouter(prefix="/github", tags=["GitHub Connector"])

@router.get("/repos/{username}")
def get_repos(username: str):
    try:
        return fetch_repos(username)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/my-repos")
def get_my_repos():
    try:
        return fetch_my_repos()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/issues/{owner}/{repo}")
def get_issues(owner: str, repo: str):
    try:
        return list_issues(owner, repo)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/issues/{owner}/{repo}")
def post_issue(owner: str, repo: str, request: IssueCreateRequest):
    try:
        return create_issue(owner, repo, request.title, request.body)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))