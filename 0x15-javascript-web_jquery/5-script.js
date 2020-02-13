#!/usr/bin/node
/*
  Write a Javascript script that adds a LI
*/
$(document).ready(function () {
  $('div#red_header').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
});
