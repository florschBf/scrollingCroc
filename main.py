import sys

import pygame
from pygame.locals import *


pygame.init()
print ('hello pygame')

FPS = 60
Frames = pygame.time.Clock()

#testcolor
black = (0,0,0)
white = (255,255,255)

#we need a surface to play on
gameboard = pygame.display.set_mode((1280,720))
gameboard.fill(black)
pygame.display.set_caption("Scrolling Croc V0.1")

ball = pygame.draw.circle(gameboard, (white), (100,50), 30)
ball_speed = [15, 15]

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

    new_pos_x = ball.__getattribute__("center")[0] - ball_speed[0]
    new_pos_y = ball.__getattribute__("center")[1] - ball_speed[1]
    new_pos = [new_pos_x, new_pos_y]
    ball.__setattr__("center", new_pos)
    if new_pos[0] < 0 or new_pos[0] > gameboard.get_width():
        ball_speed[0] = -ball_speed[0]
    if new_pos[1] < 0 or new_pos[1] > gameboard.get_height():
        ball_speed[1] = -ball_speed[1]

    print(new_pos)
    gameboard.fill(black)
    pygame.draw.circle(gameboard, (white), new_pos, 30)
    pygame.display.flip()
    Frames.tick(FPS)