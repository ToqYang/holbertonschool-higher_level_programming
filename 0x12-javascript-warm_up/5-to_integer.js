#!/usr/bin/node
/*
   Arguments used with length
*/
let myArgv = 0;
myArgv = process.argv.length;

let num = 0;
num = parseInt(process.argv[2]);

if (myArgv <= 2) {
  console.log('Not a number');
} else if (myArgv === 3) {
  if (Number.isInteger(num)) {
    console.log('My number: ' + num);
  } else {
    console.log('Not a number');
  }
}
