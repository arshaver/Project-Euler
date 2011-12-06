numerators = [3,7]
denominators = [2,5]
count = 0
for index in xrange(2,1000):
	numerators.append(2*numerators[index-1]+numerators[index-2])
	denominators.append(2*denominators[index-1]+denominators[index-2])
	if len(str(numerators[index]))>len(str(denominators[index])):
		count+=1

print count