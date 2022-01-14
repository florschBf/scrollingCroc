import sys

import pygame
from pygame.locals import *

from controller.SceneController import SceneController


pygame.init()
print('hello pygame')
scene = SceneController()
scene.launch('tutorial')


#startmenu = Startmenu(green)

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
            scene.handle(event)

    scene.update()

