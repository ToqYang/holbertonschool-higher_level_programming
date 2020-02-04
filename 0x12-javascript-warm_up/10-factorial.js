#!/usr/bin/node
/*
  Print the factorial of a number
*/
let myArgc = 0;
let num = 0;
let num2 = 2;
let fact = 0;

myArgc = process.argv.length;

num = parseInt(process.argv[2]);

if (myArgc <= 2) {
  console.log(1);
} else if (myArgc === 3) {
  if (isNaN(num)) {
    console.log(1);
  } else {
    fact = num;
    while (num2 > 1) {
      --num;
      num2 = num;
      fact = fact * num2;
    }
    console.log(fact);
  }
}
