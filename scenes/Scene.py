class Scene:

    def __init__(self):
        # technically, constructor is not 100% equiv to oncreate steps, but it will do
        # TODO think about automating SceneController interaction
        #  instead of doing it every time in specific scene constructor
        pass

    def onpause(self):
        # call me when pausing the scene
        pass

    def onresume(self):
        # call me when returning to the scene
        pass

    def onreset(self):
        # call when scene should be ended (e.g. cleanup, send back to start)
        pass
