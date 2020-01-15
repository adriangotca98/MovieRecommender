var express = require("express");
var bodyParser = require("body-parser");
var cors = require('cors')
var app = express();
var spawn = require("child_process").spawn;

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(cors())

let runPy = (query) => new Promise((resolve, reject) => {

    const { spawn } = require('child_process');
    const pyprog = spawn('python', ['./parse.py', query]);

    pyprog.stdout.on('data', function (data) {
        resolve(data);
    });

    pyprog.stderr.on('data', (data) => {
        reject(data);
    });
});

app.get('/', function (req, res) {
    res.sendfile("index.html");
});
app.post('/search', function (req, res) {
    let searchQuery = req.body.query;
    console.log(searchQuery);
    runPy().then(
        (rsp) => {
            res.end(rsp)
        },
        (err) => {
            res.end(err)
        }
    )
});
app.listen(3000, function () {
    console.log("Started on PORT 3000");
})