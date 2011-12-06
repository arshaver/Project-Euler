max = 100
primes = []

#Build list
for i in range(2,max):
    primes.append(i)

i = 0
a = 0
run1 = True
run2 = True

#sieve
while run1 == True: #run1 iterates tester number (i)
    tester = primes[i]
    run2 = True
    while run2 == True: #rune2 iterates through the primes list (by a)
        if primes[a+1]%tester == 0:
            primes.pop(a+1)
        if a < len(primes)-2:
            a = a+1
        else:
            run2 = False
            
    i = i+1
    if i > max:
        running = False
