from dotenv import load_dotenv

import os

load_dotenv('key_and_id.env')

SECRET_KEY = os.getenv('SECRET_KEY')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
