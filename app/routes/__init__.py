from fastapi import APIRouter
from app.routes import user_routes

router = APIRouter()

# Kullanıcı rotalarını ana router'a ekleyelim
router.include_router(user_routes.router, prefix="/users", tags=["Users"])
