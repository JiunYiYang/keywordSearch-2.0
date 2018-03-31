var express = require('express');
var router = express.Router();
var request = require('request');
var url = require('url');
var querystring = require('querystring');

var PythonShell = require('python-shell');

var options_q = {
    mode: 'text',
    pythonOptions: ['-u'],
    scriptPath: './../views'
}

var quickTrends;

router.get('/', function(req, res, next) {

    // var parseUrl = url.parse(req);
    // var parseQs = querystring.parse(parseUrl.query);
    // // parseQs = { keyword: 'cat', country: 'US' }
    var keyword = req.query.keyword;
    var country = req.query.country;
    var parseQs = [];
    parseQs.push({
        keyword: keyword,
        country: country
    });
    console.log(parseQs[0]);

    // encode url params
    

    // new a PythonShell if params exists
    if (parseQs) {
        var getQuickTrends = new PythonShell('quickTrends.py', options_q);
        getQuickTrends.send(JSON.stringify(parseQs[0]));
        getQuickTrends.on('message', function(message) {
            console.log(message);
            quickTrends = message;
            if (quickTrends) {
                res.render('country', {
                    title: 'KeywordMetrics 2.0',
                    trendsData: quickTrends
                });
            }
        });
    } else {
        res.render('country', { 
            title: 'KeywordMetrics 2.0',
            trendsData: ''
        });
    }
});

module.exports = router;
