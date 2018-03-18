var express = require('express');
var router = express.Router();
var vd = require('../videodata.json');
// var index = require('./index');
// var casper = require('casper').create();
// var keywords = 'influencer';

/* GET home page. */

// var PythonShell = require('python-shell');

// var options = {
//     mode: 'text',
//     pythonOptions: ['-u'],
//     scriptPath: './../views',
// };

// var getUberSuggest = new PythonShell('crawl.py', options);
// console.log(index.keywordsGlobal);
// getUberSuggest.send(index.keywordsGlobal);

// getUberSuggest.on('message', function (message) {
//   console.log(message);
//   router.get('/', function(req, res) {
//     res.render('output', {
//       title: 'Express',
//       videodata: vd,
//       message: message
//     });
//   });
// });

// getUberSuggest.end(function (err) {
//     if (err){
//         throw err;
//     };

//     console.log('finished');
// });


// casper.start('https://ubersuggest.io/');

// casper.then(function() {
//   this.sendKeys('#keywordBox', keywords);
//   this.click('#suggest-button');
// });

// casper.waitUntilVisible('span td', function() {
//   var results = this.getElementsAttribute('.dropdown-toggle span');
// });

// casper.run(function() {

// });

// module.exports = router;


router.get('/', function(req, res, next) {
  res.render('output', { 
    title: 'Express',
    videodata: vd
   });
});

module.exports = router;
