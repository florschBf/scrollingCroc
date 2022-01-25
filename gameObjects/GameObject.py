import pygame
from pygame.sprite import Sprite

class GameObject(Sprite):
    '''
    Sprite.rect -> position on surface
    Sprite.image -> displayed Sprite
    '''
    def __init__(self, surface):
        Sprite.__init__(self)
        self.state = "active"
        self.health = 100 # thinking in percentages here for starters
        self.collision = True # default GameObjects can be collided with by the player, is being handled on sprite group level though
        # GameObjects have a speed at which they traverse the screen
        self.speed = [4, 0] # default speed 8x 0y, feel free to mod
        self.border_y = True
        self.border_x = False
        self.surface = surface
        self.image = pygame.Surface([50 ,50]) #initialise a default image
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

        #default score
        self.score_value = 10
        # bool to flag as destroyed for score calculation, prevents multiple hits to generate score value
        self.already_destroyed = False
        self.tag = GameObject # overwrite, need to know specifics here in game logic

    def get_pos(self):
        return self.rect

    def set_pos(self, newX, newY):
        self.rect.x = newX
        self.rect.y = newY

    def set_color(self, color):
        self.image.fill(color)

    def return_state(self):
        #return game relevant states here, thinking of a finite state machine inactive|active|trackingPlayer|immobile
        return self.state

    def set_state(self, state):
        self.state = state

    def return_health(self):
        #thinking of destroyable objects
        return self.health

    def set_health(self, some_number):
        self.health = some_number

    def set_collision(self, am_i_collidable):
        self.collision = am_i_collidable

    def get_collision(self):
        return self.collision

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    # Methods to set borders for the gameObject e.g. it cant leave game through y(top/bottom, default: True)
    # or x (left/right, default: False)
    def set_border_y(self, yes_or_no):
        self.border_y = yes_or_no

    def set_border_x(self, bool):
        self.border_x = bool

    def update(self):
        """
        All sprites update and all GameObjects should check if they left the screen to call sprite.kill()
        Make sure to call super on all Obstacles, Enemies or whatever
        :return:
        """
        # check if we hit any borders, reverse speed if so
        x = self.get_pos().x
        y = self.get_pos().y
        # not coming back from x < -50, remove the object
        if x < -100:
            print("My time is over: " + str(self))
            self.kill()
        #not coming back from y < -50 or y > surface + 50
        if y < -100 or y > self.surface.get_height()+100:
            print("My time is over: " + str(self))
            self.kill()


