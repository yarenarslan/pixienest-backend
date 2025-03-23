from fastapi import FastAPI
from app.routes import user_routes  # Sadece user_routes import ettik
from app.logs.log_config import logger  # Logger'ı içeri aktardık

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI uygulamamız çalışıyor!"}

# Kullanıcı rotalarını ekleyelim
app.include_router(user_routes.router, prefix="/users", tags=["Users"])

# Sunucu başlatıldığında log kaydı oluştur
logger.info("FastAPI uygulaması başlatıldı!")  
