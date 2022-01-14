import os

import pygame
from pygame.locals import *

from scenes.Tutorial import Tutorial
from scenes.Startmenu import Startmenu
from scenes.Play import Play
from scenes.Endless import Endless

class SceneController:



    def __init__(self):

        #setting a few defaults, consider using a settings file later on

        width = 1280
        height = 720

        #we need a surface to play on
        self.gameBoard = pygame.display.set_mode((width, height))
        self.gameBoard.fill((15, 15, 15))
        self.FPS = 60
        self.frames = pygame.time.Clock()
        #center screen
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.display.set_caption("Scrolling Croc V0.1")

        #preloading scenes - is that smart?
        self.state = 0
        self.menu = Startmenu(self.gameBoard)
        self.tut = Tutorial(self.gameBoard)
        self.play = Play(self.gameBoard)

    def launch(self, scene):
        if scene == "start_menu":
            self.state = 0
        elif scene == "tutorial":
            self.state = 1
        elif scene == "play":
            self.state = 2

    def update(self):
        self.gameBoard.fill((15, 15, 15))

        if self.state == 0:
            self.menu.render()
        elif self.state == 1:
            self.tut.render()
        elif self.state == 2:
            self.play.render()

        #start menu on launch to select game mode
        #gameboard.blit(startmenu.render(), (screen_width/2 - (start_rect[2]/2), 300))

        pygame.display.flip()
        self.frames.tick(self.FPS)

    def handle(self, event):
        if self.state == 0:
            self.menu.controller.handle(event)
        elif self.state == 1:
            self.tut.controller.handle(event)

