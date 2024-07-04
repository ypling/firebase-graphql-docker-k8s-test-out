import React from 'react';
import {getAuth, signOut} from "firebase/auth";
import axiosInstance from "../utils/request";

const Dashboard = () => {

    const handleRequest = () => {
        axiosInstance.post("", {query: "{message}"})
    }


    const handleSignOut = () => {
        const auth = getAuth()
        signOut(auth)
    }

    return (<div>
        <h1>Dashboard</h1>
        <p>
            <button onClick={handleRequest}>Send a request</button>
        </p>
        <p>
            <a onClick={handleSignOut} href="">logout</a>
        </p>

    </div>)
}

export default Dashboard