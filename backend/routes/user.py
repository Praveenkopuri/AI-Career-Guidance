from fastapi import APIRouter
from backend.models.user import UserRegister

router = APIRouter()

@router.post("/register")
def register(user: UserRegister):
    return {
        "message": "User registration received",
        "user": user
    }