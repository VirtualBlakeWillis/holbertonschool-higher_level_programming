#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const output = {};
request.get(url, 'utf8', (error, response, body) => {
  if (error) throw error;
  const jsonData = JSON.parse(body);
  for (const item of jsonData) {
    if (item.completed) {
      if (output[item.userId]) {
        output[item.userId] = output[item.userId] + 1;
      } else {
        output[item.userId] = 1;
      }
    }
  }
  console.log(output);
});
