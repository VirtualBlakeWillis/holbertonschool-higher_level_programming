#!/usr/bin/node
// Write a script that prints two arguments passed to it, formatted "{} is {}"
import('node:process');
const argv = process.argv;

console.log('%s is %s', argv[2], argv[3]);
