import pygame

Projectile_list =[]
NPC_list =[]

def UpdateNPC():
    for npc in NPC_list:
        npc.Update()
        
def UpdateDraw(screen):
    for npc in NPC_list:
        screen.blit(npc.Image,(npc.Position.x,npc.Position.y))
        
        
def NewNpc(class_name):
    modlue =__import__(class_name)
    cls = getattr(modlue,class_name)
    inst = cls()
    return inst