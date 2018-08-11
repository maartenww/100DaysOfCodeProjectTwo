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
# Is game running boolean init
isRunning = True

player1 = Player(y_pos=SCREEN_HEIGHT * .85)
enemies = []
for x in range(90): # There are 90 ships and if you divde 90 by 18 you get the number of lines on the screen
    enemies.append(Alien())

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

        # Draws multiple enemies unto the screen in 5 lines (Check init of enemies list for more info)
        temp_x = 0
        for i in range(len(enemies)):
            enemies[i].x_pos = int(i % 18) * 50 # Adds 50 to the next object in the enemies list to spread out the enemy on the x-axis
            enemies[i].y_pos = int(i / 18) * 50 # Adds 50 to the next object in the enemies list on the y-axis to start a new line this happens each 18 enemies. Python always rounds down when converting floats to integers.
            surface.blit(enemies[i].alien_image, [enemies[i].x_pos, enemies[i].y_pos]) # Draws the enemy on the screen on the x and y axis
            temp_x += 50

if __name__ == "__main__":
    main()
    isRunning = False
    pg.quit()
    sys.exit()

