#!/usr/bin/node

let argsNumber = 0;

exports.logMe = function (item) {
  console.log(`${argsNumber}: ${item}`);
  argsNumber++;
};
