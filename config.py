from dotenv import load_dotenv
import os

# load data from .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
