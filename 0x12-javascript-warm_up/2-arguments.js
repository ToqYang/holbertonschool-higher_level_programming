#!/usr/bin/node
// Arguments
let myArgv = 0;
myArgv = process.argv.length;
if (myArgv <= 2) {
  console.log('No argument');
} else if (myArgv === 3) {
  console.log('Arguments found');
} else {
  console.log('Arguments found');
}
