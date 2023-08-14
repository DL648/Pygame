import pygame
Projectiles = []

class Projectile:
    
   
    
    def __init__(self,x,y):
        path = "../image/Projectile.png"
        self.image = pygame.image.load(path)
        self.rect =self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
        self.timelife=60
        Projectiles.append(self)
    
    def update(self,screen):
        screen.blit(self.image, self.rect)
        self.rect.y-=5
        self.timelife-=1
        if self.timelife<0:
            self.rect.y+=5
            Projectiles.remove(self)
            del self
