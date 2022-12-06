#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(url, 'utf8', (error, response, body) => {
  if (error) console.log(error);
  else {
    const jsonData = JSON.parse(body);
    console.log(jsonData.title);
  }
});
