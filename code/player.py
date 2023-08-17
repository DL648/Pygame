import pygame
from Settings import *

class Player:
      def __init__(self):
          self.image=pygame.Surface((30,60))
          self.rect = self.image.get_rect()
          self.speed = 288
      def update(self,tick):
          pass
      
      def draw(self,screen):
          screen.blit(self.image,self.rect)
          
      def move(self,tick):
          pass
          