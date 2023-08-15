import main
import pygame
from pygame import Vector2
pygame.init()

size=(1080,1920)
screen=pygame.display.set_mode(size,pygame.SCALED|pygame.FULLSCREEN)

npc =main.NewNpc("ttf")
npc1=main.NewNpc("ttf")
npc1.Position=Vector2(300,300)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
   
   
    screen.fill((255,255,255))
    main.UpdateNPC()
    main.UpdateDraw(screen)
    pygame.display.update()
