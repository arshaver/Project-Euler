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

primes = primes(1000000)

def ltrunk(prime):
	trunk = []
	prime = str(prime)
	for i in range(0,len(prime)):
		trunk.append(int(prime[i:]))
	return trunk


def rtrunk(prime):
	trunk = []
	prime = str(prime)
	for i in range(1,len(prime)+1):
		trunk.append(int(prime[:i]))
	return trunk


#checks all primes without 1,2,4,5,6,8 digits until reaches count=11
answers = []
for prime in primes:
	if len(answers) > 11:
		break
	if '4' in str(prime) or '6' in str(prime) or '8' in str(prime) :
		continue
	if len(str(prime))==1:
		continue
	if len(answers) > 11:
		break
	rlist = rtrunk(prime)
	llist = ltrunk(prime)
	if all(number in primes for number in rlist) and all(number in primes for number in llist):
		answers.append(prime)

print 'numbers:',answers
print 'answer:',sum(answers)

