/*
  Updates the text of the HTML tag HEADER to “New Header!!!”
*/
$(document).ready(function () {
  $('div#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
