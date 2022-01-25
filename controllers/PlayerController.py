import pygame.key

from gameObjects.Projectile import Projectile

class PlayerController:
    """
    Class that controls all input for the playerobject, e.g. movement and shooting
    """


    '''movement settings - switch up to change player move behaviour
    drag slows down when not accelerating, responsiveness controls quickness of controls'''
    responsiveness = 1
    drag = 0.5
    maxSpeed = 10
    accelerating = False
    decelerating = False
    rising = False
    falling = False

    def __init__(self, player, scene):
        """
        Constructor for player controllers
        :param player: Player object that will be controlled with inputs
        """
        self.player = player
        self.scene = scene

    def handle(self, event):
        """
        Methode zum Verarbeiten von Keyboard, Maus und Controller-Input
        :param event: Player Input
        :return:
        """
        if self.scene.interrupted:
            # message to player being displayed. on input, remove and proceed with game
            self.scene.ui_handler.remove_ui_element(self.scene.ui_handler.message_to_player)
        else:
            #Get keypress
            if event.type == pygame.KEYDOWN:
                # arrows for movement
                if event.key == pygame.K_LEFT:
                    self.decelerating = True
                elif event.key == pygame.K_RIGHT:
                    print(self.accelerating)
                    self.accelerating = True
                    print(self.accelerating)
                elif event.key == pygame.K_UP:
                    self.rising = True
                elif event.key == pygame.K_DOWN:
                    self.falling = True
                elif event.key == pygame.K_SPACE:
                    print('pew pew')
                    playerpos = self.player.get_pos()
                    shot = Projectile(self.scene.gameboard, 100, playerpos)
                    # player just shoots straight ahead
                    target = (playerpos.x + 1, playerpos.y)
                    shot.set_shot_direction(target, playerpos)
                    shot.add(self.scene.projectiles_player)
            #Get keyup
            elif event.type == pygame.KEYUP:
                # arrow up = stop movement
                if event.key == pygame.K_LEFT:
                    self.decelerating = False
                elif event.key == pygame.K_RIGHT:
                    self.accelerating = False
                elif event.key == pygame.K_UP:
                    self.rising = False
                elif event.key == pygame.K_DOWN:
                    self.falling = False

                # escape for start menu / pause
                elif event.key == pygame.K_ESCAPE:
                    # THIS LEAVES THE SCENE BELOW INTACT - WIE PAUSE
                    self.scene.new_scene("start_menu")

    def update(self):
        """
        Movement is realized through a changing speed tuple variable
        Increased on acceleration/rise
        Decreased on decelerate/fall
        :return:
        """
        speed = self.player.get_speed()
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
