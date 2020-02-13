#!/usr/bin/node
/*
  Updates the text color
  to #FF0000 clicks change the color
*/
$(document).ready(function () {
  $('div#toggle_header').click(function () {
    if ($('header'.hasClass('red'))) {
      $('div#toggle_header').toggleClass('green');
    } else if ($('header'.hasClass('green'))) {
      $('div#toggle_header').toggleClass('red');
    } else if ($('header').is(':empty')) {
      $('div#toggle_header').toggleClass('red');
    }
  });
});
