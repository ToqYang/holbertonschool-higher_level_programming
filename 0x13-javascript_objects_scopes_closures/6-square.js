#!/usr/bin/node
/*
  Defining Square class
  inheritance from the Rectangle class
  Add function to print characters
*/
const SquareUno = require('./5-square');

module.exports = class Square extends SquareUno {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) { console.log(c.repeat(this.width)); }
  }
};
