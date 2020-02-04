#!/usr/bin/node
/*
   Print the value passed
   of the first argument
*/
process.argv.forEach((val, index) => {
  if (index === 2) {
    console.log(val);
  }
});
