import axios from "axios";

export const axios_instance = axios.create({
  baseURL: "http://127.0.0.1:5000/",
});
