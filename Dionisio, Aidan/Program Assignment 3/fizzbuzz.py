#fizzbuzz.py
#Python 3.7.0
#Written by Aidan Dionisio
#October 3, 2018
#Given a positive integer, print all numbers from 1 to that integer,
##with special rules concerning multiples of 5 and 3.

maximum = int(input("Enter a number: "))
values = list(range(1, maximum + 1))

for val in values:
    if val % 3 == 0 and val % 5 == 0:
        print("FizzBuzz")
    elif val % 3 == 0:
        print("Fizz")
    elif val % 5 == 0:
        print("Buzz")
    else:
        print(val)
