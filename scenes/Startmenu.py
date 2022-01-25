import pygame.font

from scenes.Scene import Scene
from uiObjects.MenuSelector import MenuSelector
from controllers.MenuController import MenuController


class Startmenu(Scene):
    pygame.font.init()
    menu_font = pygame.font.get_default_font()  # getting default font for now just to render sth
    font_renderer = pygame.font.SysFont(menu_font, 30)
    item1 = 'Tutorial'
    item2 = 'Play'
    item3 = 'Endless'
    item4 = 'Options'
    item5 = 'Quit'

    def __init__(self, surface, color, selector_color, scene_controller):
        # our scene controllers and surface get set in super
        super().__init__(surface, scene_controller)

        # main color for font - consider color schemes or accents for later
        self.main_color = color
        self.selector_color = selector_color
        # menu needs a visible selector to show selected item
        # ball standing in as selector for now
        self.selector = MenuSelector(15, 15, self.selector_color)

        # creating all menu items as surfaces and rendering them on the main surface
        self.text_item1 = self.font_renderer.render(self.item1, True, self.main_color)
        self.text_item2 = self.font_renderer.render(self.item2, True, self.main_color)
        self.text_item3 = self.font_renderer.render(self.item3, True, self.main_color)
        self.text_item4 = self.font_renderer.render(self.item4, True, self.main_color)
        self.text_item5 = self.font_renderer.render(self.item5, True, self.main_color)
        self.text_items = [self.text_item1, self.text_item2, self.text_item3, self.text_item4]

        # we need a menu controllers to handle player input
        self.controller = MenuController(self.selector, self)

        # we collect active sprites in a group to draw them to surface
        self.selector.add(self.active_sprites)

    def render(self):
        # call Scene render function for sprites and controllers
        super().render()

        # rendering menu items to surface
        self.gameboard.blit(self.text_item1, (
            self.gameboard.get_width() / 2 - 30, self.gameboard.get_height() / 2 - 120, 30, 30))
        self.gameboard.blit(self.text_item2, (
            self.gameboard.get_width() / 2 - 30, self.gameboard.get_height() / 2 - 90, 30, 30))
        self.gameboard.blit(self.text_item3, (
            self.gameboard.get_width() / 2 - 30, self.gameboard.get_height() / 2 - 60, 30, 30))
        self.gameboard.blit(self.text_item4, (
            self.gameboard.get_width() / 2 - 30, self.gameboard.get_height() / 2 - 30, 30, 30))
        self.gameboard.blit(self.text_item5, (
            self.gameboard.get_width() / 2 - 30, self.gameboard.get_height() / 2, 30, 30))


    def onresume(self):
        super().onresume()

    def onpause(self):
        super().onpause()
        # resetting controllers position for when we go back to menu in the future
        self.controller.reset_menu_pos()