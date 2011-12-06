import time
def numdiv(number):
    divisors = []
    for i in range(1,number/2+1):
        if number%i == 0:
            divisors.append(i)
    divisors.append(number)
    return len(divisors)

running = True
i = 10000
current = 0

while running == True:
    triangle = (i*i+i)/2
    i += 1
    numdivisors = numdiv(triangle)
    if numdivisors > current:
        current = numdivisors
        print triangle,"has",current,"divisors"
    if numdivisors > 450:
        print "answer:", triangle,'has',current,'divisors'
        running = False

print time.clock()
