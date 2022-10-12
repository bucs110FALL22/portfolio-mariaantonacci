import turtle

window=turtle.Screen()
window.bgcolor('pink')
my_turtle=turtle.Turtle()
my_turtle.color('green')

my_turtle.speed(1)

num_sides=int(input("How many sides?: "))
side_length=int(input("What length are the sides?: "))

turtle.penup()
turtle.goto(0,0)

def drawEqShape(turtle, num_sides, side_length):
  turn_angle = 360/num_sides
  turtle.pendown()
  
  for i in range (num_sides):
    turtle.forward(side_length)
    turtle.right(turn_angle)


drawEqShape(my_turtle, num_sides, side_length)
window.exitonclick()
  