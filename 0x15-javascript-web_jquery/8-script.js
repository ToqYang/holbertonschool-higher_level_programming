#!/usr/bin/node
/*
  fetches and lists all movies 
  title by using this URL: https://swapi.co/api/films/?format=json
*/
$(document).ready(function () {
  $.getJSON('https://swapi.co/api/people/5/?format=json', function (result) {
      let name = "<li>" + result.name + "<li>" 
      $('ul#list_movies').append(name);
    });
  });