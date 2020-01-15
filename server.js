var express = require("express");
var bodyParser = require("body-parser");
var cors = require('cors')
var app = express();
var { PythonShell } = require('python-shell');

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(cors())

let runPy = (query) => new Promise((resolve, reject) => {
    let options = {
        mode: 'text',
        pythonPath: '/Library/Frameworks/Python.framework/Versions/3.8/bin/python3',
        pythonOptions: ['-u'],
        scriptPath: './',
        args: [query]
    };

    PythonShell.run('./parse.py', options, function (err, results) {
        if (err) {
            reject(err.toString());
        }
        resolve(results ? results.toString() : null);
    });
});

app.get('/', function (req, res) {
    res.sendfile("index.html");
});
app.post('/search', function (req, res) {
    let searchQuery = req.body.query;
    runPy(searchQuery).then(
        (rsp) => {
            res.end(rsp)
        },
        (err) => {
            res.status(400).end(err);
        }
    )
});
app.listen(3000, function () {
    console.log("Started on PORT 3000");
})