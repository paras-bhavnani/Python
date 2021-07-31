import re
date = 'June 03, 2007'

def checkDateFormat(date):
    if re.match('[A-Za-z]+\s[0-9]{2}[,]\s[0-9]{4}',date):
        return True
    else:
        return False

print(checkDateFormat(date))

