def ispalindrome(forward):
    reverse = ''
    forward = str(forward)
    for i in range(1,len(forward)+1):
        reverse = reverse + forward[-i]
    if forward == reverse:
        return True
    else:
        return False

def dec2bin(n):
	s = ''
	while n:
		s = str(n % 2) + s
		n = n / 2
	return s

sum = 0

for i in xrange(1,1000000+1):
	if ispalindrome(i) == True and ispalindrome(dec2bin(i)) == True:
		sum += i

print sum