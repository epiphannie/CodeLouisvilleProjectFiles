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
# unpacker(**{'last_name': 'McHealy', 'first_name': 'Ann'})

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

def multiply(*args):
    print args
    total = 1
	for num in args:
        total = num * total
    return total
multiply((2, 3, 4, 5)
