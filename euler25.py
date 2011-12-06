import math
running = True
i = 1

while running == True:
    if i*math.log(1.61803399,10)-math.log(5,10)/2 >999:
        print i
        running = False
    else:
        i = i+1
