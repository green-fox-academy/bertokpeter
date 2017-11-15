'use strict';

const express = require('express');
const app = express();

app.use('/assets', express.static('./assets'));
app.use('/tracks', express.static('./tracks'));
app.use(express.json());

app.get('/', function (req, res){
    res.sendFile(__dirname + '/foxplayer.html')
});

let playlists = {
    playlists:[
        { "id": 1, "title": "All tracks", "system": 1},
        { "id": 2, "title": "Favorites", "system": 1},
        { "id": 3, "title": "Music for programming", "system": 0},
        { "id": 4, "title": "Driving", "system": 0},
        { "id": 5, "title": "Fox house", "system": 0},
    ]
};

let tracklist = {
    tracklist:[
        { "id": 1, "title": "Warped", "artist": "Mutato Muzika", "duration": 80, "path": "tracks/01_-_Crash_Bandicoot_3_Warped.mp3", "playlists": []},
        { "id": 2, "title": "Toad Village", "artist": "Mutato Muzika", "duration": 108, "path": "tracks/02_-_Toad_Village.mp3", "playlists": ["2"]}
    ]
}

app.get('/playlists', function(req, res) {
    res.json(playlists);
});

app.get('/playlist-tracks', function(req, res) {
    res.json(tracklist);
});

app.get('/playlist-tracks/:playlist_id', function(req, res) {
    let responseTrackList = tracklist.tracklist.filter(function(element){
        return element.playlists.includes(req.params.playlist_id);
    });
    let responseJSON = {
        tracklist: responseTrackList
    }
    res.json(responseJSON);
});

app.listen(5000);
