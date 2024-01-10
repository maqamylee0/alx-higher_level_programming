#!/usr/bin/node
//import array and use map to compute new rray

const list1 = require('./100-data.js').list;
const list2 = [];

list1.map((element, index) => {
	list2[index] = element * index;;
});
console.log(list1);
console.log(list2);
