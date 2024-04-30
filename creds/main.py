import psycopg2
from aiogram import Dispatcher, Bot

TOKEN = "7122875435:AAHDHh1PjOUWyBXuWiXI0SqanAg8ajRs3Ck"

# Database connection settings
DB_HOST = "db-postgresql-nyc3-crypto-bot-ai-do-user-14569518-0.c.db.ondigitalocean.com"
DB_NAME = "defaultdb"
DB_USER = "doadmin"
DB_PASS = "AVNS_5IWnjO3mhBd_dSST_Af"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
bot = Bot(TOKEN)

# Connection to database
print("Connecting to database...")
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port="25060")
print(conn)
cursor = conn.cursor()
print("Connected to database!")