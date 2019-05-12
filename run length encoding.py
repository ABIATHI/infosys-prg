#PF-Assgn-30
def encode(message):

    ans=""
    a=(len(message)-1)
    count=1
    for i in range(0,a):
        if(message[i]==message[i+1]):
            count=count+1
        else:
            j=str(count)
            k=str(message[i])
            ans=ans+j+k
            count=1
        if((i+1)==a):
            j=str(count)
            k=str(message[i+1])
            ans=ans+j+k
    if(a==0):
            j=str(count)
            k=str(message[0])
            ans=ans+j+k
    
    return ans     

    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
