"""Seed the PostgreSQL database with movies from movies.json.

Run from the backend/ directory:
    python seed.py
"""

import json
import os
import sys

# Ensure the app package is importable
sys.path.insert(0, os.path.dirname(__file__))

from app.database import SessionLocal, engine
from app import models

# Create tables if they don't exist yet
models.Base.metadata.create_all(bind=engine)


def seed():
    db = SessionLocal()
    try:
        existing = db.query(models.Movie).count()
        if existing > 0:
            print(f"Database already contains {existing} movies. Skipping seed.")
            return

        movies_path = os.path.join(os.path.dirname(__file__), "movies.json")
        with open(movies_path, "r", encoding="utf-8") as f:
            movies_data = json.load(f)

        for entry in movies_data:
            movie = models.Movie(
                imdb_id=entry["imdbId"],
                title=entry["title"],
                release_date=entry["releaseDate"],
                trailer_link=entry["trailerLink"],
                genres=entry.get("genres", []),
                poster=entry["poster"],
                backdrops=entry.get("backdrops", []),
            )
            db.add(movie)

        db.commit()
        print(f"Successfully seeded {len(movies_data)} movies.")

    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        db.close()


if __name__ == "__main__":
    seed()
