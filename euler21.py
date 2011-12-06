def d(number): #returns the sum of all proper divisors of number (eg not counting number)
    divisorlist = []
    for i in range(1,int(number/2)+1):
        if number%i == 0:
            divisorlist.append(i)
    return sum(divisorlist)

amicables = []
for a in range(2,10001):
    b = d(a)
    if d(b) == a and a != b and a not in amicables and b not in amicables:
        amicables.append(a)
        amicables.append(b)

print sum(amicables)
