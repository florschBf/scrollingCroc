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
        self.collision = True # default GameObjects can be collided with by the player
        # GameObjects have a speed at which they traverse the screen
        self.speed = [8, 0] # default speed 8, feel free to mod
        self.permanent = False
        self.surface = surface

    def get_pos(self):
        return this.rect

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

    def set_permanent(self, yes_or_no):
        self.permanent = yes_or_no


