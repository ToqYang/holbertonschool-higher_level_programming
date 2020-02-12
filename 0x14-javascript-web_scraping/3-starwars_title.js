#!/usr/bin/node
/*
  Prints the title of a Star Wars
  based in the id
*/
const request = require('request');
let movtitle = 'http://swapi.co/api/films/';
movtitle = movtitle.concat(process.argv[2]);

request(movtitle, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
