from aiogram import Dispatcher, Bot

TOKEN = "7122875435:AAHDHh1PjOUWyBXuWiXI0SqanAg8ajRs3Ck"

# Database connection settings
DB_HOST = "localhost"
DB_NAME = "mydatabase"
DB_USER = "yourusername"
DB_PASS = "yourpassword"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
bot = Bot(TOKEN)
