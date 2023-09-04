#!/usr/bin/node

function factorial (x) {
    if (isNaN(x)) {
      return 1;
    } else if (x <= 1) {
      return 1;
    } else {
      return x * factorial(x - 1);
    }
  }
  
  const args = process.argv.slice(2);
  const input = parseInt(args[0]);
  
  console.log(factorial(input));