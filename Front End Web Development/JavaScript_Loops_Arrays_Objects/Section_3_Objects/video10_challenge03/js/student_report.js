var message = '';
var student;
var response;
var loop = true

function print(message) {
  var outputDiv = document.getElementById('output');
  outputDiv.innerHTML = message;
}

// for (var i = 0; i < students.length; i += 1) {
//   student = students[i];
//   message += '<h2>Student: ' + student.name + '</h2>';
//   message += '<p>Track: ' + student.track + '</p>';
//   message += '<p>Points: ' + student.points + '</p>';
//   message += '<p>Achievements: ' + student.achievements + '</p>';
// }


while (loop) {
  response = prompt("Type the name of a student to see records, or type 'quit' to quit").toLowerCase();
  if (response === null || response === 'quit') {
    break;
  }

  for (i=0; i<students.length; i+=1) {
    student = students[i];
    if (response !=== student.name.toLowerCase()) {
      continue;
    } else {
      message += '<h2>Student: ' + student.name + '</h2>';
      message += '<p>Track: ' + student.track + '</p>';
      message += '<p>Points: ' + student.points + '</p>';
      message += '<p>Achievements: ' + student.achievements + '</p>';
      loop = false;
      break;
      }
  }
}

print(message);
