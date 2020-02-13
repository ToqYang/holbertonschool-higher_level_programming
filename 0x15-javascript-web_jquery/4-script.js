#!/usr/bin/node
/*
  Updates the text color
  to #FF0000 clicks change the color
*/
$(document).ready(function () {
  $('div#toggle_header').click(function () {
    if ($('header').hasClass('red')) {
      $("#div1").removeClass("red");
      $("#div1").addClass("green");
    } else if ($('header').hasClass('green')) {
      $("#div1").removeClass("green");
      $("#div1").addClass("red");
    } else if ($('header').is(':empty')) {
      $('header').toggleClass('red');
    }
  });
});