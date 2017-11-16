'use strict';

const express = require('express');
const app = express();
const mysql = require('mysql');

app.use('/assets', express.static('./assets'));
app.use('/tracks', express.static('./tracks'));
app.use(express.json());

let conn = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'foxplayer'
});

conn.connect(function(err){
    if(err){
        console.log("Error connecting to Db");
        return;
    } else {
        console.log("Connection established");
    }
});

app.get('/', function (req, res){
    res.sendFile(__dirname + '/foxplayer.html')
});

app.get('/playlists', function(req, res) {
    conn.query('SELECT * FROM playlists', function(err, rows){
        if(err) {
            console.log(err.toString());
        }
        console.log("Data received from Db:\n");
        let responsePlaylists = {"playlists": []};
        rows.forEach(function(playlist){
            responsePlaylists.playlists.push({
                "id": playlist.id,
                "title": playlist.title,
                "system": playlist.system
            });
        });
        res.json(responsePlaylists);
    });
});

app.get('/playlist-tracks', function(req, res) {
    let allSelector = 'SELECT id, DISTINCT title, artist, duration, path, playlists FROM tracklist';
    conn.query(allSelector, function(err, rows){
        if(err) {
            console.log(err.toString());
        }
        console.log("Data received from Db:\n");
        let responseAllTracks = {"tracklist": []};
        rows.forEach(function(track){
            responseAllTracks.push({
                "id": track.id,
                "title": track.title,
                "artist": track.artist,
                "duration": track.duration,
                "path": track.path,
                "playlists": track.playlists_id
            });
        });
        res.json(responseAllTracks);
    });
});

app.get('/playlist-tracks/:playlist_id', function(req, res) {
    let listSelector = 'SELECT * FROM tracklist WHERE playlists_id = ' + req.params.playlist_id + ';';
    conn.query(listSelector, function(err, rows){
        if(err) {
            console.log(err.toString());
        }
        console.log("Data received from Db:\n");
        let responseTracklist = {"tracklist":[]};
        rows.forEach(function(track){
            responseAllTracks.push({
                "id": track.id,
                "title": track.title,
                "artist": track.artist,
                "duration": track.duration,
                "path": track.path,
                "playlists": track.playlists_id
            });
        });
        res.json(responseTracklist);
    });
});

app.listen(5000);
