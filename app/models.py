from sqlalchemy import Column, Integer, String, Text, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from .database import Base


class Movie(Base):
    """Represents a movie in the catalog.

    Genres and backdrops are stored as PostgreSQL native text arrays,
    avoiding the need for separate junction/child tables.
    """

    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    imdb_id = Column(String, unique=True, nullable=False, index=True)
    title = Column(String, nullable=False)
    release_date = Column(String)
    trailer_link = Column(String)
    genres = Column(ARRAY(String), default=[])
    poster = Column(String)
    backdrops = Column(ARRAY(String), default=[])

    reviews = relationship(
        "Review", back_populates="movie", cascade="all, delete-orphan"
    )


class Review(Base):
    """A user-submitted review linked to a movie via foreign key."""

    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    body = Column(Text, nullable=False)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)

    movie = relationship("Movie", back_populates="reviews")
