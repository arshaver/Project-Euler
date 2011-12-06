import itertools,math
#generate cubes
cubes = []
for i in xrange(1,100000):
	cubes.append(i**3)


def permute(cube):
	permutations = []
	for permutation in itertools.permutations(str(cube),len(str(cube))):
		permutations.append(int("".join(permutation)))
	return permutations

precube = 0
while True:
	precube +=1
	print precube
	cube = precube**3
	permutations = permute(cube)
	count = 0
	for permutation in permutations:
		if permutation in cubes:
			count +=1
	if count == 5:
		print cube
		break