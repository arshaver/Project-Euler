
while solved == False:

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

    
