#!/usr/bin/node
/*
  Incremet the value about each called
*/
exports.addMeMaybe = function (x, theFunction) {
  x = x + 1;
  theFunction(x);
};
