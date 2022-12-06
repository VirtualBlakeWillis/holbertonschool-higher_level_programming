#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, 'utf8', (error, response, body) => {
  if (error) throw error;
  fs.writeFile(filePath, body, (err) => {
    if (err) throw error;
  });
});
