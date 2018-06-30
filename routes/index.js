var express = require('express');
var router = express.Router();
var request = require('request');
var logging = require('logging');
var async = require('async');

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
    for (var i=0; i<=4; i++) {
      queryEncodeList.push(encodeURIComponent(keywordQuery[i]));
    }
    console.log(queryEncodeList);

    function sendPythonShell1(queryEncodeList) {
      return new Promise(function (resolve, reject) {
        var getGoogleTrends = new PythonShell('trendsByRegion.py', options_g);
        getGoogleTrends.send(queryEncodeList);
        getGoogleTrends.on('message', function (message) {
          resolve(message);
        });
        getGoogleTrends.end(function (err) {
          if (err){
            reject(err);
            throw err;
          }
        });
      });
    }

    function sendPythonShell2(queryEncodeList) {
      return new Promise(function (resolve, reject) {
        var getMozKeywords = new PythonShell('mozKeyword.py', options_m);
        getMozKeywords.send(queryEncodeList);
        getMozKeywords.on('message', function (message) {
          resolve(message);
        });
        getMozKeywords.end(function (err) {
          if (err){
            reject(err);
            throw err;
          }
        });
      });
    }

    async.parallel([

      function(callback) {
        console.log('parallel1 ready');
        sendPythonShell1(queryEncodeList)
          .then(function(result) {
            console.log(result);
            callback(null, result);
          })
          .catch(function(err) {
            console.error(err);
          });
      },
      function(callback) {
        console.log('parallel2 ready');
        sendPythonShell2(queryEncodeList)
          .then(function(result) {
            console.log(result);
            callback(null, result);
          })
          .catch(function(err) {
            console.error(err);
          });
      }
    ], (err, results) => {
      res.render('index', {
        title: 'Search - Kearch 2.0',
        result: results[1],
        trends_data: results[0],
        trends: ''
      })
    });

  } else {
    res.render('index', {
      title: 'Search - Kearch 2.0',
      result: '',
      trends_data: '',
      trends: ''
    });
  }

});

module.exports = router;