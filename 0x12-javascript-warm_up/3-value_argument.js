#!/usr/bin/node
/*
   Print the value passed
   of the first argument
*/
let len = 0;
len = process.argv[2];
if (len) {
  console.log(len);
} else {
  console.log('No argument');
}
