import pygame.image
from uiObjects.UiObject import UiObject


class InfoBar(UiObject):

    def __init__(self):
        self.image = pygame.image.load('assets/drawables/infos.png')
        super().__init__()
        self.filler = pygame.Surface([620, 40])
        self.filler.fill((23, 23, 23))
        self.image.blit(self.filler, (10, 50))

    def update(self):
        super().update()
        self.image.blit(self.filler, (10, 50))
