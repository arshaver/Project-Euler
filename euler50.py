#build primes
def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

primeslist = primes(1000000)
#len(primeslist) = 78498
#only have to test to 5143 though, any more and it will be over 1mil

#first number it produces is the right one! the rest just satisfy conditions
end = 5143
running = True
while running:
	for length in xrange(0,5143):
		testsum = sum(primeslist[0+length:end])
		if testsum > 1000000:
			break
		elif testsum in primeslist:
			print testsum
			running = False #edited to stop at first number
			break
	end = end - 1