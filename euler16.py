def fact(x): return (1 if x==0 else x * fact(x-1))

x = fact(100)

x = str(x)

sum = 0

for i in range(0,len(x)):
    sum = sum + int(x[i])
    
