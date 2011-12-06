f = open("/Users/anthonyshaver/Desktop/primes.txt", "r").readlines()
primes = []
for line in f:
	primes.append(int(line.rstrip()))

def testprime(a,b):
	count = 0
	for n in range(1,200):
		if n**2+a*n+b in primes:
			count += 1
		else:
			return count
			break

max = 0
ab = []
for a in primes[0:168]:
	print primes.index(a)
	for b in primes[0:168]:#prime 168 is just over 1000 (=1009)
		if testprime(a,b) > max:
			max = testprime(a,b)
			ab = [a,b]
		if testprime(-a,-b) > max:
			max = testprime(-a,-b)
			ab = [-a,-b]
		if testprime(-a,b) > max:
			max = testprime(-a,b)
			ab = [-a,b]
		if testprime(a,-b) > max:
			max = testprime(a,-b)
			ab = [a,-b]

print ab
print max