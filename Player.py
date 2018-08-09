import pygame as pg
from settings import *
# todo check http://programarcadegames.com/index.php?chapter=bitmapped_graphics_and_sound (It's a good site)
class Player:
    x_pos = SCREEN_WIDTH / 2
    y_pos = 0
    player_pos = (x_pos, y_pos)
    player_sprite_width = 42
    player_sprite_height = 46
    player_sprite_size = (player_sprite_width, player_sprite_height)
    player_Rect = pg.Rect((player_pos),(player_sprite_size))
    def __init__(self, x_pos=SCREEN_WIDTH/2, y_pos=0):
        self.y_pos = y_pos
        self.x_pos = x_pos

class Alien:
    x_pos = 0
    y_pos = 0
    alien_pos = (x_pos, y_pos)
    alien_sprite_width = 32
    alien_sprite_height = 62
    alien_sprite_size = (alien_sprite_width, alien_sprite_height)
    alien_image = pg.image.load_extended("alien_t.png")#.convert_alpha()
    alien_image = pg.transform.scale(alien_image, (32, 62))
    alien_Rect = pg.Rect((alien_pos), (alien_sprite_size))
    def __init__(self, x_pos=0, y_pos=0):
        self.x_pos = x_pos
        self.y_pos = y_pos
