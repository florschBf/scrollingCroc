import pygame.font

from scenes.Scene import Scene
from uiObjects.MenuSelector import MenuSelector
from controllers.MenuController import MenuController
from controllers.HighscoreController import HighscoreController


class Highscore(Scene):

    def __init__(self, surface, color, selector_color, scene_controller):
        pygame.font.init()
        self.menu_font = pygame.font.get_default_font()  # getting default font for now just to render sth
        self.font_renderer = pygame.font.SysFont(self.menu_font, 30)

        # our scene controllers and surface get set in super
        super().__init__(surface, scene_controller)

        # json for keeping highscores
        self.highscore = HighscoreController("assets/highscore.json")

        # main color for font - consider color schemes or accents for later
        self.main_color = color
        self.selector_color = selector_color
        # menu needs a visible selector to show selected item
        # ball standing in as selector for now
        self.selector = MenuSelector(15, 15, self.selector_color)
        self.menu_image = pygame.image.load('assets/drawables/highscore.png').convert_alpha()

        # creating all menu items as surfaces and rendering them on the main surface
        self.text_item1a = self.font_renderer.render(self.highscore.return_position_name(0), True, self.main_color)
        self.text_item1b = self.font_renderer.render(self.highscore.return_position_score(0), True, self.main_color)
        self.text_item2a = self.font_renderer.render(self.highscore.return_position_name(1), True, self.main_color)
        self.text_item2b = self.font_renderer.render(self.highscore.return_position_score(1), True, self.main_color)
        self.text_item3a = self.font_renderer.render(self.highscore.return_position_name(2), True, self.main_color)
        self.text_item3b = self.font_renderer.render(self.highscore.return_position_score(2), True, self.main_color)
        self.text_item4a = self.font_renderer.render(self.highscore.return_position_name(3), True, self.main_color)
        self.text_item4b = self.font_renderer.render(self.highscore.return_position_score(3), True, self.main_color)
        self.text_item5a = self.font_renderer.render(self.highscore.return_position_name(4), True, self.main_color)
        self.text_item5b = self.font_renderer.render(self.highscore.return_position_score(4), True, self.main_color)

        # need a menu controllers to handle player input
        self.controller = MenuController(self.selector, self)
        self.controller.set_menu_state('highscore')

        # collect active sprites in a group to draw them to surface

        # selector not needed for highscore, not drawing and updating
        # self.selector.add(self.active_sprites)

    def render(self):
        # rendering menu items to surface
        self.gameboard.blit(self.menu_image, (375, 25))
        # names
        self.gameboard.blit(self.text_item1a, (500, 270, 30, 30))
        self.gameboard.blit(self.text_item2a, (500, 300, 30, 30))
        self.gameboard.blit(self.text_item3a, (500, 330, 30, 30))
        self.gameboard.blit(self.text_item4a, (500, 360, 30, 30))
        self.gameboard.blit(self.text_item5a, (500, 390, 30, 30))

        # scores
        self.gameboard.blit(self.text_item1b, (680, 270, 30, 30))
        self.gameboard.blit(self.text_item2b, (680, 300, 30, 30))
        self.gameboard.blit(self.text_item3b, (680, 330, 30, 30))
        self.gameboard.blit(self.text_item4b, (680, 360, 30, 30))
        self.gameboard.blit(self.text_item5b, (680, 390, 30, 30))

        # call Scene render function for sprites and controllers
        super().render()

    def update_highscores(self):
        print('updating the list')
        # creating all menu items as surfaces and rendering them on the main surface
        self.text_item1a = self.font_renderer.render(self.highscore.return_position_name(0), True, self.main_color)
        self.text_item1b = self.font_renderer.render(self.highscore.return_position_score(0), True, self.main_color)
        self.text_item2a = self.font_renderer.render(self.highscore.return_position_name(1), True, self.main_color)
        self.text_item2b = self.font_renderer.render(self.highscore.return_position_score(1), True, self.main_color)
        self.text_item3a = self.font_renderer.render(self.highscore.return_position_name(2), True, self.main_color)
        self.text_item3b = self.font_renderer.render(self.highscore.return_position_score(2), True, self.main_color)
        self.text_item4a = self.font_renderer.render(self.highscore.return_position_name(3), True, self.main_color)
        self.text_item4b = self.font_renderer.render(self.highscore.return_position_score(3), True, self.main_color)
        self.text_item5a = self.font_renderer.render(self.highscore.return_position_name(4), True, self.main_color)
        self.text_item5b = self.font_renderer.render(self.highscore.return_position_score(4), True, self.main_color)

    def onresume(self):
        super().onresume()

    def onpause(self):
        super().onpause()
        # resetting controllers position for when we go back to menu in the future
        self.controller.reset_menu_pos()
