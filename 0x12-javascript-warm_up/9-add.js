#!/usr/bin/node
/*
  Print the addition of two numbers
*/
let myArgc = 0;
let num1 = 0;
let num2 = 0;

myArgc = process.argv.length;

num1 = parseInt(process.argv[2]);
num2 = parseInt(process.argv[3]);

if (myArgc <= 2) {
  console.log(num1);
} else if (myArgc === 3 || myArgc === 4) {
  if (isNaN(num1)) { console.log(num1); } else if (isNaN(num2)) {
    console.log(num2);
  } else {
    console.log(add(num1, num2));
  }
}

function add (a, b) {
  return a + b;
}
