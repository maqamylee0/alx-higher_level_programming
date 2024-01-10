#!/usr/bin/node
//concat files

//import fs
const fs = require("fs");

function concatFiles(){
	let content = "";
	let file1 = fs.readFileSync(process.argv[2], 'utf8');
	let file2 = fs.readFileSync(process.argv[3], 'utf8');
	content += file1 + '\n' + file2;
	fs.writeFileSync(process.argv[3], content, 'utf8')
}
concatFiles();
