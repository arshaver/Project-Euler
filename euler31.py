target, coins = 200, [1,2,5,10,20,50,100,200]
ways = [1] + [0 for i in xrange(200)]

for coin in coins:
    for i in xrange(coin, target+1):
        ways[i] += ways[i-coin]

print ways[target]
