#!/usr/bin/node
/*
  Multiply the number of the list
  to the index
*/
const listo = require('./100-data').list;
console.log(listo);

let c = 0;

const mapone = listo.map(x => x * c++);

console.log(mapone);
