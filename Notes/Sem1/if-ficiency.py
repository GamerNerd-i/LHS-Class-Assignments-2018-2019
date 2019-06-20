import random

#This is a functional, but inefficient way to check for all requirements.
#It checks way more things than we need.

###score = random.randint(-20,121)
###print("score = " + str(score) + "\n")

print("Example: Using several ifs.")
if 90 <= score <= 100:
    print("Great job nerd you got an A")
if 80 <= score < 90:
    print("Not bad bro you brought a B")
if 70 <= score < 80:
    print("I see you got a C")
if 60 <= score < 70:
    print("You got a little D")
if 0 <= score < 60:
    print("You F'n Failed")
if score > 100:
    print("There was no extra credit you cheater")
if score < 0:
    print("No one is dumb enough to get negative percent, not even you")

print("Done!\n")

#The easy solution is to use elif.
#elif essentially says to check everything until one is true, then stop.
#Therefore, you can even eliminate the (<) requirement above.
#However, doing so would require changing the order a little so that
##scores greater than 100 aren't read as a B.
#In addition, we can even make the final statement else,
##since theoretically all other values have been checked.

print("Example: Using elifs.")
if score > 100:
    print("There was no extra credit you cheater")
elif 90 <= score <= 100:
    print("Great job nerd you got an A")
elif 80 <= score:
    print("Not bad bro you brought a B")
elif 70 <= score:
    print("I see you got a C")
elif 60 <= score:
    print("You got a little D")
elif 0 <= score < 60:
    print("You F'n Failed")
else:
    print("No one is dumb enough to get negative percent, not even you")

print("Done!\n")

#% functions like /, but returns the remainder, not the quotient.

print("Example: Determine whether a given number is even or odd.")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(str(num) + " is even.")
else:
    print(str(num) + " is odd.")
