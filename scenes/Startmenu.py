from uiObjects.TextRenderer import TextRenderer
from controller.MenuController import MenuController


class Startmenu:

    def __init__(self, surface, color):
        #we render here
        self.menu_display = surface
        #selected holds the currently selected menu item as a position
        self.selected = 0
        #main color for font - consider color schemes or accents for later
        self.main_color = color
        #we need a menu controller to handle player input
        self.controller = MenuController()


    def render(self):
        start_screen = True
        print('menu rendering')
        #while start_screen:
            #print('menu rendering')
            #menu_tut = TextRenderer().render_text_aa("Tutorial", "Arial", 30, self.main_color)
            # menu_tut = StartmenuItem("Tutorial")
            # menu_play = StartmenuItem("Play")
            # menu_endless = StartmenuItem("Endless Mode")
            # menu_options = StartmenuItem("Options")

