import pygame , sys
from Settings import *
from player import Player
from npc import NPC

class Game:
    def __init__(self):
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.SCALED)
        self.colck = pygame.time.Clock()
        self.font = pygame.font.Font(MyFont_Pull,50)
        self.tick =0
    def run(self):  
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                    sys.exit()
            
            
            
            self.tick +=1
            
            NPC_list_count =self.font.render(f'忍者数量{len(NPC_list)}',False,'red')      
            FPS = self.font.render(f'FPS:{self.colck.get_fps():.0f}',False,'red')        
            if len(NPC_list)<Max_NPC and self.tick % 5 ==0:
               npc =NPC()           
            tick =self.colck.tick(60)
            self.screen.fill((255,255,255))
            
           
            self.screen.blit(NPC_list_count,(0,0))
            self.screen.blit(FPS,(self.screen.get_width()-FPS.get_width(),self.screen.get_height()-FPS.get_height()*1.5))
            
            if len(NPC_list)>=1:
                for npc in NPC_list:
                    npc.up()
                    npc.draw(self.screen)
                  #  pygame.draw.rect(self.screen,'red',npc.rect,2)
                  #  pygame.draw.line(self.screen,'Green',(SCREEN_WIDTH,0),npc.rect.center)
            
            pygame.display.update()    
            
            
if __name__ == '__main__':
     pygame.init()
     
     game =Game()
     game.run()

        
        
    
