import csv

data = csv.reader(open("/Users/anthonyshaver/Desktop/python/project euler/words.txt"), delimiter=',')
wordlist = list(data)[0] #don't really know why this works, but it seems to...

def namescore(name):
    score = 0
    letterscore = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
    for letter in name:
        score += letterscore[letter]
    return score

def istriangle(number):
    pos = (0.5)*(((8*number+1)**0.5)-1)
    neg = (0.5)*((-(8*number+1)**0.5)-1)
    if pos == int(pos) and pos > 0:
        return True
    elif neg == int(neg) and neg > 0:
        return True
    else:
        return False

count = 0
for word in wordlist:
	if istriangle(namescore(word)):
		count +=1

print count