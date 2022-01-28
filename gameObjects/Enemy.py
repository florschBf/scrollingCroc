import pygame
import random
from gameObjects.Obstacle import Obstacle
from controllers.EnemyController import EnemyController


class Enemy(Obstacle):

    def __init__(self, surface, movement_pattern, target_player, scene, y_start='random'):
        super().__init__(surface, movement_pattern)
        self.projectile_damage = 8
        self.controller = EnemyController(self, movement_pattern, target_player, scene)
        self.shooting = True
        if movement_pattern == 'hunter':
            self.image = pygame.image.load('assets/drawables/spaceship_red.png').convert_alpha()
        else:
            self.image = pygame.image.load('assets/drawables/spaceship_yellow.png').convert_alpha()
        self.rect = self.image.get_rect()
        # starting position
        if y_start == 'random':
            start_y = random.randint(0, self.surface.get_height() - self.image.get_height())
        else:
            start_y = y_start
        print("my starting y: " + str(start_y))
        self.set_pos(self.surface.get_width() + 30, start_y)

    def set_shooting(self, boolean):
        self.shooting = boolean

    def update(self):
        self.controller.hunt_player()
        super().update()
        if self.shooting:
            self.controller.shooting()
