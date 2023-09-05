#!/usr/bin/node

const data = require('./101-data');

const userIdsByOccurrence = {};

for (const userId in data.dict) {
  const occurrences = data.dict[userId];

  if (!userIdsByOccurrence[occurrences]) {
    userIdsByOccurrence[occurrences] = [];
  }

  userIdsByOccurrence[occurrences].push(userId);
}

console.log(userIdsByOccurrence);
