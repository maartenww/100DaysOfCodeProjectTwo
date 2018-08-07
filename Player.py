import pygame as pg
from settings import *
# todo: import a new settings file and set starting position (x_pos to the center of the screen
# todo check http://programarcadegames.com/index.php?chapter=bitmapped_graphics_and_sound (It's a good site)
class Player:
    x_pos = SCREEN_WIDTH / 2
    y_pos = 0
    player_pos = (x_pos, y_pos)
    player_sprite_width = 42
    player_sprite_heigth = 46
    player_sprite_size = (player_sprite_width, player_sprite_heigth)
    player_Rect = pg.Rect((player_pos),(player_sprite_size))
    def hello(self):
        pass
