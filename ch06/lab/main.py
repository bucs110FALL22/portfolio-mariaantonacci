import turtle

screen = turtle.Screen()
screen.bgcolor("white")
turtle.speed(1)
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
turtle.color("brown")

turtle.begin_fill()
for i in range(3):
  turtle.forward(200)
  turtle.left(120)