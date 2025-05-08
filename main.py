# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    ## GAME INIT ################################
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    ## GROUPS ###################################
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    ## TIME STUFF ###############################
    dt = 0
    game_clock = pygame.time.Clock()

    ## DISPLAY SETUP ############################
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
