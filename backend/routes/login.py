from fastapi import APIRouter
from backend.models.login import UserLogin
from database.connection import connection
import bcrypt
from backend.utils.auth import create_access_token

router = APIRouter()
@router.post("/login")
def login(user: UserLogin):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT id, name, password FROM users WHERE email = %s",
        (user.email,)
    )

    existing_user = cursor.fetchone()
    if not existing_user:
        return {
            "message": "Invalid email or password"
        }
    if not bcrypt.checkpw(
            user.password.encode("utf-8"),
            existing_user[2].encode("utf-8")
    ):
        return {
            "message": "Invalid email or password"
        }
    access_token = create_access_token(existing_user[0])
    return {
        "message": "Login successful",
        "access_token": access_token,
        "user_id": existing_user[0],
        "name": existing_user[1]
    }