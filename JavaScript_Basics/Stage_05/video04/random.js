function getRandomNumber( upper ) {
  var randomNumber = Math.floor( Math.random() * upper ) + 1;
  return randomNumber;
}

// console.log( getRandomNumber(6) );
// console.log( getRandomNumber(100) );
// console.log( getRandomNumber(10000) );

function getArea(length, width, unit ) {
  var area = width * length;
  // Always use the var keyword inside your function
  return area + " " + unit;
}

console.log( getArea(10, 20, "sq ft") );
