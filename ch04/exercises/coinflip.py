import turtle
import random

leo = turtle.Turtle()
window = turtle.Screen()  
window.bgcolor("purple")

leo.shape("turtle")
leo.color("green")

distance=10
leo.speed(0)

while True:
  coin = random.randint(1,2)
  a=150
  b=-150
  if leo.xcor()>a or leo.xcor()<b or leo.ycor()>a or leo.ycor()<b:
    break
  elif coin==1:
    print("Heads")
    leo.left(90)
  elif coin==2:
    print("Tails")
    leo.right(90)
leo.forward(50)

leo.pu()
leo.goto(0,0)

turtle.exitonclick()