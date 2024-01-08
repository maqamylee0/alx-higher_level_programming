#!/usr/bin/node
//script to print arguments

let myArg = 2;

if (process.argv[2] == null)
{	
	console.log("No argument");
}else
{
	while(process.argv[myArg] != null)
	{
		console.log(process.argv[myArg]);
		myArg++;
	}
}
