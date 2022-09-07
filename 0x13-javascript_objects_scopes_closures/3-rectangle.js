#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let column = '';
      for (let j = 0; j < this.width; j++) {
        column += 'X';
      }
      console.log(column);
    }
  }
}

module.exports = Rectangle;
