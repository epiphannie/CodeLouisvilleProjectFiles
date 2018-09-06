import re
#
# names_file = open("names.txt", encoding="utf-8")
# data = names_file.read()
# names_file.close()
#
# #print(re.match(r'Love', data))
# #print(re.search(r'Kenneth', data))
# print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))  #finds all, not overlapping
# print(re.findall(r'\w*, \w+', data))

def find_words(count, str):
    print(re.findall(r'\w{' + str(count) +',}', data))
find_words(4, "dog, cat, baby, balloon, me")
