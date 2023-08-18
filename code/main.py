import pygame , sys
from Settings import *
from ui import *
from player import Player

class Game:
    def __init__(self):#初始化
        
        #设置游戏窗口和标题
        self.screen =pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.SCALED)
        pygame.display.set_caption('DL648')
        
        self.clock =pygame.time.Clock()
        self.font=pygame.font.Font("..//Font/Minecraft.ttf",30)
        self.time = 0
        self.mould=Game_Mould.Menu
     
    def run(self):
        while True:
             for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     exit()
                     sys.exit()
             self.clock.tick(60)
             self.time += 1
             
             self.screen.fill(color_black)
             
             if self.mould == Game_Mould.Menu:   
                DrawMuenUI(self)
             if self.mould == Game_Mould.Play:
                if len(player_list) == 0:
                    player =Player()
             
                player.move(self)
                DrawPlayUI(self)
                player.draw(game)
             
                 
                     
             
             pygame.display.update()
         
pygame.quit()

if __name__ =='__main__':
         pygame.init()
         game = Game()
         game.run()
         
        
        