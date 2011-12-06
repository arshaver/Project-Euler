running = True
i = 8
max = 100
triangle = 28

while running == True:
    triangle = triangle + i
    i += 1
    print triangle
    if i > max:
        running = False
