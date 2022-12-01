#!/usr/bin/node
// Script to print first argument passed to it

const argv = process.argv;

if (argv[2]) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
