// var dieRoll = Math.floor(Math.random() * 6) + 1;
// Simulates a dice roll
var inputLow = prompt('Give me a low number');
var userLowNumber = parseInt(inputLow);
var inputHigh = prompt('Give me a high number');
var userHighNumber = parseInt(inputHigh);
var difference = userHighNumber - userLowNumber
var randomNumber = Math.floor(Math.random() * difference) + userLowNumber;
var numberAnnouncement = randomNumber + ' is a number between ' + userLowNumber + ' and ' + userHighNumber + '.';

alert(numberAnnouncement);
