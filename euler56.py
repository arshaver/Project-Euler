def digitsum(number):
	numlist = list(str(number))
	sum=0
	for num in numlist:
		sum+=int(num)
	return sum

biggest = 0
for a in xrange(1,100):
	for b in xrange(1,100):
		if digitsum(a**b) > biggest:
			biggest = digitsum(a**b)

print biggest