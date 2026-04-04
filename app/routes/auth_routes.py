from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from app.config import GITHUB_CLIENT_ID, GITHUB_REDIRECT_URI
from app.services.oauth_service import exchange_code_for_token

router = APIRouter(prefix="/auth", tags=["OAuth2"])

@router.get("/login")
def github_login():
    github_url = (
        "https://github.com/login/oauth/authorize"
        f"?client_id={GITHUB_CLIENT_ID}"
        f"&redirect_uri={GITHUB_REDIRECT_URI}"
        "&scope=repo"
    )
    return RedirectResponse(url=github_url)

@router.get("/callback")
def github_callback(code: str):
    token_data = exchange_code_for_token(code)
    return token_data