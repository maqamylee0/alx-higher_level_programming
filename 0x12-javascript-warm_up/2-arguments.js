#!/usr/bin/node

if (process.argv[2] == null) {
  console.log('No argument');
} else if (process.argv[3] == null) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
