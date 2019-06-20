#dice_simulator.py
#Python 3.7.0
#Written by Aidan Dionisio
#November 2, 2018
#Roll 2 dice a given number of times, add their values,
##then print the actual and expected results.

import random

expected = {2: 2.78,
            3: 5.56,
            4: 8.33,
            5: 11.11,
            6: 13.89,
            7: 16.67,
            8: 13.89,
            9: 11.11,
            10: 8.33,
            11: 5.56,
            12: 2.78}

actual = {}
for num in range(2, 13):
    actual[num] = 0

rolls = int(input("How many times would you like to roll the dice? "))

for roll in range(1, (rolls+1)):
    roll = random.randint(1,6) + random.randint(1,6)
    actual[roll] += 1

print("\nHere are the results:\n")

for result in actual.keys():
    percent = str(round((actual[result] / rolls) * 100, 2))
    perfect = str(round(rolls * (expected[result] / 100), 0))
    print(str(result) + " was rolled " + str(actual[result]) + " times, which is "
          + percent + "% of all rolls.")
    print(str(result) + " was expected " + perfect +  " times, which would be " +
          str(expected[result]) + "% of all rolls.\n")
