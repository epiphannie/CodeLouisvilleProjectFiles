import re

names_file = open("names.txt", encoding="utf-8")  #open file by pointing to it
data = names_file.read()  #read file into variable
names_file.close()  #close file to reduce memory load


print(re.match(r'Love', data))
print(re.match(r'Kenneth', data))
# match matches from the beginning of a string

print(re.search(r'Kenneth', data))
# search is match for anywhere in a string

last_name = r'Love'
print(re.match(last_name, data))
