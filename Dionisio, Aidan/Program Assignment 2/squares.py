#squares.py
#Python 3.7.0
#Written by Aidan Dionisio
#September 17, 2018
#Print the numbers 1 through 10, their squares, and a random number
#between the number and its square.

import random

values = list(range(1,11))

print(values)

for val in values:
    square = val**2
    print(str(val) + "\t" + str(square) + "\t" + str(random.randint(val, square)))
