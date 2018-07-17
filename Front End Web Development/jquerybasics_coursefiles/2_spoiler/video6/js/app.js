// Create the "Reveal Spoiler" button
const $button = $('<button>Reveal Spoiler</button>');

$('.spoiler').on('click', 'button', function(){
    //Show the spoiler text
    $('.spoiler span').show();
    //Hide the "Reveal Spoiler" button
    $('.spoiler button').hide();
})

//Append to web page
$('.spoiler').append($button);

//Hide the spoiler text
$('.spoiler span').hide();
// When the button is pressed
