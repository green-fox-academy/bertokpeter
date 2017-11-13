'use strict';

const express = require('express');
const app = express();

const mysql = require('mysql');
const conn = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'reddit'
});

conn.connect(function(err){
    if(err){
        console.log("Error connecting to Db");
        return;
    } else {
        console.log("Connection established");
    }
});

app.use('/assets', express.static('./assets'));

app.get('/', function(req, res){
    res.sendFile(__dirname + '/reddit.html');
});

app.get('/addpost', function(req, res){
    res.sendfile(__dirname + '/addpost.html');
});

app.get('/posts')

app.listen(4000);