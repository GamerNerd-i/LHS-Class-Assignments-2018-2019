#while_print.py
#Python 3.7.0
#Written by Aidan Dionisio
#October 8, 2018
#Generate and print a list of 15 random integers on the same line.

import random

vals = list()

while len(vals) < 15:
    vals.append(random.randint(1,30))

while len(vals) != 0:
    if len(vals) == 1:
        print(vals.pop(0))
    else:
        print(vals.pop(0), end=", ")

print("Done")
