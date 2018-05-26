var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
  res.render('signup', { 
    title: 'Kearch 2.0'
   });
});

module.exports = router;