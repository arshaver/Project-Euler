b = ''
for n in range(1,1000000):
	b = b + str(n)

print int(b[1-1])*int(b[10-1])*int(b[100-1])*int(b[1000-1])*int(b[10000-1])*int(b[100000-1])*int(b[1000000-1])