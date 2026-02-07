
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Force reload of .env
load_dotenv(override=True)

DATABASE_URL = os.getenv("DATABASE_URL")
print(f"Testing connection to: {DATABASE_URL}")

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Connection Successful!")
        print(f"Result: {result.fetchone()}")
except Exception as e:
    print("Connection Failed!")
    print(e)
