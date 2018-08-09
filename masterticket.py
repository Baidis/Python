TICKET_PRICE = 10

tickets_remaining = 99 

while tickets_remaining >= 1:
    print("There are {} tickets ramaining" .format(tickets_remaining))
    print("Money raised {}" .format((100 - tickets_remaining) * TICKET_PRICE))
    customer_name =  input("What is your name?   ")
    number_of_tickets =  input("Hello {} how many tickets would you like?  " .format(customer_name))
    try:
        number_of_tickets = int(number_of_tickets)
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining." .format(tickets_remaining))
    except ValueError as err:
        print("Please use a number of tickets")
    else:
        number_of_tickets = int(number_of_tickets)
        total = (number_of_tickets * TICKET_PRICE)
        print("Your total comes to ${} " .format(total))
        buy = input("Do you want to proceed with the purchase? y/n     ".format(customer_name))
        if buy.lower() == "y":
            # TODO: Gather payment information
            print("SOLD!")
            tickets_remaining -= number_of_tickets
        else: 
            print("Thank you {} " .format(customer_name))
print("Sorry the tickets are all sold out!!! :(")