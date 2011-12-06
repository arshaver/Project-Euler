answers = [0]*1000
for a in xrange(1,1000):
	for b in xrange(1,1000):
		if a+b+(a**2+b**2)**0.5<1000 and (a**2+b**2)**0.5 == int((a**2+b**2)**0.5):
			answers[int(a+b+(a**2+b**2)**0.5)]+=1

print answers.index(max(answers))
