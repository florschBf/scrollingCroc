import pygame
import pygame.font
from uiObjects.UiObject import UiObject


class TimeDisplay(UiObject):

    def __init__(self, initial_value):

        pygame.font.init()
        self.menu_font = pygame.font.get_default_font()  # getting default font for now just to render sth
        self.font_renderer = pygame.font.SysFont(self.menu_font, 30)
        self.default_color = (255, 255, 255)

        self.update_time_value(initial_value)

        #text item
        self.text = self.font_renderer.render("Zeit: ", True, self.default_color)
        self.value = self.font_renderer.render(str(self.time_value), True, self.default_color)

        # image and position
        self.image = pygame.Surface ([100, 60])
        self.image.fill((15, 15, 15))
        self.image.blit(self.text, (0, 10, 100, 30))
        self.image.blit(self.value, (0, 40, 100, 30))

        # jetzt super callen, image ist initialisiert
        super().__init__()

    def update_time_value(self, value):
        # value is in ms, need to divide for seconds
        self.time_value = str(round(value, 2))

    def update(self):

        self.value = self.font_renderer.render(str(self.time_value), True, self.default_color)

        # clear and redraw the update
        self.image.fill((15, 15, 15))
        self.image.blit(self.text, (0, 10, 100, 30))
        self.image.blit(self.value, (0, 38, 100, 30))
