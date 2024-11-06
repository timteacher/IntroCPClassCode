from graphics import *
            #  pointleft, pointright, clickp
def checkexit(exitleft,exitright,clickp):
    leftx = exitleft.getX()
    rightx = exitright.getX()
    bottomy = exitleft.getY()
    topy = exitright.getY()
    
    clickx = clickp.getX()
    clicky = clickp.getY()
    # if the mouse click is between exitleft , exitright 
    # ==> exitflag=1
    # else                                               
    # ==> exitflag=0
    if (leftx <= clickx <= rightx) and (botttomy <= clicky <= topy):
        exitflag=1 
    else:
        exitflag=0

    return exitflag 


def main():
    win = GraphWin('Lines', 500,500)
    win.setCoords(-5,-5,5,5)

    pboxleft = Point(3.9,4.1)
    pboxright = Point(4.9,4.9)
    exitbox = Rectangle(pboxleft,pboxright)
    exitbox.draw(win)
    exittext = Text(Point(4.4,4.5),'EXIT')
    exittext.draw(win)

    p1 = Point(0,0)
    p1.draw(win)
    p2 = win.getMouse()

    exitnow = checkexit(pboxleft, pboxright, p2)

    while exitnow ==0:
        myline = Line(p1,p2)
        myline.draw(win)
        p1 = p2
        p2 = win.getMouse()
        exitnow = checkexit(pboxleft,pboxright, p2)

main()
