from app.utils.github_exceptions import GitHubAPIError

def handle_github_response(response):
    """
    Handles GitHub API response.
    If success -> returns JSON.
    If failure -> raises GitHubAPIError with correct status_code.
    """

    if response.status_code in [200, 201]:
        return response.json()

    try:
        error_json = response.json()
        message = error_json.get("message", "GitHub API Error")
    except Exception:
        error_json = response.text
        message = "GitHub API returned invalid response"

    raise GitHubAPIError(
        status_code=response.status_code,
        message=message,
        details=error_json
    )