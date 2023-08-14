import pygame
import random
import sys
from Projectile import Projectile
pygame.init()

shoot =pygame.mixer.Sound("../Sound/shoot.wav")
size=(1080,1920)
screen =pygame.display.set_mode(size,pygame.SCALED|pygame.FULLSCREEN)

player = pygame.image.load("../image/player.png")
player_rect=player.get_rect()
player_rect.center=(size[0]/2,size[1]*0.9)

projectiles =[]
timer=pygame.time.set_timer(pygame.USEREVENT,100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit()
        if event.type ==pygame.MOUSEMOTION:
            new_x = player_rect.x + event.rel[0]
            new_y = player_rect.y + event.rel[1]
                # 检测是否超出屏幕边界
            if new_x >= 0 and new_x + player_rect.width <= size[0]:
                
                player_rect.x = new_x
            if new_y >= 0 and new_y + player_rect.height <= size[1]:
                   player_rect.y = new_y
    
        if event.type == pygame.USEREVENT:
             pro =Projectile(player_rect.centerx,player_rect.centery)
             shoot.play()
             
             projectiles.append(pro)
    
    screen.fill((255,255,255))
    for pro in projectiles:
        pro.update(screen)
    screen.blit(player,player_rect)
    pygame.display.flip()