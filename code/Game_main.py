import main
import pygame
import random
from pygame import Vector2

pygame.init()

size=(1080,1920)
#screen =pygame.display.set_mode(size)
screen=pygame.display.set_mode(size,pygame.SCALED|pygame.FULLSCREEN)

text_size =50
text_pull ="..//Font/Minecraft.ttf"
text_color = (0,0,0)
font =pygame.font.Font(text_pull,text_size)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
            
            
            
    if len(main.NPC_list)<255:
        vec=Vector2(random.randint(100,screen.get_width()-100),random.randint(100,screen.get_height()-100))   
        npc=main.NewNpc("ttf",vec)
        
    screen.fill((255,255,255))
    
    fps = clock.get_fps()
    fps_text = font.render("FPS: {:.0f}".format(fps), True, text_color)
    screen.blit(fps_text, (5, 5))
    
    npc_count =len(main.NPC_list)
    npc_count_text =font.render(f"有{npc_count}个星星",True,text_color)
    
    screen.blit(npc_count_text,(screen.get_width()-npc_count_text.get_width()+5,5))
   
    main.UpdateNPC()
    main.UpdateDraw(screen)
    clock.tick(60)
    pygame.display.update()

pygame.quit()
