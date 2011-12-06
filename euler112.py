def reverse(list):
	reversedlist = []
	for i in xrange(len(list)-1,-1,-1):
		reversedlist.append(list[i])
	return reversedlist

def isbouncy(number):
	if number < 100:
		return False
	thelist = list(str(number))
	reversedlist = reverse(thelist)
	if thelist == sorted(thelist):
		return False
	elif reversedlist == sorted(thelist):
		return False
	else:
		return True

number = 1
count = 0

while 1:
	if isbouncy(number):
		count+=1
	print float(count)/float(number)
	if float(count)/float(number)==.99:
		print number
		break
	number+=1