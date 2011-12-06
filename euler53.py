def fact(x): return (1 if x==0 else x * fact(x-1))

def ncr(n,r):
	return fact(n)/(fact(r)*fact(n-r))

count = 0
for n in xrange(1,101):
	for r in xrange(1,n):
		if ncr(n,r)>1000000:
			count +=1

print count