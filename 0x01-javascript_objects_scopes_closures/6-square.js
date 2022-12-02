#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = undefined) {
    let x = 'X';
    if (c !== undefined) {
      x = c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(x.repeat(this.width));
    }
  }
}
module.exports = Square;
