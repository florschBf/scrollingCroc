import pygame
from pygame.surface import Surface
from gameObjects.UiObject import UiObject


class MenuSelector(UiObject):
    '''
    UI Object that represents the players selection in a menu (think of an arrow or a ball infront of a text
    '''

    def __init__(self, height, width, color):
        self.position = 0

        UiObject.__init__(self)
        self.height = height
        self.width = width
        # selector rectangle image
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        #image position on screen, update using rect.x and rect.y
        self.rect = self.image.get_rect()

    def next_item(self):
        # go to next item
        self.position += 1
        if self.position > 3:
            self.position = 0

    def prev_item(self):
        # go to previous item
        self.position -= 1
        if self.position < 0:
            self.position = 3

    def get_selected(self):
        # return currently selected item
        return self.position

    def setPos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def setColor (self, color):
        self.image.fill(color)