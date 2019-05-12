def generate_next_date(day,month,year):
    #Start writing your code
    if month==1 and month==3 and month==5 and month==7 and month==8 and month==10 and month==12:
        if day==31:
          next_day=1
          next_month=month+1
        else:
            next_day=day+1
            next_month=month
    else:
        if day==30:
            next_day=1
            next_month=month+1
        else:
             next_day=day+1
             next_month=month
    if month==12:
        next_month=1
        next_year=year+1
    else:
        next_year=year
        

    print(next_day,"-",next_month,"-",next_year)


generate_next_date(22,3,2011)
