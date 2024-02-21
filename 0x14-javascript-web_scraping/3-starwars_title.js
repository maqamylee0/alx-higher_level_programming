#!/usr/bin/node
/* fetch title of movie" */

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + id + '/', (err, response, body) => {
  if (err) console.log(err);
  else console.log(JSON.parse(body).title);
});
