#!/usr/bin/node
/*
 Defining Rectangle class
 Defining two attributes width and height
 If the number are negative or 0 the object is undefined
 Add method print
 Add methods print, rotate, double
*/
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
