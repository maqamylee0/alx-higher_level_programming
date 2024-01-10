#!/usr/bin/node
// concat files

// import fs
const fs = require('fs');

function concatFiles () {
  let content = '';
  const file1 = fs.readFileSync(process.argv[2], 'utf8');
  const file2 = fs.readFileSync(process.argv[3], 'utf8');
  content += file1 + file2;
  fs.writeFileSync(process.argv[4], content, 'utf8');
}
concatFiles();
