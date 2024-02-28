$(function () {
    const nameUrl = "https://swapi-api.hbtn.io/api/films/?format=json";
    $.get(nameUrl, function (data) {
      const titles = data.results;
      for (let i = 0; i < titles.length; i++) {
        $("UL#list_movies").append("<li>" + titles[i].title + "</li>");
      }
    });
  });