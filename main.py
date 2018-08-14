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

clock = pg.time.Clock()
FPS = 60

player1 = Player(y_pos=SCREEN_HEIGHT * .85)

for x in range(90): # There are 90 ships and if you divide 90 by 18 you get the number of lines on the screen
    enemies.append(Alien())


# Main game loop
def main():
    game1 = Game()

    while isRunning:
        game1.create()
        game1.handle_events()
        game1.draw(screen)
        game1.update()
        # Updates surface
        pg.display.update()

class Game:
    xx = 0
    yy = 0
    def create(self):
        pass

    def update(self):
        player1.update()
        for enemy in enemies:
            Alien.update(enemy)
        clock.tick(FPS)
        self.xx += clock.get_time()
        if self.xx > 800:
            if self.yy == 0:
                for enemy in enemies:
                    enemy.move_right()
                print(self.xx)
                self.xx = 0
                self.yy = 2
            elif self.yy == 1:
                for enemy in enemies:
                    enemy.move_left()
                print(self.xx)
                self.xx = 0
                self.yy = 3
            elif self.yy == 2:
                for enemy in enemies:
                    enemy.move_down()
                print(self.xx)
                self.xx = 0
                self.yy = 5
            elif self.yy == 3:
                for enemy in enemies:
                    enemy.move_up()
                print(self.xx)
                self.xx = 0
                self.yy = 0
            elif self.yy == 5:
                for enemy in enemies:
                    enemy.move_down()
                print(self.xx)
                self.xx = 0
                self.yy = 1 # Alien movement

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
                elif event.key == pg.K_q:
                    player1.shoot()

    def draw(self, surface):
        # Screen background
        surface.blit(bg_image, [0, 0])

        # Draws player on surface at the x and y pos
        surface.blit(player_image, [player1.x_pos, player1.y_pos])

        # Draws multiple enemies unto the screen in 5 lines (Check init of enemies list for more info)
        for i in range(len(enemies)):
            surface.blit(enemies[i].alien_image, [enemies[i].x_pos, enemies[i].y_pos]) # Draws the enemy on the screen on the x and y axis

        for i in range(len(bullets)):
            surface.blit(bullets[i].bullet_image, [bullets[i].x_pos, bullets[i].y_pos])


if __name__ == "__main__":
    main()
    isRunning = False
    pg.quit()
    sys.exit()



