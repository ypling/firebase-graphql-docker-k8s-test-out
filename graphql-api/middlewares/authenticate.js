// Import the functions you need from the SDKs you need
const admin = require("firebase-admin");
const serviceAccount = require('../secrets/firebase-admin-sdk-key.json');
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Initialize Firebase
admin.initializeApp({
    credential: admin.credential.cert(serviceAccount)
});

const authenticate =  async (req, res, next) => {
    const idToken = req.headers.authorization?.replace("Bearer ", "")
    const decodedToken = await admin.auth().verifyIdToken(idToken)
    console.log(decodedToken)
    next()
}

module.exports = authenticate