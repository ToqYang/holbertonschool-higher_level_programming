/*
  Verify if the DOM is charged
  and after change the color
*/
document.addEventListener('DOMContentLoaded', function () {
  $('div#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });

  $('div#remove_item').click(function () {
    $('li').last().remove();
  });

  $('div#clear_list').click(function () {
    $('li').remove();
  });
});
