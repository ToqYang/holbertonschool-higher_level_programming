#!/usr/bin/node
/*
   Print square about number
*/
let myArgc = 0;
myArgc = process.argv.length;
let num = 0;
num = parseInt(process.argv[2]);

if (myArgc <= 2 || isNaN(num)) {
  console.log('Missing size');
} else if (myArgc === 3) {
  for (let i = 0; i < num; ++i) {
    console.log('X'.repeat(num));
  }
}
