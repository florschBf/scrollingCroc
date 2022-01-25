import pygame.draw

from scenes.Scene import Scene
from scenes.handlers.CollisionHandler import CollisionHandler
from scenes.handlers.TimeHandler import TimeHandler
from scenes.handlers.UiHandler import UiHandler
from gameObjects.PlayerObject import PlayerObject
from gameObjects.Obstacle import Obstacle
from controller.PlayerController import PlayerController
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
        self.my_player = PlayerObject(self.gameboard, self.green, 25, 25, (350, 350))
        self.my_player.set_color(self.green)
        self.my_player.add(self.player_sprite)

        # player needs to know game borders
        self.my_player.set_borderX(self.gameboard.get_width())
        self.my_player.set_borderY(self.gameboard.get_height())

        # and needs a controller
        self.controller = PlayerController(self.my_player, self)

        # we need a game UI
        self.ui_handler = UiHandler(self)
        self.health_display = self.ui_handler.create_health_display()
        self.time_display = self.ui_handler.create_time_display(300)
        # player needs a hud for health, score and similar
        # self.health_display = HealthDisplay(self.my_player)

        # someone needs to watch for collisions of all kinds
        self.collision_handler = CollisionHandler(self.player_sprite, self.active_sprites)
        self.collision_handler_projectiles = CollisionHandler(self.player_sprite, self.projectiles_enemies)
        self.collision_handler_shots = CollisionHandler(self.active_sprites, self.projectiles_player)

        # time handler to progress us through the level - we "auto move" the level along to fake actual movement
        # tell the handler to display time on our UI element time_display from above
        self.time_handler = TimeHandler(self, False, 300)
        self.time_handler.set_time_display(self.time_display)

        #and random obstacles for now
        obstacle1 = Obstacle(self.gameboard, "zigzag")
        obstacle1.add(self.active_sprites);
        obstacle2 = Obstacle(self.gameboard, "straight")
        obstacle2.add(self.active_sprites)
        obstacle3 = Obstacle(self.gameboard, "random")
        obstacle3.add(self.active_sprites)

    def render(self):
        # call Scene render function for sprites and controller
        super().render()
        # keep up to date on time
        self.time_handler.update()

        # handle collisions of different sprites, first player with active_sprites
        # then active_sprites with player shots
        # then player with enemy projectiles (keeping these separate from active sprites for now)
        self.collision_handler.check_for_collisions()
        self.collision_handler_shots.check_for_collisions()
        self.collision_handler_projectiles.check_for_collisions()

        # update health display after all these collisions..
        #self.health_display.update()
        # TODO consider moving gameboard UI blitting to extra UI Handler class later with more UI work
        #self.gameboard.blit(self.health_display.text, (50, 25, 100, 30))
        #self.gameboard.blit(self.health_display.healthbar, (50, 40, 100, 30))
        #self.gameboard.blit(self.time_display.text, (165, 25, 100, 30))
        #self.gameboard.blit(self.time_display.value, (165, 40, 100, 30))

        if(len(self.active_sprites.sprites()) < 1):
            # and random obstacles for now
            obstacle1 = Obstacle(self.gameboard, "zigzag")
            obstacle1.add(self.active_sprites);
            obstacle2 = Obstacle(self.gameboard, "straight")
            obstacle2.add(self.active_sprites)
            obstacle3 = Obstacle(self.gameboard, "random")
            obstacle3.add(self.active_sprites)

