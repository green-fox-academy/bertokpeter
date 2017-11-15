'use strict';

const express = require('express');
const app = express();

app.use('/assets', express.static('./assets'));
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

app.get('/playlists', function(req, res) {
    res.json(playlists);
});

app.listen(5000);
