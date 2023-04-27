const express = require('express');

const app = express();
const PORT = 3000;
const algoServerIP = "127.0.0.1";
const algoPorst = 8080;
app.use(express.json());

app.listen(PORT, (error) =>{
    if(!error)
        console.log("Server is Successfully Running, and App is listening on port " + PORT)
    else 
        console.log("Error occurred, server can't start", error);
    }
);

app.post("/signUp", (req, res) => {
    //req  parameters:  userName and password.isAdmin is false always if the user name is already exist return res = "this user name is not available"
    // createUser(req.query.userName, req.query.password, res);
});

app.post("/uploadVideo",(req, res) => {
    httpPostAsyncResponse(algoServerIP+"/uploadVideo?link=" + req.query.link + "?name=" + req.query.name,"",handleUplaodVideo,res);
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