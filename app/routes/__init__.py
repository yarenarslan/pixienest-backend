from fastapi import APIRouter
from app.routes import users

router = APIRouter()

# Kullanıcı rotalarını ana router'a ekleyelim
router.include_router(users.router, prefix="/users", tags=["Users"])
