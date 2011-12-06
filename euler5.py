running = True
sub = True
num = 0
i = 1

while running == True:
    while sub == True:
        for i in range(1,20):
            if num%i == 0:
                sub = True
            elif i == 20:
                running = False
            else:
                sub = False
        num = num + 1
print num
