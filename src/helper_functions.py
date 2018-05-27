import pygame
import random
from src import constants as C


def load_image(image: str)->pygame.image:
    image = pygame.image.load(image)
    return image


def gen_stars(screen):
    '''Does a random animation.'''
    star_coords = []
    colors = [C.RED, C.WHITE, C.GREEN, C.BLUE]
    for i in range(C.NUMBER_OF_STARS):
        star_x = random.randint(0, 640)
        star_y = random.randint(0, 480)
        star_coords.append((star_x, star_y))

    for i in star_coords:
        x, y = i
        color = random.choice(colors)
        pygame.draw.rect(screen, color, (x, y, 10, 10))
