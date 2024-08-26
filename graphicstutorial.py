import graphics


# creates a "GraphWin" object 
win = graphics.GraphWin("Example",1000,500)

win.setBackground("white")

# created a point at (500,250)
point1 = graphics.Point(500,250)
# draws point1 onto win
point1.draw(win)

# creates a point at (100,280)
center = graphics.Point(300,280)
# creates a circle with a center at "center" with radius 100
circ = graphics.Circle(center, 100)
# fill the circ blue
#circ.setFill("blue")
circ.setOutline("red")
# draws circ onto win
circ.draw(win)

point1 = graphics.Point(100,200)
point2 = graphics.Point(100,400)
lin = graphics.Line(point1,point2)
lin.draw(win)

win.getMouse()

win.close()