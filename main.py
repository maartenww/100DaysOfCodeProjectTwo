import pygame as pg
import sys

pg.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Tuple of Width and Height
SCREEN_RESOLUTION = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Color initialization
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255, 211, 0)

# Screen initialization, the first line of code initializes the screen itself.
screen = pg.display.set_mode((SCREEN_RESOLUTION))

class Game:
    def run(self):
        pass



isRunning = True

# Main game loop
def main():
    while isRunning:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()


    # Screen background color
    screen.fill(black)
    # Updates surface
    pg.display.update()




if __name__ == "__main__":
    main()
    isRunning = False