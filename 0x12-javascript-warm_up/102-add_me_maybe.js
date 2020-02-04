#!/usr/bin/node
/*
  Incremet the value about each called
*/
exports.addMeMaybe = function (x, theFunction) {
  let i = 0;
  for (i = 1; i <= x; ++i) {
  }
  theFunction(i);
};
