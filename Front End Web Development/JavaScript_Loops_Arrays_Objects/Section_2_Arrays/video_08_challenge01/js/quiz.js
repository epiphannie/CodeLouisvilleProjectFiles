var questions = [
  ['What is my first name?', 'ann'],
  ['What is the current month?', 'april'],
  ['What month is my brithday in?', 'june'],
  ['I love you', 'i love you too']
]
var question;
var answer;
var correctAnswers = [];
var incorrectAnswers = [];
var correctNumber = 0;
var incorrectNumber = 0;
var correctMessage;
var incorrectMessage;

function print(message) {
  document.write(message);
}

for (i = 0; i < questions.length; i += 1) {
  question = questions[i][0];
  answer = prompt(question)
  answer = answer.toLowerCase();
  if (answer === questions[i][1]) {
    correctAnswers.push(question);
  } else {
      incorrectAnswers.push(question);
    }
}

if (correctAnswers.length == 0) {
  correctMessage = 'You got nothing right :('
} else {
  correctMessage = '<h2> You got ' + correctAnswers.length + ' correct answers to questions: </h2>' +
  correctAnswers.join('<br>');
}

if (incorrectAnswers.length == 0) {
  incorrectMessage = '<h2>Congratulations! You had zero incorrect answers</h2>'
} else {
  incorrectMessage = '<h2> You got ' + incorrectAnswers.length + ' incorrect answers to questions: </h2>' +
  incorrectAnswers.join('<br>');
}

print(correctMessage);
print(incorrectMessage);
