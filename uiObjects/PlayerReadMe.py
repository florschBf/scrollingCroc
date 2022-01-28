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
        self.message_lines = []
        # image and text blit, position set in UiHandler
        self.image = pygame.image.load('assets/drawables/message_box.png')

        # jetzt super callen, image ist initialisiert
        super().__init__()

    def set_message(self, *args):
        for line in args:
            self.message_lines.append(self.font_renderer.render(line, True, self.default_color))

    def update(self):
        line_offset_from_top = 60
        # clear and redraw the message
        for line in self.message_lines:
            line_offset_from_top += 25
            self.image.blit(line, (25, line_offset_from_top, 100, 30))
