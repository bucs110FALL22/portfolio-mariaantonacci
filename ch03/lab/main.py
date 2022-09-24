import turtle #1. import modules
import random
x = random.randrange(1,10)
y = random.randrange(1,10)
#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
michelangelo.forward(random.randint(0,100))
leonardo.forward(random.randint(0,100))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
for run in range(10):       
  michelangelo.forward(random.randint(0,10))
  leonardo.forward(random.randint(0,10))

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

window.exitonclick()

# PART B - complete part B here
import pygame
pygame.init()
window = pygame.display.set_mode()
import math

#triangle
num_sides=3
side_length=20
coords=[]
offset=0
for i in range(num_sides):
  theta= (2.0 * math.pi * i / num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords_tri=(x,y)
  coords.append(coords_tri)
  
#square
num_sidessq=4
coords_sq=[]
for i in range(num_sidessq):
  theta= (2.0 * math.pi * i / num_sidessq)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords_square=(x,y)
  coords.append(coords_square)

#hexagon
num_sideshex=6
coords_hex=[]
for i in range(num_sideshex):
  theta= (2.0 * math.pi * i / num_sideshex)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords_hex=(x,y)
  coords.append(coords_hex)

#nonagon
num_sidesnon=9
coords_non=[]
for i in range(num_sidesnon):
  theta= (2.0 * math.pi * i / num_sidesnon)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords_non=(x,y)
  coords.append(coords_non)

#circle
num_sidescirc=360
coords_circ=[]
for i in range(num_sidescirc):
  theta= (2.0 * math.pi * i / num_sidescirc)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords_circ=(x,y)
  coords.append(coords_circ)

window.exitonclick()