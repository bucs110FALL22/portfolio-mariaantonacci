import pygame
import random
import math

width=400
height=400

pygame.init()
window = pygame.display.set_mode()
windowsize = pygame.display.get_window_size()

black=[0,0,0]
red=[255, 48, 48, 255]
blue=[100, 149, 237, 255]
green=[34, 139, 34, 255]
yellow=[255, 255, 224, 255]
pink=[255, 20, 147, 255]

x=random.randrange(0, windowsize[0])
y=random.randrange(0, windowsize[1])

center_x=windowsize[0]/2
center_y=windowsize[1]/2
radius = center_y

pygame.draw.circle(window, 'red', (center_x,center_y), radius)
pygame.draw.line(window, 'blue', [0, center_y], [windowsize[0], center_y])
pygame.draw.line(window, 'blue', [center_x, 0], [center_x, windowsize[1]])

print(windowsize[0])
print(windowsize[1])

player1=0
player2=0
player1pink=pink
player2yellow=yellow
color3=green

distance_center = math.hypot(windowsize[0]/2-x, windowsize[1]/2-y)
print(distance_center)

choice=int(input("Choose  player 1 or 2: "))

is_in_circle = distance_center<=radius
print(is_in_circle)

for i in range(10):
  x = random.randrange(0, windowsize[0])
  y = random.randrange(0, windowsize[1])
  distance_center = math.hypot(windowsize[0]/2-x, windowsize[1]/2-y)
  if distance_center < radius:
     pygame.draw.circle(window, player1pink, (x,y), 2)
     player1 += 1
  else:
     pygame.draw.circle(window, color3, (x,y), 2)

  x = random.randrange(0, windowsize[0])
  y = random.randrange(0, windowsize[1])
  pygame.draw.circle(window, 'black', (x,y), 2)
  distance_center = math.hypot(windowsize[0]/2-x, windowsize[1]/2-y)
  if distance_center < radius:
    pygame.draw.circle(window, player2yellow, (x,y), 2)
    player2 += 1
  else:
    pygame.draw.circle(window, color3, (x,y), 2)
    pygame.display.flip()
  if player1 > player2:
   print("Player 1 won")
   print("you predicted correctly") if choice == 1 else print("you   predicted incorrectly")
  elif player1 < player2:
   print("Player 2 won")
   print("you predicted correctly") if choice == 2 else print("you   predicted incorrectly")
  elif player1 == player2:
   print("TIE!")

pygame.time.wait(50000)