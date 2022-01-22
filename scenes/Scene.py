class Scene:

    def __init__(self, surface, scene_controller):
        # technically, constructor is not 100% equiv to oncreate steps, but it will do
        # setting main pygame surface and scene_controller
        self.gameboard = surface
        self.scene_controller = scene_controller

    def onpause(self):
        # call me when pausing the scene
        print("pause on scene " + str(self) + " called")

    def onresume(self):
        # call me when returning to the scene
        print("resume on scene " + str(self) + " called")

    def onreset(self):
        # call when scene should be ended (e.g. cleanup, send back to start)
        print("reset on scene " + str(self) + " called")

    def new_scene(self, scene_to_go_to):
        self.scene_controller.scene_switch(scene_to_go_to, self)