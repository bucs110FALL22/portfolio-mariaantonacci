import pygame
import random
import math

width=400
height=400

pygame.init()
window = pygame.display.set_mode((width, height))

black=[0,0,0]
red=[255, 48, 48, 255]
blue=[100, 149, 237, 255]
green=[34, 139, 34, 255]
yellow=[255, 255, 224, 255]
pink=[255, 20, 147, 255]

red_button_box = pygame.Rect(0, height/4, height/2, width/2)
blue_button_box = pygame.Rect(0, 0, height/2, width/2)
blue_button_box.topleft = red_button_box.topright
red_button = pygame.draw.rect(window, red, red_button_box)
blue_button = pygame.draw.rect(window, blue, blue_button_box)
pygame.display.flip()

selection=0
print("Who do you think will win?")
while selection==0:
  for event in pygame.event.get():
    if event.type == pygame.buttondown:
       mouse_click_pos = event.pos
      if red_button_box.point(mouse_click_pos):
        guess=1
      if blue_button_box.point(mouse_click_pos):
        guess=2

screen.fill(pink)
pygame.draw.circle(screen, yellow, (height/2, width/2), height/2)
pygame.draw.line(screen, black, (0, height/2), (width, height/2))
pygame.draw.line(screen, black, (width/2, 0), (width/2, height))
pygame.display.flip()

p1score = 0
p2score = 0

