# getenv для того чтобы достать значение переменных из .env
from os import getenv
# load_dotenv для того чтобы связать config с .env
from dotenv import load_dotenv
load_dotenv()

# Все что касается телеграм бота 
TOKEN = getenv("TOKEN")
ADMIN = getenv("ADMIN_USER")

# Все что касается базы данных
PGHOST = getenv("PGHOST")
PGDATABASE = getenv("PGDATABASE")
PGUSER = getenv("PGUSER")
PGPASSWORD = getenv("PGPASSWORD")
PGPORT =getenv("PGPORT")

IMAGE = [
    'source/image/img1.jpeg',
    'source/image/img2.jpg'
]