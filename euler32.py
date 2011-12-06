def ispandigital(string):
	thelist = []
	if len(string) != 9:
		return False
	thelist = list(string)
	if sorted(thelist) == ['1','2','3','4','5','6','7','8','9']:
		return True
	else:
		return False
		
foobar = []
sum = 0
for double in xrange(1,5000):
	for triple in xrange(1,5000):
		foo = str(double)+str(triple)+str(double*triple)
		if ispandigital(foo) and double*triple not in foobar:
			foobar.append(double*triple)
			sum += double*triple

print sum