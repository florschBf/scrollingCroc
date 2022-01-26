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
    def __init__(self, surface, width, height, start):
        GameObject.__init__(self, surface)
        self.height = height
        self.width = width
        # player rectangle image
        self.image = pygame.image.load('assets/drawables/croc_scaled2.png').convert_alpha()
        self.projectile_image = pygame.image.load('assets/drawables/bubble_projectile.png').convert_alpha()

        # image position on screen, update using rect.x and rect.y
        self.rect = self.image.get_rect()
        self.set_pos(start[0], start[1])

        # game values
        self.score = 0
        self.lives = 3
        self.game_over = False

    # UPDATE CALLED EVERY FRAME ON SPRITES
    def update(self):
        # not calling super, player borders are different, never leaves game
        pass

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
