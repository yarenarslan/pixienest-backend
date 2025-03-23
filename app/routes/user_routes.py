from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories.user_repository import create_user, get_user
from app.schemas import UserCreate, UserResponse  # Schema dosyanı ekledik

router = APIRouter()

@router.post("/")
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)
