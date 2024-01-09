#!/usr/bin/node
//convert to base b

exports.converter = function (base){
	const converter = (number) => {
		let c, r;
		c = Math.floor(number / base);
		r = number % base;
		if (c == "0")
			return r.toString();
		else
			return c.toString() + r.toString();
	}
	return converter;
}
