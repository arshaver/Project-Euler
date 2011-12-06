num = 11
running = True

while running:
    print num
    if num%20 == 0 and num%19 == 0 and num%18 == 0 and num%17 ==0 and num%16 ==0 and num%15 ==0 and num%14 ==0 and num%13 == 0 and num%12 ==0 and num%11 == 0:
        print 'answer found: ',num
        running = False
    else:
        num = num + 11
