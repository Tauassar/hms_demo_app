import axios from "axios";

const BASE_URL = 'http://164.90.197.124:9000/';

const axios_inst = axios.create({
    withCredentials: true,
    baseURL: BASE_URL
});

export default axios_inst;
