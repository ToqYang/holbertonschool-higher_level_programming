/*
  Updates the text color
  to #FF0000 clicks change the color
*/
$(document).ready(function () {
  $('div#toggle_header').click(function () {
    if ($('header').hasClass('red')) {
      $("header").removeClass("red");
      $("header").addClass("green");
    } else if ($('header').hasClass('green')) {
      $("header").removeClass("green");
      $("header").addClass("red");
    } else if ($('header').is(':empty')) {
      $("header").addClass("red");
    }
  });
});