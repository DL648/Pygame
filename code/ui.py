
import pygame , sys
from Settings import *

def DrawMuenUI(game):
   
    game.screen.blit(Game_background_image,(0,0))
    pygame.draw.rect(game.screen,color_grey,(0,0,SCREEN_WIDTH,SCREEN_HEIGHT),20)
    game.screen.blit(Game_title_image,(SCREEN_WIDTH /2  - Game_title_image.get_width()//2,SCREEN_HEIGHT*0.3))
    game.screen.blit(Game_start_image,(SCREEN_WIDTH/2-Game_start_image.get_width()//2,SCREEN_HEIGHT*0.6))
    game.screen.blit(Game_exit_image,(SCREEN_WIDTH/2-Game_exit_image.get_width()//2,SCREEN_HEIGHT*0.75))
           
    text =game.font.render(f'按键暂时没有用,游戏在{3-game.time/60:.0f}秒后开始',False,color_green)
    game.screen.blit(text,(SCREEN_WIDTH/2-text.get_width()//2,SCREEN_HEIGHT * 0.4))
    if 3- game.time/60==0:
       game.mould =Game_Mould.Play
       
       
def DrawPlayUI(game):
    
    game.screen.blit(Game_background_image,(0,0))
    pygame.draw.rect(game.screen,color_green,(0,0,SCREEN_WIDTH,SCREEN_HEIGHT),20)
               
               
               
           
          
            
            
                           
          
         
         
              
        
        