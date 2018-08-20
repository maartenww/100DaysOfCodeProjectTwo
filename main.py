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
#player_image = pg.image.load_extended('spaceship_t.png').convert_alpha()
#player_image = pg.transform.scale(player_image, (42, 46))
all_sprites = pg.sprite.Group()
player_sprites = pg.sprite.Group()
enemy_sprites = pg.sprite.Group()
bullet_sprites = pg.sprite.Group()
scoreText = pg.font.Font('lunchds.ttf', 35)

# Is game running boolean init
isRunning = True

# Time things and Fps
clock = pg.time.Clock()
FPS = 60

# Instantiate Player class
player1 = Player(y_pos=SCREEN_HEIGHT * .85)

# Instantiate Alien class
for x in range(90): # There are 90 ships and if you divide 90 by 18 you get the number of lines on the screen
    enemies.append(Alien())

# Add sprite to groups
all_sprites.add(player1)
player_sprites.add(player1)

# Add sprite to groups
all_sprites.add(enemies)
enemy_sprites.add(enemies)

# Main game loop
def main():
    game1 = Game()

    while isRunning:
        game1.create()
        game1.load_text()
        game1.handle_events()
        game1.draw(screen)
        game1.update()
        # Updates surface
        pg.display.update()

class Game:
    timer = 0
    timer2 = 0
    patternNumber = 0
    score = 0
    actualscore = 0

    def load_text(self):
        # Text display / score display
        self.actualscore = scoreText.render(str(self.score), False, (white))


    def create(self):
        pass

    def update(self):
        player1.pUpdate()
        for enemy in enemies:
            Alien.eUpdate(enemy)
        for bullet in bullets:
            Bullet.bUpdate(bullet)
            # Add sprites to group
            all_sprites.add(bullets)
            bullet_sprites.add(bullets)

        # bullet + enemy collision detection and enemy elimination.
        all_sprites.update()
        for bullet in bullet_sprites:
            self.counter = 0
            if pg.sprite.spritecollide(bullet, enemy_sprites, dokill= True):
                self.score += 1

        clock.tick(FPS)
        self.timer += clock.get_time()
        self.timer2 += clock.get_time()
        if self.timer > 800:
            if self.patternNumber == 0:
                for enemy in enemies:
                    enemy.move_right()
                print(self.timer)
                self.timer = 0
                self.patternNumber = 2
            elif self.patternNumber == 1:
                for enemy in enemies:
                    enemy.move_left()
                print(self.timer)
                self.timer = 0
                self.patternNumber = 3
            elif self.patternNumber == 2:
                for enemy in enemies:
                    enemy.move_down()
                print(self.timer)
                self.timer = 0
                self.patternNumber = 5
            elif self.patternNumber == 3:
                for enemy in enemies:
                    enemy.move_up()
                print(self.timer)
                self.timer = 0
                self.patternNumber = 0
            elif self.patternNumber == 5:
                for enemy in enemies:
                    enemy.move_down()
                print(self.timer)
                self.timer = 0
                self.patternNumber = 1 # Alien movement
        if self.timer2 > 800:
            for i in range(len(bullets)):
                bullets[i].y_pos -= 10

        screen.blit(self.actualscore, (200,400))


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



        all_sprites.draw(surface)


if __name__ == "__main__":
    main()
    isRunning = False
    pg.quit()
    sys.exit()



