/*
  Verify if the DOM is charged
  and after change the color
*/
document.addEventListener('DOMContentLoaded', function () {
  $('input#btn_translate').click(function () {
    let code = $('input#language_code').val();
    let url = 'https://fourtonfish.com/hellosalut/?lang=' + code;
    $.getJSON(url, function (result) {
      $('div#hello').text(result.hello);
    });
  });

  $(document).keypress(function (e) {
    if (e.which == 13) {
      let code = $('input#language_code').val();
      let url = 'https://fourtonfish.com/hellosalut/?lang=' + code;
      $.getJSON(url, function (result) {
        $('div#hello').text(result.hello);
      });
    }
  });
});
