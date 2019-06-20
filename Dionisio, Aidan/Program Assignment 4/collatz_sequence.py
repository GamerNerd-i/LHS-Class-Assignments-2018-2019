#collatz_sequence.py
#Python 3.7.0
#Written by Aidan Dionisio
#October 8, 2018
#Generate and print the Collatz sequence (x/2 if even, 3x+1 if odd
##for a provided number.

start = int(input("Enter a number: "))

print("The Collatz sequence for " + str(start) + " is " + str(start), end="")

while start >= 1:
    if start == 1:
        print(".")
        start = start - 1
    else:
        print(", ", end = "")
        if start % 2 == 0:
            start = start // 2
            print(str(start), end = "")
        else:
            start = (3 * start) + 1
            print(str(start), end = "")
