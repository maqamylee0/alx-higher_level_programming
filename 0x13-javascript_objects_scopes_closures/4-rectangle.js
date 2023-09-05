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
    const row = 'X'.repeat(this.width);
    const pattern = (row + '\n').repeat(this.height);
    console.log(pattern);
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
