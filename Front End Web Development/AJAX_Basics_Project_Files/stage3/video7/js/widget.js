$(document).ready(function () {
  console.log(1);
  $.getJSON('data/employees.json', function (data) {
    var statusHTML = '<ul class="bulleted">';
    $.each(data,function (index, employee) {
      if (employee.inoffice === true) {
        statusHTML +='<li class="in">';
      } else {
        statusHTML +='<li class="out">';
      }
      statusHTML += employee.name + '</li>';
    });
    statusHTML += '</ul>';
    $('#employeeList').html(statusHTML)
  }); // end getJSON
}); // end ready


$(document).ready(function () {
  console.log(2);
  $.getJSON('data/rooms.json', function (data) {
    var roomsHTML = '<ul class="rooms">';
    $.each(data,function (index, room) {
      if (room.available === true) {
        roomsHTML +='<li class="empty">';
        console.log(3)
      } else {
        roomsHTML +='<li class="full">';
        console.log(4)
      }
      roomsHTML += room.room + '</li>';
      console.log(5)
    });
    roomsHTML += '</ul>';
    $('#roomList').html(roomsHTML)
    console.log(roomsHTML);
  }); // end getJSON
}); // end ready
