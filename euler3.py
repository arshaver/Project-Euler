#this program returns the prime factorization of a number as a list

import math

num = int(raw_input('number? : '))

running = True
guess = 2
factors = []

while running:
    if num%guess == 0 and not num == guess:
        factors.append(guess)
        num = num/guess
    elif guess == num:
        factors.append(num)
        running = False
    else:
        guess = guess + 1

print factors
