from fastapi import APIRouter
from backend.models.user import UserRegister
from database.connection import connection
import bcrypt
router = APIRouter()

@router.post("/register")
def register(user: UserRegister):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT id FROM users WHERE email = %s",
        (user.email,)
    )

    existing_user = cursor.fetchone()
    if existing_user:
        return {"message": "User already exists"}
    sql = """
          INSERT INTO users (name, email, password)
          VALUES (%s, %s, %s) \
          """
    hashed_password = bcrypt.hashpw(
        user.password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    cursor.execute(sql, (user.name, user.email, hashed_password))
    connection.commit()

    return {
        "message": "User registration received",

    }