import axios from 'axios';

export default axios.create({
    baseURL:'/api/v1',
    headers: {"ngrok-skip-browser-warning": "true"}
});