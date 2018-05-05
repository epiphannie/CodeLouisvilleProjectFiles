var students = [
  {
    name: "Ann",
    track: "Fullstack",
    achievements: '10',
    points: '2000',
  },
  {
    name: "David",
    track: "Pro Programmer",
    achievements: '1000',
    points: '20000000',
  },
  {
    name: "John",
    track: "Law Dev",
    achievements: '22',
    points: '5000',
  },
  {
    name: "Eleanor",
    track: "Baby Dev",
    achievements: '1',
    points: '2',
  },
  {
    name: "Phonie",
    track: "Beyond the grave",
    achievements: '45',
    points: '7500',
  },
];

for (property in students) {
  console.log(property, ': ', students[property]);
}
