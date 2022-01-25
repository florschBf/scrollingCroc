import pygame.draw

from scenes.Scene import Scene
from scenes.handlers.CollisionHandler import CollisionHandler
from scenes.handlers.TimeHandler import TimeHandler
from scenes.handlers.UiHandler import UiHandler
from gameObjects.PlayerObject import PlayerObject
from gameObjects.Obstacle import Obstacle
from gameObjects.Enemy import Enemy
from controllers.PlayerController import PlayerController
from uiObjects.HealthDisplay import HealthDisplay
from uiObjects.TimeDisplay import TimeDisplay

class Tutorial(Scene):
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

        # someone needs to watch for collisions of all kinds
        self.collision_handler = CollisionHandler(self.player_sprite, self.active_sprites, self)
        self.collision_handler_projectiles = CollisionHandler(self.player_sprite, self.projectiles_enemies, self)
        self.collision_handler_shots = CollisionHandler(self.active_sprites, self.projectiles_player, self)

        # time handler to progress us through the level - we "auto move" the level along to fake actual movement
        # tell the handler to display time on our UI element time_display from above
        self.time_handler = TimeHandler(self, True, 300)
        self.time_handler.set_time_display(self.time_display)

        # and random obstacles for now
        obstacle1 = Obstacle(self.gameboard, "zigzag")
        obstacle1.add(self.active_sprites);
        obstacle2 = Obstacle(self.gameboard, "straight")
        obstacle2.add(self.active_sprites)
        obstacle3 = Obstacle(self.gameboard, "random")
        obstacle3.add(self.active_sprites)
        enemy1 = Enemy(self.gameboard, "random", self.my_player, self)
        enemy1.set_color(self.green)
        enemy1.add(self.active_sprites)

        self.ui_handler.create_message_to_player('Willkommen zum Tutorial', 'Keine Sorge, ScrollingCroc ist ein simples Spiel, es gibt', 'nicht viel zu lernen.')

    def render(self):
        # call Scene render function for sprites and controllers
        super().render()
        # keep up to date on time
        if not self.interrupted:
            self.time_handler.update()

            # handle collisions of different sprites, first player with active_sprites
            # then active_sprites with player shots
            # then player with enemy projectiles (keeping these separate from active sprites for now)
            self.collision_handler.check_for_collisions()
            self.collision_handler_shots.check_for_collisions()
            self.collision_handler_projectiles.check_for_collisions()

            if(len(self.active_sprites.sprites()) < 1):
                # and random obstacles for now
                obstacle1 = Obstacle(self.gameboard, "zigzag")
                obstacle1.add(self.active_sprites);
                obstacle2 = Obstacle(self.gameboard, "straight")
                obstacle2.add(self.active_sprites)
                obstacle3 = Obstacle(self.gameboard, "random")
                obstacle3.add(self.active_sprites)
                enemy1 = Enemy(self.gameboard, "random", self.my_player, self)
                enemy1.set_color(self.green)
                enemy1.add(self.active_sprites)
        else:
            self.controller.stop_movement()


