def gcd(a, b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)

a = 120
b = 96
print(gcd (120, 96))