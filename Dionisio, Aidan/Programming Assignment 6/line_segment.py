#line_segment.py
#Python 3.7.0
#Written by Aidan Dionisio
#February 22, 2019
#Draw a line segment based on user clicks, then display information about it.

from graphics import *
win = GraphWin("line_segment.py", 600, 600)

#Create the points.
p1 = win.getMouse()
p1.draw(win)
p2 = win.getMouse()
segment = Line(p1, p2)
segment.draw(win)
midpoint = segment.getCenter()
midpoint.setFill("red")
midpoint.draw(win)

#Show coordinates of endpoints and midpoint.
p1t = Point(p1.getX(), (p1.getY() + 10))
p2t = Point(p2.getX(), (p2.getY() + 10))
mt = Point(midpoint.getX(), (midpoint.getY() + 10))
co1 = "(" + str(p1.getX()) + ", " + str(p1.getY()) + ")"
co2 = "(" + str(p2.getX()) + ", " + str(p2.getY()) + ")"
coM = "(" + str(midpoint.getX()) + ", " + str(midpoint.getY()) + ")"
Text(p1t, co1).draw(win)
Text(p2t, co2).draw(win)
Text(mt, coM).draw(win)

#Calculate the length and slope of the line.
m = (p2.getY() - p1.getY()) / (p2.getX() - p1.getX())
length = (((p2.getY() - p1.getY())**2) + ((p2.getX() - p1.getX())))**(1/2)
Text(Point(300, 50), "Slope: " + str(m)).draw(win)
Text(Point(300, 100), "Length: " + str(length)).draw(win)

win.getMouse()
win.close()
