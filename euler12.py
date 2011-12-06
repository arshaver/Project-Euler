import time

def primefactors(number):
    running = True
    guess = 2
    factors = []

    while running:
        if number%guess == 0 and not number == guess:
            factors.append(guess)
            number = number/guess
        elif guess == number:
            factors.append(number)
            running = False
        else:
            guess = guess + 1
    factors.sort()
    return factors

#generates list of the counts of exponents            
def factorcount(primefactorlist):
    count = 0
    start = primefactorlist[0]
    numberlist = []
    for i in range(0,len(primefactorlist)):
        if primefactorlist[i] == start:
            count += 1
        else:
            numberlist.append(count)
            start = primefactorlist[i]
            count = 1
    numberlist.append(count)
    return numberlist

#add one to each exponent from factorcount and then multiplies them together
def thefinish(exponentlist):
    #increase each "exponent" by one
    for i in range(0,len(exponentlist)):
        exponentlist[i] = exponentlist[i]+1
    mult = 1
    for number in exponentlist:
        mult = mult*number
    return mult


running = True
i = 2

while running == True:
    triangle = (i**2+i)/2
    primefactorlist = primefactors(triangle)
    factorcountlist = factorcount(primefactorlist)
    divisors = thefinish(factorcountlist)
    if divisors > 500:
        print "answer:",triangle
        running = False
    i = i+1

print time.clock()
