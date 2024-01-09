#!/usr/bin/node
//square class

//import rectangle class
const Square = require('./5-square');
class Square1 extends Square{
	constructor(size){
		super(size);
	}
	charPrint(c){
		if (c === undefined){
			c = 'X';
		}
		for (let i = 0; i < this.height; i++){
			let row = "";
			for (let j = 0; j < this.width; j++){
				row += c;
			}
			console.log(row);
		}
	}

}
module.exports = Square1;
