from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db import get_db
from models import User
from repositories.user_repo import user_Repo
from schemas.user_schemas import Usercreate
router = APIRouter()


@router.post("/signup")
def signup(user: Usercreate, db: Session = Depends(get_db)):
    user_repo = user_Repo(db)
    # Convert Pydantic schema to SQLAlchemy model
    db_user = User(email=user.email, password=user.password)
    user_repo.create_user(db_user)
    return {"message": "User signed up successfully"}

@router.post("/login")
def login():
    return {"message": "User logged in successfully"}


