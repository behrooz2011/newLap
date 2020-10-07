var request = require("request");

var options = {
  method: 'GET',
  url: 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail',
  qs: {region: 'US', symbol: 'AAPL'},
  headers: {
    'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com',
    'x-rapidapi-key': 'e3dc5b0e9fmsh49a871c2beed174p192c1ajsnca8bc27bb9d9',
    useQueryString: true
  }
};

request(options, function (error, response, body) {
	if (error) throw new Error(error);

	console.log(body["financialData"]);
});