/* Quiz App
Ask 5 qwestions
Track # of correct answer
Report the # of answers to the participant
Rate them gold/silver/bronze/no crowm */

var correctAnswers = 0;

var questionOne = prompt( 'Question 1: What is the best color?' );
if ( questionOne.toUpperCase() === 'YELLOW' ) {
  correctAnswers +=1;
}

var questionTwo = prompt( 'Question 2: Who is the best husband?' );
if ( questionTwo.toUpperCase() === 'DAVID' ) {
  correctAnswers +=1;
}

var questionThree = prompt( 'Question 3: Where is the comfiest place?' );
if ( questionThree.toUpperCase() === 'BED' ) {
  correctAnswers +=1;
}

var questionFour = prompt( 'Question 4: What is the tastiest food?' );
if ( questionFour.toUpperCase() === 'CHEESE' ) {
  correctAnswers +=1;
}

var questionFive = prompt( 'Question 5: Where is the best beach?' ) ;
if ( questionFive.toUpperCase() === 'TURKS AND CAICOS' ) {
  correctAnswers +=1;
}

var message = 'You have gotten ' + correctAnswers + ' correct answers and earned ';

if ( correctAnswers === 5 ) {
  message += 'a gold crown!!';
} else if ( correctAnswers === 4 || correctAnswers === 3 ) {
  message += 'a silver crown!!' ;
} else if ( correctAnswers === 2 || correctAnswers === 1 ) {
  message += 'a bronze crown!!';
} else {
  message += 'no reward.  :(';
}

alert (message);
