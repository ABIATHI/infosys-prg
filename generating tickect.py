
print(generate_ticket("AI","Bangalore","London"def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    #Write your logic here
    for i in range(0,no_of_passengers):
        i=101+i
        ticket=airline+':'+source[0:3]+':'+destination[0:3]+':'+str(i)
        ticket_number_list.append(ticket)
    if no_of_passengers>=5:
        ticket_number_list=ticket_number_list[-5:]
            
    
      
        
        
    #Use the below return statement wherever applicable
    return ticket_number_list
