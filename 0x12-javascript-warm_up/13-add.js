#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const args = process.argv.slice(2);

if (args.length === 2) {
  const a = parseInt(args[0]);
  const b = parseInt(args[1]);

  if (!isNaN(a) && !isNaN(b)) {
    // check if a and b are numbers
    const result = add(a, b);
    console.log(result);
  } else {
    console.log(NaN);
  }
} else {
  console.log(NaN);
}
