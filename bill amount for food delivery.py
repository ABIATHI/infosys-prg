
def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    bill_amount=0

    if(distance_in_kms<=3):

        if(food_type=="V"):

            bill_amount=(120*quantity_ordered)

        elif(food_type=="N" ):

            bill_amount=(150*quantity_ordered)

    elif(distance_in_kms>3 and distance_in_kms<=6):

        if(food_type=="V"):

            bill_amount=(120*quantity_ordered)+((distance_in_kms-3)*3)

        elif(food_type=="N" ):

            bill_amount=(120*quantity_ordered)+((distance_in_kms-3)*3)

    elif(distance_in_kms>6):

        if(food_type=="V"):

            bill_amount=(120*quantity_ordered)+((distance_in_kms-6)+(3*3))

        elif(food_type=="N" ):

            bill_amount=(120*quantity_ordered)+((distance_in_kms-6)+(3*3))
    #write your logic here
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)
