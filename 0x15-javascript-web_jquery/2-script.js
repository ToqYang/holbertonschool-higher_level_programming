/*
  Updates the text color
  to #FF0000 clicks on the tag DIV#red_header
*/
$(document).ready(function () {
  $('div#red_header').click(function () {
    $('div#red_header').css('color', '#FF0000');
  });
});
