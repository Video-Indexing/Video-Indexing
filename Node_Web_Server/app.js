const mailer = require('./mailer.js');
const express = require('express');
var httpService = require('./httpService');
const cors = require('cors');
const firebaseService = require('./firebaseConfig');
const bodyParser = require('body-parser');
const { json } = require('stream/consumers');
const axios = require('axios');

require('dotenv').config()
const app = express();
const PORT = 5050;
app.use(express.json());
app.use(bodyParser.json());

const path = require('path');

algoServerIP = '';
algoPort = '';
if(process.env.STATUS == "production"){
    algoPort = process.env.ALGO_PROD_PORT;
    algoServerIP = process.env.ALGO_PROD_URL;
}
else{
    algoPort = process.env.ALGO_DEV_PORT;
    algoServerIP = process.env.ALGO_DEV_URL;
}


app.listen(PORT, (error) =>{
    if(!error){
        console.log(`Server is Successfully Running in ${process.env.STATUS} mode, and App is listening on port ` + PORT);
        // console.log(__filename); // prints the absolute path of the current module
        // console.log(path.basename(__filename));
    }
    else 
        console.log("Error occurred, server can't start", error);
    }
);

app.post("/user", (req, res) => {
    //req  parameters:  userName and password.isAdmin is false always if the user name is already exist return res = "this user name is not available"
    // createUser(req.query.userName, req.query.password, res);
});

//request from front to algo
app.post("/uploadVideo", (req, res) => {
    if (Object.keys(req.body).length === 0) {
        res.status(400).json({ error: 'Request body cannot be empty' });
      } else {
        res.status(200).send();
        sendToAlgoServer(algoServerIP + ":" + algoPort , JSON.stringify(req.body));
      }
});

//algo response
app.post("/uploadVideoAlgo",(req, res) => {
    if (Object.keys(req.body).length === 0) {
        res.status(400).json({ error: 'Request body cannot be empty' });
      } else {
        const data = JSON.stringify(req.body); // Get JSON data from request body
        const obj = JSON.parse(data);
        console.log(obj)
        firebaseService.createVideo(firebaseService.videoCollection, obj);
        res.status(200).send();
        // mailer.sendMailToClient("obn2468@gmail.com","or", obj.name)
        console.log("finished upload")
      }
});

app.get("/video",(req,res) => {
    res.send(getAllVideos());
});

async function sendToAlgoServer(url, data) {
    axios.post(url, data)
    .then(response => {
        console.log(response.data);
    })
    .catch(error => {
        console.error(error);
    });
  }
