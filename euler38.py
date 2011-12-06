def ispandigital(number):
	string = str(number)
	thelist = []
	if len(string) != 9:
		return False
	thelist = list(string)
	if sorted(thelist) == ['1','2','3','4','5','6','7','8','9']:
		return True
	else:
		return False

#generate big list
biglist = []
for n in range(1,10):
	biglist.append(range(1,n+1))


answers = []

for multiplier in xrange(1,10000):
	for littlelist in biglist:
		teststring = ''
		for i in littlelist:
			teststring += str(i*multiplier)
		if ispandigital(teststring):
			answers.append(teststring)

print max(answers)