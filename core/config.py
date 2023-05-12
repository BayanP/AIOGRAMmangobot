# getenv Для того чтобы достать значение переменных из .env
from os import getenv
# load_dotenv Для того чтобы связать config с .env
from dotenv import load_dotenv
load_dotenv()

# Все что косается Телеграмм бота
TOKEN = getenv("TOKEN")
ADMIN = getenv("ADMIN_USER")

# Все что косается базы данных
PGHOST = getenv("PGHOST")
PGDATABASE = getenv("PGDATABASE")
PGUSER = getenv("PGUSER")
PGPASSWORD = getenv("PGPASSWORD")
PGPORT = getenv("PGPORT")

HEADERS = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
}

IMAGE = [
    "source/image/img1.jpeg",
    "source/image/img2.jpg",
]

PARSURL = getenv("URL")
PARSDOMAIN = getenv("DOMAIN")