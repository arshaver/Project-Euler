sqsum = []
sumsq = 0

for i in range(1,101):
    sumsq = sumsq + i**2

for i in range(1,101):
    sqsum.append(i)

print 'answer: ', sum(sqsum)**2-sumsq
