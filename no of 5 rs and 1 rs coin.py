def make_amount(rupees_to_make,no_of_five,no_of_one):

    five_needed=0

    one_needed=0

    a=(no_of_five*5)+(no_of_one*1)

    if(a<rupees_to_make):

        print(-1)

    else:

        b=rupees_to_make//5

        c=rupees_to_make%5

        if(b>no_of_five):

            five_needed=b

            c=rupees_to_make-(b*5)

        if(c<=no_of_one):

            one_needed=c

            five_needed=b

            print("No. of Five needed :", five_needed)

            print("No. of One needed  :", one_needed)

        else:

            print(-1)
    #Start writing your code here
    #Populate the variables: five_needed and one_needed


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("No. of Five needed :", five_needed)
    #print("No. of One needed  :", one_needed)
    #print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28,8,5)
