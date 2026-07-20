# GoldFilmDB 🎬

A full-stack movie catalog website with a review system.

## Tech Stack

| Layer       | Technology                                        |
| ----------- | ------------------------------------------------- |
| **Frontend** | Jinja2 Templates, HTML5, CSS3, Bootstrap 5, HTMX  |
| **Backend**  | Python, FastAPI, SQLAlchemy, Pydantic              |
| **Database** | PostgreSQL                                         |

## Getting Started

### Prerequisites

- **Python 3.10+**
- **PostgreSQL** running locally
- The standard FastAPI CLI library (installed automatically via requirements)

### 1. Set up the Database

Create a PostgreSQL database called `goldfilmdb`:

```sql
CREATE DATABASE goldfilmdb;
```

### 2. Configure Environment Variables

Copy the template `.env.example` file to `.env` in the root directory:

```bash
# Windows Command Prompt / PowerShell
copy .env.example .env
```

Open the newly created `.env` file and make sure the `DATABASE_URL` matches your local PostgreSQL credentials:
```env
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/goldfilmdb
```

### 3. Install Dependencies & Seed Data

Set up a virtual environment, install the dependencies, and import the seed movie data:

```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# Install requirements
pip install -r requirements.txt

# Seed movie data from movies.json
python seed.py
```

### 4. Start the Application

Start the FastAPI application using the modern FastAPI development command:

```bash
fastapi dev main.py
```

Open your browser and navigate to:
👉 **`http://localhost:8000/`**

Interactive API documentation is also available at `http://localhost:8000/docs`.

---

## Project Structure

```
GoldFilmDB/
├── app/                      # FastAPI App Submodule (database, schemas, templates)
│   ├── templates/            # Jinja2 HTML templates + HTMX dynamic layouts
│   │   ├── base.html         # Main Layout
│   │   ├── index.html        # Main Carousel list
│   │   ├── reviews.html      # Reviews page
│   │   ├── review_list_fragment.html # HTML fragment for HTMX updates
│   │   └── trailer.html      # Youtube Player view
│   ├── models.py             # SQLAlchemy ORM models
│   ├── schemas.py            # Pydantic request/response models
│   ├── crud.py               # Database queries
│   └── database.py           # Database engine & session
├── main.py                   # Application entry point + routing
├── movies.json               # Seed catalog database
├── seed.py                   # Data imports script
├── requirements.txt          # Python dependencies
├── .env.example              # Environment template config
└── README.md
```
