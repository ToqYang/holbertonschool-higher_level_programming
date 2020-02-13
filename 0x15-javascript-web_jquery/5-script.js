/*
  Write a Javascript script that adds a LI
*/
$(document).ready(function () {
  $('div#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
});
