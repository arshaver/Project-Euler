def reverse(number):
	revnumber = str(number)
	revnumber = int(revnumber[::-1])
	return revnumber

def allodd(number):
	number = str(number)
	if '2' in number or '4' in number or '6' in number or '8' in number:
		return False
	else:
		return True


count = 0

for n in xrange(1,1000000000):
	if allodd(n+reverse(n)):
		count +=1
	