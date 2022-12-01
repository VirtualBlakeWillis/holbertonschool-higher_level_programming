#!/usr/bin/node
// Print one of two statements, based on if argument passed can be an int
import('node:process');
const argv = process.argv;

const num = Math.floor(Number(argv[2]));

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number:', num);
}
