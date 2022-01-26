import os

import pygame
import pygame.key

from scenes.Tutorial import Tutorial
from scenes.Startmenu import Startmenu
from scenes.Play import Play
from scenes.Endless import Endless
from scenes.Options import Options
from controllers.BackgroundController import BackgroundController
from controllers.SoundController import SoundController


class SceneController:

    def __init__(self):

        # setting a few defaults for screen size, consider using a settings file later on
        width = 1280
        height = 720
        old_menu_color = (150, 60, 255)
        new_menu_color = (255, 78, 225)

        # TODO game speed can be used to change feel and difficulty of the game
        self.game_speed = 10

        # we need a surface to play on
        self.gameBoard = pygame.display.set_mode((width, height))
        self.gameBoard.fill((15, 15, 15))
        self.FPS = 60
        self.frames = pygame.time.Clock()
        self.background = BackgroundController(self.gameBoard)

        self.sound = SoundController()

        # center screen
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.display.set_caption("Scrolling Croc V0.1")

        # preloading scenes - is that smart?
        # hard-coding colors here, consider themes / settings file
        self.menu = Startmenu(self.gameBoard, new_menu_color, (255, 255, 255), self)
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
            self.sound.loop_music(0)
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
            self.sound.currently_playing.fadeout(500)
            # render selected scene and call onresume
            self.state = 0
            self.sound.loop_music(0)
            self.menu.onresume()
            # do this for all other scenes as well when they are called with previous scene
        elif next_scene == "tutorial":
            prev_scene.onpause()
            self.sound.currently_playing.fadeout(500)
            self.state = 1
            self.sound.loop_music(1)
            self.tut.onresume()
        elif next_scene == "play":
            prev_scene.onpause()
            self.sound.currently_playing.fadeout(500)
            self.state = 2
            self.sound.loop_music(2)
            self.play.onresume()
        elif next_scene == "endless":
            prev_scene.onpause()
            self.sound.currently_playing.fadeout(500)
            self.state = 3
            self.sound.loop_music(3)
            self.endless.onresume()
        elif next_scene == "options":
            prev_scene.onpause()
            # self.sound.currently_playing.fadeout(500)
            self.state = 4
            # self.sound.loop_music(4)
            self.options.onresume()
        else:  # that shouldn't happen
            pass

    # deprecated xD
    def identify_previous_scene(self, scene_number):
        """
        Identifies the scene we come from when launching a new scene
        :return: the scene we came from so we can call "onpause" or "onreset" on it or sth
        """
        scene = null;
        if scene_number == 0:
            scene = self.menu
        elif scene_number == 1:
            scene = self.tut
        elif scene_number == 2:
            scene = self.play
        elif scene_number == 3:
            scene = self.endless
        elif scene_number == 4:
            scene = self.options
        return scene

    def get_active_scene(self):
        """
        Method to find active scene || currently not in use...
        :return: active scene
        """
        if self.state == 0:
            print("active scene is: " + str(self.menu))
            return self.menu
        elif self.state == 1:
            print("active scene is: " + str(self.tut))
            return self.tut
        elif self.state == 2:
            print("active scene is: " + str(self.play))
            return self.play
        elif self.state == 3:
            return self.endless
            print("active scene is: " + str(self.endless))
        elif self.state == 4:
            print("active scene is: " + str(self.options))
            return self.options

    def update(self):
        """
        Update method to be called in the main loop -
        triggers scene render according to state we're in
        :return: nth
        """

        self.gameBoard.fill((15, 15, 15))
        # running space as default background
        self.background.start_parallax("space")


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
        # pygame.display.flip()
        self.frames.tick(self.FPS)

    def reset_me(self, scene):
        if scene == self.menu:
            del(scene)
            self.menu = Startmenu(self.gameBoard, new_menu_color, (255, 255, 255), self)
        elif scene == self.tut:
            del(scene)
            self.tut = Tutorial(self.gameBoard, self)
        elif scene == self.play:
            del(scene)
            self.play = Play(self.gameBoard, self)
        elif scene == self.endless:
            del(scene)
            self.endless = Endless(self.gameBoard, self)
        elif scene == self.options:
            del(scene)
            self.options = Options(self.gameBoard, self)
        else:
            pass

    def handle(self, event):
        """
        Method to call appropriate controllers depending on active scene/state
        :param event: event to pass on to the controllers
        :return: not returning anything
        """
        if self.state == 0 and not self.menu.interrupted:
            self.menu.controller.handle(event)
        elif self.state == 1 and not self.tut.interrupted:
            self.tut.controller.handle(event)
        elif self.state == 2 and not self.play.interrupted:
            self.play.controller.handle(event)
        elif self.state == 3 and not self.play.interrupted:
            self.endless.controller.handle(event)
        elif self.state == 4 and not self.play.interrupted:
            self.options.controller.handle(event)
        else:
            # current scene is interrupted, confirm key?
            print("not doing anything else unless you confirm the message, sorry")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    print("registering the correct key, sth else is wonky maybe?")
                    current_scene = self.get_active_scene()
                    ui_handler = current_scene.ui_handler
                    current_scene.interrupted = False
                    ui_handler.remove_ui_element(ui_handler.message_to_player)

