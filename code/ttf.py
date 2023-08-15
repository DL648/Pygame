from NPC import NPC
from pygame import Vector2
class ttf(NPC):
      def __init__(self):
          super().__init__()
          
      def Update(self):
          self.Position+=Vector2(0,10)
      def Draw(self):
          pass
          
      