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

def ispandigital(number):
	string = str(number)
	thelist = []
	numberlist = []
	thelist = list(string)
	for i in thelist:
		numberlist.append(int(i))
	if sorted(numberlist) == range(1,max(numberlist)+1):
		return True
	else:
		return False


primeslist = primes(50000000)

for prime in primeslist:
	if ispandigital(prime):
		print prime