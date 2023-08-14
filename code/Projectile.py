import pygame
from main import Projectiles
class Projectile :
    
    
    timelife=5 
    def __init__(self,x,y):
        path = "../image/Projectile.png"
        self.image = pygame.image.load(path)
        self.rect =self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
        Projectiles.append(self)
        
  
    def update(self,screen):
        screen.blit(self.image, self.rect)
        self.rect.y-=5
        self.timelife-=1
        if self.timelife==0:
            
            del self
        
    