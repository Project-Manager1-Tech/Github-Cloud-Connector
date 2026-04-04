from pydantic import BaseModel

class PullRequestCreateRequest(BaseModel):
    title: str
    head: str
    base: str
    body: str | None = None