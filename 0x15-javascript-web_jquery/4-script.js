#!/usr/bin/node
/*
  Updates the text color
  to #FF0000 clicks change the color
*/
$(document).ready(function () {
  $('div#toggle_header').click(function () {
    $(".red").switchClass("red","green");
    $(".green").switchClass("green","red");
  });
});
