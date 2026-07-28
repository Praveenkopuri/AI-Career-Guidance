from fastapi import FastAPI
from backend.routes.user import router as user_router

app = FastAPI(
    title="AI Career Guidance Platform",
    version="1.0"
)

app.include_router(user_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Career Guidance Platform"
    }