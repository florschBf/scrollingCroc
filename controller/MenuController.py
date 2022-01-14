import pygame.key


class MenuController:

    def __init__(self):
        pass

    def printMyEvent(self, event):
        print(event)

    def handle(self, event):
        """
        Method to handle player input on start_menu scene
        :param event: the player input to handle
        :return: None
        """
        #Get keypress
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('going left')

            elif event.key == pygame.K_RIGHT:
                print('going right')

            elif event.key == pygame.K_UP:
                print('going up')

            elif event.key == pygame.K_DOWN:
                print('going down')

            elif event.key == pygame.K_SPACE:
                print('pew pew')
        #Get keyup
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print('stopped going left')

        print(event.type)
