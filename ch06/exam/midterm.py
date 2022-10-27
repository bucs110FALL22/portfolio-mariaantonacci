import turtle

def background(screen):
   x_pos = 800
   y_pos = 800
   screen.screensize(x_pos,y_pos,"white")

screen = turtle.Screen()
turtle.speed(1)

turtle.pencolor("orange")
turtle.penup()
turtle.goto(-200,50)
turtle.pendown()

#Sun
def sun():
  turtle.fillcolor("yellow")
  turtle.begin_fill()
  turtle.circle(50)
  turtle.end_fill()
  for i in range (18):
    turtle.right(90)
    turtle.forward(40)
    turtle.back(40)
    turtle.left(90)
    turtle.circle(50,20)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.color("black","yellow")

#Roof
def roof():
  turtle.begin_fill()
  for i in range(3):
    turtle.forward(200)
    turtle.left(120)
  turtle.end_fill()
  turtle.fillcolor("pink")
  turtle.right(90)

#Base
def base():
  turtle.begin_fill()
  for i in range (3):
    turtle.forward(200)
    turtle.left(90)
  turtle.end_fill()
  turtle.color("black","orange")
  turtle.penup()
  turtle.goto(80,-120)
  turtle.pendown()

#door
def door():
  turtle.begin_fill()
  for i in range (2):
    turtle.left(90)
    turtle.forward(82)
    turtle.left(90)
    turtle.forward(40)
  turtle.end_fill()

def main():
  my_turtle = turtle.Turtle() 
  my_turtle.shape('turtle')
  my_turtle.speed(0)
  turtle.speed(0)
  screen = turtle.Screen()
  background(screen)
  sun()
  roof()
  base()
  door()
  
  screen.exitonclick()

main()