#!/usr/bin/node
/*
   Print the value passed
   of the first argument
*/
let myArgc = 0;
myArgc = process.argv.length;

let myArgv = 'Hello';
myArgv = process.argv;

if (myArgv <= 2) {
  console.log('No argument');
} else if (myArgc === 3) {
  console.log(myArgv[2]);
}
