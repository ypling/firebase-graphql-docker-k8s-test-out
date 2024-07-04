import React, {useEffect, useState} from 'react'
import SignIn from "./Signin";
import SignUp from "./Signup";
import {getAuth, onAuthStateChanged} from 'firebase/auth'
import Dashboard from "./Dashboard";
import '../utils/authHelper'

const App = () => {
    const [page, setPage] = useState()
    useEffect(() => {
        const auth = getAuth()
        onAuthStateChanged(auth, (user) => {
            if (user) {
                setPage("LOGGED_IN")
                user.getIdToken().then((token) => {
                    console.log(token)
                })
                // User is signed in, see docs for a list of available properties
                // https://firebase.google.com/docs/reference/js/auth.user
                const uid = user.uid;
                // ...
            } else {
                setPage("SIGN_IN")
                // User is signed out
                // ...
            }
        });
    }, [])

    return (
        <>
            {page === 'LOGGED_IN' && <Dashboard/>}
            {page === 'SIGN_IN' && <SignIn goToSignUp={() => {
                setPage('SIGN_UP')
            }}/>}
            {page === 'SIGN_UP' && <SignUp goToSignIn={() => {
                setPage('SIGN_IN')
            }}/>}
        </>
    )
}

export default App