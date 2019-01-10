def get_date(day,month):
    str_day = ""
    if day < 10 :
        str_day = "0%d" %(day)
    else:
        str_day = day
    #month
    str_month = ""
    if month < 10:
        str_month = "0%d"%(month)
    else:
        str_month = month
    return ("%s.%s.%s"%(str_day,str_month,year))

def solve(y):
    # Complete this function
    months =        [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10,11,12]
    day_of_months = [31,28,31,30,31,30,31,31,30,31,30,31]
    programmer_day = 256
    sum = 0
    month = 1
    i = 0

    if y >= 1700 and y <= 1917:
        #Russia
        if y % 4 == 0 :
            day_of_months[1] = 29

    elif y == 1918:
        day_of_months[1] = 15

    elif y > 1918 :
        #Gregorian
        if y % 400 == 0 or ( y % 100 != 0 and y % 4 == 0):
            day_of_months[1] = 29

    while sum <= programmer_day:
        tmp = sum + day_of_months[i]
        if tmp > programmer_day:
            break
        sum = tmp
        i += 1
        month += 1
    day = programmer_day - sum
    return get_date(day,month)
        
        
    
year = 2017
result = solve(year)
print(result)