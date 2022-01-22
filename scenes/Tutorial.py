import pygame.draw

from scenes.Scene import Scene
from scenes.handlers.CollisionHandler import CollisionHandler
from gameObjects.PlayerObject import PlayerObject
from gameObjects.Obstacle import Obstacle
from controller.PlayerController import PlayerController
from uiObjects.HealthDisplay import HealthDisplay

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
        # player needs a hud for health, score and similar
        self.health_display = HealthDisplay(self.my_player)

        # someone needs to watch for collisions of all kinds
        self.collision_handler = CollisionHandler(self.player_sprite, self.active_sprites)

        #and an obstacle
        obstacle1 = Obstacle(self.gameboard, "zigzag")
        obstacle1.add(self.active_sprites);
        obstacle2 = Obstacle(self.gameboard, "straight")
        obstacle2.add(self.active_sprites)
        obstacle3 = Obstacle(self.gameboard, "random")
        obstacle3.add(self.active_sprites)

    def render(self):
        # call Scene render function for sprites and controller
        super().render()
        self.collision_handler.check_for_collisions()
        self.health_display.update()
        self.gameboard.blit(self.health_display.text, (50, 50, 100, 30))
        self.gameboard.blit(self.health_display.healthbar, (50, 65, 100, 30))
