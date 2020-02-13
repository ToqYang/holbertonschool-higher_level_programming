#!/usr/bin/node
/*
  Updates the text color
  to #FF0000 with .red class
*/
$(document).ready(function () {
  $('div#red_header').click(function () {
    $('header').addClass('red');
  });
});
