from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# User modelini içe aktar
from app.models.user import User  # <-- Bunu ekle
