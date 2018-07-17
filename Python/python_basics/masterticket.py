TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100

def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name?  ")
    try:
        number_of_tickets = int(input("How many tickets would you like, {}?  ".format(name)))
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue. {}. Please try again".format(err))
    else:
        price = calculate_price(number_of_tickets)
        print("Your total cost is ${}".format(price))
        response = input("Would you like to proceed with your purchase? Y/N  ")
        if response.upper() == "Y":
            print("Sold!")
            tickets_remaining -= number_of_tickets
        else:
            print("Thanks for visiting anyway, {}".format(name))
print("The tickets are sold out!")
