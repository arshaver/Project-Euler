from decimal import *
getcontext().prec = 5000



maxlen = 0
maxdenom = 0
for denom in xrange(10,1000):
	print denom
	thelist = []
	x = str(Decimal(1)/Decimal(denom))
	y = x[5:]

	for i in xrange(1,2000):
		thelist.append(y[0:i])

	for test in thelist:
		if len(test)>50 and test*2 in y:

			if len(test)> maxlen:
				maxlen = len(test)
				maxdenom = denom
			break
		
print 'max d:',maxdenom
print 'max lenght',maxlen