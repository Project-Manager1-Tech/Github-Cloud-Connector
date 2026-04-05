from fastapi import FastAPI
from app.routes.github_routes import router as github_router
from app.routes.auth_routes import router as auth_router

app = FastAPI(title="GitHub Cloud Connector", version="1.0")

@app.get("/")
def root():
    return {"message": "GitHub Cloud Connector is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(github_router)
app.include_router(auth_router)
