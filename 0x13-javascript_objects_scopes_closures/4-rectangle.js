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

  rotate () {
    this.temp = this.height;
    this.height = this.width;
    this.width = this.temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
