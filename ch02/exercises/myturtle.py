import turtle

# from turtle import Turtle
# my_turtle = Turtle()

my_turtle = turtle.Turtle()

my_turtle.shape("turtle")
my_turtle.color("purple")

num_sides= int(input("please enter the number of sides: "))
my_turtle.color("purple")
length=50
angle= 360 / num_sides

for i in[angle]*num_sides:
  my_turtle.forward(length)
  my_turtle.left(i)

my_turtle.up()
my_turtle.forward(100)
my_turtle.down()

num_sides= int(input("please enter the number of sides: "))
my_turtle.color("red")
length=50
angle= 360 / num_sides

for i in[angle]*num_sides:
  my_turtle.forward(length)
  my_turtle.left(i)
  
window.exitonclick()