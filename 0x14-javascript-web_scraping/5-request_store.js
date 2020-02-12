#!/usr/bin/node
/*
  Gets the contents of a webpage
  and stores it in a file
*/
const request = require('request');
const fs = require('fs');

const urlName = process.argv[2];
const nameFile = process.argv[3];

request(urlName, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  // Contain name of the file
  fs.writeFile(nameFile, body, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
