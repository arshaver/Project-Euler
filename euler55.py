#!/usr/bin/python

def rev(val):
	return int(str(val)[::-1])
		
def ispalindrome(forward):
	forward = str(forward)
	if forward == forward[::-1]:
		return True
	else:
		return False

def lyrchel(number):
	counter = 0
	while counter < 50:
		if ispalindrome(number + rev(number)):
			#print number,"+",rev(number),"=",number+rev(number)
			return True
			break
		else:
			#print number,"+",rev(number),"=",number+rev(number)
			number = number + rev(number)
			counter +=1
	return False
	
count = 0
for i in xrange(1,10000):
	if not lyrchel(i):
		count +=1
print count