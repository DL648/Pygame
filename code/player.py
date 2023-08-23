
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
        self.vec =Vector2(0,0)
        
    def __del__(self):
        player_list.remove(self)
    
    def move(self,game):
        if self.rect.left<0:
            self.rect.left=0
        elif self.rect.right>game.screen.get_width():
            self.rect.right=game.screen.get_width()
        if self.rect.top<0:
            self.rect.top=0
        elif self.rect.top>game.screen.get_height():
         self.rect.top=game.screen.get_height()
           
        self.rect.center = pygame.mouse.get_pos()
       
        
            
    def draw(self,game):
        
        game.screen.blit(self.image,self.rect.center)
        
        
            