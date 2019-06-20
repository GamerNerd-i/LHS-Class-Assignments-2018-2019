#grade_calculator.py
#Python 3.7.0
#Written by Aidan Dionisio
#September 5, 2018
#Ask for percentages of the user's grades and display his/her overall grade for the class.

homework = int(input("What is your percentage for homework? "))
programs = int(input("What is your percentage for programs? "))
assessments = int(input("What is your percentage for assessments? "))

overall = str((homework*0.1)+(programs*0.2)+(assessments*0.7))

print("Your overall grade for this class is " + overall + "%.")
