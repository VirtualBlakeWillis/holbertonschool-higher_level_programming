#!/usr/bin/node
const { readFileSync } = require('fs');

try {
  const contents = readFileSync(process.argv[2], 'utf-8');
  console.log(contents);
} catch (err) {
  console.log(JSON.stringify(err));
}
