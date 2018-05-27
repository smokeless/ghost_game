import sys
import pygame
from src import constants as C
from src import player as P
from src import helper_functions as hf

if __name__ == '__main__':
    pygame.init() #game init
    main_screen = pygame.display.set_mode(C.SCREEN_SIZE) #screen size.
    game_over = False
    player = P.Player(main_screen)
    clock = pygame.time.Clock()
    pygame.key.set_repeat(50, 50)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move_left(3)
        if keys[pygame.K_RIGHT]:
            player.move_right(3)
        if keys[pygame.K_SPACE]:
            player.jump()

        main_screen.fill(C.BLACK)
        player.update()
        pygame.display.flip()
        clock.tick(30)