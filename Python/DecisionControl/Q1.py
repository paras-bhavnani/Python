string1 = "Is this a joke?"
string2 = "this neccessary"

def checkForIS(string):
    if string[0:2] == "Is":
        return string
    else :
        return "Is " + string

print(checkForIS(string1))
print(checkForIS(string2))
