#!/usr/bin/node
/*
 Defining Rectangle class
 Defining two attributes width and height
 If the number are negative or 0 the object is undefined
*/
module.exports = class Rectangle {
  constructor (w, h) {
    if ((h <= 0 || h === undefined) || (w <= 0 || w === undefined)) {

    } else {
      this.width = w;
      this.height = h;
    }
  }
};
