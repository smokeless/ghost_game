import pygame
from src import constants as C
import random


class HorizontalLaser(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        super(HorizontalLaser, self).__init__()
        directions = ['left', 'right']
        self.x = 10
        self.y = random.randint(10, 480)
        self.width = 100
        self.height = 10
        self.screen = screen
        self.player = player
        self.direction = 'left'

    def is_collided_with(self, sprite):
        rect = self.get_rect()
        return rect.colliderect(sprite)

    def fire_new_laser(self):
        if self.x >= 640 or self.y >= 480:
            self.x = random.randint(0, 630)
            self.y = random.randint(0, 480)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        pygame.draw.rect(self.screen, C.WHITE, (self.x, self.y, self.width, self.height))
        if self.is_collided_with(self.player.image_rect):
            self.player.move_right(10)
        self.x += 3
        self.fire_new_laser()
