const express = require('express');
// const { test } = require('node:test');
// var firebaseService = import('./firebaseService.mjs');
// import { test } from './firebaseService.mjs'
// firebaseService.test();
var httpService = require('./httpService');
const cors = require('cors');
const firebaseService = require('./firebaseConfig');

require('dotenv').config()
// console.log(process.env)
// const path = require('path')
const app = express();
const PORT = 5050;
app.use(express.json());

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
        // var obj = { name : "welcome" , link : "", indexing : ""}
        // var json = JSON.stringify(obj);
        // console.log(json);
        // var obj2 = JSON.parse(json);
        // firebaseService.createVideo(firebaseService.videoCollection,obj2).then(x => console.log( x ));
        // firebaseService.searchVideo(firebaseService.videoCollection,"test").then(
        //     vids => console.log(vids)
        // );
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
app.post("/uploadVideo",(req, res) => {
    httpPostAsyncResponse(algoServerIP+":"+algoPort+"/uploadVideo" , req.body, handleUplaodVideo, res);
});

//algo response
app.post("/uploadVideoAlgo",(req, res) => {
    console.log(req.body);
    const obj = JSON.parse(req.body);
    firebaseService.createVideo(obj);
    res.status(200).send();
});

app.get("/videoStatus", (req, res) => {
    //req  parameters:  videoID
});

app.get("/video",(req,res) => {
    res.send(getAllVideos());
});

function handleUplaodVideo(body, res){
    res.send(body);
}