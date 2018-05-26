var express = require('express');
var path = require('path');
// var favicon = require('serve-favicon');
var morgan = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');

// i18next module
var i18n = require('i18next');
var i18nFsBackend = require('i18next-node-fs-backend');
var i18nMiddleware = require('i18next-express-middleware');

// firebase setup
var admin = require('firebase-admin');
var serviceAccount = require('./kearch-official-firebase-adminsdk-z3y78-e45c9f7092.json');
var firebaseAdmin = admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    databaseURL: 'https://kearch-official.firebaseio.com'
})

var session = require('express-session');

var routes = require('./routes/index');
var output = require('./routes/output');
var country = require('./routes/country');
var login = require('./routes/login');
var signup = require('./routes/signup');

var app = express();

// i18next setup
i18n.use(i18nMiddleware.LanguageDetector)
    .use(i18nFsBackend)
    .init({
      fallbackLng: "en",
      backend: {
        loadPath: "locales/{{lng}}/translation.json",
      }
    });

app.use(i18nMiddleware.handle(i18n, {

}));

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(morgan('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/kearch', routes);
app.use('/output', output);
app.use('/country', country);
app.use('/', login);
app.use('/signup', signup);


// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
