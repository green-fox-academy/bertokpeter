'use strict';

const express = require('express');
const app = express();

app.use('/assets', express.static('./assets'));
app.use(express.json());

app.get('/', function (req, res){
    res.sendFile(__dirname + '/foxplayer.html')
});

app.listen(5000);
