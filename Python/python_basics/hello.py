first_name = input("What is your first name?  ")
print("Hello,",  first_name)

if first_name == "Ann":
    print(first_name,  " is learning Python")
elif first_name == "Craig":
    print(first_name, "is learning with other students in the community!")
else:
    #this is just in case we have a younger user who can't yet read
    age = int(input("How old are you?  "))
    if age <= 6:
        print("Wow, you're {}!".format(age))
    print("You should totally learn Python, {}".format(first_name))
print("Have a great day {}".format(first_name))
