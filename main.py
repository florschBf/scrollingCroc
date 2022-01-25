import sys

import pygame
from pygame.locals import *

from controllers.SceneController import SceneController

pygame.init()
print('hello pygame')
scene = SceneController()
scene.launch('start_menu')

# Core loop here
while True:
    # game happening
    # still
    scene.update()
    pygame.display.flip()  # refresh every rendered frame
    # quit condition
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        else:
            # handing over all other event handling to the SceneController
            # - knows someone who can handle the event depening on scene and potentially state the game is in
            scene.handle(event)
