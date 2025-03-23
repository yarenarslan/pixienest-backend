import os
from dotenv import load_dotenv

# .env dosyasını yükleyelim
load_dotenv()

class Settings:
    PROJECT_NAME: str = "FastAPI Uygulamam"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:Ygsp1212.@localhost:5432/fastapi_db")

settings = Settings()
