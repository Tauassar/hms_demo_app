import axios from "axios";

const BASE_URL = 'http://localhost:8000/';

const axios_inst = axios.create({
    withCredentials: true,
    baseURL: BASE_URL
});

export default axios_inst;