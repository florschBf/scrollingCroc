import pygame
import pygame.font
from uiObjects.UiObject import UiObject


class ScoreDisplay(UiObject):

    def __init__(self, player, infobar):

        pygame.font.init()
        self.menu_font = pygame.font.get_default_font()  # getting default font for now just to render sth
        self.font_renderer = pygame.font.SysFont(self.menu_font, 30)
        self.default_color = (255, 255, 255)

        # player object that holds the score value
        self.player = player
        self.infobar = infobar
        self.score = self.player.score

        # text item
        self.value = self.font_renderer.render(str(self.score), True, self.default_color)

        # image and position
        # empty image cause we're just blitting crocs on infobar. kind of makes this a controller? too late to change
        self.image = pygame.Surface([0, 0])
        self.image.blit(self.value, (0, 40, 100, 30))

        # jetzt super callen, image ist initialisiert
        super().__init__()

    def update_score(self, value):
        self.score = value

    def update(self):
        self.score = self.player.score
        self.value = self.font_renderer.render(str(self.score), True, self.default_color)

        # clear and redraw the update
        self.infobar.image.blit(self.value, (270, 65, 100, 30))
