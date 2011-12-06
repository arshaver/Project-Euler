thenumbers = []

for a in range(1,1000000):
    if a%3 == 0 or a%5 == 0:
        thenumbers.append(a)

print thenumbers, ''


print 'the answer is: ', sum(thenumbers)

