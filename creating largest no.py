def create_largest_number(number_list):
    a=number_list
    for i in range(0,len(a)):
        j=i+1 
        for j in range(0,len(a)-1):
            if a[i]>a[j]:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
    s=[str(k) for k in a]
    largest_number=int("".join(s))
    return largest_number
    #remove pass and write your logic here

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
