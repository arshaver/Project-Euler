#import primelist as primes
f = open("/Users/anthonyshaver/Desktop/python/project euler/primes.txt", "r").readlines()
primes = []
for line in f:
	primes.append(int(line.rstrip()))

def circ(prime): #returns all circular iterations of prime as string of ints
	prime = str(prime)
	length = len(prime)
	primes = []
	for eachletter in prime:
		prime = prime[1:]+prime[0]
		primes.append(int(prime))
	return primes


count = 0

#checks all primes without 2,4,5,6,8 and under 1000000
for prime in primes:
	if prime > 1000000:
		break
	if ('0' in str(prime) or '2' in str(prime) or '4' in str(prime) or '6' in str(prime) or '8' in str(prime) or '5' in str(prime)) and len(str(prime))>1:
		continue
	circlist = circ(prime)
	if all(number in primes for number in circlist):
		count +=1
		print prime



print 'total:',count

