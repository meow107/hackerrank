# Time Conversion
time = "12:05:39PM"
tail_removed = ""
result = ""
hour = 0

haveResult =  time.find("AM")
isAM = False
if time.find("AM") != -1:
    isAM = True

if isAM :
    tail_removed = time.replace("AM","")
else:
    tail_removed =time.replace("PM","")

str_hour = time[0] + time[1]
hour = int(str_hour)

if not isAM:
    if hour < 12 :
        result = tail_removed.replace(str_hour, str(hour + 12))
        print(result)
    else:
        print(tail_removed)
else :
    if hour == 12 :
        result = tail_removed.replace(str_hour, "00")
        print(result)
    else:
        print(tail_removed)


        
