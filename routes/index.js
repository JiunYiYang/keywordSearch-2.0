var express = require('express');
var router = express.Router();
var request = require('request');

var PythonShell = require('python-shell');

var options_m = {
    mode: 'text',
    pythonOptions: ['-u'],
    scriptPath: './../views'
}

var options_g = {
    mode: 'text',
    pythonOptions: ['-u'],
    scriptPath: './../views'
}

var mozPlanner;
var googletrends;

router.get('/', function(req, res, next) {
  
  var keywordQuery = req.query.keywords;
  var queryEncodeList = [];
  console.log(keywordQuery);
  if (req.query.keywords != null) {
    var getGoogleTrends = new PythonShell('trendsByRegion.py', options_g);
    var getMozKeywords = new PythonShell('mozKeyword.py', options_m);

    for (var i=0; i<=4; i++) {
      queryEncodeList.push(encodeURIComponent(keywordQuery[i]));
    }
    console.log(queryEncodeList);
    getGoogleTrends.send(keywordQuery);
    getMozKeywords.send(queryEncodeList);
    getGoogleTrends.on('message', function (message) {
      console.log(message);
      googletrends = message;
    });

    getMozKeywords.on('message', function (message) {
      console.log(message);
      mozPlanner = message;
      var googletrends_local = googletrends;
      if (googletrends_local != null) {
        res.render('index', {
          title: 'KeywordMetrics 2.0',
          result: mozPlanner,
          trends_data: googletrends_local,
          trends: ''
        });
      }
    });


    getGoogleTrends.end(function (err) {
      if (err){
        throw err;
      };
      console.log('finished');
    });

    getMozKeywords.end(function (err) {
      if (err){
        throw err;
      };
      console.log('finished');
    });
  } else {
    res.render('index', {
      title: 'KeywordMetrics 2.0',
      result: '',
      trends_data: '',
      trends: ''
    });
  }
});

module.exports = router;