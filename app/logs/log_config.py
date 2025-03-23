import os
import logging

# logs klasörünün var olup olmadığını kontrol et, yoksa oluştur
log_dir = "logs"
log_file = os.path.join(log_dir, "api.log")

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Logger yapılandırması
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),  # Logları dosyaya kaydet
        logging.StreamHandler()  # Konsola yazdır
    ]
)

logger = logging.getLogger(__name__)
