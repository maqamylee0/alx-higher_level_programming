#!/usr/bin/node
// use a dict

const dict1 = require('./101-data.js').dict;
const dict2 = {};

const uniqValues = [...new Set(Object.values(dict1))];

for (let i = 0; i < Object.values(dict1).length; i++) {
  const nwList = [];
  Object.entries(dict1).forEach(([key, value]) => {
    if (value === uniqValues[i]) {
      nwList.push(key);
      dict2[uniqValues[i]] = nwList;
    }
  });
}
console.log(dict2);
