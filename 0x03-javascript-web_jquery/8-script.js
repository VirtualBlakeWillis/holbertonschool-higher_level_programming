const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const list = $('UL#list_movies');
$.getJSON(url, function (data) {
  for (const movie of data.results) {
    list.append(`<li>${movie.title}</li>`);
  }
});
