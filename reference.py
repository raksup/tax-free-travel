
import pygame
import random
import os
import time
from random import choices
from random import randint

pygame.init()
a = 0
b = 0
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")
done = False
n = 0
x = 0
y = 0
x_wall = 0
y_wall = 0
clock = pygame.time.Clock()
WHITE = (255,255,255)
RED = (255,0,0)
change_x = 0
change_y = 0
HW = width / 2
HH = height / 2
background = pygame.image.load('mountains.png')

#player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load("character.png")
      self.rect = self.image.get_rect()
      self.rect.x = width / 2
      self.rect.y = height / 2

#enemy class
class Enemy(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("enemy.png")
    self.image = pygame.transform.scale(self.image, (int(50), int(50)))
    self.rect = self.image.get_rect()
    self.rect.x = width / 3
    self.rect.y = height / 3

#wall class
class Wall(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("wall.png")
    self.image = pygame.transform.scale(self.image, (int(50), int(50)))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y