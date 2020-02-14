/*
  Add listener api to translate
*/
document.addEventListener('DOMContentLoaded', function () {
  $('input#btn_translate').click(function () {
    let code = $('input#language_code').val();
    let url = 'https://fourtonfish.com/hellosalut/?lang=' + code;
    $.getJSON(url, function (result) {
      $('div#hello').text(result.hello);
    });
  });
});
