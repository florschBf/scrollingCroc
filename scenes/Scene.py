import pygame.sprite
from scenes.handlers.UiHandler import UiHandler

class Scene:
    """
    Parent class for all game scenes
    Has a life-cycle called on by the SceneController class:
        __init__
        onpause
        onresume
        onreset
    Renders to the display while it is the active scene as determined by SceneController
    """

    def __init__(self, surface, scene_controller):
        # technically, constructor is not 100% equiv to oncreate steps, but it will do
        # setting main pygame surface and scene_controller
        self.gameboard = surface
        self.scene_controller = scene_controller
        self.interrupted = False

        # every scene has a collection of active sprites to render
        # hidden sprites dont get rendered atm but may be brought back (dont want them killed)
        # e.g. hiding UI / messages / stuff like that
        # player_sprite might not be present, but usually is
        # establishing different groups as kind of "layers" to work with, also regarding collision rules btw each other
        self.player_sprite = pygame.sprite.GroupSingle()
        self.active_sprites = pygame.sprite.Group()

        # active game scenes require additional sprite categories
        self.projectiles_player = pygame.sprite.Group()
        self.projectiles_enemies = pygame.sprite.Group()
        # UI Layer
        self.ui = pygame.sprite.Group()

        # layer to keep hidden game objects in the scene, like spawn points, ui, whatever else we can come up with
        self.hidden_sprites = pygame.sprite.Group()

        # every scene has some sort of ui - this class here initialises it on demand in the respective scene
        self.ui_handler = UiHandler(self)

    def onpause(self):
        # call me when pausing the scene
        print("pause on scene " + str(self) + " called")

    def onresume(self):
        # call me when returning to the scene
        print("resume on scene " + str(self) + " called")

    def onreset(self):
        # call when scene should be ended (e.g. cleanup, send back to start)
        print("reset on scene " + str(self) + " called")

    def new_scene(self, scene_to_go_to):
        self.scene_controller.scene_switch(scene_to_go_to, self)

    def render(self):
        """
        Method to call on scene to output scene to display
        super NEEDS to be called by the scenes in addition to their own logic for this step
        :return:
        """
        #update only if scene is not interrupted
        if not self.interrupted:
            pygame.sprite.GroupSingle.update(self.player_sprite)
            pygame.sprite.Group.update(self.active_sprites)
            pygame.sprite.Group.update(self.projectiles_player)
            pygame.sprite.Group.update(self.projectiles_enemies)
            pygame.sprite.Group.update(self.ui)
            pygame.sprite.Group.update(self.hidden_sprites)
            # run controllers update
            self.controller.update()

        # always draw the sprites if scene is rendering to prevent black screen...
        pygame.sprite.Group.draw(self.ui, self.gameboard)
        pygame.sprite.Group.draw(self.active_sprites, self.gameboard)
        pygame.sprite.GroupSingle.draw(self.player_sprite, self.gameboard)
        pygame.sprite.Group.draw(self.projectiles_player, self.gameboard)
        pygame.sprite.Group.draw(self.projectiles_enemies, self.gameboard)

        # not drawing hidden sprites

