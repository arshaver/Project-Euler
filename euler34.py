def fact(x): return (1 if x==0 else x * fact(x-1))

def isfact(number):
    sum = 0
    strnumber = str(number)
    for digits in strnumber:
        sum += fact(int(digits))
    if sum == number:
        return True
    else:
        return False

running = True
i = 3
thenumbers = []
while running:
    if isfact(i) == True:
        thenumbers.append(i)
        print "number:",i
        print "sum:",sum(thenumbers)
    i +=1
