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

primelist = primes(9999)
maybelist = []

for prime in primelist:
	if prime >1000 and (prime + 3330) in primelist and (prime + 3330*2) in primelist and prime != 1487:
		maybelist.append([prime,prime+3330,prime+3330*2])


for maybe in maybelist:
	if sorted(list(str(maybe[0]))) == sorted(list(str(maybe[1]))) == sorted(list(str(maybe[2]))):
		print str(maybe[0]) + str(maybe[1]) + str(maybe[2])

