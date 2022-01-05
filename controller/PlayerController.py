from pygame.key import *

class PlayerController:

    def __init__(self, player):
        '''
        Constructor for player controller
        :param player: Player object that will be controlled with inputs
        '''
        self.player = player

    def handle(self,event):
        if event.type == 'UserEvent':
            print('sth being done here')
