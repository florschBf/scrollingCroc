import pygame.sprite
from pygame.math import Vector2
from gameObjects import GameObject

class Projectile(GameObject):

    def __init__(self, surface, damage):
        super().__init__(surface)

        #movement related attributes
        self.velocity = 1
        self.target_vector = None
        self.border_x = False
        self.boder_y = False

        self.collision_damage = damage

    def set_shot_direction(self, target_pos, origin_pos):
        """
        Method to determine direction of the projectile and set target vector
        :param target_pos: whatever was aimed at: player in case of enemies, just straight for player
        :param origin_pos: whichever gameobject is responsible for the projectile
        :return: nth
        """
        self.target_vector = (target_pos - origin_pos).normalise()
        print(target_vector)

    def get_direction(self):
        return self.target_vector

    def update(self):
        # overwriting this completely for projectiles, not calling super, keep it simple
        pos = self.get_pos()
        direction = self.get_direction()
        new_position_x = self.pos.x + (direction.x * self.velocity)
        new_position_y = self.pos.y + (direction.y * self.velocity)
        self.set_pos(new_position.x, new_position.y)

