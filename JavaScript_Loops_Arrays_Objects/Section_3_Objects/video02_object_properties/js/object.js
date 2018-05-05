var person = {
  name : 'Ann',
  country : 'US',
  age : 30,
  treehouseStudent : true,
  skills : ['JavaScript', 'HTML', 'CSS']
};

function print(message) {
  var div = document.getElementById('output');
  div.innerHTML = message;
}

var message = '<p>Hello my name is ' + person.name + '.</p>';
message += '<p>I live in the ' + person.country + '.</p>';
person.name= 'David';
message += '<p>But I wish my name were ' + person.name + '.</p>';
person.age += 1;
message += '<p>My age is now ' + person.age + '.</p>';
message += '<p>I have ' + person.skills.length + ' skills: </p>';
message += '<p>' + person.skills.join(', ') + '</p>';
print(message);
