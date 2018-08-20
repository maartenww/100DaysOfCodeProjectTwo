import pygame as pg
from settings import *

# todo check http://programarcadegames.com/index.php?chapter=bitmapped_graphics_and_sound (It's a good site)
class Player(pg.sprite.Sprite):
    x_pos = SCREEN_WIDTH / 2
    y_pos = 0
    player_pos = (x_pos, y_pos)
    player_sprite_width = 42
    player_sprite_height = 46
    player_sprite_size = (player_sprite_width, player_sprite_height)
    def __init__(self, x_pos=SCREEN_WIDTH/2, y_pos=0):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface(((self.player_sprite_size)))
        self.image = pg.image.load_extended('spaceship_t.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (42, 46))
        self.rect = self.image.get_rect()

        self.y_pos = y_pos
        self.x_pos = x_pos
    def pUpdate(self):
        # Updates Rect position (invisible border around the sprite) with the sprite (2)
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos

        if self.rect.x < 0:
            self.rect.x = 0
            self.x_pos = 0
        elif self.rect.x > SCREEN_WIDTH - self.player_sprite_width:
            self.rect.x = SCREEN_WIDTH - self.player_sprite_width
            self.x_pos = SCREEN_WIDTH - self.player_sprite_width


    def shoot(self):
        x_pos = self.x_pos
        y_pos = self.y_pos

        # Instantiates new bullet
        bullets.append(Bullet(x_pos=x_pos + (self.player_sprite_width/2) - (Bullet.bullet_sprite_width/2) ,y_pos=y_pos-Bullet.bullet_sprite_height))

class Alien(pg.sprite.Sprite):
    x_pos = 0
    y_pos = 0
    alien_pos = (x_pos, y_pos)
    alien_sprite_width = 32
    alien_sprite_height = 62
    alien_sprite_size = (alien_sprite_width, alien_sprite_height)
    def __init__(self, x_pos=0, y_pos=0):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((self.alien_sprite_size))
        self.image = pg.image.load_extended("alien_t.png")
        self.image = pg.transform.scale(self.image, (32, 62))
        self.rect = self.image.get_rect()

        self.x_pos = x_pos
        self.y_pos = y_pos
        for i in range(len(enemies)):
            enemies[i].x_pos = int(i % 18) * 50  # Adds 50 to the next object in the enemies list to spread out the enemy on the x-axis
            enemies[i].y_pos = int(i / 18) * 50  # Adds 50 to the next object in the enemies list on the y-axis to start a new line this happens each 16 enemies. Python always rounds down when converting floats to integers.

    def eUpdate(self):
        # Updates Rect position (invisible border around the sprite) with the sprite (2)
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos

    def move_down(self):
        self.y_pos += 10

    def move_up(self):
        self.y_pos -=10

    def move_right(self):
        self.x_pos += 10

    def move_left(self):
        self.x_pos -= 10

class Bullet(pg.sprite.Sprite):
    x_pos = 0
    y_pos = 0
    bullet_pos = (x_pos, y_pos)
    bullet_sprite_width = 10
    bullet_sprite_height = 30
    bullet_sprite_size = (bullet_sprite_width, bullet_sprite_height)
    def __init__(self, x_pos=0,y_pos=0):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((self.bullet_sprite_size))
        self.image = pg.image.load_extended("laserguy.png")
        self.image = pg.transform.scale(self.image, (10, 30))
        self.rect = self.image.get_rect()

        self.x_pos = x_pos
        self.y_pos = y_pos

    def bUpdate(self):
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos



