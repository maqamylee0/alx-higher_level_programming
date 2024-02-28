'use strict';
$(() => {
  const translated = () => {
    const translatedUrl = 'https://fourtonfish.com';
    const code = $('INPUT#language_code').val();

    $.get(`${translatedUrl}/hellosalut/?lang=${code}`, (data, status) => {
      $('DIV#hello').html(data.hello);
    });
  };

  $('INPUT#btn_translate').click(translated);
  $('INPUT#language_code').keydown((ev) => {
    if (ev.key === 'Enter') translated();
  });
});