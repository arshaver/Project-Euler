
count = 0
for d in xrange(1,12001):
	print d
	for n in xrange(1,d):
		num = float(n)/float(d)
		if num < 1/2. and num > 1/3.:
			count +=1
			print count

