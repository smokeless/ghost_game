import sys
import pygame
from src import constants as C
from src import player as P
from src import helper_functions as hf
from src import Laser as L
from src import hor_lazer as H

if __name__ == '__main__':
    pygame.init() #game init
    main_screen = pygame.display.set_mode(C.SCREEN_SIZE) #screen size.
    game_over = False
    player = P.Player(main_screen)
    laser = L.Laser(main_screen, player)
    laser2 = L.Laser(main_screen, player)
    laser3 = L.Laser(main_screen, player)
    hlaser = H.HorizontalLaser(main_screen, player)
    hlaser2 = H.HorizontalLaser(main_screen, player)
    hlaser3 = H.HorizontalLaser(main_screen, player)
    laser_list =[]
    for i in range(0, C.VERTICAL_LASER):
        new_laser = L.Laser(main_screen, player)
        laser_list.append(new_laser)
    for i in range(0, C.HORIZONTAL_LASER):
        new_laser = H.HorizontalLaser(main_screen, player)
        laser_list.append(new_laser)

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
        for i in laser_list:
            i.update()
        player.update()
        pygame.display.flip()
        clock.tick(30)