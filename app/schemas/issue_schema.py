from pydantic import BaseModel

class IssueCreateRequest(BaseModel):
    title: str
    body: str | None = None