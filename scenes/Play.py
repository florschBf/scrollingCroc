import pygame.draw

from scenes.Scene import Scene
from gameObjects.PlayerObject import PlayerObject
from controllers.PlayerController import PlayerController


class Play(Scene):

    #testcolors
    black = (0,0,0)
    white = (255,255,255)
    green = (14,237,0)

    def __init__(self, surface, scene_controller):
        #call scene constructor
        super().__init__(surface, scene_controller)

        #game speed can be used to change feel and difficulty of the game
        self.game_speed = 10

        #ball standing in as a randon enemy for now
        self.ball = pygame.draw.circle(self.gameboard, self.white, (100, 50), 30)
        self.ball_speed = [1.5 * self.game_speed, 1.5 * self.game_speed]

        #we need a player
        self.my_player = PlayerObject(self.gameboard, 25, 25, (350, 350))
        self.my_player.set_color(self.green)
        self.my_player.add(self.active_sprites)

        # player needs to know game borders
        self.my_player.set_borderX(self.gameboard.get_width())
        self.my_player.set_borderY(self.gameboard.get_height())

        # and we need a controllers
        self.controller = PlayerController(self.my_player, self)

    def render(self):
        # call Scene render function for sprites and controllers
        super().render()

        new_pos_x = self.ball.__getattribute__("center")[0] - self.ball_speed[0]
        new_pos_y = self.ball.__getattribute__("center")[1] - self.ball_speed[1]
        new_pos = [new_pos_x, new_pos_y]
        self.ball.__setattr__("center", new_pos)
        if new_pos[0] < 0 or new_pos[0] > self.gameboard.get_width():
            self.ball_speed[0] = -self.ball_speed[0]
        if new_pos[1] < 0 or new_pos[1] > self.gameboard.get_height():
            self.ball_speed[1] = -self.ball_speed[1]

        pygame.draw.circle(self.gameboard, (255, 255, 255), new_pos, 15)
