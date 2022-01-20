from scenes.Scene import Scene

class Endless(Scene):

    def __init__(self, surface, scene_controller):
        super().__init__()
        self.gameboard = surface
        self.scene_controller = scene_controller

    def render(self):
        pass
