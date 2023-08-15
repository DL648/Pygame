import main
import pygame
import random
from pygame import Vector2

pygame.init()

size=(1080,1920)
screen=pygame.display.set_mode(size,pygame.SCALED|pygame.FULLSCREEN)

text_size =50
text_pull ="..//Font/Minecraft.ttf"
text_color = (0,0,0)
font =pygame.font.Font(text_pull,text_size)
text =font.render("这是神魔？",True,text_color)



clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
            
            
            
    if len(main.NPC_list)<100000:
        vec=Vector2(random.randint(0,900),100)    
        npc=main.NewNpc("ttf",vec)
    screen.fill((255,255,255))
    screen.blit(text,(0,0))
    
    fps = clock.get_fps()
    fps_text = font.render("FPS: {:.0f}".         format(fps), True, text_color)
    screen.blit(fps_text, (600, 1800))
    
    npc_count =len(main.NPC_list)
    npc_count_text =font.render(f"有{npc_count}个星星",True,text_color)
    
    screen.blit(npc_count_text,(screen.get_width()-npc_count_text.get_width(),0))
   
    main.UpdateNPC()
    main.UpdateDraw(screen)
    clock.tick(144)
    pygame.display.update()
