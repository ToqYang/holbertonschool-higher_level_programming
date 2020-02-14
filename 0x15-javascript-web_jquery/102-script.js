/*
  Verify if the DOM is charged
  and after change the color
*/
document.addEventListener('DOMContentLoaded', function () {
  $('input#btn_translate').click(function () {
    const code = $('input#language_code').val();
    url = 'https://fourtonfish.com/hellosalut/?lang=' + code;
    $.getJSON(url, function (result) {
      $('div#hello').text(result.hello);
    });
  });
});
