import random
from pygame.math import Vector2
from gameObjects.Projectile import Projectile
from controllers.ObstacleController import ObstacleController

class EnemyController(ObstacleController):
    """
    Class to control advanced enemies that shoot at the player and try to track his movements
    """

    def __init__(self, enemy, move_pattern, target_player, scene):
        super().__init__(enemy, move_pattern)
        self.enemy = enemy
        self.player = target_player
        self.shot_timer = 0
        self.scene = scene

        if move_pattern == 'hunter':
            # stays on screen until removed by player - needs an x border
            self.obstacle.border_x = True
            self.velocity = self.enemy.get_speed()[0]
            # self.hunt_refresh_timer = 0
            # self.refresh_hunt()
            self.hunt_player()


    def shoot_player(self, target_pos):
        """
        Method that spawns a Projectile GameObject and launches it in direction of player
        :param target_pos: that needs to be the position (rect) the method is aiming at
        :return:
        """
        my_pos = (self.enemy.get_pos().x, self.enemy.get_pos().y)
        shot = Projectile(self.enemy.surface, self.enemy.projectile_damage, my_pos)
        shot.set_color((122,12,230))
        # need to aim at player
        shot.set_shot_direction(target_pos, my_pos)
        shot.add(self.scene.projectiles_enemies)
        self.scene.scene_controller.sound_control.play_sound("enemy_shot")

    def shooting(self):
        """
        Method that updates a shot timer if shooting is set to be True on the Enemy GameObject
        :return:
        """
        self.shot_timer += 1
        if (self.shot_timer > 60):
            print('shot timer reached, shooting')
            self.shoot_player(self.player.rect)
            self.shot_timer = 0

    def hunt_player(self):
        if self.move_pattern == 'hunter':
            #if self.hunt_refresh_timer > 60:
            #  we need to set our speed to aim at player - if we get too close, we reverse
            #  using projectile vector2d aiming

            # get the distance
            player_distance = (self.player.get_pos().x - self.enemy.get_pos().x), (self.player.get_pos().y - self.enemy.get_pos().y)

            #normalize the vector
            try:
                target_vector = Vector2(player_distance).normalize()
                # turn the vector into a move with velocity
                target_vector *= self.velocity
                # transferring vector to speed variable, it needs to be reversed here,
                # because obstacles reduce their speed in ObstacleController logic, they don't add!
                self.enemy.speed = target_vector * -1
            except:
                #  right on top of each other fails the normalise... very rare
                pass



