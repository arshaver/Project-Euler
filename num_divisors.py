def numdiv(number):
    divisors = 0
    for i in range(1,number+1):
        if number%i==0:
            divisors +=1
    return divisors
