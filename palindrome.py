import math

def ispalindrome(forward):
    reverse = ''
    forward = str(forward)
    for i in range(1,len(forward)+1):
        reverse = reverse + forward[-i]
    if forward == reverse:
        return True
    else:
        return False

largest = 0

for a in range(999,100,-1):
    for b in range(999,100,-1):
        if ispalindrome(a*b) == True and a*b > largest:
            largest = a*b
            x = a
            y = b

print x,' times ',y,' equals ',largest
