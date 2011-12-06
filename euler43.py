def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

sum = 0

for p in all_perms(['0','1','2','3','4','5','6','7','8','9']):
	if (int(p[1]+p[2]+p[3]))%2==0 and (int(p[2]+p[3]+p[4]))%3==0 and (int(p[3]+p[4]+p[5]))%5==0 and (int(p[4]+p[5]+p[6]))%7==0 and (int(p[5]+p[6]+p[7]))%11==0 and (int(p[6]+p[7]+p[8]))%13==0 and (int(p[7]+p[8]+p[9]))%17==0:
		sum += int(str(p[0]+p[1]+p[2]+p[3]+p[4]+p[5]+p[6]+p[7]+p[8]+p[9]))
		print int(str(p[0]+p[1]+p[2]+p[3]+p[4]+p[5]+p[6]+p[7]+p[8]+p[9]))
		
print sum