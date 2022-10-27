import turtle

lightblue=[191, 239, 255, 255]

screen = turtle.Screen()
turtle.speed(10)

window = turtle.Screen()
window.bgcolor("lightblue")

#Sun
def sun():
  turtle.pencolor("orange")
  turtle.penup()
  turtle.goto(-200,50)
  turtle.pendown()
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
  turtle.color("black","brown")

#Roof
def roof():
  turtle.begin_fill()
  for i in range(3):
    turtle.forward(200)
    turtle.left(120)
  turtle.end_fill()
  turtle.fillcolor("grey")
  turtle.right(90)

#Base
def base():
  turtle.begin_fill()
  for i in range (3):
    turtle.forward(200)
    turtle.left(90)
  turtle.end_fill()
  turtle.color("black","brown")
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
  sun()
  roof()
  base()
  door()
  
  screen.exitonclick()

main()