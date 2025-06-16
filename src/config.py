from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_PORT = os.environ.get("DB_PORT")

# DNS
ASYNC_DB_URL = f'postgresql+asyncopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
DB_URL = f'postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'