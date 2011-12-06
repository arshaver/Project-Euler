import time
def ispent(number):
    pos = (1./6.)*(1+(24*number+1)**0.5)
    neg = (1./6.)*(1-(24*number+1)**0.5)
    if pos == int(pos) and pos > 0:
        return True
    elif neg == int(neg) and neg > 0:
        return True
    else:
        return False

def ishex(number):
    pos = (1./4.)*(1+(8*number+1)**0.5)
    neg = (1./4.)*(1-(8*number+1)**0.5)
    if pos == int(pos) and pos > 0:
        return True
    elif neg == int(neg) and neg > 0:
        return True
    else:
        return False

for n in range(285,100000):
    triangle = (n*(n+1))/2
    if ispent(triangle) == True and ishex(triangle)==True:
        print 'answer:',triangle

print 'time:',time.clock()
