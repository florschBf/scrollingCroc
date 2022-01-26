import random
from gameObjects.Projectile import Projectile
from controllers.ObstacleController import ObstacleController

class EnemyController(ObstacleController):

    def __init__(self, enemy, move_pattern, target_player, scene):
        super().__init__(enemy, move_pattern)
        self.enemy = enemy
        self.player = target_player
        self.shot_timer = 0
        self.scene = scene

    def shoot_player(self, target_pos):
        print('pew pew')
        my_pos = (self.enemy.get_pos().x, self.enemy.get_pos().y)
        shot = Projectile(self.enemy.surface, self.enemy.projectile_damage, my_pos)
        shot.set_color((122,12,230))
        # need to aim at player
        shot.set_shot_direction(target_pos, my_pos)
        shot.add(self.scene.projectiles_enemies)
        self.scene.scene_controller.sound.play_sound("enemy_shot")

    def shooting(self):
        self.shot_timer += 1
        if (self.shot_timer > 60):
            print('shot timer reached, shooting')
            self.shoot_player(self.player.rect)
            self.shot_timer = 0