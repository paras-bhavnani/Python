import re
cardSample = '4123-7845-9624-1526'
def crediCardCheck(card):
    if re.match('^[3,4,9][0-9]{3}[-]([0-9]{4}[-]){2}[0-9]{4}', card):
        return True
    else:
        return False
print(crediCardCheck(cardSample))