import pygame as pg
import sys
from Player import *
from settings import *

pg.init()
# Screen initialization, the first line of code initializes the screen itself.
screen = pg.display.set_mode((SCREEN_RESOLUTION))
# Title Init
pg.display.set_caption('SP Ayce, In Vayyyders')
# Initialize image
bg_image = pg.image.load_extended('starfield.jpg').convert()
player_image = pg.image.load_extended('spaceship_t.png').convert_alpha()
player_image = pg.transform.scale(player_image, (42, 46))
alien_image = pg.image.load_extended("alien_t.png").convert_alpha()
alien_image = pg.transform.scale(alien_image, (32, 62))
# Is game running boolean init
isRunning = True

player1 = Player(y_pos=SCREEN_HEIGHT * .85)
enemies = []
for x in range(1):
    enemies.append(Alien(y_pos=20))

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
        # Updates Rect position (invisble border around the sprite) with the sprite
        player1.player_Rect.x = player1.x_pos
        player1.player_Rect.y = player1.y_pos

        # Border collision in a nutshell.
        if player1.player_Rect.x < 0:
            player1.player_Rect.x = 0
            player1.x_pos = 0
        elif player1.player_Rect.x > SCREEN_WIDTH - player1.player_sprite_width:
            player1.player_Rect.x = SCREEN_WIDTH - player1.player_sprite_width
            player1.x_pos = SCREEN_WIDTH - player1.player_sprite_width

        # Updates Rect position (invisible border around the sprite) with the sprite
        for enemy in enemies:
            enemy.alien_Rect.x = enemy.x_pos
            enemy.alien_Rect.y = enemy.y_pos

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
        # Draws player on surface at the x and y pos
        surface.blit(player_image, [player1.x_pos, player1.y_pos])
        # Draws multiple enemies unto the screen and at x and y
        # While incrementing the x pos to spread the enemies out.
        for enemy in enemies:
            surface.blit(alien_image, [enemy.x_pos, enemy.y_pos])




if __name__ == "__main__":
    main()
    isRunning = False
    pg.quit()
    sys.exit()
