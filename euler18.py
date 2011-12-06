mastertriangle = [[75],
[95,64],
[17,47,82],
[18,35,87,10],
[20,4,82,47,65],
[19,1,23,75,3,34],
[88,2,77,73,7,63,67],
[99,65,4,28,6,16,70,92],
[41,41,26,56,83,40,80,70,33],
[41,48,72,33,47,32,37,16,94,29],
[53,71,44,65,25,43,91,52,97,51,14],
[70,11,33,28,77,73,17,78,39,68,17,57],
[91,71,52,38,17,14,91,43,58,50,27,29,48],
[63,66,4,68,89,53,67,30,73,16,69,87,40,31],
[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

triangle = mastertriangle
#n is the number of 
n = 3

#generate same size triangle full of zeros
hightriangle = []
for i in range(0,len(mastertriangle)):
    hightriangle.append([0]*(i+1))

#must first copy top 3 rows of triangle
for i in range(0,3):
    hightriangle[i] = triangle[i]

#put top 3 values from each row into hightriangle
for i in range(3,len(mastertriangle)):
    #iterate n times for top n numbers
    for z in range(1,n+1):
        #find max of the row
        maxrow = max(triangle[i])
        #put it into hightriangle in the same position
        hightriangle[i][triangle[i].index(maxrow)] = maxrow
        #replace maxrow in triangle with zero so max() can find next highest
        triangle[i][triangle[i].index(maxrow)] = 0
