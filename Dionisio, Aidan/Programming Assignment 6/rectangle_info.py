#rectangle_info.py
#Python 3.7.0
#Written by Aidan Dionisio
#February 25, 2019
#Draw a rectangle based on user clicks, then print its perimeter and area.

from graphics import *
win = GraphWin("rectangle_info.py", 600, 600)

#Get points. Draw the rectangle.
p1 = win.getMouse()
p2 = win.getMouse()
Rectangle(p1, p2).draw(win)

#Get side lengths.
height = p2.getY() - p1.getY()
width = p2.getX() - p1.getX()

if height < 0:
    height = height * -1
if width < 0:
    width = width * -1

#Calculate and display perimeter and area.
area = height * width
perimeter = 2*(height + width)
Text(Point(300, 50), "Area: " + str(area)).draw(win)
Text(Point(300, 100), "Perimeter: " + str(perimeter)).draw(win)

win.getMouse()
win.close()
