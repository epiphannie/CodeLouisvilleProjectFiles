var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function () {
  if(xhr.readyState === 4 && xhr.status === 200) {
    var employees = JSON.parse(xhr.responseText);
    var statusHTML = '<ul class="bulleted">';
    for (var i=0; i<employees.length; i += 1) {
      if (employees[i].inoffice === true) {
        statusHTML += '<li class="in">';
      } else {
        statusHTML += '<li class="out">';
      }
      statusHTML += employees[i].name;
      statusHTML += '</li>';
    }
    statusHTML += '</ul>';
    document.getElementById('employeeList').innerHTML = statusHTML;
  }
};
xhr.open('GET', '../data/employees.json');
xhr.send();


var xhrRoom = new XMLHttpRequest();
xhrRoom.onreadystatechange = function () {
  if(xhrRoom.readyState === 4 && xhrRoom.status === 200) {
    var rooms = JSON.parse(xhrRoom.responseText);
    var roomsHTML = '<ul class="rooms">';
    for (var i=0; i<rooms.length; i += 1) {
      if (rooms[i].available === true) {
        roomsHTML += '<li class="empty">';
      } else {
        roomsHTML += '<li class="full">';
      }
      roomsHTML += room[i].room;
      roomsHTML += '</li>';
    }
    roomsHTML += '</ul>';
    document.getElementById('roomList').innerHTML = roomsHTML;
  }
};
xhrRoom.open('GET', '../data/rooms.json');
xhrRoom.send();
