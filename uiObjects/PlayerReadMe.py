import pygame.font
import pygame.sprite
from uiObjects.UiObject import UiObject

class PlayerReadMe(UiObject):
    """
    Class to send messages to the player - for explanation, story whatever.
    Renders in surface on bottom of screen.
    Sets scene to interrupted while open, so game freezes!
    """

    def __init__(self):
        pygame.font.init()
        self.menu_font = pygame.font.get_default_font()  # getting default font for now just to render sth
        self.font_renderer = pygame.font.SysFont(self.menu_font, 30)
        self.default_color = (255, 255, 255)

        # text item
        self.text = self.font_renderer.render("Nachricht: ", True, self.default_color)
        self.confirm = self.font_renderer.render("Mit Return bestätigen, dann geht's weiter.", True, self.default_color)
        self.message_lines = []
        # image and position
        self.image = pygame.Surface([600, 200])
        self.image.fill((15, 15, 15))
        self.image.blit(self.text, (10, 10, 100, 30))

        # jetzt super callen, image ist initialisiert
        super().__init__()

    def set_message(self, *args):
        for line in args:
            self.message_lines.append(self.font_renderer.render(line, True, self.default_color))

    def update(self):
        line_offset_from_top = 10
        # clear and redraw the update
        self.image.fill((115, 115, 115))
        self.image.blit(self.text, (10, 10, 100, 30))
        for line in self.message_lines:
            line_offset_from_top += 20
            self.image.blit(line, (10, line_offset_from_top, 100, 30))
        self.image.blit(self.confirm, (10, self.image.get_height()-30, 100, 30))

