import pygame.draw
import random

from scenes.Scene import Scene
from scenes.handlers.CollisionHandler import CollisionHandler
from scenes.handlers.TimeHandler import TimeHandler
from scenes.handlers.UiHandler import UiHandler
from gameObjects.PlayerObject import PlayerObject
from gameObjects.Obstacle import Obstacle
from gameObjects.Enemy import Enemy
from gameObjects.PowerUp import PowerUp
from gameObjects.Boss import Boss
from controllers.PlayerController import PlayerController
from controllers.EncounterController import EncounterController
from uiObjects.HealthDisplay import HealthDisplay
from uiObjects.TimeDisplay import TimeDisplay

class Endless(Scene):
    #testcolors
    black = (0,0,0)
    white = (255,255,255)
    green = (14,237,0)

    def __init__(self, surface, scene_controller):
        #call scene constructor
        super().__init__(surface, scene_controller)

        #we need a player
        self.my_player = PlayerObject(self.gameboard, 25, 25, (350, 350))
        self.my_player.add(self.player_sprite)
        # player needs to know game borders
        self.my_player.set_borderX(self.gameboard.get_width())
        self.my_player.set_borderY(self.gameboard.get_height())

        # and needs a controllers
        self.controller = PlayerController(self.my_player, self)

        # we need a game UI
        self.ui_handler = UiHandler(self)
        self.health_display = self.ui_handler.create_health_display()
        self.time_display = self.ui_handler.create_time_display(300)
        self.score_display = self.ui_handler.create_score_display()
        self.life_display = self.ui_handler.create_life_display()

        # someone needs to watch for collisions of all kinds
        self.collision_handler = CollisionHandler(self.player_sprite, self.active_sprites, self)
        self.collision_handler_projectiles = CollisionHandler(self.player_sprite, self.projectiles_enemies, self)
        self.collision_handler_shots = CollisionHandler(self.active_sprites, self.projectiles_player, self)
        self.collision_handler_powerups = CollisionHandler(self.player_sprite, self.powerups, self)

        # time handler to progress us through the level - we "auto move" the level along to fake actual movement
        # tell the handler to display time on our UI element time_display from above
        self.time_handler = TimeHandler(self, True, 300)
        self.time_handler.set_time_display(self.time_display)
        self.wave_timer = 300
        self.wave_threshold = 500
        self.wave_counter = 0
        self.wave_multiplier = 1

        # this is an action scene
        # - now that time is set, encounter controller knows what else to run on the screen for this level
        self.ui_handler.create_message_to_player('Willkommen im Endless-Modus', 'Der endet wirklich nicht.')

    def endless_waves(self):
        self.wave_multiplier = 0
        for x in range (0, self.wave_counter):
            if x % 5 == 0:
                self.wave_multiplier += 1
        if self.wave_multiplier == 0:
            self.wave_multiplier += 1
        amount_obs = random.randint(0, 4) * self.wave_multiplier
        amount_enemy = random.randint(0, 3) * self.wave_multiplier
        amount_hunter = random.randint(0, 2) * self.wave_multiplier
        amount_powerup = random.randint(0, 2)  // self.wave_multiplier

        for x in range(0, amount_obs):
            print("spawning obstacle")
            self.spawn_obstacle()
        for x in range(0, amount_enemy):
            self.spawn_enemy()
            print("spawning enemy")
        for x in range(0, amount_hunter):
            self.spawn_hunter()
            print("spawning hunter")
        for x in range(0, amount_powerup):
            self.relief()
            print("spawning powerup")
        if self.wave_counter > 5:
            amount_boss = random.randint(0, 1)
            for x in range(0, amount_boss):
                self.spawn_boss()
                print("spawning boss")

    def relief(self):
        new_relief = PowerUp(self.gameboard, 'random')
        new_relief.add(self.powerups)
        print(new_relief)

    def spawn_obstacle(self, movement = 'random', y_start = 'random'):
        new_obstacle = Obstacle(self.gameboard, movement, y_start)
        new_obstacle.add(self.active_sprites)

    def spawn_enemy(self, movement = 'random', y_start = 'random'):
        new_enemy = Enemy(self.gameboard, movement  , self.my_player, self)
        new_enemy.set_color(self.green)
        new_enemy.add(self.active_sprites)
        if y_start != 'random':
            new_enemy.set_pos = (self.get_pos().x, y_start)

    def spawn_hunter(self):
        new_enemy = Enemy(self.gameboard,  'hunter', self.my_player, self)
        new_enemy.set_color((255, 85, 0))
        new_enemy.add(self.active_sprites)

    def spawn_boss(self):
        # boss needs no y_start and pattern will always be 'boss' specific
        new_boss = Boss(self.gameboard, 'boss', self.my_player, self)
        new_boss.add(self.active_sprites)
        new_boss.health = 2000

    def render(self):
        # call Scene render function for sprites and controllers
        super().render()
        # keep up to date on time
        if not self.interrupted:
            # make sure the level proceeds as planned
            self.time_handler.update()
            self.wave_timer += 1
            if self.wave_timer > self.wave_threshold:
                self.endless_waves()
                self.wave_counter += 1
                self.wave_timer = 0

            # handle collisions of different sprites, first player with active_sprites
            # then active_sprites with player shots
            # then player with enemy projectiles (keeping these separate from active sprites for now)
            self.collision_handler.check_for_collisions()
            self.collision_handler_shots.check_for_collisions()
            self.collision_handler_projectiles.check_for_collisions()
            self.collision_handler_powerups.check_for_collisions()

        else:
            self.controller.stop_movement()
