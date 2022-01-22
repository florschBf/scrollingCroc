import random

import pygame.sprite
from gameObjects.GameObject import GameObject

class Obstacle(GameObject):
    """
    GameObject that moves through the screen from right to left and needs to be avoided by the player
    Has health (like all gameObjects) and can porentially be destroyed (like all gameObjects)
    """

    def __init__(self, surface, movement_pattern):
        """
        Constructor needs to know the height of the screen for spawn point
        :param surface_height: the height of said screen
        :param movement_pattern: the type of controller the obstacle should have
            valid input Strings:
            * straight - TODO can be used for immovable obstacles like walls, stones etc
            * zigzag - TODO predictable pattern for moving obstacles
            * random - TODO unpredictable pattern for weird moving obstacles
        """
        # init self as a GameObject
        super.__init__(surface)

        # starting position
        start_y = random.randint(0, self.surface.height)
        self.set_pos(0, start_y)

        #controller that handles movement
        self.controller = ObstacleController(self, movement_pattern)

    def update(self):
        self.controller.get_move(self.get_pos())