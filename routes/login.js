var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
  res.render('login', { 
    title: 'Kearch 2.0'
   });
});

module.exports = router;