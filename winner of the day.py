def find_winner_of_the_day(*match_tuple):
    #Remove pass and write the logic here
    count1=0
    count2=0
    for i in match_tuple:
        if i=="Team1":
             count1=count1+1
        else:
            count2=count2+1
    if count1>count2:
        return "Team1"
    elif count1<count2:
        return "Team2"
    else:
        return "Tie"
#Invoke the function with each of the print statements given below

print(find_winner_of_the_day("Team1","Team2","Team2","Team1","Team2"))
