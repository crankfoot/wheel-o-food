import random, sys

options = ["BEC","MEATSAWS PASTA", "SAUSAGE PASTA", "BURGERS", "BRATS", "CHOOSE AGAIN"]
options.append("PIZZA!")
black = [0 for a in options]
count = 40000

options = [o.lower() for o in options]

for a in range(count):
    sys.stdout.write("\r")
    sys.stdout.write(str(count-a)+ " ")
    black[random.randrange(len(options))] += 1
    for b in range(len(options)):
        string = options[b]
        if black[b] == max(black):
            string = string.upper()
        sys.stdout.write(string+" "+str(black[b])+" ")
    sys.stdout.flush()

input()
