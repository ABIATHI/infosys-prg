
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    total_ticket_amount=((no_of_adults*37550.0)+(no_of_children*(37550.0/3)))
    total_ticket=total_ticket_amount+(total_ticket_amount*(7/100))
    total_ticket_2=total_ticket*(10/100)
    total_ticket_cost=total_ticket-total_ticket_2
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)
