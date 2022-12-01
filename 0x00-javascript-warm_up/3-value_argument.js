#!/usr/bin/node
// Script to print first argument passed to it
import('node:process');
const argv = process.argv;

if (argv.length >= 3) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
