let express = require('express');

let app = express();
express.json.type = "application/json"
app.use('/assets', express.static("./assets"));

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

app.listen(8080);