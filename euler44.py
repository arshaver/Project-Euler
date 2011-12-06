import itertools,math,time

start = time.time()

def ispent(number):
    pos = (1./6.)*(1+(24*number+1)**0.5)
    neg = (1./6.)*(1-(24*number+1)**0.5)
    if pos == int(pos) and pos > 0:
        return True
    elif neg == int(neg) and neg > 0:
        return True
    else:
        return False

pentagonals = []
for number in xrange(1,10000000):
	if ispent(number):
		pentagonals.append(number)
print len(pentagonals),'pents calculated in',time.time()-start,'seconds'

def pentcompare(pentagonals):
	staticlist = pentagonals
	choplist = pentagonals
	for index in xrange(1,len(pentagonals)):
		for pair in itertools.izip(staticlist,choplist[index::]):
			if ispent(sum(pair)) and ispent(abs(pair[0]-pair[1])):
				print abs(pair[0]-pair[1])

pentcompare(pentagonals)