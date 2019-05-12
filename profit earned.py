def calculate(distance,no_of_passengers):
    expenditure=(distance*70)/(10)
    cost=(no_of_passengers*80)
    if expenditure<cost:
        profit=cost-expenditure
    else:
        profit=-1
            
    return(profit)         
    #Remove pass and write your logic here



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
