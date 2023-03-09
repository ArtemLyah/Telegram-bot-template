from dotenv import load_dotenv
import os

# load data from .env
load_dotenv()

db_settings = {
    "drivername":"postgresql+psycopg2",
    "username":os.getenv("DB_USER"),
    "password":os.getenv("DB_PASSWORD"),
    "host":os.getenv("DB_HOST"),
    "port":5432,
    "database":os.getenv("DB_NAME")
}

BOT_TOKEN = os.getenv("BOT_TOKEN")
FATHER_ID = int(os.getenv("FATHER_ID"))

create_db = True