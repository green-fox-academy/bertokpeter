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
app.use(express.json());

app.get('/', function(req, res){
    res.sendFile(__dirname + '/reddit.html');
});

app.get('/addpost', function(req, res){
    res.sendFile(__dirname + '/addpost.html');
});

app.get('/posts', function(req, res) {
    conn.query('SELECT * FROM posts', function(err, rows){
        if(err) {
            console.log(err.toString());
        }
        console.log("Data received from Db:\n");
        let response = {"posts":[]};
        rows.forEach(function(row){
            response.posts.push({"id": row.id,
            "title": row.title,
            "url": row.url,
            "timestamp": row.timestamp,
            "score": row.score});
        });
        res.set('Content-Type', 'application/json');
        res.json(response);
    });
});

app.post('/posts', function(req, res){
    conn.query('INSERT INTO posts SET ?', req.body, function(err, results, fields){
        if(err) throw err;
    });
    conn.query(`SELECT * FROM posts WHERE title = "${req.body.title}"`, function(err, rows){
        if(err) {
            console.log(err.toString());
        }
        console.log("Data received from Db:\n");
        let response = {
            "id": rows[0].id,
            "title": rows[0].title,
            "url": rows[0].url,
            "timestamp": rows[0].timestamp,
            "score": rows[0].score
        };
        res.set('Content-Type', 'application/json');
        res.json(response);
    });
});

app.listen(4000);