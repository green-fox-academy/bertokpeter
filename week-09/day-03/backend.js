'use strict';
const express = require('express');
const app = express();

express.json.type = "application/json"
app.use('/assets', express.static("./assets"));
app.use(express.json());

app.get('/', function(req,res) {
    res.sendFile(__dirname + '/index.html');
});

app.get('/doubling', function(req,res) {
    if (req.query.input === undefined){
        res.json({'error': "Please provide an input!"});
    } else {
        res.json({'received': req.query.input*1, "result": req.query.input*2});
    }
});

app.get('/greeter', function(req,res) {
    if (req.query.name === undefined){
        res.json({'error': "Please provide a name!"});
    } else if (req.query.title === undefined){
        res.json({'error': "Please provide a title!"});
    } else {
        res.json({'welcome_message': "Oh, hi there " + req.query.name + ", my dear " + req.query.title + "!"});
    }
});

app.get('/appenda/:appendable', function(req, res) {
    res.json({"appended": req.params.appendable + "a"});
});

app.post('/dountil/:what', function(req, res) {
    let result = 0;
    if (!req.body.until) {
        res.json({"error": "Please provide a number"})
    } else {
        if (req.params.what === "sum"){
            result = sum(req.body.until);
        } else if (req.params.what === "factor"){
            result = factor(req.body.until);
        }
        res.json({"result": result})
    }
});

app.post('/arrays', function(req,res) {
    let result = 0;
    if (!req.body.what || !req.body.numbers){
        res.json({"error": "Please provide what to do with the numbers!"});
    } else {
        if (req.body.what === "sum") {
            result = req.body.numbers.reduce((prev, current) => prev+current);
        } else if (req.body.what === "multiply") {
            result = req.body.numbers.reduce((prev, current) => prev*current);
        } else if (req.body.what === "double") {
            result = req.body.numbers.map((number) => number*2);
        }
        res.json({"result": result});
    }
});

app.listen(8080);

function sum(until){
    let summa = 0;
    for (let i=0; i < until+1; i++){
        summa += i;
    }
    return summa
}

function factor(until) {
    let factor = 1;
    for (let i=1; i < until+1; i++){
        factor *= i;
    }
    return factor
}