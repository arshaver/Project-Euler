allnumbers = []
somenumbers = []

for a in range(2,101):
    for b in range(2,101):
        allnumbers.append(a**b)

print len(allnumbers)

for i in range(0,len(allnumbers)):
    if allnumbers[i] not in somenumbers:
        somenumbers.append(allnumbers[i])

print len(somenumbers)
