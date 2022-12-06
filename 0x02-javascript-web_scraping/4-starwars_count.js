#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const wedgeAntilles = 'https://swapi-api.hbtn.io/api/people/18/';
let count = 0;

request.get(url, 'utf8', (error, response, body) => {
  if (error) throw error;
  const jsonData = JSON.parse(body);
  for (const i in jsonData.results) {
    if (jsonData.results[i].characters.indexOf(wedgeAntilles) > -1) {
      count++;
    }
  }
  console.log(count);
});
