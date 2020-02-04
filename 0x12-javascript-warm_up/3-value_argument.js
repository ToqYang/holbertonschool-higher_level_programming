#!/usr/bin/node
/*
   Print the value passed
   of the first argument
*/
let idx = 0;
let value = 'Holberton';
process.argv.forEach((val, index) => {
  if (index === 2) {
    value = val;
  }
  ++idx;
});

if (idx === 3) {
  console.log(value);
} else {
  console.log('No argument');
}
