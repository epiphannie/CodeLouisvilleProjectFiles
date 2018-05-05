var HTMLBadges = prompt('How many HTML badges do you have?');
var CSSBadges = prompt('How many CSS badges do you have?');
var totalBadges = parseInt(HTMLBadges) + parseInt(CSSBadges);
// parseInt returns the ingeer form of a string variable
// parseFloat does the same with decimal values
// Will work on strings with letters and non-number characters,
// if the number is at the beginning
alert('Wow you have ' + totalBadges + ' badges!');
