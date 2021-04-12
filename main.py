'''

4/12/21

Review

1. import turtle library
import turtle # Top pf page

2. declare turtle
var1 = turtle.Turtle()

3. declare screen (option)
var2 = turtle.Screen()

4. movements
  a. forward
  var1.forward(DISTANCE)
  var1.fd(DISTANCE)

  b. backward
  var1.backward(DISTANCE)
  var1.bk(DISTANCE)

  c. turn right
  var1.right(ANGLE)

  d. turn left
  var1.left(ANGLE)

5. pen features
  penup
  var1.penup()

  pendown
  var1.pendown()

  move to point
  var1.goto(X, Y)

  move to the origin
  var1.home()

  color
  var1.color(R,G,B or Basic Color Name or Hex Code)

  shape (arrow,turtle, circle, square, triangle)
  var1.shape(SHAPE)

  speed (0,10)
  var1.speed()
  
  write
  var1.write(TEXT,MOVE,ALIGN,STYLE)
  FONT = (FONTTYPE,FONTSIZE,FONTSTYLE)

  width (1,10)
  var1.width()

  circle
  var1.circle(RADIUS)
  var1.circle(RADIUS,ANGLE)
  var1.circle(RADIUS,ANGLE,SIDES)

  fill color
  var1.fill(R,G,B or Basic Color Name or Hex Code)
  
  var1.begin_fill()
  # SHAPE
  var1.end_fill()
'''


# Exercize 1 - DRAW A STAR
'''
import turtle
geekyTurtle = turtle.Turtle()

def drawStar(l):
  for i in range(5):
    geekyTurtle.forward(l)
    geekyTurtle.right(144)

drawStar(int(input("LENGTH : ")))
'''
# Exercize 2 - DRAWING SHAPES WITH circle()
'''
import turtle
pen = turtle.Turtle()
def drawShape(r,s):
  pen.circle(r,360,s)

drawShape(float(input("RADIUS : ")), int(input("NUMBER OF SIDES : ")))
'''
# Exercize 3 - MAKE A SPIRAL
'''
import turtle
pen = turtle.Turtle()
# List with colors
colors = ['orange','red','blue','green','cyan','purple']
# For Loop
for x in range(50):
  pen.color(colors[x % 6])
  pen.width(x / 5 + 1)
  pen.forward(x)
  pen.left(20)
'''
