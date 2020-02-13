#!/usr/bin/node
/*
  Fetches and replaces the
  name of this URL: https://swapi.co/api/people/5/?format=json
*/
$(document).ready(function () {
    $.getJSON('https://swapi.co/api/people/5/?format=json', function (result) {
        $('div#character').text(result.name);
      });
    });
