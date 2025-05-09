# this allows us to use code from
# the open-source pygame library
# throughout this file
## BASE IMPORTS #################################
import sys
import pygame
from constants import *

## CLASS IMPORTS ################################
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    ## GAME SETUP ###############################
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    ## MAIN GAME LOOP ####################################################
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        ## GAMEPLAY #######################################
        updatable.update(dt)
        for asteroid in asteroids:
            ## SHOT PLAYER
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
            ## SHOT ASTEROID
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()


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
