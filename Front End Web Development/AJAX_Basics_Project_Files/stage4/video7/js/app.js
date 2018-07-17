$(document).ready(function() {

  $('form').submit( function (evt) {
    evt.preventDefault();
    var request = $('#search').val();
    var flickerAPI = "http://api.flickr.com/services/feeds/photos_public.gne?jsoncallback=?";
    var flickrOptions = {
      tags: request,
      format: "json"
    };
    function displayPhotos(data) {
      var photoHTML = '<ul>';
      $.each(data.items,function(i,photo) {
        photoHTML += '<li class="grid-25 tablet-grid-50">';
        photoHTML += '<a href="' + photo.link + '" class="image">';
        photoHTML += '<img src="' + photo.media.m + '"></a></li>';
      }); // end each
      photoHTML += '</ul>';
      $('#photos').html(photoHTML);
    }
    $.getJSON(flickerAPI, flickrOptions, displayPhotos);
  }); //end submit


}); // end ready

//replace button click event with form submit event
//respond to submit event
//elect the form, add adubmit method, which will run the programming
//stop the form from submitting
//retrieve the value in the input field. Select th
