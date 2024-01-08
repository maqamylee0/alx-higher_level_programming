#!/usr/bin/node
//convert arg1 to integer

const myVar = parseInt(process.argv[2]);

if (isNaN(myVar))
{
	console.log("Missing size");
}else
{	
	for (let i = 0; i < myVar; i++)
	{
		let row = "";
		for (let j = 0; j < myVar; j++)
		{
			row += "X";
		}
		console.log(row)
	}
}
