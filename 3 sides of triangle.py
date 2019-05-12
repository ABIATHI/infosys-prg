
num3=5def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    if num1>(num2+num3):
       print(failure)
    elif num2>(num1+num3):
        print(failure)
    elif num3>(num2+num1):
        print(failure)
    else:
        print(success)

    #Write your logic here

    #Use the following messages to return the result wherever necessary
    return success
    return failure

#Provide different values for the variables, num1, num2, num3 and test your program
num1=3
num2=3
form_triangle(num1, num2, num3)
