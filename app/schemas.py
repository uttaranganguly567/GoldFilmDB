"""Pydantic schemas that define the exact JSON contract the React frontend expects.

Field names use camelCase to match the original Spring Boot responses.
``validation_alias`` maps from the snake_case SQLAlchemy attribute names so that
``from_attributes`` construction works seamlessly.
"""

from pydantic import BaseModel, ConfigDict, Field


class ReviewResponse(BaseModel):
    """JSON shape returned for a single review."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    body: str


class ReviewCreate(BaseModel):
    """POST body the frontend sends when submitting a review."""

    reviewBody: str
    imdbId: str


class MovieResponse(BaseModel):
    """JSON shape returned for a movie, including nested reviews.

    The camelCase field names match what the React frontend already parses,
    while ``validation_alias`` lets Pydantic read from the snake_case
    SQLAlchemy model attributes.
    """

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    imdbId: str = Field(validation_alias="imdb_id")
    title: str
    releaseDate: str = Field(validation_alias="release_date")
    trailerLink: str = Field(validation_alias="trailer_link")
    genres: list[str]
    poster: str
    backdrops: list[str]
    reviews: list[ReviewResponse] = []
