import pygame
from .helper_functions import *
from .constants import *


class Player(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.display):
        super(Player, self).__init__()
        self.right_sprite = load_image('assets/ghost.png')
        self.image_rect = self.right_sprite.get_rect()
        self.screen = screen
        self.left_sprite = load_image('assets/ghost.png')
        self.left_sprite = pygame.transform.flip(self.left_sprite, True, False)
        self.sprite = self.right_sprite
        self.facing = 'right'
        self.jumping = False

    def get_rect(self):
        print(self.image_rect)

    def move_left(self, distance: int):
        if self.facing == 'right':
            self.facing = 'left'
            self.sprite = self.left_sprite

        if self.image_rect.x - distance < X_MIN:
            self.image_rect.x = self.image_rect.x
        else:
            self.image_rect.x = self.image_rect.x - distance

    def move_right(self, distance: int):
        if self.facing == 'left':
            self.facing = 'right'
            self.sprite = self.right_sprite

        if self.image_rect.x + distance > X_MAX:
            self.image_rect.x = self.image_rect.x
        else:
            self.image_rect.x = self.image_rect.x + distance

    def move_down(self, distance: int):
        self.image_rect.y += distance

    def jump(self):
        self.jumping = True
        if self.image_rect.y - 30 < CEILING:
            self.jumping = False
        else:
            self.image_rect.y -= 30

    def _check_gravity(self):
        if self.image_rect.y < FLOOR and not self.jumping:
            self.image_rect.y += GRAVITY
        if self.jumping:
            self.jumping = False

    def update(self):
        self.screen.blit(self.sprite, self.image_rect)
        self._check_gravity()