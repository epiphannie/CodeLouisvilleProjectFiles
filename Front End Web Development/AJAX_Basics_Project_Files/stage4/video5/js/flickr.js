$(document).ready(function () {
  $('button').click(function () {
    $(this).addClass("selected");
    $("button").removeClass("selected");
    var flickerAPI = "http://api.flickr.com/services/feeds/photos_public.gne?jsoncallback=?";
    var animal = $(this).text();
    var flickrOptions = {
      tags: animal,
      format: "json"
    };
    function displayPhotos(data) {
      
    };
    $.getJSON(flickrAPI, flickrOptions, displayPhotos);

  }); //end click
}); // end ready
