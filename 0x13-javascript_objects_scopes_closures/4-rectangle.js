#!/usr/bin/node
//rectangle class

class Rectangle{

	constructor(w,h){
		if (w > 1 && h > 1){
			this.width = w;
			this.height = h;
		}
	}
	//print rectangle
	print(){
		for (let i = 0; i < this.height; i++){
			let row = "";
			for (let j = 0; j < this.width; j++){
				row += "X";
			}
			console.log(row);
		}
	}
	// rotate rectangle
	rotate(){
		let h = this.height;
		this.height = this.width;
		this.width = h;
	}
	//double sides
	double(){
		this.height *= 2;
		this.width *= 2;
	}
}
module.exports = Rectangle;
