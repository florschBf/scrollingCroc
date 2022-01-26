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

        self.type_number = random.randint(0,2)
        if self.type_number == 0:
            self.power = 'health'
            self.image = pygame.transform.scale(pygame.image.load('assets/drawables/croc_scaled.png').convert_alpha(),
                                                (80, 80))
        elif self.type_number == 1:
            self.power = 'bigshot'
            self.image = pygame.transform.scale(pygame.image.load('assets/drawables/bubble_projectile.png').convert_alpha(),
                                                (80, 80))
        elif self.type_number == 2:
            self.power = 'life'
            self.image = pygame.transform.scale(pygame.image.load('assets/drawables/croc_scaled.png').convert_alpha(),
                                                (80, 80))



    def powerup(self, scene):
        if self.power == 'health':
            scene.my_player.health += 25
            if scene.my_player.health > 100:
                scene.my_player.health = 100
        elif self.power == 'bigshot':
            scene.controller.projectiles_per_shot = 3
        elif self.power == 'life':
            print('no lives yet')
            pass

