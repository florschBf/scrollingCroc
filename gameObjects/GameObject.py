from pygame.sprite import Sprite

class GameObject(Sprite):
    '''
    Sprite.rect -> position on surface
    Sprite.image -> displayed Sprite
    '''
    def __init__(self):
        Sprite.__init__(self)

    def getPos(self):
        return this.rect

    def returnState(self):
        #return game relevant states here, thinking of a finite state machine inactive|active|trackingPlayer|immobile
        pass

    def returnHealth(self):
        #thinking of destroyable objects
        pass

    pass
