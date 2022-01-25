import pygame.sprite
from gameObjects.GameObject import GameObject


class PlayerObject(GameObject):
    """
    Player Object to represent the player in the game
    """

    # movement as tupel: positive = x/y+, negative = x/y-
    movement = [0, 0]
    # gameBoard constraints for player to stay on screen, set dynamically
    borderX = [0, 0]
    borderY = [0, 0]

    # Constructor currently generates a rectangle for us
    def __init__(self, surface, color, width, height, start):
        GameObject.__init__(self, surface)
        self.height = height
        self.width = width
        # player rectangle image
        self.image = pygame.Surface([width, height])
        self.image.set_at(start, color)

        # image position on screen, update using rect.x and rect.y
        self.rect = self.image.get_rect()

        # game values
        self.score = 0
        self.tag = 'player'

    # UPDATE CALLED EVERY FRAME ON SPRITES
    def update(self):
        # not calling super, player borders are different, never leaves game

        # Handle movement every frame
        new_pos_x = self.rect.x + self.movement[0]
        new_pos_y = self.rect.y + self.movement[1]

        if self.borderX[0] < new_pos_x < self.borderX[1]-self.width:
            self.rect.x = new_pos_x
        elif new_pos_x < self.borderX[0]:
            # hit left edge, bounce from border
            self.movement[0] = 4
        elif new_pos_x > self.borderX[1]-self.width:
            # hit right edge, bounce from border
            self.movement[0] = -4

        if self.borderY[0] < new_pos_y < self.borderY[1]-self.height:
            self.rect.y = new_pos_y
        elif new_pos_y < self.borderY[0]:
            # hit top edge, bounce from border
            self.movement[1] = 4
        elif new_pos_y > self.borderY[1]-self.height:
            # hit bottom edge, bounce from border
            self.movement[1] = -4

    # Player logic methods
    # Player should have borders on screen he cant't pass so he stays in the window
    def set_borderX(self, max_x_coord):
        self.borderX[1] = max_x_coord

    def set_borderY(self, max_y_coord):
        self.borderY[1] = max_y_coord

    # MOVEMENT METHODS FOR CONTROLLER TO CALL
    def get_speed(self):
        return self.movement

    def accelerate(self, speed_increase):
        self.movement[0] += speed_increase

    def decelerate(self, speed_decrease):
        self.movement[0] -= speed_decrease

    def rise(self, updrift):
        self.movement[1] -= updrift

    def fall(self, downdrift):
        self.movement[1] += downdrift
