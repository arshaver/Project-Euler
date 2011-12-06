from math import log

f = open("/Users/anthonyshaver/Desktop/python/project euler/base_exp.txt", "r")
foolist = []

for line in f:
	foolist.append(line.rstrip())

baselist = []
for pair in foolist:
	comma = pair.index(",")
	baselist.append([int(pair[0:comma]),int(pair[comma+1:])])

reducedlist = []
for number in baselist:
	x = log(number[0])
	reducedlist.append(number[1]*(x))

print reducedlist.index(max(reducedlist))+1