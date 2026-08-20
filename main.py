from fastapi import FastAPI
from backend.routes.user import router as user_router
from backend.routes.login import router as login_router
from backend.routes.profile import router as profile_router

app = FastAPI(
    title="AI Career Guidance Platform",
    version="1.0"
)

app.include_router(user_router)
app.include_router(login_router)
app.include_router(profile_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Career Guidance Platform"
    }