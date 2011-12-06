import itertools
def cleanlist(thelist):
	thelist = sorted(thelist)
	for element in thelist:
		if thelist.count(element)>1:
			for i in xrange(1,thelist.count(element)):
				thelist.remove(element)
	return thelist

def isabundant(number):
	divisors = [1]
	for i in xrange(2,int(number**0.5)+1):
		if number%i==0:
			divisors.append(i)
			divisors.append(number/i)
	if sum(cleanlist(divisors))>number:
		return True
	else:
		return False


abundants = []
for i in xrange(1,28123):
	if isabundant(i):
		abundants.append(i)

print "abundants done"

canbe = []
for combination in itertools.combinations(abundants,2):
	combosum = sum(combination)
	if combosum < 28123 and combosum not in canbe:
		print combosum,
		canbe.append(combosum)

cantbe = []
for i in xrange(1,28123):
	if i not in canbe:
		cantbe.append(i)

print sum(cantbe)

