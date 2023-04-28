const express = require('express');
require('dotenv').config()

console.log(process.env)
const app = express();
const PORT = 3000;
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
    if(!error)
        console.log(`Server is Successfully Running in ${process.env.STATUS} mode, and App is listening on port ` + PORT)
    else 
        console.log("Error occurred, server can't start", error);
    }
);

app.post("/user", (req, res) => {
    //req  parameters:  userName and password.isAdmin is false always if the user name is already exist return res = "this user name is not available"
    // createUser(req.query.userName, req.query.password, res);
});

app.post("/uploadVideo",(req, res) => {
    // const obj = {link: req.query.link, age: req.query.name};
    httpPostAsyncResponse(algoServerIP+":"+algoPort+"/uploadVideo" , req.body, handleUplaodVideo, res);
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