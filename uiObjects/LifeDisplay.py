import pygame
import pygame.font
from uiObjects.UiObject import UiObject


class LifeDisplay(UiObject):

    def __init__(self, player, infobar):

        pygame.font.init()
        self.menu_font = pygame.font.get_default_font()  # getting default font for now just to render sth
        self.font_renderer = pygame.font.SysFont(self.menu_font, 30)
        self.default_color = (255, 255, 255)
        self.infobar = infobar
        # empty image cause we're just blitting crocs on infobar. kind of makes this a controller? too late to change
        self.image = pygame.Surface([0, 0])

        # player object that holds the score value
        self.player = player
        self.lives = self.player.lives

        # croc image to represent lives
        self.croc = pygame.image.load('assets/drawables/croc_lives.png').convert_alpha()

        # image and position
        self.blit_crocs()

        # jetzt super callen, image ist initialisiert
        super().__init__()

    def update(self):
        self.lives = self.player.lives
        self.blit_crocs()

    def blit_crocs(self):
        offset = 400
        print(self.lives)
        for x in range(0, self.lives):
            if x > 8:
                pass
            else:
                self.infobar.image.blit(self.croc, (0 + offset, 60, 100, 30))
                offset += 30
