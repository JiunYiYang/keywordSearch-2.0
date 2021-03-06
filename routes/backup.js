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

      getGoogleTrends.send(queryEncodeList);
      getMozKeywords.send(queryEncodeList);
      console.log('sent');

      getGoogleTrends.on('message', function (message) {
        console.log(message);
        googletrends = message;
      });

      getGoogleTrends.end(function (err) {
        if (err){
          throw err;
        };
        console.log('finished');
        
        var googletrends_local = googletrends;
        if (googletrends_local != null) {
          res.render('index', {
            title: 'Search - Kearch 2.0',
            result: mozPlanner,
            trends_data: googletrends_local,
            trends: ''
          });
        }
      });

      getMozKeywords.on('message', function (message) {
        console.log(message);
        mozPlanner = message;
      });

      getMozKeywords.end(function (err) {
        if (err){
          throw err;
        };
        console.log('finished');
      });
    } else {
      res.render('index', {
        title: 'Search - Kearch 2.0',
        result: '',
        trends_data: '',
        trends: ''
      });
    }