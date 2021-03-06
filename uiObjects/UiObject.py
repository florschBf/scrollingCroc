from pygame.sprite import Sprite


class UiObject(Sprite):
    """
    Sprite.rect -> position on surface
    Sprite.image -> displayed Sprite
    """

    def __init__(self):
        Sprite.__init__(self)
        self.rect = self.image.get_rect()

    def get_pos(self):
        return self.rect

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def return_state(self):
        # return game relevant states here, thinking of a finite state machine visible|invisible for UI?
        pass

    def hide(self):
        """
        Method to hide UI elements on demand
        :return:
        """
        print("hide on UI Object called")
        print(self.groups())
