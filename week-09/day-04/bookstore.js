'use strict';

const express = require('express');
const app = express();
const mysql = require('mysql');

app.use(express.json());

const conn = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'bookstore'
});

conn.connect(function(err){
    if(err){
        console.log("Error connecting to Db");
    } else {
        console.log("Connection established");
    }
});

conn.end();
app.listen(3000);