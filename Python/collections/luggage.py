# def packer(name = None, **kwargs):
# # packing key word arguments
#     print(kwargs)
#
# packer(name="Kenneth", num=42, spanish_inquisition=None)
#
# def unpacker(first_name=None, last_name=None):
#     if first_name and last_name:
#         print("Hi! {} {}".format(first_name, last_name))
#     else:
#         print("Hi, no name!")
#
# packer(name="Kenneth", num=42, spanish_inquisition=None)
# unpacker(**{'last_name': 'McHealy', 'first_name': 'Ann'})
#
# course_minutes = {"Python Basics": 232, "Djengo Basics": 237, "Flask Basics": 189, "Java Basics": 133}
#
# for course, minutes in course_minutes.items():
#     print("{} is {} minutes long".format(course, minutes))

# def word_count(string):
#     word_list = string.lower().split()
#     dict = {}
#     for word in word_list:
#         count = 0
#         index = 0
#         while index < len(word_list):
#             if word_list[index] == word:
#                 count += 1
#                 index += 1
#             else:
#                 index += 1
#         dict[word] = count
#     print dict
#
#
# word_count("a a b c a d d")

# def num_teachers(dict):
#
#     return len(dict.keys())
#
# print num_teachers({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
# 'Kenneth Love': ['Python Basics', 'Python Collections']})

# def num_courses(dict):
#     length = 0
#     for key in dict:
#         length += len(dict[key])
#     return length
#
# print num_courses({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
# 'Kenneth Love': ['Python Basics', 'Python Collections']})

# def courses(dict):
#     list = []
#     for key in dict:
#         list += dict[key]
#     return list
#
# print courses({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#     'Kenneth Love': ['Python Basics', 'Python Collections']})
#
# def most_courses(dict):
#     max_length = 0
#     for key in dict:
#         length = len(dict[key])
#         if length > max_length:
#             max_length = length
#             max_teacher = key
#         else:
#             continue
#     return max_teacher
#
# print most_courses({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#     'Kenneth Love': ['Python Basics', 'Python Collections', 'something else']})
#
# def multiply(*args):
#     print(args)
#     total = 1
#     for num in args:
#         total = num * total
#     print(total)
#     return total
# multiply(2, 3, 4, 5)

# COURSES = {
# "Python Basics": {"Python", "functions", "variables",
# "booleans", "integers", "floats",
# "arrays", "strings", "exceptions",
# "conditions", "input", "loops"},
# "Java Basics": {"Java", "strings", "variables",
# "input", "exceptions", "integers",
# "booleans", "loops"},
# "PHP Basics": {"PHP", "variables", "conditions",
# "integers", "floats", "strings",
# "booleans", "HTML"},
# "Ruby Basics": {"Ruby", "strings", "floats",
# "integers", "conditions",
# "functions", "input"}
# }
#
# def covers(set):
#     list = []
#     for course, contents in COURSES.items():
#         if len(set) == len(contents & set):
#             print(course)
#             list.append(course)
#             print(list)
#         else:
#             continue
#     return list
#
# covers({'strings'})

# def move(player, direction):
#     x, y, hp = player
#     xd, yd = direction
#     print(x + xd)
#     print(y + yd)
#     if x + xd == -1 or x + xd == 10:
#         hp -= 5
#     else:
#         x += xd
#     if y + yd == -1 or y + yd == 10:
#         hp -= 5
#     else:
#         y += yd
#     return x, y, hp
# print(move((0, 9, 5), (0, 1)))

# TILES = ('-', ' ', '-', ' ', '-', '||',
#     '_', '|', '_', '|', '_', '|', '||',
#     '&', ' ', '_', ' ', '||',
#     ' ', ' ', ' ', '^', ' ', '||', 'end'
# )
#
# for tile in TILES:
#     if tile == "||":
#         output = ""
#         line_end = "\n"
#     else:
#         output = tile
#         line_end = ""
#     print(output, end = line_end)

# def __str__(pattern):
#     strepresentation = ''
#     for item in pattern:
#         if item == ".":
#             strepresentation += "dot-"
#         elif item == "_":
#             strepresentation += "dash-"
#     result = strepresentation[:-1]
#     return result
#
# print(__str__(['.', '.', '.']))
# print(__str__([]))
# print(__str__(['.', '_', '.']))
