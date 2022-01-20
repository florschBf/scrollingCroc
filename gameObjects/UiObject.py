from pygame.sprite import Sprite


class UiObject(Sprite):
    """
    Sprite.rect -> position on surface
    Sprite.image -> displayed Sprite
    """

    def __init__(self):
        Sprite.__init__(self)

    def getPos(self):
        return self.rect

    def returnState(self):
        # return game relevant states here, thinking of a finite state machine inactive|active|trackingPlayer|immobile
        pass

    def hide(self):
        """
        Method to hide UI elements on demand
        :return:
        """
        self.groups()

    pass
