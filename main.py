"""GoldFilmDB — FastAPI application.

Exposes REST endpoints and Jinja2 server-rendered pages with HTMX.
"""

from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
import os

# Changed from relative imports to absolute imports since main.py is at the root
from app import models, schemas, crud
from app.database import engine, get_db

# Create tables on startup (safe no-op if they already exist)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="GoldFilmDB API",
    description="A simple movie catalog API — Python/FastAPI/HTMX edition",
    version="1.1.0",
)

# Configure Jinja2 templates to look inside the app/templates directory
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "app", "templates"))

# CORS — mirrors the old WebConfig.java that allowed localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Expand to support any origin in dev
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# HTML Pages (Served for standard browser navigation & HTMX)
# ---------------------------------------------------------------------------


@app.get("/", response_class=HTMLResponse)
def index_page(request: Request, db: Session = Depends(get_db)):
    """Render the main movies list catalog page."""
    movies = crud.get_all_movies(db)
    return templates.TemplateResponse(request, "index.html", {"movies": movies})


@app.get("/movies/{imdb_id}", response_class=HTMLResponse)
def reviews_page(request: Request, imdb_id: str, db: Session = Depends(get_db)):
    """Render the reviews list page for a single movie."""
    movie = crud.get_movie_by_imdb_id(db, imdb_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return templates.TemplateResponse(request, "reviews.html", {"movie": movie})


@app.get("/trailer/{yt_trailer_id}", response_class=HTMLResponse)
def trailer_page(request: Request, yt_trailer_id: str):
    """Render the trailer play view page."""
    return templates.TemplateResponse(request, "trailer.html", {"ytTrailerId": yt_trailer_id})


# ---------------------------------------------------------------------------
# REST API Endpoints & HTMX Endpoints
# ---------------------------------------------------------------------------


@app.get("/api/v1/movies", response_model=list[schemas.MovieResponse])
def get_all_movies(db: Session = Depends(get_db)):
    """Return every movie in the catalog as JSON."""
    return crud.get_all_movies(db)


@app.get("/api/v1/movies/{imdb_id}", response_model=schemas.MovieResponse)
def get_single_movie(imdb_id: str, db: Session = Depends(get_db)):
    """Return a single movie by its IMDb ID, including its reviews as JSON."""
    movie = crud.get_movie_by_imdb_id(db, imdb_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@app.post("/api/v1/reviews")
def create_review(
    request: Request,
    db: Session = Depends(get_db),
    # Support JSON requests or URL-encoded form submissions from HTMX
    reviewBody: str = Form(None),
    imdbId: str = Form(None),
):
    """Submit a new review. 
    
    If called via HTMX form submission, returns an HTML list item fragment.
    If called via JSON client, returns JSON data.
    """
    # Check if this is an HTMX form request (content-type: application/x-www-form-urlencoded)
    content_type = request.headers.get("content-type", "")
    
    if "application/x-www-form-urlencoded" in content_type:
        if not reviewBody or not imdbId:
            raise HTTPException(status_code=400, detail="Missing form parameters")
        
        review = crud.create_review(db, reviewBody, imdbId)
        if not review:
            raise HTTPException(status_code=404, detail="Movie not found")
            
        # Render and return only the HTML fragment for the single review
        return templates.TemplateResponse(
            request,
            "review_list_fragment.html", 
            {"r": review}
        )
    
    # Otherwise assume it's a JSON request from standard client
    # We parse the body manually to avoid signature conflicts
    try:
        import json
        async def parse_json():
            body = await request.body()
            return json.loads(body)
        
        # FastAPI handles run-sync execution for body reading
        import asyncio
        payload = asyncio.run(request.json())
        review_body = payload.get("reviewBody")
        imdb_id = payload.get("imdbId")
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid request payload")

    review = crud.create_review(db, review_body, imdb_id)
    if not review:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"id": review.id, "body": review.body}
