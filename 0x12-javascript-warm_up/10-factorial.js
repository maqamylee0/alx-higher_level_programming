#!/usr/bin/node
// convert arg1 to integer

const myVar = parseInt(process.argv[2]);
let fact = 1;
function factorial (myVar) {
  if (isNaN(myVar)) {
    console.log(fact);
  } else {
    while (myVar > 1) {
      fact = fact * myVar;
      myVar = myVar - 1;
    }
  }
  console.log(fact);
}
factorial(myVar);
