def factorial(number):
    fact=1
    i=1
    while(i<=number):
        if number==0:
            fact=1
        else:    
           fact=fact*i
           i=i+1
    return fact    
    #remove pass and write your logic to find and return the factorial of given number


def find_strong_numbers(num_list):
    l1=[]
    l2=[]
    for i in num_list:
        sum1=0
        while(i>0):
            rem=i%10
            a=factorial(rem)
            sum1=sum1+a
            i=i//10
        l1.append(sum1)
    l2=set(l1)&set(num_list)
    l3=list(l2)                
    
            
    return l3
            
     #remove pass and write your logic to find and return the list of strong numbers from the given list

num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
