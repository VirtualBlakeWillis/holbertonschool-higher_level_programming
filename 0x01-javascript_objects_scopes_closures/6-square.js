#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    /* --- Original Solution ---
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
    */
    process.stdout.write((c.repeat(this.width) + '\n').repeat(this.width));
  }
}
module.exports = Square;
