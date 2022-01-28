import pygame
import pygame.font
from uiObjects.UiObject import UiObject


class TimeDisplay(UiObject):

    def __init__(self, initial_value, infobar):

        pygame.font.init()
        self.menu_font = pygame.font.get_default_font()  # getting default font for now just to render sth
        self.font_renderer = pygame.font.SysFont(self.menu_font, 30)
        self.default_color = (255, 255, 255)

        self.update_time_value(initial_value)
        self.value = self.font_renderer.render(str(self.time_value), True, self.default_color)

        # image and position
        # empty image cause we're just blitting crocs on infobar. kind of makes this a controller? too late to change
        self.image = pygame.Surface([0, 0])
        self.infobar = infobar
        self.infobar.image.blit(self.value, (165, 60, 100, 30))

        # jetzt super callen, image ist initialisiert
        super().__init__()

        self.time_value = 0

    def update_time_value(self, value):
        # value is in ms, need to divide for seconds
        self.time_value = str(round(value, 2))

    def update(self):

        self.value = self.font_renderer.render(str(self.time_value), True, self.default_color)

        # clear and redraw the update
        self.infobar.image.blit(self.value, (170, 65, 100, 30))
