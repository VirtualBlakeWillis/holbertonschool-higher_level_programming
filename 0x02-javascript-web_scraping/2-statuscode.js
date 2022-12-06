#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], function (err, body) {
  if (err) throw err;
  console.log('code: ' + body.statusCode);
});
