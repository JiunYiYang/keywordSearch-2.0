var express = require('express');
var router = express.Router();
var vd = require('../videodata.json');

router.get('/', function(req, res, next) {
  res.render('output', { 
    title: 'Express',
    videodata: vd
   });
});

module.exports = router;
