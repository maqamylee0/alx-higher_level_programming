class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const row = 'X'.repeat(this.width);
    const pattern = row + '\n';
    const result = pattern.repeat(this.height);
    console.log(result);
  }
}
module.exports = Rectangle;
