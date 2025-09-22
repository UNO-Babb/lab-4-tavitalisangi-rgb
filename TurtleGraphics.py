#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(Jay, sides):
    for s in range(sides):
        Jay.forward(50)
        Jay.right(360/sides)

def fillCorner(turtle3, corner):
    #draw big square
    drawSquare(turtle3, 100)
    
    if corner == 1:
        turtle3.begin_fill()
        drawSquare(turtle3, 50)
        turtle3.end_fill()
    elif corner == 2:
        turtle3.forward(50)
        turtle3.begin_fill()
        drawSquare(turtle3, 50)
        turtle3.end_fill()
    elif corner == 3:
        turtle3.left(90)
        turtle3.backward(50)
        turtle3.right(90)
        turtle3.begin_fill()
        drawSquare(turtle3, 50)
        turtle3.end_fill()
    elif corner == 4:
       turtle3.forward(100)
       turtle3.right(90)
       turtle3.forward(50)
      
       turtle3.begin_fill()
       drawSquare(turtle3, 50)
       turtle3.end_fill()
       
       
def squaresInSquares(jill, x):
    size = 200
    step = size // x 
    
    for i in range(x):
        drawSquare(jill, size - i*step)
        jill.penup()
        jill.forward(step/2)
        jill.right(90)
        jill.forward(step/2)
        jill.left(90)
        jill.pendown()
  
        
       
def main():
    myTurtle = turtle.Turtle()
    
    # drawSquare(myTurtle, 100)
    
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 4) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
