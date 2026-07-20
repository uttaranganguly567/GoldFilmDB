import os
import sys
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()
db_url = os.getenv("DATABASE_URL")
print("Initializing engine...")
engine = create_engine(db_url)
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

print("Querying database movies count...")
try:
    from app import models
    count = db.query(models.Movie).count()
    print(f"SUCCESS: Found {count} movies in database.")
except Exception as e:
    print(f"ERROR: {e}")
finally:
    db.close()
