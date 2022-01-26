from gameObjects.Obstacle import Obstacle
from controllers.EnemyController import EnemyController

class Enemy(Obstacle):

    def __init__(self, surface, movement_pattern, target_player, scene):
        super().__init__(surface, movement_pattern)
        self.projectile_damage = 8
        self.controller = EnemyController(self, movement_pattern, target_player, scene)
        self.shooting = True

    def set_shooting(self, boolean):
        self.shooting = boolean

    def update(self):
        super().update()
        if self.shooting:
            self.controller.shooting()