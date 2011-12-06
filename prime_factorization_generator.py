def primefactors(number):
    running = True
    guess = 2
    factors = []

    while running:
        if number%guess == 0 and not number == guess:
            factors.append(guess)
            number = number/guess
        elif guess == number:
            factors.append(number)
            running = False
        else:
            guess = guess + 1
    return factors
