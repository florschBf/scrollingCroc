import pygame.sprite
from pygame.math import Vector2
from gameObjects.GameObject import GameObject

class Projectile(GameObject):

    def __init__(self, surface, damage, starting_pos, image = None):
        GameObject.__init__(self, surface)

        #movement related attributes
        self.velocity = 25
        self.target_vector = None
        self.border_x = False
        self.boder_y = False
        self.set_pos(starting_pos[0], starting_pos[1])

        # possibility for different powerups here (size, collision damage, frequency)
        # hardcoding for the moment
        self.collision_damage = damage


        if image == None:
            self.image = pygame.Surface([10, 10])
            self.image.fill((125,125,200))
        else:
            self.image = image

    def set_shot_direction(self, target_pos, origin_pos):
        """
        Method to determine direction of the projectile and set target vector
        :param target_pos: whatever was aimed at: player in case of enemies, just straight for player
        :param origin_pos: whichever gameobject is responsible for the projectile
        :return: nth
        """
        print ("aiming at: " + str(target_pos))
        print ("shot coming from: " + str(origin_pos))
        target_distance = (target_pos[0] - origin_pos[0]), (target_pos[1] - origin_pos[1])
        self.target_vector = Vector2(target_distance).normalize()
        print("target vector: " + str(self.target_vector))

    def get_direction(self):
        return self.target_vector

    def update(self):
        # keep it simple
        super().update()
        pos = self.get_pos()
        direction = self.get_direction()
        new_position_x = pos.x + (direction.x * self.velocity)
        new_position_y = pos.y + (direction.y * self.velocity)
        self.set_pos(new_position_x, new_position_y)
