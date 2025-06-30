import './App.css';
import api from './api/axiosConfig';
import {useState, useEffect} from 'react';
import Layout from './components/Layout';
import {Routes, Route} from 'react-router-dom';
import Home from './components/home/Home';
import Header from './components/header/Header';
import Trailer from './components/trailer/Trailer';
import Reviews from './components/reviews/Reviews';

function App() {

  const [movies, setMovies] = useState([]);
  const [movie, setMovie] = useState(null);
  const [reviews, setReviews] = useState([]);

  const getMovies = async () => {
    console.log("Attempting to fetch movies.");
    try {
      const response = await api.get("/movies");
      console.log("Response: ", response.data);
      setMovies(response.data);
    } catch (err) {
      console.error("API Error:", err.response || err);
    }
  };

  const getMovieData = async (movieId) => {
    try {
      const response = await api.get(`api/v1/movies/${movieId}`);
      const singleMovie = response.data;
      setMovie(singleMovie);
      setReviews(singleMovie.reviews);  
    } 
    catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    getMovies();
  }, [])

  return (
    <div className="App">
      <Header />
      <Routes>
        <Route path="/" element={<Layout/>}>
          <Route index element={<Home movies={movies}/>}></Route>.
          <Route path="/Trailer/:ytTrailerId" element={<Trailer />}></Route>
          <Route path="/Reviews/:movieId" element = {<Reviews getMovieData = {getMovieData} movie = {movie} reviews = {reviews} setReviews = {setReviews} />}></Route>
        </Route>
      </Routes>

    </div>
  );
}

export default App;
