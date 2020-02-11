#!/usr/bin/node
/*
  Read two files and
  concatenate the files
  and write a file
*/
const files = require('fs');

const text1 = files.readFileSync(process.argv[2], 'utf8');
const text2 = files.readFileSync(process.argv[3], 'utf8');

files.writeFileSync(process.argv[4], (text1 + text2));
