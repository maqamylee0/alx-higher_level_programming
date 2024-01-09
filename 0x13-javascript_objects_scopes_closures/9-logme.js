#!/usr/bin/node
//logging using a var
var logged = 0;
exports.logMe = function (item){
	console.log(logged + ": " +item);
	logged++;
}
