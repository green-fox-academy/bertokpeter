let express = require('express');

let app = express();

app.use('/assets', express.static("./assets"));

app.get('/', function(req,res) {
    res.sendFile(__dirname + '/index.html');
});

app.get('/doubling', function(req,res) {
    let response = {"received": req.query.input, "result": req.query.input*2}
    res.send(JSON.stringify(response));
});

app.listen(8080);