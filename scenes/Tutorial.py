import pygame.draw
from gameObjects.PlayerObject import PlayerObject
from controller.PlayerController import PlayerController

class Tutorial:
    #testcolor
    black = (0,0,0)
    white = (255,255,255)
    green = (14,237,0)

    def __init__(self, display):
        self.gameBoard = display

        self.gameSpeed = 10

        self.ball = pygame.draw.circle(self.gameBoard, self.white, (100, 50), 30)
        self.ball_speed = [1.5 * self.gameSpeed, 1.5 * self.gameSpeed]

        #we collect active sprites in a group to draw them to surface
        self.activeSprites = pygame.sprite.Group()

        #we need a player and a controller
        self.my_player = PlayerObject(self.green, 25, 25, (350,350))
        self.my_player.setColor(self.green)
        self.my_player.add(self.activeSprites)

        #player needs to know game borders
        self.my_player.setBorderX(self.gameBoard.get_width())
        self.my_player.setBorderY(self.gameBoard.get_height())
        print(self.my_player.borderX)
        print(self.my_player.borderY)

        self.controller = PlayerController(self.my_player)


    def render(self):
        new_pos_x = self.ball.__getattribute__("center")[0] - self.ball_speed[0]
        new_pos_y = self.ball.__getattribute__("center")[1] - self.ball_speed[1]
        new_pos = [new_pos_x, new_pos_y]
        self.ball.__setattr__("center", new_pos)
        if new_pos[0] < 0 or new_pos[0] > self.gameBoard.get_width():
            self.ball_speed[0] = -self.ball_speed[0]
        if new_pos[1] < 0 or new_pos[1] > self.gameBoard.get_height():
            self.ball_speed[1] = -self.ball_speed[1]

        pygame.sprite.Group.update(self.activeSprites)
        pygame.sprite.Group.draw(self.activeSprites, self.gameBoard)
        pygame.draw.circle(self.gameBoard, (255, 255, 255), new_pos, 15)

        self.controller.update()
