import pygame ,sys
from Settings import *
from pygame import Vector2

class Player:
    def __init__(self):
        self.image = Player_image
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2 - self.image.get_width()//2, SCREEN_HEIGHT*0.5)
        self.MaxLife = 100
        self.Life = self.MaxLife
        self.speed = 5
        player_list.append(self)

    def __del__(self):
        player_list.remove(self)

    def move(self, game):
   #     keys = pygame.key.get_pressed()

#        if keys[pygame.K_a] and self.rect.left > 0:
#            self.rect.move_ip(-self.speed, 0)
#        if keys[pygame.K_d] and self.rect.right < SCREEN_WIDTH:
#            self.rect.move_ip(self.speed, 0)
#        if keys[pygame.K_w] and self.rect.top > 0:
#            self.rect.move_ip(0, -self.speed)
#        if keys[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT:
#            self.rect.move_ip(0, self.speed)
         
         for event in pygame.event.get():
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and self.rect.top > 0:
                   self.rect.move_ip(0, -self.speed)
                if event.key == pygame.K_s and self.rect.bottom <SCREEN_HEIGHT:
                    self.rect.move_ip(0,self.speed)
                if event.key == pygame.K_a and self.rect.left>0:
                    self.rect.move_ip(-self.speed,0)
                if event.key == pygame.K_d and self.rect.right < SCREEN_WIDTH:
                    self.rect.move_ip(self.speed,0)
                    
         

    def draw(self, game):
        game.screen.blit(self.image, self.rect.center)
        
            