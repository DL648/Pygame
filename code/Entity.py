import pygame
from pygame.math import Vector2
from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self):
        self.Name = "name"
        self.LifeMax = 100
        self.Life = self.LifeMax
        self.Defence = 10
        self.Damage = 10
        self.Friendly = True
        self.Position = Vector2(0, 0)
        self.Velocity = Vector2(0, 0)
        
    @abstractmethod
    def Update(self):
        pass
    
    @abstractmethod
    def Draw(self):
        pass
    