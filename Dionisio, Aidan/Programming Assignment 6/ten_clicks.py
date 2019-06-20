#ten_clicks.py
#Python 3.7.0
#Written by Aidan Dionisio
#February 25, 2019
#Draw 10 circles based on clicks.

import random
from graphics import *
win = GraphWin("ten_clicks.py", 600, 600)

clicks_left = 10
characters = ["a", "b", "c", "d", "e", "f", "1", "2", "3",
              "4", "5", "6", "7", "8", "9", "0"]

while clicks_left > 0:
    point = win.getMouse()
    radius = random.randint(10, 50)
    color = ("#" + characters[random.randint(0, 15)]
             + characters[random.randint(0, 15)]
             + characters[random.randint(0, 15)]
             + characters[random.randint(0, 15)]
             + characters[random.randint(0, 15)]
             + characters[random.randint(0, 15)])
    circle = Circle(point, radius)
    circle.setFill(color)
    circle.draw(win)
    clicks_left += -1

win.getMouse()
win.close()
