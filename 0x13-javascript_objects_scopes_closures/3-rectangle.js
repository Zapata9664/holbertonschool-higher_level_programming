#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w == null || h == null) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let iteration = 0;
    const dr = 'X';
    const result = dr.repeat(this.width);
    for (iteration; iteration < this.height; iteration++) {
      console.log(result);
    }
  }
}

module.exports = Rectangle;
