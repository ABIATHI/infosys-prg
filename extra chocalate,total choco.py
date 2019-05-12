#Global variables
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    total=0
    for k in chocolates_received:
        total=total+k
    return total
    #Remove pass and write your logic here to find and return the total number of chocolates

def reward_child(child_id_rewarded,extra_chocolates):
    ab=list(child_id)
    if child_id_rewarded not in child_id:
        print("Child id is not valid")
    if extra_chocolates>=1:
        for i in range(0,len(ab)):
            if ab[i]==child_id_rewarded:
                j=i 
                chocolates_received[j]=chocolates_received[j]+extra_chocolates
        print(chocolates_received)
    else:
        print("Extra_chocolates is less than 1")
   
    
    #Remove pass and write your logic here


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("Extra chocolates is less than 1")
    #print("Child id is invalid")
    #print(chocolates_received)


print(calculate_total_chocolates())
#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(20,2)
