#!/usr/bin/node
/*
  Convert base 10 to other string
*/
exports.converter = function (base) {
  function num (x) {
    return (parseInt(x, 10).toString(base));
  }
  return (num);
};
