import random

import pygame.sprite
from gameObjects.GameObject import GameObject
from controllers.ObstacleController import ObstacleController


class Obstacle(GameObject):
    """
    GameObject that moves through the screen from right to left and needs to be avoided by the player
    Has health (like all gameObjects) and can porentially be destroyed (like all gameObjects)
    """

    def __init__(self, surface, movement_pattern, y_start='random'):
        """
        Constructor needs to know the height of the screen for spawn point
        :param surface: the surface we are rendering on
        :param movement_pattern: the type of controllers the obstacle should have
            valid input Strings:
            * straight
            * zigzag
            * random
        """
        # init self as a GameObject
        super().__init__(surface)
        self.collision_damage = 2
        self.image = pygame.transform.scale(pygame.image.load('assets/drawables/asteroid_brown.png').convert_alpha(), (80, 80))
        self.rect = self.image.get_rect()

        # starting position
        if y_start == 'random':
            start_y = random.randint(0, self.surface.get_height() - self.image.get_height())
        else:
            start_y = y_start
        print("my starting y: " + str(start_y))
        self.set_pos(self.surface.get_width() + 30, start_y)

        # controllers that handles movement
        self.controller = ObstacleController(self, movement_pattern)

    def update(self):
        super().update()
        self.controller.moving()
