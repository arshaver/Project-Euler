import time

max = 100000
run1 = True
primes = [2,3]
i = 1

#Build (better) list
while run1 == True:
    primes.append(6*i-1)
    primes.append(6*i+1)
    i = i+1
    if primes[len(primes)-1] > max:
        run1 = False

    
def primetest(tester):
    run2 = True
    a = 0
    while run2 == True: #run2 iterates through the primes list (by a)
        if primes[a+1]%tester == 0 and primes[a+1] != tester:
            primes.pop(a+1)
        if a < len(primes)-2:
            a = a+1
        else:
            run2 = False
            
for i in range(0,int(max**0.5)):
    primetest(primes[i])



print sum(primes)

print 'time: ',time.clock()
