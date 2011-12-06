def fifth(number):
    sum = 0
    strnumber = str(number)
    for digit in strnumber:
        sum += int(digit)**5
    if sum == number:
        return True
    else:
        return False

i = 2
fifths = []
running = True

while running:
    if fifth(i) == True:
        fifths.append(i)
        print i
    i +=1
    if i == 194980:
        running = False
print "total:",sum(fifths)
