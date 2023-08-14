import pygame
import random
import sys
from Projectile import Projectile
pygame.init()
#加载音效
shoot =pygame.mixer.Sound("../Sound/shoot.wav")
#设置画面
size=(1080,1920)
screen =pygame.display.set_mode(size,pygame.SCALED|pygame.FULLSCREEN)
#限制帧率上限
FPS = 144
clock =pygame.time.Clock()
#创建字体对象
font = pygame.font.Font(None, 56) 
#生成玩家
player = pygame.image.load("../image/player.png")
player_rect=player.get_rect()
player_rect.center=(size[0]/2,size[1]*0.9)
#创建弹幕列表
projectiles =[]
#设置一个计时器
timer=pygame.time.set_timer(pygame.USEREVENT,100)
#主循环
while True:
    #=========保持运行==============
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit()
           #===========玩家移动============
        if event.type ==pygame.MOUSEMOTION:
            new_x = player_rect.x + event.rel[0]
            new_y = player_rect.y + event.rel[1]
              
            if new_x >= 0 and new_x + player_rect.width <= size[0]:
                
                player_rect.x = new_x
            if new_y >= 0 and new_y + player_rect.height <= size[1]:
                   player_rect.y = new_y
           #=========计时器触发======================
        if event.type == pygame.USEREVENT:
             #============生成弹幕===========
             pro =Projectile(player_rect.centerx,player_rect.centery)
             shoot.play()#播放发射音效
             projectiles.append(pro)#添加到弹幕列表
    
    #====刷新屏幕以白色填充=======
    screen.fill((255,255,255))
    #把弹幕列表里的弹幕绘制出来
    for pro in projectiles:
        pro.update(screen)
    #=========绘制玩家
    screen.blit(player,player_rect)
    # 渲染帧率文本
    fps_text = font.render("FPS: " + str(int(clock.get_fps())), True, (0, 0, 0)) 
    # 将帧率文本显示在屏幕左上角
    screen.blit(fps_text, (10, 10)) 
    #更新整个屏幕
    pygame.display.flip()
    #限制FPS
    clock.tick(FPS)
pygame.quit()
    