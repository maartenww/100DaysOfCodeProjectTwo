import pygame as pg
import sys
from Player import Player
from settings import *

pg.init()
# Screen initialization, the first line of code initializes the screen itself.
screen = pg.display.set_mode((SCREEN_RESOLUTION))
# Title Init
pg.display.set_caption('SP Ayce, In Vayyyders')
# Initialize image
bg_image = pg.image.load_extended('starfield.jpg').convert()
player_image = pg.image.load_extended('spaceship.png').convert()
player_image = pg.transform.scale(player_image, (42, 46))
# Is game running boolean init
isRunning = True

player1 = Player()
player1.y_pos = SCREEN_HEIGHT * .85
# Main game loop
def main():
    game1 = Game()

    while isRunning:
        game1.handle_events()
        game1.draw(screen)
        game1.update()
        # Updates surface
        pg.display.update()

class Game:
    def run(self):
        pass

    def update(self):
        player1.player_Rect.x = player1.x_pos
        player1.player_Rect.y = player1.y_pos
        if player1.player_Rect.x < 0:
            player1.player_Rect.x = 0
            player1.x_pos = 0
        elif player1.player_Rect.x > SCREEN_WIDTH - player1.player_sprite_width:
            player1.player_Rect.x = SCREEN_WIDTH - player1.player_sprite_width
            player1.x_pos = SCREEN_WIDTH - player1.player_sprite_width

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT: # Quits the game if you click 'x'
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    player1.x_pos -= 10
                elif event.key == pg.K_d:
                    player1.x_pos += 10

    def draw(self, surface):
        # Screen background
        surface.blit(bg_image, [0, 0])
        surface.blit(player_image, [player1.x_pos, player1.y_pos])

if __name__ == "__main__":
    main()
    isRunning = False
