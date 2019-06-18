#So far, every line of code has gone in order.
#With if statements, not everything has to be in order.

#First, let's look at Boolean expressions.
#Boolean expresions determine whether something is True or False.

#Comparison operators function exactly like they do in math.
#Operators are ( < > == != >= <= ).
#They can also be chained, just like in math.

import random

print("Example: Print something cool depending on the number.")

num = random.randint(-20, 75)

print("num = " + str(num))

if num > 20:
    if num > 50:
        print("That's a really large number!")
    else:
        print("That's a large number.")
if num < 0:
    print("That's a negative number.")

print("Done!\n")

print("Example: Print a score checker that indicates whether you passed."
      + "\nAlso determine the letter grade of the score.\n")

score = random.randint(0,101)
print("score = " + str(score))

if score >= 60:
    print("You passed!")
else:
    print("You failed lmao rip")

#Technically you could also use "if score < 60" in place of else.
#However, this would take a little more processing power,
#so else is ultimately more efficient.

#(and, or, not) are considered logical operators.
##and requires that all conditions are met to read True.
##or requires only one condition to be met to read True.

if score >= 90:
    print("Great job nerd, you got an A.")
if score >= 80 and score < 90:
    print("Not bad bro you brought a B")
if 60 <= score < 80:
    print("You're getting there!")
if score < 20 or score > 90:
    print("You're a special one, aren't you?")

#fors and ifs can be used together to check all items in a list.
#in and not in are used in basically the way you would expect.

print("\nExample: Generate a pizza based on what we have and what is requested.")

available_toppings = ["sausage", "pepperoni", "pineapple", "green peppers", "onions"]
requested_toppings = ["sausage", "green peppers", "hot dogs"]
print(str(available_toppings) + " are available. The customer requested " +
      str(requested_toppings) + ".")

for topping in requested_toppings:
    if topping in available_toppings:
        print("Adding " + topping + " to the pizza.")
    else:
        print("We don't have " + topping + " here.")

print("Done!")
