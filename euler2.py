running = True
fib = [1,2]
i = 1

# generate fib sequence
while running:
    num = fib[i] + fib[i-1]
    if num > 4000000:
        running = False
    else:
        fib.append(num)
    i = i + 1

#print fib


i = 0
running = True

while running == True:
    if fib[i] % 2 != 0:
        fib[i] = 0
    i = i+1
    print fib
    if i == len(fib):
        running = False

print "answer: ", sum(fib)
    
