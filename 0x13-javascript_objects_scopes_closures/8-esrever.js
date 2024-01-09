#!/usr/bin/node
//reversed version of a list

exports.esrever = function (list){
	let list2 = [];
	let j = 0;
	for (let i = list.length - 1; i > 0; i--){
		list2[j] = list[i];
		j++;
	}
	return list2;

}
