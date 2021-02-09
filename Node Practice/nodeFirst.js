// var http = require('http');

// http.createServer(function (req, res) {

//   res.writeHead(200, {'Content-Type': 'text/html'});
//   res.end('Hello World!');
 
// }).listen(3000);
////^^^^^^^^^^^^^^^^^^^^^^^^^^^^ number 2 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
// var http = require('http');
// var dt = require('./module1');

// http.createServer(function (req, res) {
//   res.writeHead(200, {'Content-Type': 'text/html'});
//   res.write("The date and time are currently: " + dt.myDateTime());
//   res.end();    
// }).listen(8080);
//######################################## Query String ###############################
// var http = require('http');
// http.createServer(function (req, res) {
//   res.writeHead(200, {'Content-Type': 'text/html'});
//   res.write(req.url);
//   res.write(req);
//   res.end();
// }).listen(8080);

// ############################# Split Query Strinng ################################
var http = require('http');
var url = require('url');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  /*Use the url module to turn the querystring into an object:*/
  var q = url.parse(req.url, true).query;
  /*Return the year and month from the query object:*/
  var txt = q.year + " " + q.month;
  res.end(txt);
}).listen(8080);
console.log("listening ...")