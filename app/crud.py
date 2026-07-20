"""Database query functions (replaces Spring Data repositories + service layer)."""

from sqlalchemy.orm import Session, joinedload
from . import models


def get_all_movies(db: Session) -> list[models.Movie]:
    """Return every movie with its reviews eagerly loaded."""
    return (
        db.query(models.Movie)
        .options(joinedload(models.Movie.reviews))
        .all()
    )


def get_movie_by_imdb_id(db: Session, imdb_id: str) -> models.Movie | None:
    """Look up a single movie by its IMDb ID, with reviews."""
    return (
        db.query(models.Movie)
        .options(joinedload(models.Movie.reviews))
        .filter(models.Movie.imdb_id == imdb_id)
        .first()
    )


def create_review(db: Session, body: str, imdb_id: str) -> models.Review | None:
    """Create a review and link it to the movie with the given IMDb ID.

    Returns ``None`` if no movie matches the IMDb ID.
    Unlike the old Spring Boot code that manually pushed into a MongoDB array,
    the PostgreSQL foreign key handles the association automatically.
    """
    movie = (
        db.query(models.Movie)
        .filter(models.Movie.imdb_id == imdb_id)
        .first()
    )
    if not movie:
        return None

    review = models.Review(body=body, movie_id=movie.id)
    db.add(review)
    db.commit()
    db.refresh(review)
    return review
