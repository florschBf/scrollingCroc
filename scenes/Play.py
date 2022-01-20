from scenes.Scene import Scene


class Play(Scene):

    def __init__(self, surface, scene_controller):
        super().__init__()
        self.gameBoard = surface
        self.scene_controller = scene_controller

    def render(self):
        pass
