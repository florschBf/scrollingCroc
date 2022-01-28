import random
import pygame

from gameObjects.Obstacle import Obstacle
from gameObjects.Projectile import Projectile
from gameObjects.PowerUp import PowerUp
from gameObjects.Enemy import Enemy
from controllers.BossController import BossController


class Boss(Obstacle):

    def __init__(self, surface, movement_pattern, target_player, scene):
        super().__init__(surface, movement_pattern)
        self.speed = [0, 6]  # stays at right_side, only y movement
        # self.image = pygame.Surface([100, 300])
        # self.rect = self.image.get_rect()
        # self.image.fill((203, 0, 0))
        self.image = pygame.image.load('assets/drawables/boss1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.controller = BossController(self, movement_pattern, target_player, scene)
        self.set_pos(1280, 360 - 75)

        self.health = 20000
        self.projectile_damage = 5

        # timers are used to trigger different kinds of abilities
        self.base_move_timer = 0
        self.special_move_timer = 0
        self.spawn_timer = 0
        self.ultimate_timer = 0
        self.relief_timer = 0

    def base_move(self):
        """
        Method that spawns Projectile GameObjects and launches them at the screen in various directions
        :return:
        """
        my_pos = (self.get_pos().x + self.image.get_height()/2, self.get_pos().y + self.image.get_height()/2)
        scene = self.controller.scene
        for x in range(5):
            shot = Projectile(self.surface, self.projectile_damage, my_pos)
            shot.set_color((122, 12, 230))
            # need to aim at player
            if x == 0:
                shot.set_shot_direction((600, 0), my_pos)
                shot.add(scene.projectiles_enemies)
            elif x == 1:
                shot.set_shot_direction((300, 144), my_pos)
                shot.add(scene.projectiles_enemies)
            elif x == 2:
                shot.set_shot_direction((0, 288), my_pos)
                shot.add(scene.projectiles_enemies)
            elif x == 3:
                shot.set_shot_direction((300, 432), my_pos)
                shot.add(scene.projectiles_enemies)
            elif x == 4:
                shot.set_shot_direction((600, 676), my_pos)
                shot.add(scene.projectiles_enemies)
            scene.scene_controller.sound_control.play_sound("enemy_shot")

    def special_move(self):
        self.spawn_obstacle(movement='straight', y_start=0)
        self.spawn_obstacle(movement='straight', y_start=115)
        self.spawn_obstacle(movement='straight', y_start=230)
        self.spawn_obstacle(movement='straight', y_start=345)
        self.spawn_obstacle(movement='straight', y_start=460)
        self.spawn_obstacle(movement='straight', y_start=575)
        self.spawn_obstacle(movement='straight', y_start=690)

    def spawn_obstacles(self):

        amount_obs = random.randint(0, 3)
        amount_enemy = random.randint(0, 2)
        amount_hunter = random.randint(0, 1)
        for x in range(0, amount_obs):
            print("spawning obstacle")
            self.spawn_obstacle()
        for x in range(0, amount_enemy):
            self.spawn_enemy()
            print("spawning enemy")
        for x in range(0, amount_hunter):
            self.spawn_hunter()
            print("spawning hunter")

    def ultimate(self):
        # difficult enough already, getting cramps in hands...
        pass

    def relief(self):
        new_relief = PowerUp(self.controller.scene.gameboard, 'random')
        new_relief.add(self.controller.scene.powerups)

    def spawn_obstacle(self, movement='random', y_start='random'):
        new_obstacle = Obstacle(self.controller.scene.gameboard, movement, y_start)
        new_obstacle.add(self.controller.scene.active_sprites)

    def spawn_enemy(self, movement='random', y_start='random'):
        new_enemy = Enemy(self.controller.scene.gameboard, movement, self.controller.player, self.controller.scene)
        new_enemy.add(self.controller.scene.active_sprites)

    def spawn_hunter(self):
        new_enemy = Enemy(self.controller.scene.gameboard,  'hunter', self.controller.player, self.controller.scene)
        new_enemy.add(self.controller.scene.active_sprites)

    def update(self):
        super().update()
        self.base_move_timer += 1
        self.special_move_timer += 1
        self.spawn_timer += 1
        self.ultimate_timer += 1
        self.relief_timer += 1
        self.controller.attack()
