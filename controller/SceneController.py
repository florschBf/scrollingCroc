import os

import pygame

from scenes.Tutorial import Tutorial
from scenes.Startmenu import Startmenu
from scenes.Play import Play
from scenes.Endless import Endless
from scenes.Options import Options


class SceneController:

    def __init__(self):

        # setting a few defaults for screen size, consider using a settings file later on
        width = 1280
        height = 720
        # we need a surface to play on
        self.gameBoard = pygame.display.set_mode((width, height))
        self.gameBoard.fill((15, 15, 15))
        self.FPS = 60
        self.frames = pygame.time.Clock()
        # center screen
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.display.set_caption("Scrolling Croc V0.1")

        # preloading scenes - is that smart?
        # hard-coding colors here, consider themes / settings file
        self.menu = Startmenu(self.gameBoard, (150, 60, 255), (255, 255, 255), self)
        self.tut = Tutorial(self.gameBoard, self)
        self.play = Play(self.gameBoard, self)
        self.endless = Endless(self.gameBoard, self)
        self.options = Options(self.gameBoard, self)

        # starting state is menu
        self.state = 0
        self.prevState = 0

    def launch(self, scene):
        """
        Method to set state to launch selected scene without previous scene input
        e.g start of game (launch) or when desired for other reasons, like omitting onpause (should not do that)
        :param scene: viable Strings:
            start_menu
            tutorial
            play
            endless
            options
        :return: nth
        """
        if scene == "start_menu":
            self.state = 0
        elif scene == "tutorial":
            self.state = 1
        elif scene == "play":
            self.state = 2
        elif scene == "endless":
            self.state = 3
        elif scene == "options":
            self.state = 4
        else:  # that shouldn't happen
            pass

    def scene_switch(self, next_scene, prev_scene):
        """
        Method to set state to launch selected scene
        :param next_scene: viable Strings:
            start_menu
            tutorial
            play
            endless
            options
        :param prev_scene: the calling scene
        :return: nth
        """
        if next_scene == "start_menu":
            # call pause on previous scene
            prev_scene.onpause()
            # render selected scene and call onresume
            self.state = 0
            self.menu.onresume()
            # do this for all other scenes as well when they are called with previous scene
        elif next_scene == "tutorial":
            prev_scene.onpause()
            self.state = 1
            self.tut.onresume()
        elif next_scene == "play":
            prev_scene.onpause()
            self.state = 2
            self.play.onresume()
        elif next_scene == "endless":
            prev_scene.onpause()
            self.state = 3
            self.endless.onresume()
        elif next_scene == "options":
            prev_scene.onpause()
            self.state = 4
            self.options.onresume()
        else:  # that shouldn't happen
            pass

    # deprecated xD
    def identify_previous_scene(scene_number):
        """
        Identifies the scene we come from when launching a new scene
        :return: the scene we came from so we can call "onpause" or "onreset" on it or sth
        """
        scene = null;
        if scene_number == 0:
            scene = self.menu
        elif scene_number == 1:
            scene = self.tutorial
        elif scene_number == 2:
            scene = self.play
        elif scene_number == 3:
            scene = self.endless
        elif scene_number == 4:
            scene = self.options
        return scene


    def update(self):
        """
        Update method to be called in the main loop -
        triggers scene render according to state we're in
        :return: nth
        """
        self.gameBoard.fill((15, 15, 15))

        # check state and call render
        if self.state == 0:
            self.menu.render()
        elif self.state == 1:
            self.tut.render()
        elif self.state == 2:
            self.play.render()
        elif self.state == 3:
            self.endless.render()
        else:
            # invalid state, don't know what to render || close? rendering start_menu I guess, should never happen
            self.menu.render()

        # tell pygame to update the display and stick to selected FPS
        pygame.display.flip()
        self.frames.tick(self.FPS)

    def handle(self, event):
        """
        Method to call appropriate controller depending on active scene/state
        :param event: event to pass on to the controller
        :return: not returning anything
        """
        if self.state == 0:
            self.menu.controller.handle(event)
        elif self.state == 1:
            self.tut.controller.handle(event)
        elif self.state == 2:
            self.play.controller.handle(event)
        elif self.state == 3:
            self.endless.controller.handle(event)
        elif self.state == 4:
            self.options.controller.handle(event)
        else:
            print("not in a valid state??? this is bad.")
