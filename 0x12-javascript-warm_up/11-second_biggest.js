#!/usr/bin/node
// find largest argument

function largest () {
  let i = 3;
  let max = process.argv[2];
  let max2 = 0;
  if (process.argv[2] == null || process.argv[3] == null) {
    max = 0;
    console.log(max);
  } else {
    while (process.argv[i] != null) {
      if (process.argv[i] > max) {
        max = process.argv[i];
        i++;
      }
    }
    console.log('max : ' + max);
    const maxArg = process.argv[2];
    i = 3;
    while (process.argv[i] !== null) {
      if (process.argv[i] == max) { continue; } else
        if (process.argv[i] > maxArg) { max2 = process.argv[i]; }
      i++;
    }
    console.log(max2);
  }
}
largest();
