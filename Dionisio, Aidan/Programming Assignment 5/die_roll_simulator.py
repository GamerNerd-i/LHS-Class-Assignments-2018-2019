#die_roll_simulator.py
#Python 3.7.0
#Written by Aidan Dionisio
#October 31, 2018
#Simulate rolling a die a user-given number of times, then print
##the total times a number was rolled and the percentage of the total rolls it is.

import random

rolls = {1: 0,
         2: 0,
         3: 0,
         4: 0,
         5: 0,
         6: 0}

total = int(input("How many times would you like to roll the die? "))

for roll in range(1, (total + 1)):
    roll = random.randint(1, 6)
    rolls[roll] += 1

print("Here are the results:")

for val in rolls.keys():
    percent = round(((rolls[val] / total)*100), 1)
    print(str(val) + " was rolled " + str(rolls[val]) + " times, which is " +
          str(percent) + "% of all rolls.")
