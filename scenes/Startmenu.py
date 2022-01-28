import pygame.font

from scenes.Scene import Scene
from uiObjects.MenuSelector import MenuSelector
from controllers.MenuController import MenuController


class Startmenu(Scene):

    def __init__(self, surface, color, selector_color, scene_controller):
        pygame.font.init()
        self.menu_font = pygame.font.get_default_font()  # getting default font for now just to render sth
        self.font_renderer = pygame.font.SysFont(self.menu_font, 30)
        self.item1 = 'Tutorial'
        self.item2 = 'Play'
        self.item3 = 'Endless'
        self.item4 = 'Options'
        self.item5 = 'Quit'
        # our scene controllers and surface get set in super
        super().__init__(surface, scene_controller)

        # main color for font - consider color schemes or accents for later
        self.main_color = color
        self.selector_color = selector_color
        # menu needs a visible selector to show selected item
        # ball standing in as selector for now
        self.selector = MenuSelector(15, 15, self.selector_color)
        self.menu_image = pygame.image.load('assets/drawables/croc_menu3.png').convert_alpha()

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
        # rendering menu items to surface
        self.gameboard.blit(self.menu_image, (375, 25))
        self.gameboard.blit(self.text_item1, (610, 270, 30, 30))
        self.gameboard.blit(self.text_item2, (610, 300, 30, 30))
        self.gameboard.blit(self.text_item3, (610, 330, 30, 30))
        self.gameboard.blit(self.text_item4, (610, 360, 30, 30))
        self.gameboard.blit(self.text_item5, (610, 390, 30, 30))

        # call Scene render function for sprites and controllers
        super().render()

    def onresume(self):
        super().onresume()

    def onpause(self):
        super().onpause()
        # resetting controllers position for when we go back to menu in the future
        self.controller.reset_menu_pos()
