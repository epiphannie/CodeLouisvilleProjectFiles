sodas = ['pepsi', 'cherry coke', 'sprite']
chips = ['doritos', 'fritos']
candy = ['snickers', 'm&ms', 'twizzlers']

while True:
    choice = input("Would you like a SODA, some CHIPS, or a CANDY? ").lower()

    try:
        if choice == 'soda':
            snack = sodas.pop()
        elif choice == 'chips':
            snack = chips.pop()
        elif choice == 'candy':
            snack = candy.pop()
        else:
            print("Sorry I didn't understand that.")
            continue
    except IndexError:
        print("we're all out of {}! Sorry!".format(choice))
    else:
        print("here is your {}: {}".format(choice, snack))
