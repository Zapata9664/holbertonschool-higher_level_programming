#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let iterator = 0;
    if (c == null) {
      this.print();
    } else {
      for (iterator; iterator < this.width; iterator++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
