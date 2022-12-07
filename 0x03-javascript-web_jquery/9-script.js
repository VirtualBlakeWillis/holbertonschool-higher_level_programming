
$.ajax({
  type: 'GET',
  url: 'https://stefanbohacek.com/hellosalut/?lang=fr',
  success: function (data) {
    $('DIV#hello').text(data.hello);

  }
});
