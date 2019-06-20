#leap_year.py
#Python 3.7.0
#Written by Aidan Dionisio
#October 3, 2018
#Determine whether a given year is a leap year.

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        century = year / 100
        if century % 4 == 0:
            print("The year " + str(year) + " is a leap year.")
        else:
            print("The year " + str(year) + " is not a leap year.")
    else:
        print("The year " + str(year) + " is a leap year.")
else:
    print("The year " + str(year) + " is not a leap year.")
