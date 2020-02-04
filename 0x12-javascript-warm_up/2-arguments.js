#!/usr/bin/node
// Arguments
const myArgv = process.argv.length;

if (myArgv <= 2) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
