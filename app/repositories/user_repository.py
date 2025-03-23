from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate
from app.utils.hash import hash_password  # Yeni ekledik

def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)  # Şifreyi hashledik
    db_user = User(username=user.username, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
