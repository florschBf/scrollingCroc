import pygame.sprite

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

        # every scene has a collection of active sprites to render
        # hidden sprites dont get rendered atm but may be brought back (dont want them killed)
        # e.g. hiding UI / messages / stuff like that
        # player_sprite might not be present, but usually is
        self.player_sprite = pygame.sprite.GroupSingle()
        self.active_sprites = pygame.sprite.Group()
        self.hidden_sprites = pygame.sprite.Group()

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
        # update and draw the active sprites
        pygame.sprite.GroupSingle.update(self.player_sprite)
        pygame.sprite.GroupSingle.draw(self.player_sprite, self.gameboard)
        pygame.sprite.Group.update(self.active_sprites)
        pygame.sprite.Group.draw(self.active_sprites, self.gameboard)
        pygame.sprite.Group.update(self.hidden_sprites)
        # not drawing hidden sprites


        # run controller update
        self.controller.update()