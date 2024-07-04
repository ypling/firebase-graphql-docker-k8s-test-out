import axios from 'axios';
import {getAuth} from "firebase/auth";

// Set up Axios instance
const axiosInstance = axios.create({
    baseURL: '/graphql',
    // You can add other Axios configurations here
});

// Add an interceptor to include idToken in the Authorization header
axiosInstance.interceptors.request.use(
    async (config) => {
        // Get the idToken from wherever you have stored it after sign-in with Firebase Authentication
        const idToken = await getAuth().currentUser.getIdToken(); // Implement this function to get the idToken
        // Add the idToken to the Authorization header
        config.headers.Authorization = `Bearer ${idToken}`;
        return config;
    },
    (error) => {
        // Handle request errors
        return Promise.reject(error);
    }
);

export default axiosInstance;