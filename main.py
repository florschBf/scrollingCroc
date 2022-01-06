import sys

import pygame
from pygame.locals import *
from pygame.sprite import Sprite

from controller.PlayerController import PlayerController
from gameObjects.PlayerObject import PlayerObject


pygame.init()
print ('hello pygame')

#setting a few defaults, consider using a settings file later on
FPS = 60
frames = pygame.time.Clock()
width = 1280
height = 720
gameSpeed = 10 #variable to control overall game speed for difficulty settings later on

#testcolor
black = (0,0,0)
white = (255,255,255)
green = (14,237,0)

#we need a surface to play on
gameboard = pygame.display.set_mode((width,height))
gameboard.fill(black)
pygame.display.set_caption("Scrolling Croc V0.1")

ball = pygame.draw.circle(gameboard, (white), (100,50), 30)
ball_speed = [1.5 * gameSpeed, 1.5 * gameSpeed]

#we collect active sprites in a group to draw them to surface
activeSprites = pygame.sprite.Group()

#we need a player and a controller
my_player = PlayerObject(green, 25, 25, (350,350))
my_player.setColor(green)
my_player.add(activeSprites)
#player needs to know game borders
my_player.setBorderX(gameboard.get_width())
my_player.setBorderY(gameboard.get_height())
print(my_player.borderX)
print(my_player.borderY)


controller = PlayerController(my_player)


#Core loop here
while True:
    #game happening
    #still
    pygame.display.update() #refresh every rendered frame
    #quit condition
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        else:
            controller.handle(event)

    new_pos_x = ball.__getattribute__("center")[0] - ball_speed[0]
    new_pos_y = ball.__getattribute__("center")[1] - ball_speed[1]
    new_pos = [new_pos_x, new_pos_y]
    ball.__setattr__("center", new_pos)
    if new_pos[0] < 0 or new_pos[0] > width:
        ball_speed[0] = -ball_speed[0]
    if new_pos[1] < 0 or new_pos[1] > height:
        ball_speed[1] = -ball_speed[1]

    #print(new_pos)
    gameboard.fill(black)
    pygame.sprite.Group.update(activeSprites)
    pygame.sprite.Group.draw(activeSprites, gameboard)
    pygame.draw.circle(gameboard, (white), new_pos, 15)
    pygame.display.flip()
    controller.update()
    frames.tick(FPS)