def factor(n):
	if n == 1: return [1]
	i = 2
	limit = n**0.5
	while i <= limit:
		if n % i == 0:
			ret = factor(n/i)
			ret.append(i)
			return ret
		i += 1
	return [n]

print factor(1000000)