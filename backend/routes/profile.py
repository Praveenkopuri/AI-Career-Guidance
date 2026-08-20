from fastapi import APIRouter, Depends
from backend.utils.auth import verify_token
from jose import jwt

router = APIRouter()
@router.get("/profile")
def profile(token: str):
    payload = verify_token(token)

    if not payload:
        return {
            "message": "Invalid or expired token"
        }

    return {
        "message": "This is a protected profile",
        "user_id": payload["user_id"]
    }