#!/usr/bin/node
/* print status code of get request */

const request = require('request');
const url = process.argv[2];

request(url, (err, response) => {
  if (err) console.log(err);
  else console.log(response.statusCode);
});
