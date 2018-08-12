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

    def update(self):
        # Updates Rect position (invisible border around the sprite) with the sprite
        self.player_Rect.x = self.x_pos
        self.player_Rect.y = self.y_pos

        # Border collision in a nutshell.
        if self.player_Rect.x < 0:
            self.player_Rect.x = 0
            self.x_pos = 0
        elif self.player_Rect.x > SCREEN_WIDTH - self.player_sprite_width:
            self.player_Rect.x = SCREEN_WIDTH - self.player_sprite_width
            self.x_pos = SCREEN_WIDTH - self.player_sprite_width

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
        for i in range(len(enemies)):
            enemies[i].x_pos = int(i % 18) * 50  # Adds 50 to the next object in the enemies list to spread out the enemy on the x-axis
            enemies[i].y_pos = int(i / 18) * 50  # Adds 50 to the next object in the enemies list on the y-axis to start a new line this happens each 16 enemies. Python always rounds down when converting floats to integers.

    def move_right(self):
        self.x_pos += 10
        self.y_pos += 10
    def move_left(self):
        self.x_pos -= 10
        self.y_pos -= 10

    def update(self):
        # Updates Rect position (invisible border around the sprite) with the sprite
        self.alien_Rect.x = self.x_pos
        self.alien_Rect.y = self.y_pos

