#!/usr/bin/node
/*
  Updates the text color
  to #FF0000 clicks change the color
*/
$(document).ready(function () {
  $('div#toggle_header').click(function () {
    if ($('header'.hasClass('red'))) {
      $('header').toggleClass('green');
    } else if ($('header'.hasClass('green'))) {
      $('header').toggleClass('red');
    } else if ($('header').is(':empty')) {
      $('header').toggleClass('red');
    }
  });
});