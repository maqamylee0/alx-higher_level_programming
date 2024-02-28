'use strict';
$(() => {
  $('INPUT#btn_translate').click(() => {
    const translateUrl = 'https://fourtonfish.com';
    const code = $('INPUT#language_code').val();
    $.get(`${translateUrl}/hellosalut/?lang=${code}`, (data, status) => {
      $('DIV#hello').html(data.hello);
    });
  });
});