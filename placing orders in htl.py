menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,3,0]

'''This method accepts the item followed by the quantity required by a customer in the format item1, quantity_required, item2, quantity_required etc.'''
def place_order(*item_tuple):
    m=list(menu)
    n=list(item_tuple)

    for i in range(0,len(n),2):
        for j in range(0,len(menu)):
            if m[j]==n[i]:
                if check_quantity_available(j,n[i+1])==True:
                    print (n[i],"is available")
                    break
                else:
                    print(n[i],"stock is over")
      
    #Remove pass and write your logic here


    #Populate the item name in the below given print statements
    #Use it to display the output wherever applicable
    #Also, do not modify the text in it for verification to work
    
   

    
  


'''This method accepts the index position of the item requested by the customer in the quantity_available list, and the requested quantity of the item.'''
def check_quantity_available(index,quantity_requested):
        if quantity_available[index]>=quantity_requested:
            new=quantity_available[index]-quantity_requested
            flag=0 
        else:
            flag=1
                
        if flag==0:
            return True
        else:
            return False
    #Remove pass and write your logic here to return an appropriate boolean value.


#Provide different values for items ordered and test your program
place_order("Fried Rice",2,"Soup",1)
#place_order("Soup",1,"Veg Roll", 2, "Fried Rice1",1)
