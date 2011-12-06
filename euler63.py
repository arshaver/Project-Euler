count = 0

for base in xrange(1,100):
	for exponent in xrange(1,1000):
		if len(str(base**exponent)) == exponent:
			count +=1
		elif len(str(base**exponent)) > exponent:
			break

print count
