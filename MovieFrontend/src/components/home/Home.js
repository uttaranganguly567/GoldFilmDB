import Hero from '../hero/Hero';

const Home = ({movies}) => {

    if(!movies || movies.length === 0){
        return <div>No movies found, check the backend connection.</div>;
    }
    return (
        <Hero movies = {movies} />
    )
}

export default Home