/*
  fetches and lists all movies
  title by using this URL: https://swapi.co/api/films/?format=json
*/
$(document).ready(function () {
  $.getJSON('https://swapi.co/api/films/?format=json', function (result) {
    for (const mov of result.results) {
      let movie = "<li>" + mov.title + "</li>"
      $('ul#list_movies').append(movie);
    }
  });
});
