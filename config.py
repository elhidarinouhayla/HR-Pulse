from dotenv import load_dotenv
import os

load_dotenv()


KEY = os.getenv("ENDPOINT")
ENDPOINT = os.getenv("ENDPOINT")
DB_URL = os.getenv("DATABASE_URL")