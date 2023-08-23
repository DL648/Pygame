from pygame.math import Vector2
from enum import Enum
import pygame

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1080
color_black =(0,0,0)
color_red=(255,80,80)
color_green=(80,255,80)
color_grey=(125,125,125)

player_list =[]

NPC_list = []

Projctile_list =[]

Game_background_image = pygame.image.load('..//images/Background/GAME_MENU.png')
Game_title_image = pygame.image.load('..//images/UI/Pygame.png')
Game_start_image =pygame.image.load('..//images/UI/START.png')
Game_exit_image =pygame.image.load('..//images/UI/EXIT.png')
Player_image =pygame.transform.scale(pygame.image.load('..//images/Player.png'),(60,88))
   

class Game_Mould(Enum):
    Menu =1
    Play =2
    End =3

