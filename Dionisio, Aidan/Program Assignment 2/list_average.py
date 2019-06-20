#list_average.py
#Python 3.7.0
#Written by Aidan Dionisio
#September 12, 2018
#Print the length, sum, product, and average of a randomly
#generated list of numbers.

import random

values = []
val_items = random.randint(1,20)

for val in range(val_items):
    values.append(random.randint(1,20))

print(values)

sum_ = 0
for val in values:
    sum_ = val + sum_

avg = sum_ / val_items

prod = 1
for val in values:
    prod = val * prod



print("This list contains " + str(val_items) + " numbers.")
print("The sum of the values in this list is " + str(sum_) + ".")
print("The product of the values in this list is " + str(prod) + ".")
print("The average of the values un this list is " + str(avg) + ".")
