import axios from "axios";

const instance = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
});

instance.interceptors.response.use(
  (response) => response,
  (error) => {
    const config = error.config || {};
    const skip401Redirect = config.skip401Redirect;

    if (error.response && error.response.status === 401 && !skip401Redirect) {
      const currentPath = window.location.pathname;
      if (currentPath !== "/login") {
        localStorage.removeItem("token");
        window.location.href = "/login";
      }
    }

    return Promise.reject(error);
  },
);

export default instance;
