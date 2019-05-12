def convert_currency(amount_needed_inr,current_currency_name):
    current_currency_amount=0
    if current_currency_name=="Euro":
        current_currency_amount=amount_needed_inr*0.01417
    elif current_currency_name=="british pound":
        current_currency_amount=amount_needed_inr*0.0100
    elif current_currency_name=="austrailain dollar":
        current_currency_amount=amount_needed_inr*0.02140
    elif current_currency_name=="canadian dollar":
        current_currency_amount=amount_needed_inr*0.02027
    #write your logic here
    return current_currency_amount


#Provide different values for amount_needed_inr,current_currency_name and test your program
currency_needed=convert_currency(3500,"british pound")
if(currency_needed!= -1):
    print(currency_needed )
else:
    print("Invalid currency name")
