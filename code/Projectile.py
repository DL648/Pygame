import random
import pygame
class Projectile :
    
    def __init__(self,x,y):
        path = "../image/Projectile.png"
        self.image = pygame.image.load(path)
        self.rect =self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
        
  
    def update(self,screen):
        screen.blit(self.image, self.rect)
        self.rect.y-=5
        
    