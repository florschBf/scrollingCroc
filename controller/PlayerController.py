import pygame
from pygame.key import *

class PlayerController:

    '''movement settings - switch up to change player move behaviour
    drag slows down when not accelerating, responsiveness controls quickness of controls'''
    responsiveness = 1
    drag = 0.5
    maxSpeed = 15
    accelerating = False
    decelerating = False
    rising = False
    falling = False

    def __init__(self, player):
        '''
        Constructor for player controller
        :param player: Player object that will be controlled with inputs
        '''
        self.player = player

    def handle(self,event):
        '''
        Methode zum Verarbeiten von Keyboard, Maus und Controller-Input
        :param event: Player Input
        :return:
        '''
        #Get keypress
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('going left')
                self.decelerating = True
            elif event.key == pygame.K_RIGHT:
                print('going right')
                print(self.accelerating)
                self.accelerating = True
                print(self.accelerating)
            elif event.key == pygame.K_UP:
                print('going up')
                self.rising = True
            elif event.key == pygame.K_DOWN:
                print('going down')
                self.falling = True
            elif event.key == pygame.K_SPACE:
                print('pew pew')
        #Get keyup
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print('stopped going left')
                self.decelerating = False
            elif event.key == pygame.K_RIGHT:
                print('stopped going right')
                self.accelerating = False
            elif event.key == pygame.K_UP:
                print('stopped going up')
                self.rising = False
            elif event.key == pygame.K_DOWN:
                print('stopped going down')
                self.falling = False

    def update(self):
        speed = self.player.getSpeed()
        print(speed)
        #x movement
        if self.accelerating:
            if speed[0] < self.maxSpeed:
                self.player.accelerate(self.responsiveness)
        elif self.decelerating:
            if speed[0] > -self.maxSpeed:
                self.player.decelerate(self.responsiveness)
        else:
            #no movement, apply default drag
            if speed[0] > 0:
                self.player.decelerate(self.drag)
            elif speed[0] < 0:
                self.player.accelerate(self.drag)

        #y movement
        if self.rising:
            if speed[1] < self.maxSpeed:
                self.player.rise(self.responsiveness)
        elif self.falling:
            if speed[1] > -self.maxSpeed:
                self.player.fall(self.responsiveness)
        else:
            #no movement, apply default drag
            if speed[1] < 0:
                self.player.fall(self.drag)
            elif speed[1] > 0:
                self.player.rise(self.drag)