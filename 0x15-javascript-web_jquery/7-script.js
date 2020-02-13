#!/usr/bin/node
/*
  Fetches and replaces the
  name of this URL: https://swapi.co/api/people/5/?format=json
*/
$(document).ready(function () {
  $('button').click(function () {
    $.getJSON('https://swapi.co/api/people/5/?format=json', function (result) {
      $.each(result, function (key, value) {
        if (key === 'name') {
          $('div#character').append(value + ' ');
        }
      });
    });
  });
});
