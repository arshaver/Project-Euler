line1 = [8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8]
line2 = [49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0]
line3 = [81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65]
line4 = [52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91]
line5 = [22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80]
line6 = [24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50]
line7 = [32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70]
line8 = [67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21]
line9 = [24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72]
line10 = [21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95]
line11 = [78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92]
line12 = [16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57]
line13 = [86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58]
line14 = [19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40]
line15 = [4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66]
line16 = [88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69]
line17 = [4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36]
line18 = [20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16]
line19 = [20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54]
line20 = [1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48]

matrix = [line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20]

from operator import mul

largestrow = 0
largestcol = 0
largestdiag = 0
largestotherdiag = 0

#to check horizontals
guess = []
for rownumber in range(0,19):
    for offset in range(0,16):
        for a in range(0,4):
            guess.append(matrix[rownumber][a+offset])
        if reduce(mul,guess) > largestrow:
            largestrow = reduce(mul,guess)
        guess = []
print 'largest row: ',largestrow

#to check verticals
guess = []
for columnnumber in range(0,19):
    for offset in range(0,16):
        for a in range(0,4):
            guess.append(matrix[a+offset][columnnumber])
        if reduce(mul,guess) > largestcol:
            largestcol = reduce(mul,guess)
        guess = []
print 'largest col: ',largestcol

#to check diags
guess = []
for y in range(0,17):
    for x in range(0,17):
        for a in range(0,4):
            print matrix[a+y][a+x]
            guess.append(matrix[a+y][a+x])
        if reduce(mul,guess) > largestdiag:
            largestdiag = reduce(mul,guess)
        guess = []
print 'largest diag: ',largestdiag

#to check other diag
guess = []
for y in range(0,17):
    for x in range(19,2,-1):
        for a in range(0,4):
            #print matrix[y+a][x-a]
            guess.append(matrix[y+a][x-a])
        if reduce(mul,guess) > largestotherdiag:
            largestotherdiag = reduce(mul,guess)
        guess = []
print 'largest other diag: ',largestotherdiag

#print final answer
print 'largest overall: ',max([largestrow,largestcol,largestdiag,largestotherdiag])
