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
app.use(cors())
// app.options('*', cors()) 
const PORT = 5050;
app.use(express.json());
app.use(bodyParser.json());

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
        mailer.sendMailToClient("obn2468@gmail.com","or", obj.name)
        console.log("sent mail from /uploadVideoAlgo post")
        console.log("finished upload")
      }
});

app.get("/video",(req,res) => {
    res.send(getAllVideos());
});

app.get("/videosByTag",(req,res) => {
    let data = JSON.stringify(req.body); // Get JSON data from request body
    let obj = JSON.parse(data);
    let tag = obj.tag
    firebaseService.searchVideosByTags(firebaseService.videoCollection,tag, (error, searchResults) => {
        if (error) {
          res.status(500).send('Internal Server Error'); // Handle error response
        } else {
          res.json(searchResults); // Return search results as JSON response
        }
      });

  
app.get("/searchVideoByName",(req,res) => {
    // console.log(req);
    const name = req.query.name;
    firebaseService.searchVideo(firebaseService.videoCollection,name).then( (r) =>
    {
        const json = JSON.stringify(r)
        console.log(json);
        if(json == "{}")
            res.send(200);
        else
            res.send(json);    
    });
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
