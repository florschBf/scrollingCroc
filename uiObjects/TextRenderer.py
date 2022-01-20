import pygame
from pygame import font


class TextRenderer:
    """
    Klasse um Text auszugeben
    """
    font.init()

    def render_text(self, text_string, textFont, textSize, textColor):
        new_font = pygame.font.Font(textFont, textSize)
        new_text = new_font.render(text_string, 0, textColor)
        return new_text

    def render_text_aa(self, text_string, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(text_string, 1, textColor)
        return newText
