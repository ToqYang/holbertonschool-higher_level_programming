#!/usr/bin/node
/*
  Defining Square class
  inheritance from the Rectangle class
*/
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
