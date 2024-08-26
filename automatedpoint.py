import graphics


# creates a "GraphWin" object 
win = graphics.GraphWin("Example",1000,500)

win.setBackground("white")

# created a point at (500,250)
point1 = graphics.Point(500,250)
# draws point1 onto win
point1.draw(win)

for i in range(250,500):
    point1 = graphics.Point(500,i)
    # draws point1 onto win
    circ = graphics.Circle(point1,20)
    list = ["blue","red","green"]
    circ.setFill(list[i%3])
    circ.draw(win)

# creates a point at (100,280)
center = graphics.Point(300,280)
# creates a circle with a center at "center" with radius 100
circ = graphics.Circle(center, 100)
# fill the circ blue
circ.setFill("blue")
# draws circ onto win
circ.draw(win)

win.getMouse()

win.close()