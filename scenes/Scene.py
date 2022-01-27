import pygame.sprite
from scenes.handlers.UiHandler import UiHandler
from scenes.handlers.TimeHandler import TimeHandler
# collision handlers handled on scene basis

class Scene:
    """
    Parent class for all game scenes
    Has a life-cycle called on by the SceneController class:
        __init__
        onpause
        onresume
        onreset - called manually right now, not on scene switching.
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
        self.active_sprites = pygame.sprite.Group() # enemy obstacles
        self.powerups = pygame.sprite.Group()

        # active game scenes require additional sprite categories
        self.projectiles_player = pygame.sprite.Group() # player projectiles
        self.projectiles_enemies = pygame.sprite.Group() # enemy projectiles
        # UI + UI OnTop Layer
        self.ui = pygame.sprite.Group() # base ui
        self.ui_on_top = pygame.sprite.Group() # ui thats always on top

        # layer to keep hidden game objects in the scene, like spawn points, ui, whatever else could come up
        self.hidden_sprites = pygame.sprite.Group()

        # every scene has some sort of ui - this class here initialises it on demand in the respective scene
        self.ui_handler = UiHandler(self)
        # most scenes need to keep track of time, so we all get a timehandler, even though it might not display time
        self.time_handler = TimeHandler(self, True)


    def onpause(self):
        # call me when pausing the scene
        print("pause on scene " + str(self) + " called")
        self.time_handler.pause_time()

    def onresume(self):
        # call me when returning to the scene
        print("resume on scene " + str(self) + " called")
        self.time_handler.resume_time()

    def onreset(self):
        # call when scene should be ended (e.g. cleanup, send back to start)
        print("reset on scene " + str(self) + " called")
        self.scene_controller.reset_me(self)

    def new_scene(self, scene_to_go_to):
        self.scene_controller.scene_switch(scene_to_go_to, self)

    def game_over_message(self):
        self.ui_handler.create_highscore_input('Bam.', '', 'Mehr Glück beim nächsten Mal...', '', 'GAME OVER!')

    def game_over(self):
        print("cleaning up and leaving")
        self.onreset()
        self.new_scene('start_menu')

    def get_score(self):
        # implemented in scenes with score
        try:
            return self.my_player.score
        except:
            return 0

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
            pygame.sprite.Group.update(self.powerups)
            pygame.sprite.Group.update(self.projectiles_player)
            pygame.sprite.Group.update(self.projectiles_enemies)
            pygame.sprite.Group.update(self.ui)
            pygame.sprite.Group.update(self.ui_on_top)
            pygame.sprite.Group.update(self.hidden_sprites)
            # run controllers update
            self.controller.update()

        # always updating:


        # always draw the sprites if scene is rendering to prevent black screen...
        pygame.sprite.Group.draw(self.ui, self.gameboard)
        pygame.sprite.Group.draw(self.active_sprites, self.gameboard)
        pygame.sprite.GroupSingle.draw(self.player_sprite, self.gameboard)
        pygame.sprite.Group.draw(self.powerups, self.gameboard)
        pygame.sprite.Group.draw(self.projectiles_player, self.gameboard)
        pygame.sprite.Group.draw(self.projectiles_enemies, self.gameboard)
        pygame.sprite.Group.draw(self.ui_on_top, self.gameboard)

        # not drawing hidden sprites

