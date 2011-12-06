import time

n = 13
running = True
maxit = 0
maxnum = 0
run = 0

for n in range(13,1000000):
    it = 0
    run = n
    running = True
    while running == True:
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n+1
        it = it+1
        if n == 1:
            running = False
    if it > maxit:
            maxit = it
            maxnum = run

print time.clock()
