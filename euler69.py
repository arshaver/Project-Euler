primes = [2,3,5,7,11,13,17,19,23,27,31,37,41]
limit=10**6
max = 1
for p in primes:
  if max * p > limit: break
  max *= p
print "Answer to PE69 = ", max