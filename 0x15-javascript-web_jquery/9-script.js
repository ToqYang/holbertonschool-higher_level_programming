#!/usr/bin/node
/*
  Write a Javascript script that fetches from 
  https://fourtonfish.com/hellosalut/?lang=fr and 
  displays the value of hello from that fetch in the HTML’s tag DIV#hello.
*/
$(document).ready(function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (result) {
      $('div#hello').text(result.hello);
    });
});