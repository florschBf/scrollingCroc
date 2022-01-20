from scenes.Scene import Scene


class Options(Scene):

    def __init__(self, surface, scene_controller):
        super().__init__()
        self.options_display = surface
        self.scene_controller = scene_controller

    def render(self):
        pass
