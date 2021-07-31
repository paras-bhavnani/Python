date1 = (2014,7,2)
date2 = (2014,7,11)

def dayGap(date1, date2):
    days = 0
    for i in range(3):
        if i == 0:
            days = abs(date2[i] -date1[i]) * 365
        if i == 1:
            days = abs(date2[i] -date1[i]) * 30
        if i == 2:
            days = abs(date2[i] -date1[i])
    print(days)

dayGap(date1, date2)