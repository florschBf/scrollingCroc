import pygame.sprite
from gameObjects.GameObject import GameObject

class PlayerObject(GameObject):
    """
    Player Object to represent the player in the game
    @TODO graphic, controls, movement...
    """

    health = 100
    state = 'active'

    #movement as tupel: positive = x/y+, negative = x/y-
    movement = [0,0]
    #gameBoard constraints for player to stay on screen, set dynamically
    borderX = [0,0]
    borderY = [0,0]

    #Constructor currently generates a rectangle for us
    def __init__(self, color, width, height, start):
        GameObject.__init__(self)

        #player rectangle image
        self.image = pygame.Surface([width,height])
        self.image.set_at(start, color)

        #image position on screen, update using rect.x and rect.y
        self.rect = self.image.get_rect()

    #UPDATE CALLED EVERY FRAME ON SPRITES
    def update(self):
        #Handle movement every frame
        newPosX = self.rect.x + self.movement[0]
        newPosY = self.rect.y + self.movement[1]

        if newPosX > self.borderX[0] and newPosX < self.borderX[1]:
            self.rect.x = newPosX
        elif newPosX < self.borderX[0]:
            #hit left edge, bounce from border
            self.movement[0] = 4
        elif newPosX > self.borderX[1]:
            #hit right edge, bounce from border
            self.movement[0] = -4

        if newPosY > self.borderY[0] and newPosY < self.borderY[1]:
            self.rect.y = newPosY
        elif newPosY < self.borderY[0]:
            #hit top edge, bounce from border
            self.movement[1] = 4
        elif newPosY > self.borderY[1]:
            #hit bottom edge, bounce from border
            self.movement[1] = -4

    def getPos(self):
        return self.rect

    #GAME LOGIC RELATED METHODS
    def returnHealth(self):
        return self.health

    def returnState(self):
        return self.state

    def setHealth(self, someNumber):
        self.health = someNumber

    def setState(self,someState):
        self.state = someState

    #VISUAL AND POSITION SETTERS
    def setPos(self, newX, newY):
        self.rect.x = newX
        self.rect.y = newY

    def setColor(self, color):
        self.image.fill(color)

    def setBorderX(self, max_X_coord):
        self.borderX[1] = max_X_coord

    def setBorderY(self, max_Y_coord):
        self.borderY[1] = max_Y_coord


    #MOVEMENT METHODS FOR CONTROLLER TO CALL
    def getSpeed(self):
        return self.movement

    def accelerate(self, speed_increase):
        self.movement[0] += speed_increase

    def decelerate(self, speed_decrease):
        self.movement[0] -= speed_decrease

    def rise(self, updrift):
        self.movement[1] -= updrift
        print(self.movement[1])

    def fall(self, downdrift):
        self.movement[1] += downdrift