import pygame.image
from gameObjects.Obstacle import Obstacle
import random


class PowerUp(Obstacle):
    """
    GameObject that is beneficial to the Player - increase energy, change shot size/speed, stuff like that is possible
    """

    def __init__(self, surface, movement_pattern):
        super().__init__(surface, movement_pattern)
        self.collision_damage = 0
        self.health = 800

        self.type_number = random.randint(0, 2)
        if self.type_number == 0:
            self.power = 'health'
            self.image = pygame.transform.scale(pygame.image.load('assets/drawables/powerup_health.png').convert_alpha(),
                                                (80, 80))
        elif self.type_number == 1:
            self.power = 'bigshot'
            self.image = pygame.transform.scale(pygame.image.load('assets/drawables/powerup_bubble.png').convert_alpha(),
                                                (80, 80))
        elif self.type_number == 2:
            self.power = 'life'
            self.image = pygame.transform.scale(pygame.image.load('assets/drawables/powerup_extra_life.png').convert_alpha(),
                                                (80, 80))

    def powerup(self, scene):
        if self.power == 'health':
            scene.my_player.health += 25
            if scene.my_player.health > 100:
                scene.my_player.health = 100
        elif self.power == 'bigshot':
            if scene.controller.projectiles_per_shot < 3:  # more was too easy
                scene.controller.projectiles_per_shot += 1
        elif self.power == 'life':
            scene.my_player.lives += 1
