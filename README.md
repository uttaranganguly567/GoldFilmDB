# GoldFilmDB - A Full-Stack Movie Review App

GoldFilmDB is a full-stack web application built with Spring Boot and React that allows users to browse movies, watch trailers, and post reviews.

This repository is a **monorepo** containing two separate projects:

  * `MovieBackend`: The Spring Boot REST API.
  * `MovieFrontend`: The React client application.

## 🚀 Live Demo

The application is deployed on Render:

**[https://goldfilmdb-zj31.onrender.com/](https://www.google.com/search?q=https://goldfilmdb-zj31.onrender.com/)**

*(Note: The backend is on a free Render plan, so it may take 30-60 seconds to "wake up" on the first load.)*

-----

## ✨ Features

  * **Browse Movies:** View a carousel of featured movies.
  * **Watch Trailers:** Open a modal to watch the embedded movie trailer.
  * **Read Reviews:** See a list of existing reviews for any movie.
  * **Post Reviews:** Submit a new review for any movie.

-----

## 🛠 Tech Stack

| Area | Technology |
| :--- | :--- |
| **Backend** | Spring Boot, Spring Data MongoDB, Java 22 |
| **Frontend** | React, React Router, Axios, Bootstrap |
| **Database** | MongoDB Atlas (Cloud) |
| **Deployment** | Docker, Render (Web Service + Static Site) |

-----

## 📁 Project Structure

```
GoldFilmDB/
├── MovieBackend/       # The Spring Boot application
│   ├── src/main/java/com/uttaran/Movies/
│   ├── Dockerfile          # For Render deployment
│   └── pom.xml           # Maven dependencies
│
└── MovieFrontend/      # The React application
    ├── src/
    ├── package.json
    └── .env.development  # Local API proxy config
```

-----

## 🏃‍♂️ Getting Started: Running Locally

To run this project on your local machine, you will need to run both the backend and frontend servers.

### Prerequisites

  * **Java 22** (or higher)
  * **Maven**
  * **Node.js**
  * **MongoDB Atlas Account**: You need a cloud MongoDB URI.

### 1\. Backend Setup (`MovieBackend`)

1.  **Navigate to the backend:**

    ```bash
    cd MovieBackend
    ```

2.  **Create `.env` file:** Create a file named `.env` in the `MovieBackend` root. This project uses `spring-dotenv` to load these variables locally.

    ```
    MONGO_DATABASE=your_database_name
    MONGO_USER=your_mongodb_username
    MONGO_PASSWORD=your_mongodb_password
    MONGO_CLUSTER=your_mongodb_cluster_url.net

    # This tells the backend to trust your local frontend
    CORS_ALLOWED_ORIGIN=http://localhost:3000
    ```

3.  **Run the server:**

    ```bash
    ./mvnw spring-boot:run
    ```

    The backend server will start on `http://localhost:8080`.

### 2\. Frontend Setup (`MovieFrontend`)

1.  **Open a new terminal** and navigate to the frontend:

    ```bash
    cd MovieFrontend
    ```

2.  **Install dependencies:**

    ```bash
    npm install
    ```

3.  **Run the client:**

    ```bash
    npm start
    ```

    The React app will open and run on `http://localhost:3000`. The file `.env.development` is already configured to proxy API requests to your backend at `http://localhost:8080`.

-----

## 🌐 Deployment on Render

This application is configured for a monorepo deployment on Render.

### Backend Service (`movies-backend`)

  * **Service Type:** Web Service
  * **Runtime:** `Docker`
  * **Root Directory:** `MovieBackend`
  * **Environment Variables:**
      * `MONGO_DATABASE`: (Your database name)
      * `MONGO_USER`: (Your database username)
      * `MONGO_PASSWORD`: (Your database password)
      * `MONGO_CLUSTER`: (Your cluster URL)
      * `CORS_ALLOWED_ORIGIN`: `https://goldfilmdb-zj31.onrender.com` (The live frontend URL)

### Frontend Service (`movies-frontend`)

  * **Service Type:** Static Site
  * **Root Directory:** `MovieFrontend`
  * **Build Command:** `npm run build`
  * **Publish Directory:** `build`
  * **Environment Variable:**
      * `REACT_APP_API_URL`: `https://goldfilmdb.onrender.com/api/v1` (The live backend URL)
  * **Rewrite Rule:**
      * **Type:** `Rewrite`
      * **Source:** `/*`
      * **Destination:** `/index.html`

-----

## 📋 API Endpoints

  * `GET /api/v1/movies`: Get all movies.
  * `GET /api/v1/movies/{imdbId}`: Get a single movie by its IMDB ID.
  * `POST /api/v1/reviews`: Post a new review.

-----

## 👏 Acknowledgments & Credits

  * **Project Author:** [Uttaran Ganguly](https://www.google.com/search?q=https://github.com/uttaranganguly567)
