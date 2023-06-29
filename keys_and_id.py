from dotenv import load_dotenv

import os

#key_and_id.env - хранит ключи, где SECRET_KEY - рандомные символ, TELEGRAM_TOKEN - токен бота телеграм, TELEGRAM_CHAT_ID - id чата телеграм
load_dotenv('key_and_id.env')

SECRET_KEY = os.getenv('SECRET_KEY')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
