function randomNumber (upper, lower) {
return Math.floor(Math.random() * (upper - lower + 1)) + lower;
}

alert(randomNumber(100, 5));
