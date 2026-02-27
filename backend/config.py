from dotenv import load_dotenv
import os

load_dotenv()


KEY = os.getenv("KEY")
ENDPOINT = os.getenv("ENDPOINT")
DB_URL = os.getenv("DB_URL")

