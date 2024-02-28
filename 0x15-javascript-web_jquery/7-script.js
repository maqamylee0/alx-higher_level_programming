$(function () {
    const nameUrl = "https://swapi-api.hbtn.io/api/people/5/?format=json";
    $.get(nameUrl, function (data, status) {
      $("DIV#character").text(data.name);
    });
  });