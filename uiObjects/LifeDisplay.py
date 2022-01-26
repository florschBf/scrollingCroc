import pygame
import pygame.font
from uiObjects.UiObject import UiObject


class LifeDisplay(UiObject):

    def __init__(self, player):

        pygame.font.init()
        self.menu_font = pygame.font.get_default_font()  # getting default font for now just to render sth
        self.font_renderer = pygame.font.SysFont(self.menu_font, 30)
        self.default_color = (255, 255, 255)

        # player object that holds the score value
        self.player = player
        self.lives = self.player.lives

        #text item
        self.text = self.font_renderer.render("Extrakrokodile: ", True, self.default_color)
        self.croc = pygame.transform.scale(pygame.image.load('assets/drawables/croc.png').convert_alpha(), (30, 30))

        # image and position
        self.image = pygame.Surface ([100, 60])
        self.image.fill((15, 15, 15))
        self.image.blit(self.text, (0, 10, 100, 30))
        self.blit_crocs()

        # jetzt super callen, image ist initialisiert
        super().__init__()

    def update(self):
        self.lives = self.player.lives

        # clear and redraw the update
        self.image.fill((15, 15, 15))
        self.blit_crocs()

    def blit_crocs(self):
        offset = 0
        print(self.lives)
        for x in range(0,self.lives):
            self.image.blit(self.croc, (0 + offset, 30, 100, 30))
            offset += 30