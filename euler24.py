def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]


permlist = []

for p in all_perms([0,1,2,3,4,5,6,7,8,9]):
	permlist.append(int(str(p[0])+str(p[1])+str(p[2])+str(p[3])+str(p[4])+str(p[5])+str(p[6])+str(p[7])+str(p[8])+str(p[9])))

permlist.sort()
print permlist[999999]