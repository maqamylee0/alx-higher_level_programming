#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (this.isValidDimensions(width, height)) {
      this.width = width;
      this.height = height;
    }
  }

  isValidDimensions (width, height) {
    return width > 0 && height > 0;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
