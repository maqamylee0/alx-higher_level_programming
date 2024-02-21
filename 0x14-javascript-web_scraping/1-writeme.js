#!/usr/bin/node
/* script that writes a string to a file */

const fs = require('fs');
const filename = process.argv[2];
const text = process.argv[3];
fs.writeFile(filename, text, 'utf-8', (err) => {
  if (err) console.log(err);
});
