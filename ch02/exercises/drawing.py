import turtle

my_turtle = turtle.Turtle()

my_turtle.shape("turtle")
my_turtle.color("purple")

num_sides= int(input("please enter the number of sides: "))
length_sides= int(input("please enter the length of sides: "))

for i in[length_sides]*num_sides:
  my_turtle.forward(length_sides)
  my_turtle.left(i)

window.exitonclick()