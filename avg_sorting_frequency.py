def find_more_than_average():
    sum1=0
    count=0
    for i in list_of_marks:
       sum1=sum1+i
       average=sum1/(len(list_of_marks))
    for j in list_of_marks:   
        if j>average:
           count=count+1
    l1=(count/len(list_of_marks))*100   
    return l1
    #Remove pass and write your logic here

def sort_marks():
    a=list(list_of_marks)
    for i in range(0,len(a)):
        j=i+1 
        for j in range(0,len(a)-1):
            if a[i]<=a[j]:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
    return a            
    #Remove pass and write your logic here

def generate_frequency():
    l1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in list_of_marks:
        for j in range(0,len(l1)):
           if i==j:
               l1[j]=l1[j]+1
    return l1
    #Remove pass and write your logic here

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
