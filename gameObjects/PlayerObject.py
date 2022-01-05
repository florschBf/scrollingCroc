import pygame.sprite
from gameObjects.GameObject import GameObject

class PlayerObject(GameObject):
    """
    Player Object to represent the player in the game
    @TODO graphic, controls, movement...
    """

    health = 100
    state = 'active'
    #Constructor currently generates a rectangle for us
    def __init__(self, color, width, height, start):
        GameObject.__init__(self)

        #player rectangle image
        self.image = pygame.Surface([width,height])
        self.image.set_at(start, color)

        #image position on screen, update using rect.x and rect.y
        self.rect = self.image.get_rect()

    def getPos(self):
        return self.rect

    def returnHealth(self):
        return self.health

    def returnState(self):
        return self.state

    def setHealth(self, someNumber):
        self.health = someNumber

    def setState(self,someState):
        self.state = someState

    def setPos(self, newX, newY):
        self.rect.x = newX
        self.rect.y = newY

    def setColor(self, color):
        self.image.fill(color)