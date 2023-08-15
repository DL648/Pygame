from Entity import Entity
from abc import ABC,abstractmethod
from main import NPC_list
import pygame
class NPC(Entity):
        
        def __init__(self):
            super().__init__()
            self.Image=pygame.image.load(f"../image/Entity/NPC/{type(self).__name__}.png")
            self.Width=self.Image.get_width()
            self.Height=self.Image.get_height()
            self.Rect=pygame.Rect(0,0,self.Width,self.Height)
            NPC_list.append(self)
        
        def Update(self):
            self.Position=self.Position+self.Velocity
        @abstractmethod   
        def Draw(self,screen):
            pass
            
        
            
       


            
            
            
            
            

                
            
