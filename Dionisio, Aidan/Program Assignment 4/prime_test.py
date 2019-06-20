#prime_test.py
#Python 3.7.0
#Written by Aidan Dionisio
#October 8, 2018
#Check whether a given number is prime or composite.

import math

val = int(input("Enter a number to determine whether it is prime or composite: "))
check = 2

while check <= math.sqrt(val):
    if val % check != 0:
        check = check + 1
        if check <= math.sqrt(val):
            check = check
        elif check > math.sqrt(val):
            print("The number " + str(val) + " is a prime number.")
    elif val % check == 0:
        print("The number " + str(val) + " is a composite number.")
        check = check + math.sqrt(val)
