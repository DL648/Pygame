
import pygame ,sys
from Settings import *
from pygame import Vector2

class Player:
    def __init__(self):
        self.image = Player_image
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2 - self.image.get_width()//2,SCREEN_HEIGHT*0.95)
        self.MaxLife =100
        self.Life =self.MaxLife
        player_list.append(self)
        
        
    def __del__(self):
        player_list.remove(self)
    
    def move(self,game):
         event = pygame.event.poll()
         if event.type == pygame.MOUSEMOTION:
            
            self.rect.move_ip(event.rel)
          
          
           
            
    def draw(self,game):
        
        game.screen.blit(self.image,self.rect.center)
        
        
            