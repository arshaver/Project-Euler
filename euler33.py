def fractiontest(num,denom):
	value = float(num)/float(denom)
	frac = [[int(str(num)[0]),int(str(num)[1])],[int(str(denom)[0]),int(str(denom)[1])]]
	if frac[0] == frac[1]:
		return False
	elif frac[0][0] == frac [1][0] and frac[1][1] != 0:
		valuetest = float(frac[0][1])/float(frac[1][1])
	elif frac[0][0] == frac[1][1] and frac[1][0] != 0:
		valuetest = float(frac[0][1])/float(frac[1][0])
	elif frac[0][1] == frac[1][0] and frac[1][1] != 0:
		valuetest = float(frac[0][0])/float(frac[1][1])
	elif frac[0][1] == frac[1][1] and frac[1][0] != 0:
		valuetest = float(frac[0][0])/float(frac[1][0])
	else:
		return False
	if valuetest == value:
		return True
	else:
		return False

for num in xrange(10,100):
	for denom in xrange(num,100):
		if fractiontest(num,denom):
			print num,"/",denom

#note: does not give full solution, must hand search the possibilites
# and eliminate trivial answer.

# correct answers: (16/64), (19/95), (49/98), (26/65)