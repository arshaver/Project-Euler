x = 1
while 1:
	if sorted(list(str(x))) == sorted(list(str(2*x))) == sorted(list(str(3*x))) == sorted(list(str(4*x))) == sorted(list(str(5*x))) == sorted(list(str(6*x))):
		print x
		break
	else:
		x+=1