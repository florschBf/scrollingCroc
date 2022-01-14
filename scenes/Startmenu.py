from uiObjects.TextRenderer import TextRenderer


class Startmenu:

    main_color = None
    def __init__(self, color):
        self.selected = "tutorial"
        self.main_color = color

    def render(self):
        startscreen = True
        while startscreen:
            menu_tut = TextRenderer().render_text_aa("Tutorial", "Arial", 30, main_color)
            # menu_tut = StartmenuItem("Tutorial")
            # menu_play = StartmenuItem("Play")
            # menu_endless = StartmenuItem("Endless Mode")
            # menu_options = StartmenuItem("Options")
        return menu_tut

