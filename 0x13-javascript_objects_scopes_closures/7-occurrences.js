#!/usr/bin/node
/*
  Number of occurrences
*/
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) { ++count; }
  }

  return (count);
};
