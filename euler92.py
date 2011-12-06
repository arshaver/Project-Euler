def next(num):
	foo = str(num)
	sum = 0
	for number in foo:
		sum+=int(number)**2
	return sum


#generate numbers that will lead to 1, store them in one_list
one_list = []
for i in xrange(1,10000):
	first = next(i)
	number = i
	while 1:
		number = next(number)
		if number == 1:
			if first not in one_list:
				one_list.append(first)
			break
		elif number == 89:
			break
		else:
			continue


count = 0
for i in xrange(1,10000001):
	if next(i) in one_list:
		count +=1
		
		
print 10000000-count