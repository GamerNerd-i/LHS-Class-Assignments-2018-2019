#speeding_ticket.py
#Python 3.7.0
#Written by Aidan Dionisio
#October 3, 2018
#Given a speed and the speed limit, decide whether the speed was legal and
##calculate the fine, if any.

speed_limit = int(input("What is the speed limit? "))
clocked_speed = int(input("What is the driver's speed? "))

if clocked_speed > speed_limit:
    fine = 50 + 5*(clocked_speed - speed_limit)
    if clocked_speed > 90:
        fine = fine + 200
        print("Going " + str(clocked_speed) + " MPH in a " + str(speed_limit) +
          " MPH zone is a $" + str(fine) + " fine.")
    else:
        print("Going " + str(clocked_speed) + " MPH in a " + str(speed_limit) +
          " MPH zone is a $" + str(fine) + " fine.")
else:
    print("That is a legal speed in this zone.")
