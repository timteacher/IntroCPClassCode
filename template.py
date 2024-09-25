import graphics
def screen1(w):
    """p = graphics.Point(500,250)
    i = graphics.Image(p, "Zelle-Logo.png")"""

    pt = graphics.Point(350,250)
    t = graphics.Text(pt,"Hello")

    tl = graphics.Point(250,40)
    br = graphics.Point(490,80)
    box = graphics.Rectangle(tl,br)
    box.setFill("white")
    #i.draw(win)
    box.draw(w)
    t.draw(w)

def screen2(w):
    tl = graphics.Point(250,40)
    br = graphics.Point(300,80)
    box = graphics.Rectangle(tl,br)
    box.setFill("red") 
    tl = graphics.Point(250, 120)
    br = graphics.Point(300, 160)
    box2 = graphics.Rectangle(tl,br)
    box2.setFill("red")
    box.draw(w)
    box2.draw(w)
    

def skill(win): 
    skip = 2
    st = 0
    sp = 0
    while skip>0:
        #print("you have 2 skill points") drawing text somewhere
        numst = graphics.Text(graphics.Point(220,60),str(st))
        numst.draw(win)
        numsk = graphics.Text(graphics.Point(220, 140), str(sp))
        numsk.draw(win)
        mc = win.getMouse()
        x = mc.getX()
        y = mc.getY()
        numst.undraw()
        numsk.undraw()
        if (250<x and x<300 and 40<y and y<80):#check if in st "+"
            st+=1
            skip-=1
        elif (250<x and x<300 and 120<y and y<160): #check if in sk 
            sp+=1
            skip-=1
    numst = graphics.Text(graphics.Point(220,60),str(st))
    numst.draw(win)
    numsk = graphics.Text(graphics.Point(220, 140), str(sp))
    numsk.draw(win)
    return st, sp    
    
# creates a "GraphWin" object 

win = graphics.GraphWin("Example",1000,500)
win.setBackground("black")
screen1(win)
gameRunning = True
while gameRunning:
    uc = win.getMouse()
    x = uc.getX()
    y = uc.getY()
    if (x>250 and x<490) and (y>40 and y<80):
        print("Click succeeded")
        gameRunning=False  
win.setBackground("white")

screen2(win)
skill(win)

win.getMouse()

win.close()