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

#returns list of primes less than n

primeslist = primes(10000)

i = 3
running = True
while running:
	if i in primeslist:
		i+=2
		pass
	n = 1
	while 1:
		if 2*n**2>i:
			print "answer:",i
			running = False
			break
		elif i-2*n**2 in primeslist:
			break
		else:
			n+=1
	i+=2