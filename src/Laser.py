import pygame
from src import constants as C
import random


class Laser(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        super(Laser, self).__init__()
        self.x = random.randint(10, 630)
        self.y = 10
        self.width = 10
        self.height = 100
        self.screen = screen
        self.player = player

    def is_collided_with(self, sprite):
        rect = self.get_rect()
        return rect.colliderect(sprite)

    def fire_new_laser(self):
        if self.x >= 640 or self.y >= 480:
            self.x = random.randint(0, 630)
            self.y = 10

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        pygame.draw.rect(self.screen, C.WHITE, (self.x, self.y, self.width, self.height))
        if self.is_collided_with(self.player.image_rect):
            self.player.move_down(10)
        self.y += 3
        self.fire_new_laser()
