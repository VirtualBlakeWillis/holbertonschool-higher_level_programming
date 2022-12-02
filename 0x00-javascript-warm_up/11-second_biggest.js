#!/usr/bin/node

const numArray = [];
if (isNaN(process.argv[2]) || isNaN(process.argv[3])) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    numArray.push(process.argv[i]);
  }
  numArray.sort(function (a, b) {
    return a - b;
  });
  console.log(numArray[numArray.length - 2]);
}
