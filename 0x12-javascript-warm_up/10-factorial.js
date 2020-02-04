#!/usr/bin/node
/*
  Print the factorial of a number
*/
function fact (x) {
  if (x === 0) {
    return 1;
  }
  return x * fact(x - 1);
}

let myArgc = 0;
let num = 0;

myArgc = process.argv.length;

num = parseInt(process.argv[2]);

if (myArgc <= 2) {
  console.log(1);
} else if (myArgc === 3) {
  if (isNaN(num)) {
    console.log(1);
  } else {
    console.log(fact(num));
  }
}
