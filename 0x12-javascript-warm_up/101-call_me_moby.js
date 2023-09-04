#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
    for (let j = 0; j < x; j++) {
      theFunction();
    }
  };