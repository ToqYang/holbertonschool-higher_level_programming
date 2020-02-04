#!/usr/bin/node
/*
   Love to C
*/
let myArgc = 0;
myArgc = process.argv.length;
let num = 0;
num = parseInt(process.argv[2]);

if (myArgc <= 2) {
  console.log('Missing number of occurrences');
} else if (myArgc === 3) {
  for (let i = 0; i < num; ++i) {
    console.log('C is fun');
  }
}
