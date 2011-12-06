n = int(raw_input('n: '))

numbers = []
primes = [2]

for i in range(2,n+1):
    numbers.append(i)


for i in range(1,int(n**.5+1)):
    if numbers[i]%primes[len(primes)-1] == 0:
        primes.append(numbers[i])
        numbers.pop(i)
        
print primes
