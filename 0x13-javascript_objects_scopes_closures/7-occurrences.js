#!/usr/bin/node
// function to return number of occurences in a list

exports.nbOccurences = function (list, searchElement) {
  let nb = 0;
  list.forEach((element) => {
    if (element === searchElement) {
      nb += 1;
    }
  });
  return nb;
};
