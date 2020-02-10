#!/usr/bin/node
/*
  Reversed version of a list
*/
exports.esrever = function (list) {
  const mylist = [];
  for (let i = list.length - 1; i >= 0; i--) {
    mylist.push(list[i]);
  }
  return (mylist);
};
