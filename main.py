# this allows us to use code from
# the open-source pygame library
# throughout this file
## BASE IMPORTS #################################
import pygame
from constants import *

## CLASS IMPORTS ################################
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    ## GAME INIT ################################
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    ## DISPLAY SETUP ############################
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ## TIME STUFF ###############################
    dt = 0
    game_clock = pygame.time.Clock()
    ## GROUPS/CONTAINERS ########################
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    ## GAME SETUP ###############################
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    ## MAIN GAME LOOP ###############################################
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        ## GAMEPLAY #######################################
        updatable.update(dt)

        ## DRAW CALLS #####################################
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        ## FRAME RATE LOGIC ###############################
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
        #print(dt)


if __name__ == "__main__":
    main()
