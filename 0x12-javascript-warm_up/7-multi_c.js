#!/usr/bin/node

if (parseInt(process.argv[2]) === isNaN || parseInt(process.argv[2]) == null) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < (parseInt(process.argv[2])); i++) {
    console.log('C is fun');
  }
}
