#!/usr/bin/node
const {readFileSync, promises: fsPromises} = require('fs');

try {
  const contents = readFileSync(process.argv[2], 'utf-8', );
  console.log(contents);
} catch (err) {
  console.log(err);
}