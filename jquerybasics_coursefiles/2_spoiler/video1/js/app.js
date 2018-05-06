//Hide spoiler on page load
$('.spoiler span').hide();
//When button is pressed, show the spoiler, hide the button
$('.spoiler button').click( () => {
  $('.spoiler span').show();
  $('.spoiler button').hide();
});
