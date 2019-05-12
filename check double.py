def check_double(number):
    l1=[]
    l2=[]
    count1=0
    count2=0
    b=number
    a=number*2
    while b>0:
        r=b%10
        l1.append(r)
        count1=count1+1
        b=b//10
    print(l1)    
    while a>0:
        r1=a%10
        l2.append(r1)
        count2=count2+1
        a=a//10
    print(l2)    
    l1.sort() 
    l2.sort()
    if count2==count1:
        for i in range(0,len(l1)):
            if l1[i]==l2[i]:
                flag=0
            else:
                flag=1
    else:
        return False
    if flag==0:
        return True
    else:
        return False
    #Remove pass and write your logic here

#Provide different values for number and test your program
print(check_double(100))
