import pygame
import random
from pygame import Vector2
from Settings import *

class NPC:
    def __init__(self):
        self.image =pygame.image.load('..//images/Ninja.png')
        self.rect=self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        self.vec=Vector2(random.randint(-5,5),random.randint(-5,5))
        NPC_list.append(self)
        self.type =len(NPC_list)
        self.font =pygame.font.Font(MyFont_Pull,20)
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)
                
    def up(self):
       
       self.rect.move_ip(self.vec)
       if self.check_OnScreen(SCREEN_WIDTH,SCREEN_HEIGHT):
          
           self.rect.center= (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
          
                
    def check_OnScreen(self, screen_width, screen_height):
       if self.rect.right >= screen_width or self.rect.left <= 0 or self.rect.bottom >= screen_height or self.rect.top <= 0:
          
         
         return True
         
       return False  
         
             
             
             
             
        
            
        
