#!/usr/bin/node
// Script to notify via console if arguments are passed
import('node:process');
const av = process.argv;

if (av.length > 3) {
  console.log('Arguments found');
} else if (av.length === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
