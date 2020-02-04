#!/usr/bin/node
/*
  Print the second more biggest
*/

let myArgc = 0;
let num = 0;
let num1 = 0;
let num2 = 0;

myArgc = process.argv.length;

if (myArgc <= 2 || myArgc === 3) {
  console.log(0);
} else {
  for (let i = 2; i < myArgc; i++) {
    num = parseInt(process.argv[i]);
    if (num > num1) {
      num2 = num1;
      num1 = process.argv[i];
    } else if (num > num2 && num !== num1) {
      num2 = num;
    }
  }
  console.log(num2);
}
