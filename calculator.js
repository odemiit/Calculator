// jshint esversion:6

const express = require('express');
const app = express();
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended: true}));
//body parser allows you to go into any of your routes. 


app.get("/", function(req, res) {
    //res.send("Hello World");
    res.sendFile(__dirname + "/index.html");
});

app.post("/", function(req, res) {

    var num1 = req.body.num1;
    var num2 = req.body.num2;
    
    res.send("Thanks for posting that!");
});

app.listen(3000, function() {
    console.log("Server started on port 3000");
});